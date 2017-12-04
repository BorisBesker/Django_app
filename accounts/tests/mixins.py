from . factories import UserFactory


class CreateUserMixin:

    password = '123'

    def create_user(self, username, email):
        return UserFactory(username=username, password=self.password, email=email)









