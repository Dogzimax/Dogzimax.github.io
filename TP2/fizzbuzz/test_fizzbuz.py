from unittest import TestCase
from fizzbuzz import FizzBuzz

class FizzBuzzTest(TestCase):
    def test_returns_number_for_input_not_divisible_by_3_or_5(self):
        self.fizzbuzz = FizzBuzz()
        self.assertEqual('1',  self.fizzbuzz.convert(1))
        self.assertEqual('2',  self.fizzbuzz.convert(2))
        self.assertEqual('4',  self.fizzbuzz.convert(4))
        self.assertEqual('7',  self.fizzbuzz.convert(7))
        self.assertEqual('11', self.fizzbuzz.convert(11))
        self.assertEqual('13', self.fizzbuzz.convert(13))
        self.assertEqual('14', self.fizzbuzz.convert(14))
    def test_returns_number_for_input_divisible_by_3(self):
        self.fizzbuzz = FizzBuzz()
        self.assertEqual('3',  self.fizzbuzz.convert(3))
        self.assertEqual('6',  self.fizzbuzz.convert(6))
        self.assertEqual('9',  self.fizzbuzz.convert(9))
        self.assertEqual('12',  self.fizzbuzz.convert(12))
    def test_returns_number_for_input_divisible_by_5(self):
        self.fizzbuzz = FizzBuzz()
        self.assertEqual('5',  self.fizzbuzz.convert(5))
        self.assertEqual('10',  self.fizzbuzz.convert(10))
        self.assertEqual('20',  self.fizzbuzz.convert(20))
        self.assertEqual('25',  self.fizzbuzz.convert(25))
    def test_returns_number_for_input_divisible_by_3_and_5(self):
        self.fizzbuzz = FizzBuzz()
        self.assertEqual('15',  self.fizzbuzz.convert(15))
        self.assertEqual('30',  self.fizzbuzz.convert(30))
        self.assertEqual('45',  self.fizzbuzz.convert(45))
        self.assertEqual('60',  self.fizzbuzz.convert(60))
 
