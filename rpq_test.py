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


class RpqTest_pmtn(unittest.TestCase):

    def test_schrage_pmtn1(self):
        schedule = Schedule("./dane rpq/in50.txt")
        self.assertEqual(schrage_pmtn(schedule), 1492)

    def test_schrage_pmtn2(self):
        schedule = Schedule("./dane rpq/in100.txt")
        self.assertEqual(schrage_pmtn(schedule), 3070)

    def test_schrage_pmtn3(self):
        schedule = Schedule("./dane rpq/in200.txt")
        self.assertEqual(schrage_pmtn(schedule), 6398)


if __name__ == '__main__':
    unittest.main()
