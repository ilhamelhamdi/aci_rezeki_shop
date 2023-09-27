from django.test import TestCase, Client
from main.models import Item, Category

class MainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/')
        self.assertTemplateUsed(response, 'index.html')

class AboutTest(TestCase):
    def test_about_url_is_exist(self):
        response = Client().get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/about/')
        self.assertTemplateUsed(response, 'about.html')

# TODO: create test for view item
class ItemViewTest(TestCase):
    data = {
        'name': 'Dummy name',
        'amount':100,
        'description': 'Dummy description',
        'price': 10000,
    }
    def setUp(self):
        Item.objects.create(name="Kemeja", amount=5, description="Kemeja Alisan", price=100000)
    def test_item_url_is_exist(self):
        response = Client().get('/item/1')
        self.assertEqual(response.status_code, 200)