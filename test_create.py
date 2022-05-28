
import unittest
from cars import Car

class CarTest(unittest.TestCase):
  """Car klassini tekshirish uchun test"""
  def serUp(self):
    make = "GM"
    model = "Malibu"
    year = 2020
    self.price=40000
    self.km=1000
    self.avto1 = Car(make,model,year,)
    self.avto2 = Car(make,model,year, price=self.price)

def test_create(self):
  # Qiymatlar mavjudligini assertNotNone metodi bilan tekshiramiz
  self.assertNotNone(self.avto1.make)
  self.assertNotNone(self.avto1.model)
  self.assertNotNone(self.avto1.year)
  # Qiymat mavjud emasligini assertIsNone metodi bilan tekshiramiz
  self.assertNone(self.avto1.price)
  # Qiymat tengligini assertEquals metodi bilan tekshiramiz
  self.assertEqual(0,self.avto1.get_km())
  # avto2 narhini tekshiramiz
  self.assertEquel(4000,self.avto2.price)