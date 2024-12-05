from unittest import TestCase
from service.exp2.array import *


class Test(TestCase):
    def test_order_or_not(self):
        # 边界情况
        self.assertEqual(order_or_not([1, 2]), 1)  # 两个元素，升序
        self.assertEqual(order_or_not([2, 1]), 2)  # 两个元素，降序

        # 典型情况
        self.assertEqual(order_or_not([1, 5, 4, 9]), 0)  # 无序
        self.assertEqual(order_or_not([1, 2, 3, 4, 9, 18]), 1)  # 升序
        self.assertEqual(order_or_not([92, 39, 23, 12, 3]), 2)  # 降序
        self.assertEqual(order_or_not([1, 2, 3, 4, 9, 18, 12, 11]), 3)  # 先升后降
        self.assertEqual(order_or_not([18, 9, 4, 3, 2, 1, 32, 33, 36]), 4)  # 先降后升
