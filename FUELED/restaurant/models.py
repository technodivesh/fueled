from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Restaurant(models.Model):

    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=100,null=True,blank=True)
    location = models.CharField(max_length=100,null=True, blank=True)
    address = models.CharField(max_length=100,null=True,blank=True)
    city = models.CharField(max_length=50,null=True,blank=True)
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

    class Meta:
        # unique_together = ['restaurant', 'review']
        ordering = ['-created_on']

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

    # def __str__(self):
    #     return self.restaurant


class Visited(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.restaurant.name
