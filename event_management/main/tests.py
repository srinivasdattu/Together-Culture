from django.test import TestCase, Client
from django.urls import reverse

class MainViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
    def test_home_page(self):
        """
        Ensure the home page loads and uses the correct template.
        """
        url = reverse('home')  # name='home' in main/urls.py
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_signup_page(self):
        """
        Ensure the signup page loads and uses the correct template.
        """
        url = reverse('signup')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_signin_page(self):
        url = reverse('signin')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signin.html')

    def test_admin_signin_page(self):
        url = reverse('admin_signin')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_signin.html')       
    def test_admin_members_page(self):
        url = reverse('admin_members')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_members.html')
    def test_admin_dashboard_page(self):
        url = reverse('admin_dashboard')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_dashboard.html')
    def test_admin_events_page(self):
        url = reverse('admin_events')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_events.html')

    def test_admin_create_event_page(self):
        url = reverse('admin_create_event')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_create_event.html')

    def test_member_events_page(self):
        url = reverse('member_events')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'member_events.html')

    def test_digital_content_page(self):
        url = reverse('digital_events')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'digital_content.html')
