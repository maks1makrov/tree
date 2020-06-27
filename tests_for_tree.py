import unittest

from example2 import Node
from example2 import Manager

class Test_tree(unittest.TestCase):
    def test_1(self):
        root = Node("-5-", 5)
        m = Manager(root)
        m.add(Node("-4.5-", 4.5))
        self.assertEqual(m.delete(4.5), "deleted of mark - 4.5 is done ")
    def test_2(self):
        root = Node("-5-", 5)
        m = Manager(root)
        m.add(Node("-4.5-", 4.5))
        m.add(Node("-4.4-", 4.4))
        m.delete(4.5)
        self.assertEqual(m.delete(4.5), "can not find mark - 4.5")


