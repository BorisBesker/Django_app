from django.contrib import auth
from django.core.urlresolvers import reverse
from django.test import TestCase

from . mixins import CreateUserMixin


User = auth.get_user_model()


class LoginViewTest(CreateUserMixin, TestCase):

    def setUp(self):
        """Setup test data for every test method, creates new user."""
        self.user = self.create_user(username='Boris', email='boris@gmail.com')

    def test_login_view_url_exists_at_desired_location(self):
        """Tests that login view exists at desired location"""
        resp = self.client.get('/accounts/login/')
        self.assertNotEquals(resp.status_code, 404)

    def test_login_view_url_accessible_by_name(self):
        """Tests that login view is accessible by name"""
        resp = self.client.get(reverse('accounts:login'))
        self.assertNotEqual(resp.status_code, 404)

    def test_login_view_get_uses_correct_template_not_logged_in(self):
        """Test that login view uses the correct template when user sends GET request and user is not logged in"""
        resp = self.client.get(reverse('accounts:login'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed((resp, 'accounts/login.html'))

    def test_login_view_get_successful_redirect_logged_in(self):
        """Test that login view redirects the user if logged in, on GET request"""
        self.client.login(username=self.user.username, password=self.password)
        resp = self.client.get(reverse('accounts:login'))
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, '/googlemaps/welcome/')

    def test_login_view_post_user_logged_in(self):
        """Test that login view logs the User, and redirects him when validation passes after POST request. """
        resp = self.client.post(reverse('accounts:login'), {'username': self.user.username, 'password': self.password})
        user = auth.get_user(self.client)
        self.assertTrue(user.is_authenticated())
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, '/googlemaps/welcome/')

    def test_login_view_post_invalid_login(self):
        """Test that login view uses the correct template when validation fails. """
        resp = self.client.post(reverse('accounts:login'), {'username': self.user.username, 'password': 'invalid'})
        self.assertEquals(resp.status_code, 200)
        self.assertTemplateUsed((resp, 'accounts/login.html'))


class RegisterViewTest(CreateUserMixin, TestCase):

    def setUp(self):
        """Setup test data for every test method, creates new user."""
        self.user = self.create_user(username='Boris', email='boris@gmail.com')

    def test_register_view_url_exists_at_desired_location(self):
        """Tests that login view exists at desired location"""
        resp = self.client.get('/accounts/register/')
        self.assertNotEquals(resp.status_code, 404)

    def test_register_view_url_accessible_by_name(self):
        """Tests that login view is accessible by name"""
        resp = self.client.get(reverse('accounts:register'))
        self.assertNotEqual(resp.status_code, 404)

    def test_login_view_get_uses_correct_template_not_logged_in(self):
        """Test that register view uses the correct template when user sends GET request and user is not logged in"""
        resp = self.client.get(reverse('accounts:register'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed((resp, 'accounts/registration.html'))

    def test_register_view_get_successful_redirect_logged_in(self):
        """Test that register view redirects the user if logged in, on GET request"""
        self.client.login(username=self.user.username, password=self.password)
        resp = self.client.get(reverse('accounts:register'))
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, '/googlemaps/welcome/')

    def test_register_view_post_user_successful_registration(self):
        """Test that register view registers the User, logs and redirects him when validation passes after POST
        request. """
        resp = self.client.post(reverse('accounts:register'), {'username': 'booris', 'email': 'boriss@gmail.com', 'password': 'boris', 'password1': 'boris'})
        user_registered = User.objects.filter(username='booris').exists()
        self.assertTrue(user_registered)
        user = auth.get_user(self.client)
        self.assertTrue(user.is_authenticated())
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, '/googlemaps/welcome/')

    def test_register_view_post_user_unsuccessful_registration(self):
        """Test that register view does not register user and uses the correct template when validation fails after POST
        request. """
        resp = self.client.post(reverse('accounts:register'), {'username': self.user.username, 'email': 'wrong@mail.com', 'password': self.password, 'password1': self.password})
        user_registered = User.objects.filter(email='wrong@mail.com').exists()
        self.assertFalse(user_registered)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed((resp, 'accounts/registration.html'))


class LogoutViewTest(CreateUserMixin, TestCase):
    """Integration tests for LogoutView, every method of LoginViewTest except setUp is a test case for different
      functionality
      """
    def setUp(self):
        """Setup test data for every test method, creates new user."""
        self.user = self.create_user(username='Boris', email='boris@gmail.com')

    def test_logout_view_url_exists_at_desired_location(self):
        """Tests that logout view exists at desired location"""
        resp = self.client.get('/accounts/logout/')
        self.assertNotEquals(resp.status_code, 404)

    def test_logout_view_url_accessible_by_name(self):
        """Tests that logout view is accessible by name"""
        resp = self.client.get(reverse('accounts:logout'))
        self.assertNotEqual(resp.status_code, 404)

    def test_Logout_redirect_if_not_logged_in(self):
        """Tests that logout view redirects the user if not logged in"""
        resp = self.client.get(reverse('accounts:logout'))
        self.assertRedirects(resp, '/accounts/login/?next=/accounts/logout/')

    def test_logout_view_login_successful_redirect(self):
        """Tests that logout view redirects the user successfully to correct url"""
        self.client.login(username=self.user.username, password=self.password)
        resp = self.client.get(reverse('accounts:logout'))
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, '/accounts/login/')
