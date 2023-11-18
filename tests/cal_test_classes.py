from unittest import TestCase
from backEnd.classes import Order

class OrderMakingTestCase(TestCase):

    def test_check_order_counter(self):
        current_counter = Order.counter
        order1 = Order([])
        self.assertEqual(order1.order_id, f"order-{current_counter}")
        
        order2 = Order([])
        self.assertEqual(order2.order_id, f"order-{current_counter + 1}")
