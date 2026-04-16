from cart import ShoppingCart
import unittest
class TestMethods(unittest.TestCase):

    def test_total(self):
        tmp=ShoppingCart()
        tmp.add_item('name',100,1)
        tmp.DISCOUNT_CODES["SAVE10"]
        self.assertEqual(tmp.get_total(),90)
        #self.assertEqual(tmp.get_item_count(),1)
        #discountu yanlış hesaplıyor
    def test_discount(self):
        tmp=ShoppingCart()
        tmp.add_item('name',50,1)
        tmp.DISCOUNT_CODES["SAVE20"]
        self.assertEqual(tmp.apply_discount("SAVE20"),tmp.DISCOUNT_CODES)
        # if kısmında subtotal >= discount olmalı

    def test_add_item_quantity(self):
        tmp=ShoppingCart()
        tmp.add_item('name',10,1)
        tmp.add_item('name',10,3)
        self.assertEqual(tmp._items["name"]["quantity"],4)
        # toplamı yanlış yapıyor