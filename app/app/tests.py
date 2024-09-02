from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    def test_add_nums(self):
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_substract_nums(self):
        res = calc.substract(10, 3)
        self.assertEqual(res, 7)
