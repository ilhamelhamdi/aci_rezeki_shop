from django.test import TestCase, Client
from main.models import Item, Category

class ItemTestCase(TestCase):
    def setUp(self):
        Item.objects.create(name="Kemeja", amount=5, description="Kemeja Alisan", price=100000)
        Item.objects.create(name="Waistbag", amount=10, description="Lorem ipsum", price=500000)

    def test_item_can_be_created(self):
        kemeja = Item.objects.get(name="Kemeja")
        waistbag = Item.objects.get(name="Waistbag")
        self.assertEqual(kemeja.amount, 5)
        self.assertEqual(waistbag.amount, 10)

    def test_item_can_be_updated(self):
        kemeja = Item.objects.get(name="Kemeja")
        kemeja.amount = 10
        kemeja.save()
        self.assertEqual(kemeja.amount, 10)

    def test_item_can_be_deleted(self):
        kemeja = Item.objects.get(name="Kemeja")
        kemeja.delete()
        self.assertEqual(Item.objects.count(), 1)

class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name="Pakaian")
        Category.objects.create(name="Elektronik")
    
    def test_category_can_be_created(self):
        obj1 = Category.objects.get(name="Pakaian")
        obj2 = Category.objects.get(name="Elektronik")
        self.assertEqual(obj1.name, "Pakaian")
        self.assertEqual(obj2.name, "Elektronik")

    def test_category_can_be_updated(self):
        obj = Category.objects.get(name="Pakaian")
        obj.name = "Makanan"
        obj.save()
        self.assertEqual(obj.name, "Makanan")

    def test_category_can_be_deleted(self):
        obj = Category.objects.get(name="Pakaian")
        obj.delete()
        self.assertEqual(Category.objects.count(), 1)