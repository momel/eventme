# -*- codding: utf-8 -*-

from django.conf.urls import url

app_path = 'eventme.apps.core.views.'

urlpatterns = [
    # url for main page
    url(r'^$', app_path + 'mainpage.main'),

    # url for 'Sign in', 'Sign out' and 'Sign up' actions
    url(r'^login/$', app_path + 'login.sign_in', name='login'),
    url(r'^logout/$', app_path + 'login.sign_out', name='logout'),
    url(r'^register/$', app_path + 'login.sign_up', name='register'),
]
