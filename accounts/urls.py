from django.conf.urls import url
from . import views

app_name='accounts'

urlpatterns = [
    url(r'^signup/$', views.SignUp.as_view(), name='signup'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_request,  name='logout'),
]