from django.conf.urls import  url
from django.views import static
from django.conf import settings ##新增
from . import  views

app_name='blog'
urlpatterns=[
    url(r'^$',views.IndexView.as_view(),name='index'),
    #url(r'^post/(?P<pk>[0-9]+)/$',views.PostDetailView.as_view(),name='detail'),
    url(r'^post/(?P<pk>[0-9]+)/$',views.detail,name='detail'),
    url(r'^archive/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',views.ArchiveView.as_view(),name='archive'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='media'),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),
]
