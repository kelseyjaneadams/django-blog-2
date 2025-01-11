from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):
    """
    Test suite for the `CollaborateForm` in the application.
    """

    def test_form_is_valid(self):
        """
        Tests if the form is valid when all fields are provided.

        - A valid form instance is created with all required fields.
        - Verifies that the `is_valid()` method returns `True`.
        """
        # Create a form instance with all valid fields
        form = CollaborateForm({
            'name': 'Kelsey',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        # Assert that the form is valid
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_name_is_required(self):
        """
        Tests if the form is invalid when the 'name' field is missing.

        - The 'name' field is left empty.
        - Verifies that the `is_valid()` method returns `False`.
        - Ensures the form's errors include a validation error for the 'name' field.
        """
        # Create a form instance with an empty 'name' field
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        # Assert that the form is invalid
        self.assertFalse(
            form.is_valid(),
            msg="Name was not provided, but the form is valid"
        )
        # Check if the 'name' field is listed in the errors
        self.assertIn('name', form.errors, msg="No error for 'name' field")

    def test_email_is_required(self):
        """
        Tests if the form is invalid when the 'email' field is missing.

        - The 'email' field is left empty.
        - Verifies that the `is_valid()` method returns `False`.
        - Ensures the form's errors include a validation error for the 'email' field.
        """
        # Create a form instance with an empty 'email' field
        form = CollaborateForm({
            'name': 'Matt',
            'email': '',
            'message': 'Hello!'
        })
        # Assert that the form is invalid
        self.assertFalse(
            form.is_valid(),
            msg="Email was not provided, but the form is valid"
        )
        # Check if the 'email' field is listed in the errors
        self.assertIn('email', form.errors, msg="No error for 'email' field")

    def test_message_is_required(self):
        """
        Tests if the form is invalid when the 'message' field is missing.

        - The 'message' field is left empty.
        - Verifies that the `is_valid()` method returns `False`.
        - Ensures the form's errors include a validation error for the 'message' field.
        """
        # Create a form instance with an empty 'message' field
        form = CollaborateForm({
            'name': 'Matt',
            'email': 'test@test.com',
            'message': ''
        })
        # Assert that the form is invalid
        self.assertFalse(
            form.is_valid(),
            msg="Message was not provided, but the form is valid"
        )
        # Check if the 'message' field is listed in the errors
        self.assertIn('message', form.errors, msg="No error for 'message' field")
