import unittest
from schedule import Schedule


class ScheduleTest(unittest.TestCase):

    def test_cmax_1(self):

        schedule1 = Schedule()
        schedule1.load_from_file("ta0")
        self.assertEqual(schedule1.cmax(), 40)

    def test_cmax_2(self):

        schedule1 = Schedule()
        schedule1.load_from_file("ta120")
        self.assertEqual(schedule1.cmax(), 30148)

    def test_cmax_3(self):

        schedule1 = Schedule()
        schedule1.load_from_file("ta62")
        self.assertEqual(schedule1.cmax(), 5878)


unittest.main()
