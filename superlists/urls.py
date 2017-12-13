from django.conf.urls import url
from django.contrib import admin

import lists.views

urlpatterns = [
    url(r'^$', lists.views.home_page, name='home')
]
