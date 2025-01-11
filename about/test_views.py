from django.test import TestCase
from django.urls import reverse
from .models import About, CollaborateRequest
from .forms import CollaborateForm


class TestAboutView(TestCase):
    """
    Test suite for the `about_me` view in the application.
    """

    def setUp(self):
        """
        Sets up the initial test data.

        - Creates an `About` instance to simulate the "About Me" content.
        - This ensures the database has the necessary data for testing
          the `about_me` view and its associated features.
        """
        self.about_content = About.objects.create(
            title="About Me",
            content="This is about me."
        )

    def test_render_about_page_with_collaborate_form(self):
        """
        Tests the rendering of the About page.

        - Verifies the page successfully loads with an HTTP 200 response.
        - Confirms the About Me content appears in the rendered page.
        - Ensures the `CollaborateForm` is correctly included in the context.
        """
        # Simulate a GET request to the 'about' page
        response = self.client.get(reverse('about'))

        # Check if the response status code is 200 (success)
        self.assertEqual(response.status_code, 200)

        # Verify that the "About Me" title is in the response content
        self.assertIn(b'About Me', response.content)

        # Confirm that the form in the context is an instance of CollaborateForm
        self.assertIsInstance(
            response.context['collaborate_form'], CollaborateForm
        )

    def test_collaboration_form_submission(self):
        """
        Tests a successful submission of the collaboration form.

        - Simulates a user filling out and submitting the form with valid data.
        - Verifies the submission is saved to the database.
        - Ensures the success message is included in the response.
        """
        # Prepare the data for form submission
        fields = {
            'name': 'Test User',
            'email': 'testuser@example.com',
            'message': 'I would love to collaborate!'
        }

        # Simulate a POST request with the form data
        response = self.client.post(reverse('about'), data=fields)

        # Verify that the page renders successfully with an HTTP 200 response
        self.assertEqual(response.status_code, 200)

        # Check if the collaboration request was saved in the database
        self.assertTrue(
            CollaborateRequest.objects.filter(email='testuser@example.com').exists()
        )

        # Confirm the success message is present in the response content
        self.assertIn(
            b'Collaboration request received! I endeavour to respond within 2 working days.',
            response.content
        )
