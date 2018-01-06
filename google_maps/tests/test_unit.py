from django.test import TestCase

from google_maps.models import Location


class LocationModelTest(TestCase):

    def setUp(self):
        """Setup test data for every test method, creates new location."""
        Location.objects.create(name='Split')

    def test_location_model_name_label(self):
        """Test location model name field has correct label."""
        location = Location.objects.get(name='Split')
        field_label = location._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_location_model_date_label(self):
        """Test location model date field has correct label """
        location = Location.objects.get(name='Split')
        field_label = location._meta.get_field('dates').verbose_name
        self.assertEqual(field_label, 'dates')

    def test_location_model_name_field_max_length(self):
        """Test location model name field has correct max length."""
        location = Location.objects.get(name='Split')
        max_length = location._meta.get_field('name').max_length
        self.assertEqual(max_length, 128)
