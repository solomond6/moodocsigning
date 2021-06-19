from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^$', views.loginview, name='login'),
    url(r'^accounts/login/$', views.loginview),
    url(r'^accounts/authview/$', views.authview, name='authview'),
    url(r'^accounts/logout/$', views.logoutview, name='logoutview'),
    url(r'^accounts/loggedin/$', views.loggedin, name='loggedin'),
    url(r'^accounts/invalid/$', views.invalid, name='invalid_login'),
    url(r'^accounts/register/$', views.register_user, name='register_user'),
    url(r'^accounts/register_success/$', views.register_success, name='register_success'),
]