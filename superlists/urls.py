from django.conf.urls import url
from django.contrib import admin
import lists

urlpatterns = [
    url(r'^$', lists.views.home_page, name='home')
]
