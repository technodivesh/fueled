from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):

    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=244,verbose_name='email address', unique=True)
    # password = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
      return self.username


# #Create your models here.
# class Profile(models.Model):

#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     emp_id = models.IntegerField('Emp Id',null=True, blank=True)
#     last_location = models.CharField('Last Location',max_length=100, null=True, blank=True)

#     def __str__(self):
#       return self.user.username

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()


# Reference from
# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html
