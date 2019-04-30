from rpq import *
import unittest


class RpqTest(unittest.TestCase):

    def test_schrage1(self):
        schedule = Schedule("./dane rpq/in50.txt")
        schedule = schrage(schedule)
        self.assertEqual(schedule.cmax(), 1513)

    def test_schrage2(self):
        schedule = Schedule("./dane rpq/in100.txt")
        schedule = schrage(schedule)
        self.assertEqual(schedule.cmax(), 3076)

    def test_schrage3(self):
        schedule = Schedule("./dane rpq/in200.txt")
        schedule = schrage(schedule)
        self.assertEqual(schedule.cmax(), 6416)
