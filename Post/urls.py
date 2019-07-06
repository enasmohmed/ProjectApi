from django.conf.urls import url

from Post.views import PostDetail, PostList, PostDelete, PostViewSet
from.import views

app_name='Post'

urlpatterns = [
    url(r'^$', views.all_posts, name='all_posts'),
    url(r'^(?P<id>\d+)$', views.post, name='post'),
    url(r'^create$', views.create_post, name='create_post'),
    url(r'^(?P<id>\d+)/edit$', views.edit_post, name='edit_post'),
    url(r'^(?P<id>\d+)/delete$', views.delete_post, name='delete_post'),
    url(r'^post/$', PostList.as_view(), name='Post_list'),
    url(r'^postdetail/(?P<Post_id>[0-30]+)/$', PostDetail.as_view(), name='PostDetail'),
    url(r'^postdelete/(?P<Post_id>[0-30]+)/$', PostDelete.as_view(), name='PostDelete'),
]
