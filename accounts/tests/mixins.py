from django.contrib.auth.models import User

from . factories import UserFactory


class CreateUserMixin:

    password = '123'

    def create_user(self, username, email):
        return UserFactory(username=username, password=self.password, email=email)







# User.objects.create_user(username='boris', password='123', email='boris@gmail.com')


