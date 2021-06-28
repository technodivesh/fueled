from rest_framework.test import APITestCase
from rest_framework import status


from restaurant.models import Restaurant

from django.contrib.auth import get_user_model
User = get_user_model()
# from fldUser.models import User


class RestaurantAPITestCase(APITestCase):


    def setUp(self):
        user = User(username='testuser', email='test@test.com')
        user.set_password("testpasswd")
        user.save()
        resto = Restaurant.objects.create(
                name="test_test",
                added_by=user
                )

    def test_user_create(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    def test_resto_create(self):
        resto_count = Restaurant.objects.count()
        self.assertEqual(resto_count, 1)

    
    def test_resto_post(self):
        user = User.objects.first()
        url = "http://localhost:8000/api/restaurants/"
        data = {"name": "SomeResto","added_by":user.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # def test_review_post(self):
    #     resto = Restaurant.objects.first()
    #     url = "http://localhost:8000/api/restaurants/"
    #     data = {"name": "SomeResto","added_by":user.id}
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

