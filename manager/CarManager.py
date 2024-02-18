import os
import re
from Util import *
from Config import *
from .DataSetManager import *
from enums.RentEnum import *
from enums.MessageEnum import *

class CarManager(DataSetManager):
    
    # Init to use specific file
    def __init__(self):
        super().__init__(os.path.join(project_dir, 'data_set/', 'car_data.txt'))
    
    # Add new data function
    def add_new_data(self):
        new_data = {}
        
        # Loop the car's attribute from config and input the value
        for attribute in car_data_attributes:
            if attribute == 'tahun':
                while True:
                    year_input = input("Masukkan tahun mobil (format: YYYY): ")
                    if re.match(regex_patterns['year'], year_input):
                        new_data[attribute] = year_input
                        break
                    else:
                        print(f"{MessageEnum.YEAR_WARNING.value}\n")
            elif attribute == 'harga':
                while True:
                    price_input = input(f"Masukkan {attribute} sewa mobil: ")
                    if re.match(regex_patterns['price'], price_input):
                        new_data[attribute] = int(price_input)
                        break
                    else:
                        print(f"{MessageEnum.PRICE_WARNING.value}\n")
            elif attribute != 'status':
                new_data[attribute] = input(f"Masukkan {attribute} mobil: ")
        
        # Hardcode for new data value
        new_data['status'] = "available"

        # Call DataSetManager to add new data and store to file
        car_id = self.add_new_data_set(new_data, RentEnum.CAR_ID_PREFIX.value)
        
        # Show output after add new data
        clear_screen()
        print(f"{MessageEnum.ADD_SUCCESS_MESSAGE.value} {car_id}")
        show_table_data(self.read_data_set(), car_header_attributes, car_data_attributes, False)

        return car_id

    # Update data function
    def update_data(self):
        
        # Show cars data for manipulate
        show_table_data(self.read_data_set(), car_header_attributes, car_data_attributes, False)
        
        while True:
            car_id = input(MessageEnum.UPDATE_INPUT_MESSAGE.value)

            # Check if car_id is in cars dictionary
            if car_id in self.read_data_set():
                print(MessageEnum.UPDATE_CHOICE_MESSAGE.value)
                
                # Car attributes for update
                for i, attribute in enumerate(car_data_attributes, 1):
                    print(f"{i}. {attribute.capitalize()}")

                while True:
                    selected_field = input(f"\n{choose_option}")

                    # Check input is digit since we'll use as index
                    if selected_field.isdigit():
                        selected_index = int(selected_field) - 1
                        if 0 <= selected_index < len(car_data_attributes):
                            selected_attribute = car_data_attributes[selected_index]
                            if selected_attribute == 'tahun':
                                while True:
                                    year_input = input("Masukkan tahun mobil (format: YYYY): ")
                                    if re.match(regex_patterns['year'], year_input):
                                        updated_value = year_input
                                        break
                                    else:
                                        print(f"{MessageEnum.YEAR_WARNING.value}\n")
                            elif selected_attribute == 'harga':
                                while True:
                                    price_input = input(f"{MessageEnum.UPDATE_VALUE_MESSAGE.value}{selected_attribute} sewa mobil: ")
                                    if re.match(regex_patterns['price'], price_input):
                                        updated_value = price_input
                                        break
                                    else:
                                        print(f"{MessageEnum.PRICE_WARNING.value}\n")
                            else:
                                updated_value = input(f"{MessageEnum.UPDATE_VALUE_MESSAGE.value}{selected_attribute} mobil: ")
                            
                            # Fetch the updated value
                            updated_car_data = {selected_attribute: updated_value}

                            # Call DataSetManager to update the data and store to file
                            updated_car_id = self.update_data_set(car_id, updated_car_data)

                            # Show output after update data
                            clear_screen()
                            print(f"{MessageEnum.UPDATE_SUCCESS_MESSAGE.value} {updated_car_id}")
                            show_table_data(self.read_data_set(), car_header_attributes, car_data_attributes, False)
                            
                            return updated_car_id
                        else:
                            print(f"{MessageEnum.CHOICE_NOT_EXIST.value}\n")
                    else:
                        print(f"{MessageEnum.CHOICE_NOT_EXIST.value}\n")
                break
            else:
                print(f"{MessageEnum.ID_NOT_FOUND_WARNING.value}\n")

    # Delete data function
    def delete_data(self):
        
        # Show cars data for manipulate
        show_table_data(self.read_data_set(), car_header_attributes, car_data_attributes, False)

        car_id = input(MessageEnum.DELETE_INPUT_MESSAGE.value)

        # Call DataSetManager to delete the data and store to file
        deleted_car_id = self.delete_data_set(car_id)
        
        if deleted_car_id:
            # Show output after delete data
            clear_screen()
            print(f"{MessageEnum.DELETE_SUCCESS_MESSAGE.value} {deleted_car_id}")
            show_table_data(self.read_data_set(), car_header_attributes, car_data_attributes, False)

        return deleted_car_id
    
    # Update car data for rent function
    def update_car_for_rent(self, car_id, updated_car_data):
        self.update_data_set(car_id, updated_car_data)

