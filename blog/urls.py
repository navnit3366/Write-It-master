from django.conf.urls import url
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='blog-home'),
    url(r'^about/$', views.about, name='blog-about'),
    url(r'^post/(?P<pk>[0-9]+)/$', PostDetailView.as_view(), name='post-detail'),
    url(r'^post/new/$', PostCreateView.as_view(), name='post-create'),
    url(r'^post/(?P<pk>[0-9]+)/update/$', PostUpdateView.as_view(), name='post-update'),
    url(r'^post/(?P<pk>[0-9]+)/delete/$', PostDeleteView.as_view(), name='post-delete'),
    url(r'^user/(?P<username>[a-zA-Z0-9_\-]+)/$', UserPostListView.as_view(), name='user-posts')
]
