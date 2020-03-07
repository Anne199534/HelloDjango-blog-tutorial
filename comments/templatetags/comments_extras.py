#!/usr/bin/env python
# coding:utf-8
"""
Name : comments_extras
Author  : anne
Time    : 2019-12-26 21:15
Desc:
"""
from django import template
from ..forms import CommentForm

register = template.Library()

@register.inclusion_tag('comments/inclusions/_form.html',takes_context=True)
def show_comment_form(context,post,form=None):
    if form is None:
        form = CommentForm()
    return {
        'form':form,
        'post':post,
    }

@register.inclusion_tag('comments/inclusions/_list.html', takes_context=True)
def show_comments(context, post):
    comment_list = post.comment_set.all().order_by('-created_time')
    comment_count = comment_list.count()
    return {
        'comment_count': comment_count,
        'comment_list': comment_list,
    }