"""AlmaPro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from AlumniNetwork import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('home/', views.home),
    path('about/', views.about),
    path('contact/', views.contact),
    path('news/',views.news),
    path('data/',views.data),
    path('dashboard/',views.dashboard),
    path('notice/', views.NoticeListView.as_view(),name='notice_list'),
    path('notice/<int:pk>', views.NoticeDetailView.as_view()),

    path('myprofile/', views.MyProfileListView.as_view()),
    path('myprofile/<int:pk>', views.MyProfileDetailView.as_view()),
    path('myprofile/follow/<int:pk>', views.follow),
    path('myprofile/unfollow/<int:pk>', views.unfollow),

    path('', RedirectView.as_view(url="home/")),
]

