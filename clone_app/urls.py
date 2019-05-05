from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
app_name = 'clone_app'

urlpatterns = [
    url(r'login/$',auth_views.LoginView.as_view(template_name='clone_app/login.html'),name='login'),
    url(r'signup/$',views.Signup.as_view(), name='signup'),
    url(r'logout/$',auth_views.LogoutView.as_view(), name='logout'),

]