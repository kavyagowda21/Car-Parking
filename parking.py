











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
        nearest_slot_number = min(self.slots_available)
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
      
      
       def match_methods(self, inputText):
        """
        This method takes query as input and executes the query on the predefined set of commands and matching methods
        to be executed, and prints the output to the console or writes it to a output file based on the mode selected.
        Predefined Commands :
        1. Create_parking_lot <capacity:int>
        2. Park <vehicle_registration_number:str> driver_age <age:int>
        3. Leave <parking_slot:int>
        4. Slot_number_for_car_with_number <vehicle_registration_number:str>
        5. Slot_numbers_for_driver_of_age <age:int>
        6. Vehicle_registration_number_for_driver_of_age <age:int>
        :param query:str Command to be executed with arguments separated by " ".
        """

          if inputText.startswith('create_parking_lot'):
            try:
                total_slots= int(inputText.split(' ')[1])
                status = self.create_slots(total_slots)
                if status:
                    print(f'Created parking of {total_slots} slots')
                    
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
                    print(
                        f'Car with vehicle registration number "{numberPlate}" has been parked at '
                        f'slot number {result}')
             except Exception as exception:
                print(f'Error in Query - {inputText} : {exception}')
                
         #leave working 
            
              
      
      
      
