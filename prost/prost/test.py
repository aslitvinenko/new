import unittest
from prost import prost


class ProstTestCase(unittest.TestCase):
    def test_prost(self):
        self.assertEqual(prost(7), True)
        self.assertEqual(prost(123), False)
        self.assertEqual(prost(67), True)
        self.assertEqual(prost(68), False)
        self.assertEqual(prost(90), False)


if __name__ == '__main__':
    unittest.main()