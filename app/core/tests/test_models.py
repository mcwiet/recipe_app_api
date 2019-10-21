from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def sample_user(email='test@test.com', password='testpasss'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@mike.com'
        password = '1password'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_normalize_user_email(self):
        """Test that email gets normalized to lowercase when creating user"""
        email = 'test@MIKE.COM'
        user = get_user_model().objects.create_user(email, '1password')

        self.assertEqual(user.email, email.lower())

    def test_valid_email_address(self):
        """Test that an creating a user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '1pass')

    def test_create_super_user(self):
        """Test create super user that is staff and super user"""
        user = get_user_model().objects.create_superuser(
            'email@email.com',
            '1password'
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_tag_str(self):
        """Test tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)
