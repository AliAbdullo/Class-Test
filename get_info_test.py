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


def test_get_info(self):
  avto1_info='GM Malibu, 2020-yil,0km yurgan.'
  self.assertEqueal(avto1_info,self.avto.get_info())
  # avto1 narhi va km o'zgartirmamiz
  self.avto1.set_price(50000)
  self.avto1.add_km(20000)
  avto1_info = 'GM Malibu, 2020-yil, 20000km yurgan, Narhi:50000'
  self.assertEqueal(avto1_info, self.avto1.get_info())

unittest.main()