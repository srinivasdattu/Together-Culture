from django.test import TestCase, Client
from django.urls import reverse

class MainViewsTest(TestCase):
    def setUp(self):
        self.client = Client()


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
