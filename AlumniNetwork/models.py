from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, RegexValidator
from django.db import models

# Create your models here.
from django.db.models import CASCADE


class Branch(models.Model):
    name = models.CharField(max_length=100)
    hod = models.CharField(max_length=100)

    def __str__(self):
        return "%s (%s)" % (self.name, self.hod)


class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=CASCADE)
    name = models.CharField(max_length=100)
    branch = models.ForeignKey(to=Branch, on_delete=CASCADE, null=True)

    def __str__(self):
        return "%s (%s)" % (self.name, self.branch)


# Create your models here.
class Notice(models.Model):
    msg = models.TextField()
    cr_date = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=100)
    branch = models.ForeignKey(to=Branch, on_delete=CASCADE, null=True, blank=True)

    def __str__(self):
        return self.subject


class MyProfile(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(to=User, on_delete=CASCADE)
    age = models.IntegerField(default=18, validators=[MinValueValidator(18)])
    address = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, default="single", choices=(
    ("single", "single"), ("married", "married"), ("widow", "widow"), ("seprated", "seprated"),
    ("commited", "commited")))
    gender = models.CharField(max_length=20, default="female", choices=(("male", "male"), ("female", "female")))
    phone_no = models.CharField(validators=[RegexValidator("^0?[5-9]{1}\d{9}$")], max_length=15, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    pic = models.ImageField(upload_to="images\\", null=True)

    def __str__(self):
        return "%s" % self.user

class FollowUser(models.Model):
    profile = models.ForeignKey(to=MyProfile, on_delete=CASCADE, related_name="profile")
    followed_by = models.ForeignKey(to=MyProfile, on_delete=CASCADE, related_name="followed_by")
    def __str__(self):
        return "%s is followed by %s" % (self.profile, self.followed_by)