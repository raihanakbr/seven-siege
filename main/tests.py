from django.test import TestCase, Client
from django.db import models
from main.models import Item

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

class TestModels(TestCase):
    def setUp(self):
        self.item1 = Item.objects.create(
            name = 'Ash',
            amount = 1,
            price = 100,
            category = 'Operator',
            description = 'Ash is a fast-paced front liner; capable of breaching, \
                        flanking and dividing the Defender\'s attention in seconds.',
        )

    def test_data_types_on_item_attributes(self):
        self.assertIsInstance(self.item1._meta.get_field('name'), models.CharField)
        self.assertIsInstance(self.item1._meta.get_field('date_added'), models.DateField)
        self.assertIsInstance(self.item1._meta.get_field('amount'), models.IntegerField)
        self.assertIsInstance(self.item1._meta.get_field('price'), models.IntegerField)
        self.assertIsInstance(self.item1._meta.get_field('category'), models.TextField)
        self.assertIsInstance(self.item1._meta.get_field('description'), models.TextField)