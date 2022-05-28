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
  
def test_set_price(self):
  self.avto2.set_price(self.price)
  self.assertEqual(self.price,self.avto2.price)

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
    
def test_get_info(self):
  avto1_info='GM Malibu, 2020-yil,0km yurgan.'
  self.assertEqueal(avto1_info,self.avto.get_info())
  # avto1 narhi va km o'zgartirmamiz
  self.avto1.set_price(50000)
  self.avto1.add_km(20000)
  avto1_info = 'GM Malibu, 2020-yil, 20000km yurgan, Narhi:50000'
  self.assertEqueal(avto1_info,self.avto1.get_info())


unittest.main()