#!/usr/bin/env python
# coding:utf-8
"""
Name : urls
Author  : anne
Time    : 2019-12-26 21:59
Desc:
"""
from django.urls import path
from . import views

app_name = 'comments'
urlpatterns = [
    path('comment/<int:post_pk>',views.comment,name='comment'),
]