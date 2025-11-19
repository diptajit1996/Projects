from urllib import response

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class RegisterTestCase(APITestCase):
    def test_register(self):
        data = {
            "username": "testcase",
            "email": "testcase@example.com",
            "password": "NewPassword@123",
            "password2": "NewPassword@123"
        }
        response = self.client.post(reverse('register'), data)  # here we are sending a post request to the register and getting the response and storing it as temporarily database
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # here in assertEqual we are matching the response status code and status of http 201.


# Note: By default the status code response was 'ok' because of that it got run when we have put status.HTTP_200_OK.
# But if we want to compare another response status code than 1st we have to write status code in views.py because we are fetcing the response from urls.py and that urls name is coming from that method in views.py. So for that purpose we have to write status code in in that method in views.py, than compare the response which you have set in views.py same response you set over here. Then it will be correct otherwise it will show AssertionError.


class LoginLogoutTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="example", password="NewPassword@123")

    def test_login(self):
        data = {
            "username": "example",
            "password": "NewPassword@123"
        }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout(self):
        self.token = Token.objects.get(user__username="example")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
