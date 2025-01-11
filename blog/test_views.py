from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CommentForm
from .models import Post


class TestBlogViews(TestCase):
    """
    Test suite for the blog views.
    """

    def setUp(self):
        """
        Set up test data, including a superuser and a sample post.

        - Creates a superuser to simulate an authenticated user.
        - Creates a blog post with 'Published' status for testing.
        """
        # Create a superuser for authentication in tests
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        # Create a blog post instance
        self.post = Post.objects.create(
            title="Blog title",
            author=self.user,
            slug="blog-title",
            excerpt="Blog excerpt",
            content="Blog content",
            status=1  # Published
        )

    def test_render_post_detail_page_with_comment_form(self):
        """
        Test the post_detail view renders correctly with the comment form.

        - Sends a GET request to the post_detail view.
        - Verifies the HTTP status code is 200.
        - Confirms the post's title and content are present in the response.
        - Ensures the 'comment_form' in the response context is an instance of CommentForm.
        """
        # Send a GET request to the post_detail view
        response = self.client.get(reverse('post_detail', args=['blog-title']))
        # Assert the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Assert the post title and content are in the HTML response
        self.assertIn(b"Blog title", response.content)
        self.assertIn(b"Blog content", response.content)
        # Assert the context includes an instance of CommentForm
        self.assertIsInstance(
            response.context['comment_form'], CommentForm
        )

    def test_successful_comment_submission(self):
        """
        Test successful submission of a comment on a post.

        - Logs in the superuser to simulate an authenticated user.
        - Sends a POST request with comment data to the post_detail view.
        - Verifies the HTTP status code is 200.
        - Confirms the success message is in the response content.
        """
        # Log in the test superuser
        self.client.login(username="myUsername", password="myPassword")
        # Data to simulate a comment submission
        post_data = {
            'body': 'This is a test comment.'
        }
        # Send a POST request to the post_detail view
        response = self.client.post(reverse('post_detail', args=['blog-title']), post_data)
        # Assert the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Assert the success message is in the response content
        self.assertIn(
            b'Comment submitted and awaiting approval',
            response.content
        )
