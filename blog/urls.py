#!/usr/bin/env python
# coding:utf-8
"""
Name : urls
Author  : anne
Time    : 2019-12-25 11:56
Desc:
"""
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('posts/<int:pk>/',views.PostDetailView.as_view(),name='detail'),
    path('archives/<int:year>/<int:month>/',views.archive,name='archive'),
    path('categories/<int:pk>/', views.CategoryView.as_view(), name='category'),
    path('tags/<int:pk>/', views.TagView.as_view(), name='tag'),
]