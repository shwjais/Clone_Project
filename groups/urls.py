from django.conf.urls import url
from . import views


app_name = 'groups'

urlpatterns = [
    url(r'^$',views.Listgroups.as_view(),name='all'),
    url(r'^new/$',views.Creategroup.as_view(),name='create'),
    url(r'posts/in/(?P<slug>[-\w]+)/$',views.Singlegroup.as_view(),name='single'),
    url(r'leave/(?P<slug>[-\w]+)/$', views.Leavegroup.as_view(), name='leave'),
    url(r'join/(?P<slug>[-\w]+)/$',views.Joingroup.as_view(),name='join')



]
