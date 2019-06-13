from rpq import carlier_new as carlier
from rpq import Schedule
import unittest


class CarlierTestIn(unittest.TestCase):

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


class CarlierTestM(unittest.TestCase):

    def test_carlierm0(self):
        schdl = Schedule("./dane rpq/data000.txt")
        schdl, cmax = carlier(schdl)
        self.assertEqual(cmax, 228)

    def test_carlierm1(self):
        schdl = Schedule("./dane rpq/data001.txt")
        schdl, cmax = carlier(schdl)
        self.assertEqual(cmax, 3016)

    def test_carlierm2(self):
        schdl = Schedule("./dane rpq/data002.txt")
        schdl, cmax = carlier(schdl)
        self.assertEqual(cmax, 3665)

    def test_carlierm3(self):
        schdl = Schedule("./dane rpq/data003.txt")
        schdl, cmax = carlier(schdl)
        self.assertEqual(cmax, 3309)

    def test_carlierm4(self):
        schdl = Schedule("./dane rpq/data004.txt")
        schdl, cmax = carlier(schdl)
        self.assertEqual(cmax, 3191)

    def test_carlierm5(self):
        schdl = Schedule("./dane rpq/data005.txt")
        schdl, cmax = carlier(schdl)
        self.assertEqual(cmax, 3618)

    def test_carlierm6(self):
        schdl = Schedule("./dane rpq/data006.txt")
        schdl, cmax = carlier(schdl)
        self.assertEqual(cmax, 3446)

    def test_carlierm7(self):
        schdl = Schedule("./dane rpq/data007.txt")
        schdl, cmax = carlier(schdl)
        self.assertEqual(cmax, 3821)

    def test_carlierm8(self):
        schdl = Schedule("./dane rpq/data008.txt")
        schdl, cmax = carlier(schdl)
        self.assertEqual(cmax, 3634)
