from django.test import TestCase

from accounts.forms import UserForm, RegisterForm
from . mixins import CreateUserMixin

from django.contrib.auth.models import User


class UserFormTest(CreateUserMixin, TestCase):

    def setUp(self):
        self.form = UserForm()
        self.user = self.create_user(username='Mate', email='boris@gmail.com')

    def test_user_form_user_field_label(self):
        self.assertIsNone(self.form.fields['username'].label)

    def test_user_form_password_field_label(self):
        self.assertIsNone(self.form.fields['password'].label)

    def test_user_form_is_valid(self):
        form = UserForm(data={'username': self.user.username, 'password': self.password})
        self.assertTrue(form.is_valid())

    def test_user_form_is_invalid(self):
        form = UserForm(data={'username': self.user.username, 'password': '1234'})
        self.assertFalse(form.is_valid())


class RegisterFormTest(CreateUserMixin, TestCase):

    def setUp(self):
        self.form = RegisterForm()
        self.user = self.create_user(username='Boris', email='boris@gmail.com')
        self.form_data = {'username': 'User1', 'password': self.password, 'password1': self.password, 'email': self.user.email}

    def test_registration_form_user_field_label(self):
        self.assertTrue(self.form.fields['username'].label == 'Username')

    def test_registration_form_password_field_label(self):
        self.assertIsNone(self.form.fields['password'].label)

    def test_registration_form_confirm_password_field_label(self):
        self.assertTrue(self.form.fields['password1'].label == 'Confirm password')

    def test_registration_form_is_invalid_passwords_not_match(self):
        self.form_data['password1'] = 12345
        form = RegisterForm(data=self.form_data)
        self.assertFalse(form.is_valid())

    def test_registration_form_is_invalid_mail_already_exists(self):
        form = RegisterForm(data=self.form_data)
        self.assertFalse(form.is_valid())

    def test_registration_form_is_invalid_user_does_already_exist(self):
        form = RegisterForm(data=self.form_data)
        self.assertFalse(form.is_valid())

    def test_registration_form_is_valid(self):
        """Form validation passes when correct data is sent."""
        self.form_data['email'] = 'boris@gmai1.com'
        form = RegisterForm(data=self.form_data)
        self.assertTrue(form.is_valid())










