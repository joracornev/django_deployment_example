from django.db import models
from django.contrib.auth.models import User#
# Create your models here.

class UserProfileInfo(models.Model):#

    user = models.OneToOneField(User, on_delete = models.CASCADE )# one to one is extemded field to User class
# additional classes

    portfolio_site = models.URLField(blank = True)#
    profile_pic = models.ImageField(upload_to ='profile_pics', blank = True) #'[profile_pics]'-dir inside of [media]dir

    def __str__(self):
        return self.user.username
