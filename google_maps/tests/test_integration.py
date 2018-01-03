from django.core.urlresolvers import reverse
from django.contrib import auth
from django.test import TestCase

from accounts.tests.mixins import CreateUserMixin
from google_maps.models import DateVisited


User = auth.get_user_model()


class WelcomeViewTest(CreateUserMixin, TestCase):

    def setUp(self):
        """Setup test data for every test method, creates new user."""
        self.user = self.create_user(username='Boris', email='boris@gmail.com')

    def test_welcome_view_url_exists_at_desired_location(self):
        """Tests that login view exists at desired location."""
        resp = self.client.get('/googlemaps/welcome/')
        self.assertNotEquals(resp.status_code, 404)

    def test_welcome_view_url_accessible_by_name(self):
        """Tests that login view is accessible by name."""
        resp = self.client.get(reverse('google_maps:welcome'))
        self.assertNotEqual(resp.status_code, 404)

    def test_welcome_view_redirect_if_not_logged_in(self):
        """Test that welcome view redirects user to login page if not logged in."""
        resp = self.client.get(reverse('google_maps:welcome'))
        self.assertRedirects(resp, '/accounts/login/?next=/googlemaps/welcome/')

    def test_welcome_view_uses_correct_template_when_logged_in(self):
        """Test that Welcome view uses the correct template when user is logged in."""
        self.client.login(username=self.user.username, password=self.password)
        resp = self.client.get(reverse('google_maps:welcome'))
        self.assertEquals(resp.status_code, 200)
        self.assertTemplateUsed((resp, 'google_maps/welcome.html'))


class ListLocationsView(CreateUserMixin, TestCase):

    def setUp(self):
        """Setup test data for every test method, creates new user."""
        self.user = self.create_user(username='Boris', email='boris@gmail.com')

    def test_list_locations_view_url_exists_at_desired_location(self):
        """Tests that list locations view exists at desired location."""
        resp = self.client.get('/googlemaps/location/')
        self.assertNotEquals(resp.status_code, 404)

    def test_list_locations_view_url_accessible_by_name(self):
        """Tests that list locations view is accessible by name."""
        resp = self.client.get(reverse('google_maps:locations_list'))
        self.assertNotEqual(resp.status_code, 404)

    def test_list_locations_view_redirect_if_not_logged_in(self):
        """Test that list locations view redirects user to login page if not logged in."""
        resp = self.client.get(reverse('google_maps:locations_list'))
        self.assertRedirects(resp, '/accounts/login/?next=/googlemaps/location/')

    def test_list_locations_view_uses_correct_template_when_logged_in(self):
        """Test that list locations view uses the correct template when user is logged in."""
        self.client.login(username=self.user.username, password=self.password)
        resp = self.client.get(reverse('google_maps:locations_list'))
        self.assertEquals(resp.status_code, 200)
        self.assertTemplateUsed((resp, 'google_maps/locations.html'))

    def test_list_locations_view_post_successful_valid_data(self):
        """Test that list locations view, handles the post request successfully, saves DateVisited record
        and returns the saved location."""
        location = {'place': 'Split'}
        self.client.login(username=self.user.username, password=self.password)
        resp = self.client.post(reverse('google_maps:locations_list'), location)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(DateVisited.objects.get(location__name=location['place']))
        self.assertJSONEqual(str(resp.content, encoding='utf8'), location)

    def test_list_locations_view_post_successful_invalid_data(self):
        """Test that list locations view, handles the invalid post request successfully and raises 400 error."""
        location = {'place': '指事字'}
        self.client.login(username=self.user.username, password=self.password)
        resp = self.client.post(reverse('google_maps:locations_list'), location)
        self.assertEqual(resp.status_code, 400)
