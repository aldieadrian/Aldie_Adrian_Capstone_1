import re
from .DataSetManager import *
from Config import *
from Util import *
from enums.MessageEnum import *
from enums.RentEnum import *

class CustomerManager(DataSetManager):
    
    # Init to use specific file
    def __init__(self):
        super().__init__(os.path.join(project_dir, 'data_set/', 'customer_data.txt'))

    # Add new data function
    def add_new_data(self):
        new_data = {}
        
        # Loop the customer's attribute from config and input the value
        for attribute in customer_data_attributes:
            if attribute == 'nama':
                while True:
                    name_input = input(f"Masukkan {attribute} customer: ")
                    if re.match(regex_patterns['alphabet'], name_input):
                        new_data[attribute] = name_input
                        break
                    else:
                        print(f"{MessageEnum.NAME_WARNING.value}\n")
            elif attribute == 'telepon':
                while True:
                    phone_input = input(f"Masukkan {attribute} customer: ")
                    if re.match(regex_patterns['phone'], phone_input):
                        new_data[attribute] = phone_input
                        break
                    else:
                        print(f"{MessageEnum.PHONE_WARNING.value}\n")
            elif attribute == 'ktp':
                while True:
                    ktp_input = input(f"Masukkan {attribute} customer: ")
                    if re.match(regex_patterns['ktp'], ktp_input):
                        if self.is_ktp_exist(ktp_input):
                            print(f"{attribute.capitalize()} {MessageEnum.DATA_EXIST.value}\n")
                        else:
                            new_data[attribute] = ktp_input
                            break
                    else:
                        print(f"{MessageEnum.KTP_WARNING.value}\n")
            else:
                new_data[attribute] = input(f"Masukkan {attribute} customer: ")
        
        # Call DataSetManager to add new data and store to file
        customer_id = self.add_new_data_set(new_data, RentEnum.CUSTOMER_ID_PREFIX.value)

        # Show output after add new data
        clear_screen()
        print(f"{MessageEnum.ADD_SUCCESS_MESSAGE.value} {customer_id}")
        show_table_data(self.read_data_set(), customer_header_attributes, customer_data_attributes, False)

        return customer_id

    # Update data function
    def update_data(self):

        # Show cars data for manipulate
        show_table_data(self.read_data_set(), customer_header_attributes, customer_data_attributes, False)

        while True:
            customer_id = input(MessageEnum.UPDATE_INPUT_MESSAGE.value)

            # Check if customer_id is in customers dictionary
            if customer_id in self.read_data_set():
                print(f"\n{MessageEnum.UPDATE_CHOICE_MESSAGE.value}")
                
                # Customer attributes for update
                for i, attribute in enumerate(customer_data_attributes, 1):
                    print(f"{i}. {attribute.capitalize()}")

                while True:
                    selected_field = input(f"\n{choose_option}")

                    # Check input is digit since we'll use as index
                    if selected_field.isdigit():
                        selected_index = int(selected_field) - 1
                        if 0 <= selected_index < len(customer_data_attributes):
                            selected_attribute = customer_data_attributes[selected_index]
                            if selected_attribute == 'nama':
                                while True:
                                    name_input = input(f"{MessageEnum.UPDATE_VALUE_MESSAGE.value}{selected_attribute} customer: ")
                                    if re.match(regex_patterns['alphabet'], name_input):
                                        updated_value = name_input
                                        break
                                    else:
                                        print(f"{MessageEnum.NAME_WARNING.value}\n")
                            elif selected_attribute == 'telepon':
                                while True:
                                    phone_input = input(f"{MessageEnum.UPDATE_VALUE_MESSAGE.value}{selected_attribute} customer: ")
                                    if re.match(regex_patterns['phone'], phone_input):
                                        updated_value = phone_input
                                        break
                                    else:
                                        print(f"{MessageEnum.PHONE_WARNING.value}\n")
                            elif selected_attribute == 'ktp':
                                while True:
                                    ktp_input = input(f"{MessageEnum.UPDATE_VALUE_MESSAGE.value}{selected_attribute} customer: ")
                                    if re.match(regex_patterns['ktp'], ktp_input):
                                        if self.is_ktp_exist(ktp_input):
                                            print(f"{attribute.capitalize()} {MessageEnum.CHOICE_NOT_EXIST.value}\n")
                                        else:
                                            updated_value = ktp_input
                                            break
                                    else:
                                        print(f"{MessageEnum.KTP_WARNING.value}\n")
                            else:
                                updated_value = input(f"{MessageEnum.UPDATE_VALUE_MESSAGE.value}{selected_attribute} customer: ")
                            
                            # Fetch the updated value
                            updated_customer_data = {selected_attribute: updated_value}

                            # Call DataSetManager to update the data and store to file
                            updated_data_id = self.update_data_set(customer_id, updated_customer_data)

                            # Show output after update data
                            clear_screen()
                            print(f"{MessageEnum.UPDATE_SUCCESS_MESSAGE.value} {updated_data_id}")
                            show_table_data(self.read_data_set(), customer_header_attributes, customer_data_attributes, False)

                            return updated_data_id
                        else:
                            print(f"{MessageEnum.CHOICE_NOT_EXIST.value}\n")
                    else:
                        print(f"{MessageEnum.CHOICE_NOT_EXIST.value}\n")
                break
            else:
                print(f"{MessageEnum.ID_NOT_FOUND_WARNING.value}\n")

    # Check if KTP already exist
    def is_ktp_exist(self, ktp):
        # Check if ktp exists in the current customer data set
        for customer_id, customer_data in self.read_data_set().items():
            if customer_data['ktp'] == ktp:
                return True
        return False

    # Delete data function
    def delete_data(self):

         # Show cars data for manipulate
        show_table_data(self.read_data_set(), customer_header_attributes, customer_data_attributes, False)

        customer_id = input(MessageEnum.DELETE_INPUT_MESSAGE.value)

        # Call DataSetManager to delete the data and store to file
        deleted_data_id = self.delete_data_set(customer_id)
        
        if deleted_data_id:
            # Show output after delete data
            clear_screen()
            print(f"{MessageEnum.DELETE_SUCCESS_MESSAGE.value} {deleted_data_id}")
            show_table_data(self.read_data_set(), customer_header_attributes, customer_data_attributes, False)
        
        return deleted_data_id