import unittest
from parking import CarParking
class TestParkingLot(unittest.TestCase):
  def test_create_parking_lot(self):
        parking_management = CarParking()
        result = parking_management.create_slots(5)
        self.assertEqual(True, result)
  def test_allocate_slot(self):
        parking_management = CarParking()
        parking_management.create_slots(5)
        result=parking_management.allocate_slot('KA-10-200','red')
        self.assertNotEqual(-1, result)
  def test_deallocate_slot(self):
        parking_management = CarParking()
        parking_management.create_slots(5)
        parking_management.allocate_slot('KA-10-200','red')
        result=parking_management.deallocate_slot(1)
        self.assertNotEqual(False, result)
  def test_car_with_color(self):
        parking_management=CarParking()
        parking_management.create_slots(5)
        parking_management.allocate_slot('KA-10-200','red')
        result=parking_management.find_car_with_color('red')
        self.assertEqual(['KA-10-200'],result)

  def test_find_slot_number_for_car_with_color(self):
        parking_management=CarParking()
        parking_management.create_slots(5)
        parking_management.allocate_slot('KA-10-200','red')
        result=parking_management.find_slot_number_for_car_with_color('red')
        self.assertEqual([1],result)

  def test_find_slot_number_for_registration_number(self):
        parking_management=CarParking()
        parking_management.create_slots(5)
        parking_management.allocate_slot('KA-10-200','red')
        result=parking_management.find_slot_number_for_registration_number('KA-10-200')
        self.assertEqual(1,result)
if __name__ == '__main__':
    unittest.main()






