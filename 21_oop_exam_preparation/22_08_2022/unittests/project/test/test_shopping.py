from project.shopping_cart import ShoppingCart
from unittest import TestCase, main


class TestShoppingCart(TestCase):

    def setUp(self) -> None:
        self.cart = ShoppingCart("Cart", 100.0)

    def test_correct_init(self):
        self.assertEqual("Cart", self.cart.shop_name)
        self.assertEqual(100.0, self.cart.budget)
        self.assertEqual({}, self.cart.products)

    def test_name_setter_invalid_name_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.shop_name = "cart"

        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.cart.shop_name = "Cart1"

        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_add_to_cart_method_invalid_price_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.add_to_cart("product", 100.0)

        self.assertEqual("Product product cost too much!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.cart.add_to_cart("product", 101.1)

        self.assertEqual("Product product cost too much!", str(ve.exception))

    def test_add_to_cart_method_successfully(self):
        expected = "product product was successfully added to the cart!"

        result = self.cart.add_to_cart("product", 50.0)

        self.assertEqual(expected, result)
        self.assertEqual({"product": 50.0}, self.cart.products)

    def test_remove_from_cart_unexisting_product_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.remove_from_cart("product")

        self.assertEqual("No product with name product in the cart!", str(ve.exception))

    def test_remove_from_cart_successfully(self):
        self.cart.add_to_cart("product1", 50.0)
        self.cart.add_to_cart("product2", 50.0)
        expected = "Product product1 was successfully removed from the cart!"

        result = self.cart.remove_from_cart("product1")

        self.assertEqual({"product2": 50.0}, self.cart.products)
        self.assertEqual(expected, result)

    def test_add_dunder(self):
        other_cart = ShoppingCart("OtherCart", 200.0)
        self.cart.add_to_cart("product1", 50.0)
        other_cart.add_to_cart("product2", 50.0)

        new_cart = self.cart + other_cart

        self.assertEqual("CartOtherCart", new_cart.shop_name)
        self.assertEqual(300.0, new_cart.budget)
        self.assertEqual({"product1": 50.0, "product2": 50.0}, new_cart.products)

    def test_buy_products_method_bigger_sum_raises_value_error(self):
        self.cart.add_to_cart("product1", 80.0)
        self.cart.add_to_cart("product2", 80.0)
        expected = "Not enough money to buy the products! Over budget with 60.00lv!"

        with self.assertRaises(ValueError) as ve:
            self.cart.buy_products()

        self.assertEqual(expected, str(ve.exception))

    def test_buy_products_method_successfully(self):
        self.cart.add_to_cart("product1", 20.0)
        self.cart.add_to_cart("product2", 30.0)
        expected = "Products were successfully bought! Total cost: 50.00lv."

        result = self.cart.buy_products()

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
