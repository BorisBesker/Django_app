from django.contrib.auth.models import User
import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    password = factory.PostGenerationMethodCall('set_password', 'defaultpassword')
