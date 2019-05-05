from django.conf.urls import url
from . import views


app_name='posts'

urlpatterns = [
    url(r'^$',views.Postlist.as_view(),name='all'),
    url(r'^new/$',views.Createpost.as_view(),name='create'),
    url(r'by/(?P<username>[-\w]+)',views.Userposts.as_view(),name='for_user'),
    url(r'by/(?P<username>[-\w]+)/(?P<pk>\d+)/$', views.Postdetail.as_view(), name='single'),
    url(r'delete/(?P<pk>\d+)/$',views.Deletepost.as_view(),name='delete')



]
