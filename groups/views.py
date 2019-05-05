from django.shortcuts import render
from django.contrib.auth.mixins import (LoginRequiredMixin,PermissionRequiredMixin)
from django.urls import reverse
from django.views import generic
from groups.models import Group,Groupmember
from django.shortcuts import get_object_or_404
from django.contrib import messages
from . import models
from django.db import IntegrityError

class Creategroup(LoginRequiredMixin,generic.CreateView):
    fields = ('name','description')
    model = Group

class Singlegroup(generic.DetailView):
    model = Group

class Listgroups(generic.ListView):
    model = Group

# Create your views here.
class Joingroup(LoginRequiredMixin,generic.RedirectView):


    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})


    def get(self,request,*args,**kwargs):
        group = get_object_or_404(Group,slug=self.kwargs.get('slug'))


        try:
            Groupmember.objects.create(user=self.request.user,group=group)

        except IntegrityError:
            messages.warning(self.request,'warning already member')


        else:
            messages.success(self.request,'You are now a member')


        return super().get(request,*args,**kwargs)


class Leavegroup(LoginRequiredMixin,generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})
    def get(self, request, *args, **kwargs):


        try:
            membership = models.Groupmember.objects.filter(
               user= self.request.user,
                group__slug = self.kwargs.get('slug')
            ).get()

        except models.Groupmember.DoesNotExist:
            messages.warning(self.request,'Sorry you are not in this group')

        else:
            membership.delete()
            messages.success(self.request,'you have left the group')
        return super().get(request,*args,**kwargs)

