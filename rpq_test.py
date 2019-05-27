from rpq import *
import unittest
import sys


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

    def test_carlier1(self):
        schdl1 = Schedule("./dane rpq/in50.txt")
        schdl1, cmax = carlier(schdl1)
        self.assertEqual(cmax, 1492)

    def test_carlier2(self):
        schdl2 = Schedule("./dane rpq/in100.txt")
        schdl2, cmax = carlier(schdl2)
        self.assertEqual(cmax, 3070)

    def test_carlier3(self):
        schdl3 = Schedule("./dane rpq/in200.txt")
        schdl3, cmax = carlier(schdl3)
        self.assertEqual(cmax, 6398)

    def test_carlierm1(self):
        schdl = Schedule("./dane rpq/data001.txt")
        schdl, cmax = carlier(schdl)
        self.assertEqual(cmax, 3016)