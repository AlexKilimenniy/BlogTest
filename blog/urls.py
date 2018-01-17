from django.conf.urls import url
from blog.views import PostsListView, addlike

urlpatterns = [
    url(r'^$', PostsListView.as_view(), name='blog'),
    url(r'^post/addlikes/(?P<pk>\d+)/$', addlike, name='post_like')
]