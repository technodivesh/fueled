from rest_framework.test import APITestCase
from rest_framework import status


# from restaurant.models import Restaurant

from django.contrib.auth import get_user_model
User = get_user_model()
# from fldUser.models import User

class UserAPITestCase(APITestCase):


    def setUp(self):
        user = User(username='testuser', email='test@test.com')
        user.set_password("testpasswd")
        user.save()

    def test_user_create(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)


    def test_user_post(self):
        url = "http://localhost:8000/api/users/"
        data = {"username": "testUserPost","email":"testUserPost@test.com"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)