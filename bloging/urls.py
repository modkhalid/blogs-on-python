from django.conf.urls import url ,include
from . import views

urlpatterns=[
    url(r'^$',views.PostListView.as_view(),name='post_list'),
    url(r'^post/(?P<pk>\d+)/$',views.PostDetailView.as_view(),name='post_detail'),
    url(r'^about/$',views.About.as_view(),name='about'),
    url(r'^post/(?P<pk>\d+)/edit/$',views.PostUpdateView.as_view(),name='edit_post'),
    url(r'^post/new/$',views.PostCreateView.as_view(),name='create_post'),
    url(r'^post/(?P<pk>\d+)/delete/$',views.PostDeleteView.as_view(),name="delete_post"),
    url(r'^draft/$',views.PostDraftView.as_view(),name='post_draft'),
    url(r'^post/(?P<pk>\d+)/comment/$',views.PostComment,name='post_comment'),
    url(r'comment/(?P<pk>\d+)/approve/$',views.AproveComment,name='comment_approve'),
    url(r'comment/(?P<pk>\d+)/remove$',views.CommentRemove,name='comment_remove'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.PostPublish, name='post_publish'),
]
