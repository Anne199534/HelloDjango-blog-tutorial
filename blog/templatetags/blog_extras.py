#!/usr/bin/env python
# coding:utf-8
"""
Name : blog_extras
Author  : anne
Time    : 2019-12-26 15:57
Desc:
"""
from django import template
from ..models import Post,Category,Tag
register = template.Library()

@register.inclusion_tag('blog/inclusions/_recent_posts.html', takes_context=True)
def show_recent_posts(context,num=5):
    return{
        'recent_post_list':Post.objects.all().order_by('-created_time')[:num],
    }

@register.inclusion_tag('blog/inclusions/__archives.html', takes_context=True)
def show_archives(context):
    return{
        'date_list':Post.objects.dates('created_time','month',order='DESC'),
    }

@register.inclusion_tag('blog/inclusions/_categories.html', takes_context=True)
def show_categories(context):
    return {
        'category_list': Category.objects.all(),
    }
@register.inclusion_tag('blog/inclusions/_tags.html', takes_context=True)
def show_tags(context):
    return {
        'tag_list': Tag.objects.all(),
    }

