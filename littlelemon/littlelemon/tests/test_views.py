from django.test import TestCase
from restaurant.views import MenuItemsView, SingleMenuItemView
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class TestMenuView(TestCase):
    
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Pizza", price=120, inventory=50)
        Menu.objects.create(title="Pasta", price=100, inventory=30)

    def test_getall(self):
        items = Menu.objects.all()

        serialized_data = MenuSerializer(items, many=True).data

        response = self.client.get('/restaurant/menu/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), serialized_data)