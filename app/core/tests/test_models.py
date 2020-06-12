from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):


    def test_create_user_with_email(self):
        """ Test creating a new user with an email """

        email = 'test@gmail.com'
        password = 'Testpass123'
        is_active=True
        user = get_user_model().objects.create_user(
            email = email,
            password = password,
            is_active=is_active
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))
        self.assertEqual(user.is_active,is_active)

    def test_new_user_email_normalized(self):
        """ Test the email for a new user is normalized """ 
        email ='test@gMAIL.com'
        user = get_user_model().objects.create_user(email,'pass123')

        self.assertEqual(user.email,email.lower())

    def test_new_user_invalid_email(self):
        """ Test creating user with no email raises error """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,"pass123")

    def test_create_new_superuser(self):
        """ Test creating a new superuser """
        user = get_user_model().objects.create_superuser(
            'test@gmai.com', 
            'pass123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
