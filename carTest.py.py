import unittest
from cars import Car

class CarTest(unittest.TestCase):
  """Car klassini tekshirish uchun test"""
  
  def test_create(self):
    # avto1 obyektini km va narhini bermasdan yaratamiz ekan
    avto1 = Car("toyota","camry",2020)
    # Qiymatlar mavjudligini AssertIsNotNone metodi bilan tekshiramiz
    self.assertIsNotNone(avto1.make)
    self.assertIsNotNone(avto1.model)
    self.assertIsNotNone(avto1.year)
    # Qiymat mavjud emasligini assertIsNone metodi bilan tekshiramiz
    self.assertIsNone(avto1.price)
    # Qiymat tengligini assertEquals metodi bilan tekshiramiz
    self.assertEqual(0,avto1.get_km())
    # Yangi obyekt yaratamiz va narhini ham ko'rsatamiz
    avto2 = Car("toyota","camry",2020,price=75000)
    self.assertEqual(75000,avto2.price)

unittest.main()    
    
    