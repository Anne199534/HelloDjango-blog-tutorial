from django.shortcuts import render,get_object_or_404
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
from .models import Post,Category,Tag
from django.views.generic import ListView,DetailView
import markdown
from pure_pagination  import PaginationMixin
import re


# Create your views here.
from django.http import HttpResponse


# def index(request):
#     post_list = Post.objects.all().order_by('-created_time')
#     return render(request,'blog/index.html',context={'post_list':post_list})

# def category(request,pk):
#     cate = get_object_or_404(Category,pk=pk)
#     post_list = Post.objects.filter(category=cate).order_by('-created_time')
#     return render(request,'blog/index.html',context={'post_list':post_list})

def archive(request,year,month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month).order_by('-created_time')
    return render(request,'blog/index.html',context={'post_list':post_list})



# def tag(request,pk):
#     t = get_object_or_404(Tag,pk=pk)
#     post_list = Post.objects.filter(tags=t).order_by('-created_time')
#     return render(request,'blog/index.html',context={'post_list':post_list})

# def detail(request,pk):
#     post = get_object_or_404(Post,pk=pk)
#     #阅读量+1
#     post.increase_views()
#     md = markdown.Markdown(
#                          extensions=[
#                              'markdown.extensions.extra',
#                              'markdown.extensions.codehilite',
#                              TocExtension(slugify=slugify),
#
#                          ])
#     post.body = md.convert(post.body)
#     m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>',md.toc,re.S)
#     post.toc = m.group(1) if m is not None else ''
#     return render(request,'blog/detail.html',context={'post':post})



#-------------------------------------------------- 将试图函数改写成视图类
class IndexView(PaginationMixin,ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    #指定paginate_by 属性后开启分页功能，其值代表每一页包含多少篇文章
    paginate_by = 10


class CategoryView(IndexView):
    def get_queryset(self):
        cate = get_object_or_404(Category,pk=self.kwargs.get('pk'))
        return super(CategoryView,self).get_queryset().filter(category=cate)

class TagView(IndexView):
    def get_queryset(self):
        t = get_object_or_404(Tag,pk=self.kwargs.get('pk'))
        return super(TagView,self).get_queryset().filter(category=t)


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get(self,request,*args,**kwargs):
        # 覆写 get 方法的目的是因为每当文章被访问一次，就得将文章阅读量 +1
        # get 方法返回的是一个 HttpResponse 实例
        # 之所以需要先调用父类的 get 方法，是因为只有当 get 方法被调用后，
        # 才有 self.object 属性，其值为 Post 模型实例，即被访问的文章 post
        response = super(PostDetailView,self).get(request,*args,**kwargs)

        #文章阅读量 +1
        #self.object的值就是被访问的文章
        self.object.increase_views()
        #视图必须返回一个HttpResponse对象
        return response
    def get_object(self, queryset=None):
        #复写get_object 方法的目的是因为需要对post的body值进行渲染
        post = super().get_object(queryset=None)
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            TocExtension(slugify=slugify),
        ])
        post.body = md.convert(post.body)
        m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
        post.toc = m.group(1) if m is not None else ''

        return post
