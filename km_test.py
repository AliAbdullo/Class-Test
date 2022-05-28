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


def test_add_km(self):
  # Musbat qiymat berib ko'ramiz
  self.avto1.add_km(self.km)
  self.assertEqual(self.km,self.avto1.get_km())
  # Manfiy qiymat berib ko'ramiz
  new_km=-5000
  try:
    self.avto1.add_km(new_km)
  except ValueError as error:
    self.assertEqual(type(error),ValueError)