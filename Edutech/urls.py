from django.conf.urls import url
from . import views
from django.urls import path
urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^home/$', views.home, name='home'),
    url(r'^profile/$', views.profile, name='profile'),
    path('update/',views.update_profile, name='update_profile' )
    
]