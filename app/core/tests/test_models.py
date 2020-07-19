from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with email is successful"""
        email = 'test@blahblah.com'
        password = 'password1'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
            )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for the new user is normalized/case sensitive"""
        email = 'test@BLAHBlah.com'
        user = get_user_model().objects.create_user(email, 'test123')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """user with invalid email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_craete_new_superuser(self):
        """test creating a super user"""
        user = get_user_model().objects.create_super_user(
            'test@blahblah.com',
            'password1'
            )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
