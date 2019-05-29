from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post,Category
import markdown
from comments.forms import CommentForm
# Create your views here.

def index(request):
    """

    :param request:
    :return:
     #return HttpResponse("Welcome!!!")
    return  render(request,'blog/index.html',context={
        'title':'我的博客首页',
        'welcome':'欢迎访问我的博客首页',
    })
    """
    #- 号表示逆序，如果不加 - 则是正序。
    post_list=Post.objects.all().order_by('-createTime')
    return  render(request,'blog/index.html',context={
        'post_list':post_list,
    })

def detail(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.boby=markdown.markdown(post.boby,
                                extensions=[
                                    'markdown.extensions.extra',
                                    'markdown.extensions.codehilite',
                                    'markdown.extensions.toc',
                                ])
    form =CommentForm()

    comment_list=post.comment_set.all()
    return  render(request,'blog/detail.html',context={
        'post':post,
        'form':form,
        'comment_list':comment_list,
    })

#归档
def archive(request,year,month):
    post_list=Post.objects.filter(createTime__year=year,createTime__month=month).order_by('-createTime')
    return render(request,'blog/index.html',context={'post_list':post_list})

#分类
def category(request,pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-createTime')
    return render(request, 'blog/index.html', context={'post_list': post_list})