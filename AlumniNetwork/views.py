from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from AlumniNetwork.models import Notice, Profile, MyProfile, FollowUser
from django.db.models import Q
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from django.template.backends.django import Template


# Create your views here.
def home(request):
    return render(request, 'AlumniNetwork/home.html')


def about(request):
    return render(request, 'AlumniNetwork/about.html')


def contact(request):
    return render(request, 'AlumniNetwork/contact.html')


def news(request):
    return render(request, 'AlumniNetwork/news.html')


def data(request):
    my_variable = "Hello World !"
    years_old = 15
    array_city_capitale = ["Paris", "London", "Washington"]
    return render(request, 'AlumniNetwork/index.html',
                  {"my_var": my_variable, "years": years_old, "array_city": array_city_capitale})


def dashboard(request):
    return render(request, 'AlumniNetwork/dashboard.html')


class NoticeListView(ListView):
    model = Notice

    def get_queryset(self):
        si = self.request.GET.get('si')
        if si == None:
            si = ''
        if self.request.user.is_superuser:
            return Notice.objects.filter(Q(msg__icontains=si) | Q(subject__icontains=si)).order_by('-id')
        else:
            return Notice.objects.filter(Q(branch__isnull=True) | Q(branch=self.request.user.profile.branch)).filter(
                Q(msg__icontains=si) | Q(subject__icontains=si)).order_by('-id')


class NoticeDetailView(DetailView):
    model = Notice


class MyProfileListView(ListView):
    model = MyProfile

    def get_queryset(self):
        si = self.request.GET.get("si")
        if si == None:
            si = ""
        profList = MyProfile.objects.filter(
            Q(name__icontains=si) | Q(address__icontains=si) | Q(gender__icontains=si) | Q(
                status__icontains=si)).order_by("-id");
        for p1 in profList:
            p1.followed = False
            ob = FollowUser.objects.filter(profile=p1, followed_by=self.request.user.myprofile)
            if ob:
                p1.followed = True
        return profList


class MyProfileDetailView(DetailView):
    model = MyProfile


def follow(req, pk):
    user = MyProfile.objects.get(pk=pk)
    FollowUser.objects.create(profile=user, followed_by=req.user.myprofile)
    return HttpResponseRedirect(redirect_to="/social/myprofile")


def unfollow(req, pk):
    user = MyProfile.objects.get(pk=pk)
    FollowUser.objects.filter(profile=user, followed_by=req.user.myprofile).delete()
    return HttpResponseRedirect(redirect_to="/social/myprofile")
