from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    def test_create_success_user_with_email(self):
        """Test creating new user succesfully with email"""
        email = "alirzayev@caspiansoft.com"
        password = "Secret1223"
        user = get_user_model().objects \
            .create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalizer(self):
        """ Test make new user email normalizer """
        email = "alirzayev@CASPIANSOFT.COM"
        user = get_user_model().objects \
            .create_user(email, "pass1234")

        self.assertEqual(user.email, email.lower())

    def test_new_user_email_validation(self):
        """ Test new user email is valid or not """
        with self.assertRaises(ValueError):
            get_user_model().objects \
                .create_user(None, "pass1234")

    def test_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'alirzayev@caspiansoft.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
