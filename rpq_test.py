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
        sys.setrecursionlimit(30000)
        schdl2 = Schedule("./dane rpq/in100.txt")
        schdl2, cmax = carlier(schdl2)
        self.assertEqual(cmax, 3070)

    def test_carlier3(self):
        sys.setrecursionlimit(30000)
        schdl3 = Schedule("./dane rpq/in200.txt")
        schdl3, cmax = carlier(schdl3)
        self.assertEqual(cmax, 6398)


# schdl1 = Schedule("./dane rpq/in50.txt")
# schdl2 = Schedule("./dane rpq/in100.txt")
# schdl3 = Schedule("./dane rpq/in200.txt")
#
#
#
# schdl1 = schrage_pmtn(schdl1)
# print("Otrzymano wynik: " + str(schdl1))
# print("Prawidłowy wynik dla instancji in50 to: 1492")
#
# schdl2 = schrage_pmtn(schdl2)
# print("Otrzymano wynik: " + str(schdl2))
# print("Prawidłowy wynik dla instancji in100 to: 3070")
#
# schdl3 = schrage_pmtn(schdl3)
# print("Otrzymano wynik: " + str(schdl3))
# print("Prawidłowy wynik dla instancji in200: 6398")


# schdl1 = Schedule("./dane rpq/in50.txt")
# schdl2 = Schedule("./dane rpq/in100.txt")
# schdl3 = Schedule("./dane rpq/in200.txt")



# schdl1 = schrage_heap(schdl1)
# print("Otrzymano wynik: " + str(schdl1.cmax()))
# print("Prawidłowy wynik dla instancji in50 to: 1492")
#
# schdl2 = schrage_heap(schdl2)
# print("Otrzymano wynik: " + str(schdl2.cmax()))
# print("Prawidłowy wynik dla instancji in100 to: 3070")
#
# schdl3 = schrage_heap(schdl3)
# print("Otrzymano wynik: " + str(schdl3.cmax()))
# print("Prawidłowy wynik dla instancji in200: 6398")


# schdl1 = Schedule("./dane rpq/in50.txt")
# schdl2 = Schedule("./dane rpq/in100.txt")
# schdl3 = Schedule("./dane rpq/in200.txt")
#
#
#
# schdl1 = carlier(schdl1)
# print("Otrzymano wynik: " + str(schdl1))
# print("Prawidłowy wynik dla instancji in50 to: 1492")
#
# schdl2 = carlier(schdl2)
# print("Otrzymano wynik: " + str(schdl2))
# print("Prawidłowy wynik dla instancji in100 to: 3070")
#
# schdl3 = carlier(schdl3)
# print("Otrzymano wynik: " + str(schdl3))
# print("Prawidłowy wynik dla instancji in200: 6398")