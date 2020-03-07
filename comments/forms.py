#!/usr/bin/env python
# coding:utf-8
"""
Name : forms
Author  : anne
Time    : 2019-12-26 20:36
Desc:
"""
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','email','url','text']
