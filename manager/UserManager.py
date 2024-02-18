import re
import os
from .DataSetManager import *
from Config import *
from Util import *
from enums.MessageEnum import *
from enums.RentEnum import *

class UserManager(DataSetManager):

    # Init to use specific file
    def __init__(self):
        super().__init__(os.path.join(project_dir, 'data_set/', 'user_data.txt'))

    # Add new data function
    def add_new_data(self):
        new_data = {}

        # Loop the user's attribute from config and input the value
        for attribute in user_data_attributes:
            if attribute == 'username':
                while True:
                    username_input = input(f"Masukkan {attribute} user: ")
                    if re.match(regex_patterns['username'], username_input):
                        if self.is_username_exist(username_input):
                            print(f"{attribute.capitalize()} {MessageEnum.DATA_EXIST.value}\n")
                        else:
                            new_data[attribute] = username_input
                            break
                    else:
                        print(f"{MessageEnum.USERNAME_WARNING.value}\n")
            elif attribute == 'password':
                while True:
                    password_input = input(f"Masukkan {attribute} user: ")
                    if re.match(regex_patterns['password'], password_input):
                        new_data[attribute] = password_input
                        break
                    else:
                        print(f"{MessageEnum.PASSWORD_WARNING.value}\n")
            elif attribute == 'nama':
                while True:
                    name_input = input(f"Masukkan {attribute} user: ")
                    if re.match(regex_patterns['alphabet'], name_input):
                        new_data[attribute] = name_input
                        break
                    else:
                        print(f"{MessageEnum.NAME_WARNING.value}\n")
            elif attribute != 'role':
                new_data[attribute] = input(f"Masukkan {attribute} user: ")
        
        # Hardcode for new data value
        new_data['role'] = "admin"

        # Call DataSetManager to add new data and store to file
        user_id = self.add_new_data_set(new_data, RentEnum.USER_ID_PREFIX.value)

        # Show output after add new data
        clear_screen()
        print(f"{MessageEnum.ADD_SUCCESS_MESSAGE.value} {user_id}")
        show_table_data(self.read_data_set(), user_header_attributes, user_data_attributes, False)

        return user_id

    # Update data function
    def update_data(self):

        # Show user data for manipulate
        show_table_data(self.read_data_set(), user_header_attributes, user_data_attributes, False)

        while True:
            user_id = input(MessageEnum.UPDATE_INPUT_MESSAGE.value)

            # Check if user_id is in users dictionary
            if user_id in self.read_data_set():
                print(MessageEnum.UPDATE_CHOICE_MESSAGE.value)
                
                # User attributes for update
                for i, attribute in enumerate(user_data_attributes, 1):
                    print(f"{i}. {attribute.capitalize()}")

                while True:
                    selected_field = input(f"\n{choose_option}")

                    # Check input is digit since we'll use as index
                    if selected_field.isdigit():
                        selected_index = int(selected_field) - 1
                        if 0 <= selected_index < len(user_data_attributes):
                            selected_attribute = user_data_attributes[selected_index]
                            
                            # Logic special case for attribute 'username'
                            if selected_attribute == 'username':
                                while True:
                                    username_input = input(f"{MessageEnum.UPDATE_VALUE_MESSAGE.value}{selected_attribute} user: ")
                                    if re.match(regex_patterns['username'], username_input):
                                        if self.is_username_exist(username_input):
                                            print(f"{selected_attribute.capitalize()} {MessageEnum.DATA_EXIST.value}\n")
                                        else:
                                            updated_value = username_input
                                            break
                                    else:
                                        print(f"{MessageEnum.USERNAME_WARNING.value}\n")
                            elif selected_attribute == 'password':
                                while True:
                                    password_input = input(f"{MessageEnum.UPDATE_VALUE_MESSAGE.value}{selected_attribute} user: ")
                                    if re.match(regex_patterns['password'], password_input):
                                        updated_value = password_input
                                        break
                                    else:
                                        print(f"{MessageEnum.PASSWORD_WARNING.value}\n")
                            elif selected_attribute == 'nama':
                                while True:
                                    name_input = input(f"{MessageEnum.UPDATE_VALUE_MESSAGE.value}{selected_attribute} user: ")
                                    if re.match(regex_patterns['alphabet'], name_input):
                                        updated_value = name_input
                                        break
                                    else:
                                        print(f"{MessageEnum.NAME_WARNING.value}\n")
                            else:
                                updated_value = input(f"{MessageEnum.UPDATE_VALUE_MESSAGE.value}{selected_attribute} user: ")
                            
                            # Fetch the updated value
                            updated_user_data = {selected_attribute: updated_value}

                            # Call DataSetManager to update the data and store to file
                            updated_data_id = self.update_data_set(user_id, updated_user_data)

                            # Show output after update data
                            clear_screen()
                            print(f"{MessageEnum.UPDATE_SUCCESS_MESSAGE.value} {updated_data_id}")
                            show_table_data(self.read_data_set(), user_header_attributes, user_data_attributes, False)

                            return updated_data_id
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
        show_table_data(self.read_data_set(), user_header_attributes, user_data_attributes, False)

        user_id = input(MessageEnum.DELETE_INPUT_MESSAGE.value)

         # Call DataSetManager to delete the data and store to file
        deleted_data_id = self.delete_data_set(user_id)

        if deleted_data_id:
            # Show output after delete data
            clear_screen()
            print(f"{MessageEnum.DELETE_SUCCESS_MESSAGE.value} {deleted_data_id}")
            show_table_data(self.read_data_set(), user_header_attributes, user_data_attributes, False)
        
        return deleted_data_id

    # Username existence check function
    def is_username_exist(self, username):
        # Check if username exists in the current user data set
        for user_id, user_data in self.read_data_set().items():
            if user_data['username'] == username:
                return True
        return False

    # Login function
    def login(self, username, password):
        for user_id, user_data in self.read_data_set().items():
            if user_data["username"] == username:
                if user_data["password"] == password:
                    return user_data
                else:
                    print("\nPassword salah.")
                    return None
        print("\nUsername tidak ditemukan.")
        return None
