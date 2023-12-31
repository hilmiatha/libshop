from django.test import TestCase, Client
from .models import Item

# Create your tests here.
class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')
    
    def setUp(self):
        self.tesObj = Item.objects.create(
            name = "tes nama",
            price = 2,
            amount = 1,
            genre = "tes genre",
            description = "tes desc"
        )
    
        
    def test_model_method(self):
        obj = Item.objects.get(id=self.tesObj.id)
        self.assertEqual(obj.name, "tes nama")
        self.assertEqual(obj.amount, 1)
        self.assertEqual(obj.price, 2)
        self.assertEqual(obj.genre, "tes genre")
        self.assertEqual(obj.description, "tes desc")
        