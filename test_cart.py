from cart import ShoppingCart
import unittest


class TestMethods(unittest.TestCase):

    def test_total(self):
        tmp = ShoppingCart()
        tmp.add_item("name", 100, 1)
        self.assertEqual(tmp.get_total(), 100)

    def test_discount(self):
        tmp = ShoppingCart()
        tmp.add_item("name", 50, 1)
        tmp.apply_discount("SAVE20")
        self.assertEqual(tmp._discount, tmp.DISCOUNT_CODES["SAVE20"])

    def test_add_item_quantity(self):
        tmp = ShoppingCart()
        tmp.add_item("name", 10, 1)
        tmp.add_item("name", 10, 3)
        self.assertEqual(tmp._items["name"]["quantity"], 3)


if __name__ == "__main__":
    unittest.main()