import unittest
from schedule import Schedule


class ScheduleTest(unittest.TestCase):

    def test_randomize(self):
        """test sprawdza czy po zastowowaniu ulepszonego algorytmu NEH ilość zadań pozostaje bez zmian"""
        schedule1 = Schedule()
        schedule1.load_from_file("ta10")
        schedule2 = Schedule()
        schedule2.load_from_file("ta10")
        schedule1.randomize()
        self.assertEqual(len(schedule1.joblist), len(schedule2.joblist))

    def test_neh_extnd1(self):
        """test sprawdza czy po zastowowaniu ulepszonego algorytmu NEH ilość zadań pozostaje bez zmian"""
        schedule1 = Schedule()
        schedule1.load_from_file("ta0")
        schedule2 = Schedule()
        schedule2.load_from_file("ta0")
        schedule1.extend_neh_lng()
        self.assertEqual(len(schedule1.joblist), len(schedule2.joblist))

    def test_neh_extnd2(self):
        """test sprawdza czy po zastowowaniu ulepszonego algorytmu NEH ilość zadań pozostaje bez zmian"""
        schedule1 = Schedule()
        schedule1.load_from_file("ta2")
        schedule2 = Schedule()
        schedule2.load_from_file("ta2")
        schedule1.extend_neh_lng()
        self.assertEqual(len(schedule1.joblist), len(schedule2.joblist))

    def test_neh_extnd3(self):
        """test sprawdza czy po zastowowaniu ulepszonego algorytmu NEH ilość zadań pozostaje bez zmian"""
        schedule1 = Schedule()
        schedule1.load_from_file("ta40")
        schedule2 = Schedule()
        schedule2.load_from_file("ta40")
        schedule1.extend_neh_lng()
        self.assertEqual(len(schedule1.joblist), len(schedule2.joblist))

    def test_neh_extnd3(self):
        """test sprawdza czy po zastowowaniu ulepszonego algorytmu NEH zadania się nie powtarzają"""
        schedule1 = Schedule()
        schedule1.load_from_file("ta40")
        schedule2 = Schedule()
        schedule2.load_from_file("ta40")
        schedule1.extend_neh_lng()
        self.assertEqual(len(schedule1.joblist), len(set(schedule2.joblist)))

    def test_neh_basic(self):
        """test sprawdza czy po zastowowaniu ulepszonego algorytmu NEH ilość zadań pozostaje bez zmian"""
        schedule1 = Schedule()
        schedule1.load_from_file("ta0")
        schedule2 = Schedule()
        schedule2.load_from_file("ta0")
        schedule1.basic_neh()
        self.assertEqual(len(schedule1.joblist), len(schedule2.joblist))


unittest.main()
