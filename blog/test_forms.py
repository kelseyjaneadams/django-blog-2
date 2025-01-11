from django.test import TestCase
from .forms import CommentForm


class TestCommentForm(TestCase):
    """
    Test suite for the `CommentForm` in the application.
    """

    def test_form_is_valid(self):
        """
        Tests if the form is valid when the 'body' field is provided.

        - A valid form instance is created with the 'body' field filled.
        - Verifies that the `is_valid()` method returns `True`.
        """
        # Create a form instance with a valid 'body' field
        comment_form = CommentForm({'body': 'This is a great post'})
        # Assert that the form is valid
        self.assertTrue(comment_form.is_valid(), msg="Form is invalid")

    def test_form_is_invalid(self):
        """
        Tests if the form is invalid when the 'body' field is empty.

        - The 'body' field is left empty.
        - Verifies that the `is_valid()` method returns `False`.
        - Ensures the form's errors include a validation error for the 'body' field.
        """
        # Create a form instance with an empty 'body' field
        comment_form = CommentForm({'body': ''})
        # Assert that the form is invalid
        self.assertFalse(comment_form.is_valid(), msg="Form is valid")
        # Check if the 'body' field is listed in the errors
        self.assertIn('body', comment_form.errors, msg="No error for 'body' field")
