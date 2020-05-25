from django.contrib import admin
from django.contrib.admin import ModelAdmin

from AlumniNetwork.models import Branch, Profile, Notice, FollowUser, MyProfile

admin.site.register(Branch)
admin.site.register(Profile)


# Register your models here.
class NoticeAdmin(admin.ModelAdmin):
    list_filter = ["cr_date", "branch"]
    list_display = ["subject", "cr_date"]
    search_fields = ["subject", "msg"]


admin.site.register(Notice, NoticeAdmin)


class FollowUserAdmin(ModelAdmin):
    list_display = ["profile", "followed_by"]
    search_fields = ["profile", "followed_by"]
    list_filter = ["profile", "followed_by"]


admin.site.register(FollowUser, FollowUserAdmin)


class MyProfileAdmin(ModelAdmin):
    list_display = ["name"]
    search_fields = ["name", "status", "phone_no"]
    list_filter = ["status", "gender"]


admin.site.register(MyProfile, MyProfileAdmin)
