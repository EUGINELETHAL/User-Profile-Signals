from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Subject(models.Model):
    name = models.CharField(max_length=30)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    profile_pic = models.ImageField(upload_to= 'media/', null=True)
    bio = models.TextField(max_length=500, blank=True,null=True)
    country = models.CharField(max_length=255, blank=True,null=True )
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True,null=True)
    age = models.IntegerField(null=True)
    interests = models.CharField(max_length=30,null=True)
    


    # interests = models.ManyToManyField(Subject, related_name='interested_students')
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

