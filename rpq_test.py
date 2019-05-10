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




schdl1 = Schedule("./dane rpq/in50.txt")
schdl2 = Schedule("./dane rpq/in100.txt")
schdl3 = Schedule("./dane rpq/in200.txt")



schdl1 = schrage_pmtn(schdl1)
print("Otrymano wynik: " + str(schdl1))
print("Prawidłowy wynik dla instancji in50 to: 1492")

schdl2 = schrage_pmtn(schdl2)
print("Otrymano wynik: " + str(schdl2))
print("Prawidłowy wynik dla instancji in100 to: 3070")

schdl3 = schrage_pmtn(schdl3)
print("Otrymano wynik: " + str(schdl3))
print("Prawidłowy wynik dla instancji in200: 6398")