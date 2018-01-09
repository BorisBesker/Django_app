from django.test import TestCase

from accounts.forms import UserForm, RegisterForm
from . mixins import CreateUserMixin


class UserFormTest(CreateUserMixin, TestCase):

    def setUp(self):
        """Setup test data for every test method, creates new user and instantiated new UserForm"""
        self.form = UserForm()
        self.user = self.create_user(username='Mate', email='boris@gmail.com')

    def test_user_form_user_label(self):
        """Test UserForm check if correct label is rendered, also test whether the label value is
        None, because even though Django will render the correct label it returns None if the value
        is not explicitly set.
        """
        self.assertIsNone(self.form.fields['username'].label)

    def test_user_form_password_label(self):
        """Test UserForm to check if correct label is rendered, also test whether the label value is
        None, because even though Django will render the correct label it returns None if the value
        is not explicitly set.
        """
        self.assertIsNone(self.form.fields['password'].label)

    def test_user_form_is_valid(self):
        """Test UserForm validation passes when correct data is sent."""
        form = UserForm(data={'username': self.user.username, 'password': self.password})
        self.assertTrue(form.is_valid())

    def test_user_form_is_invalid(self):
        """Test UserForm validation fails when incorrect data is sent."""
        form = UserForm(data={'username': self.user.username, 'password': '1234'})
        self.assertFalse(form.is_valid())


class RegisterFormTest(CreateUserMixin, TestCase):

    def setUp(self):
        """Setup test data for every test method, creates new user and instantiated new
        RegisterForm. Initialized keys with values in form_data dictionary.
        """
        self.form = RegisterForm()
        self.user = self.create_user(username='Boris', email='boris@gmail.com')
        self.form_data = {
            'username': 'User1',
            'password': self.password,
            'password1': self.password,
            'email': self.user.email
        }

    def test_registration_form_u_label(self):
        """Test RegisterForm if correct user label is rendered. """
        self.assertTrue(self.form.fields['username'].label == 'Username')

    def test_registration_form_p_label(self):
        """Test RegisterForm to check if correct password label is rendered, also test whether the
        value is None, because even though Django will render the correct label it returns None if
        the value is not explicitly set.
        """
        self.assertIsNone(self.form.fields['password'].label)

    def test_registration_form_c_p_l(self):
        """Test RegisterForm to check if correct password label is rendered. """
        self.assertTrue(self.form.fields['password1'].label == 'Confirm password')

    def test_registration_form_p_no_match(self):
        """Test RegisterForm validation fails when user enters passwords that are not the same."""
        self.form_data['password1'] = 12345
        form = RegisterForm(data=self.form_data)
        self.assertFalse(form.is_valid())

    def test_registration_form_m_ex(self):
        """Test RegisterForm validation fails when email already exists."""
        form = RegisterForm(data=self.form_data)
        self.assertFalse(form.is_valid())

    def test_registration_form_u_exists(self):
        """Test RegisterForm validation fails when user already exists."""
        form = RegisterForm(data=self.form_data)
        self.assertFalse(form.is_valid())

    def test_registration_form_is_valid(self):
        """Test RegisterForm validation passes when correct data is sent."""
        self.form_data['email'] = 'boris@gmai1.com'
        form = RegisterForm(data=self.form_data)
        self.assertTrue(form.is_valid())
