from django.core.urlresolvers import reverse
from django.contrib import auth
from django.test import TestCase

from accounts.tests.mixins import CreateUserMixin


User = auth.get_user_model()


class WelcomeViewTest(CreateUserMixin, TestCase):

    def setUp(self):
        """Setup test data for every test method, created new user."""
        self.user = self.create_user(username='Boris', email='boris@gmail.com')

    def test_welcome_view_url_exists_at_desired_location(self):
        resp = self.client.get('/googlemaps/welcome/')
        self.assertNotEquals(resp.status_code, 404)

    def test_welcome_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('google_maps:welcome'))
        self.assertNotEqual(resp.status_code, 404)

    def test_welcome_view_redirect_if_not_logged_in(self):
        """Test that Welcome view redirects user to login page if not logged in."""
        resp = self.client.get(reverse('google_maps:welcome'))
        self.assertRedirects(resp, '/accounts/login/?next=/googlemaps/welcome/')

    def test_welcome_view_uses_correct_template_when_logged_in(self):
        """Test that Welcome view uses the correct template when user is logged in """
        self.client.login(username=self.user.username, password=self.password)
        resp = self.client.get(reverse('google_maps:welcome'))
        self.assertEquals(resp.status_code, 200)
        self.assertTemplateUsed((resp, 'google_maps/welcome.html'))
