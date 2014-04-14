from django.conf.urls import patterns, url
from MusicPost import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/', views.about, name='about'),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^welcome/$', views.welcome, name='welcome'),
        url(r'^logout/$', views.user_logout, name='logout'),)

