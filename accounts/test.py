from django.test import TestCase

from .serializers import UserSerializer
from .models import User


class UserSerializerTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='test')

    def test_get_serializer(self):
        serializer = UserSerializer(self.user)
        data = serializer.data
        print(data)
        self.assertEqual(data['user_name'], 'test')
    
    # def test_create_serializer(self):

