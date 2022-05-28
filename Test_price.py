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



def test_set_price(self):
  self.avto2.set_price(self.price)
  self.assertEqual(self.price,self.avto2.price)