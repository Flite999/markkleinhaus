from django.test import TestCase
from django.urls import reverse


class HomePageTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)


class NavigationTests(TestCase):
    def test_current_projects_page_status_code(self):
        response = self.client.get(reverse('current_projects'))
        self.assertEqual(response.status_code, 200)

    def test_past_projects_page_status_code(self):
        response = self.client.get(reverse('past_projects'))
        self.assertEqual(response.status_code, 200)
