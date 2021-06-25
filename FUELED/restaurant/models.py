from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Restaurant(models.Model):

    name = models.CharField('Restaurant Name', max_length=50)
    desc = models.TextField('Description',null=True, blank=True)
    locality = models.CharField('Area Name', max_length=50,null=True, blank=True)
    city = models.CharField(max_length=20,null=True, blank=True)
    state = models.CharField(max_length=50,null=True, blank=True)
    country = models.CharField(max_length=50,null=True, blank=True)
    longi = models.FloatField('Longitude', null=True, blank=True)
    latit = models.FloatField('Latitude', null=True, blank=True)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Review(models.Model):

    restaurant = models.ForeignKey(Restaurant, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    review = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True)

    # class Meta:
    #     unique_together = ['restaurant', 'review']
    #     ordering = ['review']

    def __str__(self):
        return self.review[:50]


class Comment(models.Model):

    review = models.ForeignKey(Review, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment[:50]


class ThumbDown(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)


class Visited(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
