from django.core.urlresolvers import reverse
from django.test import TestCase

from accounts.tests.mixins import CreateUserMixin
from google_maps.models import DateVisited


class WelcomeViewTest(CreateUserMixin, TestCase):

    def setUp(self):
        """Setup test data for every test method, creates new user."""
        self.user = self.create_user(username='Boris', email='boris@gmail.com')

    def test_welcome_view_url_exists(self):
        """Tests that login view exists at desired location."""
        resp = self.client.get('/googlemaps/welcome/')
        self.assertNotEqual(resp.status_code, 404)

    def test_welcome_view_url_access(self):
        """Tests that login view is accessible by name."""
        resp = self.client.get(reverse('google_maps:welcome'))
        self.assertNotEqual(resp.status_code, 404)

    def test_welcome_view_redirect(self):
        """Test that welcome view redirects user to login page if not logged in."""
        resp = self.client.get(reverse('google_maps:welcome'))
        self.assertRedirects(resp, '/accounts/login/?next=/googlemaps/welcome/')

    def test_welcome_view_corr_temp(self):
        """Test that Welcome view uses the correct template when user is logged in."""
        self.client.login(username=self.user.username, password=self.password)
        resp = self.client.get(reverse('google_maps:welcome'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed((resp, 'google_maps/welcome.html'))


class ListLocationsView(CreateUserMixin, TestCase):

    def setUp(self):
        """Setup test data for every test method, creates new user."""
        self.user = self.create_user(username='Boris', email='boris@gmail.com')

    def test_locations_view_url_exists(self):
        """Tests that list locations view exists at desired location."""
        resp = self.client.get('/googlemaps/location/')
        self.assertNotEqual(resp.status_code, 404)

    def test_locations_view_url_access(self):
        """Tests that list locations view is accessible by name."""
        resp = self.client.get(reverse('google_maps:locations_list'))
        self.assertNotEqual(resp.status_code, 404)

    def test_locations_view_redirect(self):
        """Test that list locations view redirects user to login page if not logged in."""
        resp = self.client.get(reverse('google_maps:locations_list'))
        self.assertRedirects(resp, '/accounts/login/?next=/googlemaps/location/')

    def test_locations_view_corr_temp(self):
        """Test that list locations view uses the correct template when user is logged in."""
        self.client.login(username=self.user.username, password=self.password)
        resp = self.client.get(reverse('google_maps:locations_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed((resp, 'google_maps/locations.html'))

    def test_locations_view_post_vd(self):
        """Test that list locations view, handles the post request successfully, saves DateVisited
        record and returns the saved location."""
        location = {'place': 'Split'}
        self.client.login(username=self.user.username, password=self.password)
        resp = self.client.post(reverse('google_maps:locations_list'), location)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(DateVisited.objects.get(location__name=location['place']))
        self.assertJSONEqual(str(resp.content, encoding='utf8'), location)

    def test_locations_view_post_id(self):
        """Test that list locations view, handles the  post request with invalid data successfully
        and raises 400 error."""
        location = {'place': '指事字'}
        self.client.login(username=self.user.username, password=self.password)
        resp = self.client.post(reverse('google_maps:locations_list'), location)
        self.assertEqual(resp.status_code, 400)
