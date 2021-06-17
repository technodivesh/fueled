from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    thumb_down = models.TextField()
    last_loc_longi = models.FloatField('Longitude', null=True, blank=True)
    last_loc_latit = models.FloatField('Latitude', null=True, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html
  # <li>Username: {{ user.username }}</li>
  # <li>Location: {{ user.profile.location }}</li>
  # users = User.objects.all().select_related('profile')