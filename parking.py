import argparse
import sys

class CarParking:
      def __init__(self):
         self.slots=0
         self.slots_taken={}
         self.slots_available=[]
         
      
      def create_slots(self, total_slots):
        try:
            self.slots = total_slots
            for i in range(1,self.slots+1):
                 self.slots_available.append(i)
            return True
        except Exception as exception:
            print(exception)
            return False
      
      def nearby_slot(self):
        if self.slots_available==[]:
          nearest_slot_number=-1  
        else:
          nearest_slot_number = min(self.slots_available)
          self.slots_available.remove(nearest_slot_number)
        return nearest_slot_number
       
      def allocate_slot(self,numberPlate,carColor):
          self.numberPlate=numberPlate
          self.carColor=carColor
          if len(self.slots_taken) < self.slots:
            parking_slot = self.nearby_slot()
            ticket=[parking_slot,numberPlate,carColor]
            self.slots_taken[numberPlate]=ticket  
          else:
            parking_slot = -1    
          return parking_slot

      def deallocate_slot(self,slot_number):
        if len(self.slots_taken) > 0:
          key=-1
          for registration_number,car_info in self.slots_taken.items():
            if slot_number==car_info[0]:
              key=registration_number
          if key==-1:
            return False
          else:    
            self.slots_available.append(slot_number)           
            del self.slots_taken[key]
            return car_info[0]
        else:
               # no such slot
              return False
      def find_car_with_color(self,colour):
        all_cars=' '
        cars=[]
        for car_info in self.slots_taken.values():
          cars.append(car_info[2]) 
        if colour in cars:
          for car_info in self.slots_taken.values():
            if colour==car_info[2]:
              all_cars=all_cars+car_info[1]+'  '
        else:
          return False      
        return all_cars
      def find_slot_number_for_car_with_color(self,colour):
        all_cars=' '
        cars=[]
        for car_info in self.slots_taken.values():
          cars.append(car_info[2]) 
        if colour in cars:
          for car_info in self.slots_taken.values():
            if colour==car_info[2]:
              all_cars=all_cars+'  '+str(car_info[0])
        else:
          return False      
        return all_cars

      def find_slot_number_for_registration_number(self,registration_number):
        if registration_number in self.slots_taken:
          slot_value=self.slots_taken[registration_number][0]
          return slot_value
        else:
          return False
      def match_methods(self, inputText):
        if inputText.startswith('create_parking_lot'):
            try:
                total_slots= int(inputText.split(' ')[1])
                status = self.create_slots(total_slots)
                if status:
                    print(f'Created parking with {total_slots} slots')
                    
            except Exception as exception:
                print(f'Error in Query - {inputText} : {exception}')

        elif inputText.startswith('park'):
            try:
                numberPlate= inputText.split(' ')[1]
                color = inputText.split(' ')[2]
                result = self.allocate_slot(numberPlate, color)
                if result == -1:
                    print('Sorry, Parking Lot is full.')
                else:
                    print(f'Allocated slot number {result}')
                        
                        
            except Exception as exception:
                print(f'Error in Query - {inputText} : {exception}')
                
         #leave working 
        elif inputText.startswith('leave'):
            try:
                leaving_parking_slot = int(inputText.split(' ')[1])
                parking_ticket = self.deallocate_slot(leaving_parking_slot)
              
                if parking_ticket:
                    print(f'Slot number {leaving_parking_slot} is free ')
                                  
                else:
                    print(f'Slot number {leaving_parking_slot} cannot be vacated.')
            except Exception as exception:
                print(f'Error in Query - {inputText} : {exception}')
        elif inputText.startswith('status'):
            try:
              print(f'Slot No.\tRegistration No\tColor ')
              for i in self.slots_taken.values():
                print(f"\t{i[0]}\t\t{i[1]}\t\t{i[2]}")
              
            except Exception as exception:
                print(f'Error in Query - {inputText} : {exception}')
        elif inputText.startswith('registration_numbers_for_cars_with_colour'):
            try:
              colour=inputText.split(' ')[1]
              result=self.find_car_with_color(colour)
              if result:
                print(result)
              else:
                print(f'No cars with color {colour}')

            except Exception as exception:
                print(f'Error in Query - {inputText} : {exception}')
        elif inputText.startswith('slot_numbers_for_cars_with_colour'):
            try:
              colour=inputText.split(' ')[1]
              result=self.find_slot_number_for_car_with_color(colour)
              if result:
                print(result)
              else:
                print(f'No cars with color {colour}')

            except Exception as exception:
                print(f'Error in Query - {inputText} : {exception}')
        elif inputText.startswith('slot_number_for_registration_number'):
            try:
              registration_number=inputText.split(' ')[1]
              result=self.find_slot_number_for_registration_number(registration_number)
              if result:
                print(result)
              else:
                print(f'No cars with Registration Number: {registration_number}')

            except Exception as exception:
                print(f'Error in Query - {inputText} : {exception}')

if __name__ == '__main__':

    parking_management = CarParking()
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', action="store", required=True, dest='input_file', help="Input File")
    parser.add_argument('--output_file', action="store", required=False, dest='output_file', help="Output File")

    args = parser.parse_args()
    if args.output_file:
        sys.stdout = open(args.output_file, "w")

    if args.input_file:
        with open(args.input_file) as input_file:
            for line in input_file:
                line = line.rstrip('\n')
                parking_management.match_methods(line)  















      
