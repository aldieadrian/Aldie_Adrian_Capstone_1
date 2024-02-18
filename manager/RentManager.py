import re
from .DataSetManager import *
from datetime import datetime, date
from tabulate import tabulate
from Util import *
from Config import *
from enums.RentEnum import *
from .CarManager import * 
from enums.MessageEnum import *

class RentManager(DataSetManager):

    # Init to use specific file
    def __init__(self):
        super().__init__(os.path.join(project_dir, 'data_set/', 'rent_data.txt'))

    # Add new data function
    def add_new_rent_data(self, cars, customers):
        new_data = {}
        car_id = ''

        # Loop the rent's attribute from config and input the value
        for attribute in rent_data_attributes:
            if attribute == 'customer_id':
                while True:
                    show_table_data(customers, customer_header_attributes, customer_data_attributes, False)
                    customer_id_input = input("Masukkan ID Customer: ")
                    if is_data_exist(customer_id_input, customers):
                        new_data[attribute] = customer_id_input
                        clear_screen()
                        break
                    else:
                        print(f"ID Customer tidak ditemukan. Silahkan Coba lagi\n")
            elif attribute == 'car_id':
                while True:
                    show_table_data(cars, car_header_attributes, car_data_attributes, False)
                    car_id_input = input("Masukkan ID Mobil: ")
                    if is_data_exist(car_id_input, cars):
                        if is_data_available(car_id_input, cars):
                            new_data[attribute] = car_id_input
                            car_id = car_id_input
                            # Set the rent_date based on today's date
                            new_data['rent_date'] = get_today_date_string()
                            clear_screen()
                            break
                        else:
                            print(f"Mobil tidak tersedia. Silahkan pilih mobil lain\n")
                    else:
                        print(f"ID Mobil tidak ditemukan. Silahkan Coba lagi\n")
            elif attribute == 'duration':
                while True:
                    duration_input = input("Masukkan Durasi Peminjaman: ")
                    if re.match(regex_patterns['duration'], duration_input):
                        new_data[attribute] = int(duration_input)
                        clear_screen()
                        break
                    else:
                        print(f"{MessageEnum.DURATION_WARNING.value}\n")

        # Hardcode for new data value
        new_data['return_date'] = RentEnum.NOT_YET.value
        subtotal = self.calculate_subtotal(new_data, cars)
        new_data['subtotal'] = subtotal
        new_data['charge'] = 0
        new_data['total'] = subtotal
        new_data['status'] = RentEnum.ON_RENT.value

        # Call DataSetManager to add new data and store to file
        rent_id = self.add_new_data_set(new_data, RentEnum.RENT_ID_PREFIX.value)

        # Call DataSetManager to update the data and store to file (car data)
        self.update_car_data_for_rent(car_id, RentEnum.ON_RENT.value)

        # Show output after add new data
        clear_screen()
        print(f"{MessageEnum.ADD_SUCCESS_MESSAGE.value} {rent_id}")
        show_table_data(self.read_data_set(), rent_header_attributes, rent_data_attributes, False)

        return rent_id

    # Return rented car function
    def return_rented_car(self, cars):

        # Get rent dictionary to manipulate
        rents = self.read_data_set()

        # Show rent data for manipulate
        show_table_data(rents, rent_header_attributes, rent_data_attributes, False)
        
        while True:
            rent_id_input = input("Masukkan ID Penyewaan: ")

            if is_data_exist(rent_id_input, rents):
                rent_data = rents[rent_id_input]
                if rent_data['status'] == RentEnum.ON_RENT.value:

                    # Set car data to return
                    car_data = cars[rent_data['car_id']]

                    # Check actual duration when car returned
                    actual_duration = date.today() - datetime.strptime(rent_data['rent_date'], '%Y-%m-%d').date()

                    # Calculate charge based on latency return
                    charge = 0
                    if actual_duration.days > rent_data['duration']:
                        difference = actual_duration.days - rent_data['duration']
                        charge = difference * (int(car_data['harga']) + late_charge)

                    # Accumulate total and charge amount
                    total = rent_data['total'] + charge

                    # Fetch the updated value
                    updated_rent_data = {
                        'return_date': get_today_date_string(),
                        'charge': charge,
                        'total': total,
                        'status': RentEnum.RETURNED.value,
                    }

                    # Call DataSetManager to update the data and store to file (rent data)
                    self.update_data_set(rent_id_input, updated_rent_data)

                    # Call DataSetManager to update the data and store to file (car data)
                    self.update_car_data_for_rent(rent_data['car_id'], RentEnum.AVAILABLE.value)

                    # Show output after update data
                    clear_screen()
                    print(f"Penyewaan dengan ID {rent_id_input} sudah selesai. Terima Kasih!\n")
                    show_table_data(self.read_data_set(), rent_header_attributes, rent_data_attributes, False)
                    
                    break
                else:
                    print(f"Transaksi Penyewaan sudah selesai. Silahkan Coba lagi\n")
            else:
                print(f"ID Penyewaan tidak ditemukan. Silahkan Coba lagi\n")

    # Update car data when rent is returned function
    def update_car_data_for_rent(self, car_id, status):
        updated_car_data = {'status': status}
        carManager = CarManager()
        carManager.update_car_for_rent(car_id, updated_car_data)

    # Calculate the subtotal function
    def calculate_subtotal(self, data, datas):
        duration = data['duration']
        price = datas[data['car_id']]['harga']
        return int(duration) * int(price)
