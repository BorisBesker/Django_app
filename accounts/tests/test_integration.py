from django.test import TestCase
from django.core.urlresolvers import reverse

from django.contrib import auth

from . mixins import CreateUserMixin


class LoginViewTest(CreateUserMixin, TestCase):

    def setUp(self):
        self.create_user(username='Boris', password='123', email='boris@gmail.com')

    def test_login_view_url_exists_at_desired_location(self):
        resp = self.client.get('/accounts/login/')
        self.assertNotEquals(resp.status_code, 404)

    def test_login_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('accounts:login'))
        self.assertNotEqual(resp.status_code, 404)

    def test_login_view_get_uses_correct_template_not_logged_in(self):
        resp = self.client.get(reverse('accounts:login'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed((resp, 'accounts/login.html'))

    def test_login_view_user_loged_in(self):
        #self.client.login(username='boris', password='123')
        resp = self.client.post(reverse('accounts:login'), {'username': 'boris', 'password': '123'})
        user = auth.get_user(self.client)
        self.assertTrue(user.is_authenticated())

      #  print(resp.context)
       # self.assertTrue(resp.context['User'].is_authenticated())
      #  print(resp.context)


 #  def test_login_view_get_successful_redirect_logged_in(self):
     #   self.client.login(username='boris', password='123')
       # resp = self.client.get(reverse('accounts:login'))
       # self.assertEqual(resp.status_code, 302)


class RegisterViewTest(CreateUserMixin, TestCase):

    def setUp(self):
        self.create_user(username='Boris', password='123', email='boris@gmail.com')

    def test_register_view_url_exists_at_desired_location(self):
        resp = self.client.get('/accounts/register/')
        self.assertNotEquals(resp.status_code, 404)

    def test_register_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('accounts:register'))
        self.assertNotEqual(resp.status_code, 404)


class LogoutViewTest(CreateUserMixin, TestCase):

    def setUp(self):
        self.create_user(username='Boris', password='123', email='boris@gmail.com')

    def test_logout_view_url_exists_at_desired_location(self):
        resp = self.client.get('/accounts/logout/')
        self.assertNotEquals(resp.status_code, 404)

    def test_logout_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('accounts:logout'))
        self.assertNotEqual(resp.status_code, 404)

    def test_Logout_redirect_if_not_logged_in(self):
        resp = self.client.get(reverse('accounts:logout'))
        self.assertRedirects(resp, '/accounts/login/?next=/accounts/logout/')

    def test_logout_view_login_successful_redirect(self):
        self.client.login(username='boris', password='123')
        resp = self.client.get(reverse('accounts:logout'))
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, '/accounts/login/')

