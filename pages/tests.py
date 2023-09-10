from django.test import TestCase, SimpleTestCase
from django.urls import reverse

# Create your tests here.

class HomePageTests(SimpleTestCase):
    def test_home_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_home_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        
    def test_home_by_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response,'home.html')
    
    def test_home_by_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, '<h1><strong>Home Page</strong></h1>')


class AboutPageTests(SimpleTestCase):
    def test_about_url(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_about_url_by_name(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_about_by_template(self):
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response,'about.html')
    
    def test_about_by_content(self):
        response = self.client.get(reverse('about'))
        self.assertContains(response, '<h1><strong>About Page</strong></h1>')
