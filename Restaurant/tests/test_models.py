from django.test import TestCase
from Restaurant.models import MenuItem, Booking


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        itemstr = item.get_item()

        self.assertEqual(itemstr, "IceCream : 80")