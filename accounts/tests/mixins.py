from . factories import UserFactory


class CreateUserMixin:
    password = '123'

    def create_user(self, username, email):
        """Creates the user for test data using UserFactory

        :param username:
        :param email:
        :return:
        """
        return UserFactory(username=username, password=self.password, email=email)
