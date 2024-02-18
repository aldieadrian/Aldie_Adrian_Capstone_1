from Config import *
from Util import *
from manager.UserManager import UserManager
from manager.CarManager import CarManager
from manager.CustomerManager import CustomerManager
from manager.RentManager import RentManager
from enums.MessageEnum import MessageEnum

# Initialize manager class
userManager = UserManager()
carManager = CarManager()
customerManager = CustomerManager()
rentManager = RentManager()

# Define logged_in_user for session
logged_in_user = {}

def main():
    global logged_in_user
    
    # Check logged_in_user is exist or not
    if not logged_in_user:
        login()

    # Main Menu
    while True:
        print(f"Halo {logged_in_user['nama']} di Aplikasi Rental Mobil")
        main_menu()
        choice = input(f"\n{choose_option}")
        if choice == '1': # Penyewaan mobil
            clear_screen()
            rent_menu()
            continue
        elif choice == '2': # Kelola data customer
            clear_screen()
            customer_menu()
            continue
        elif choice == '3': # Lihat data mobil
            clear_screen()
            show_table_data(carManager.read_data_set(), car_header_attributes, car_data_attributes, True)
            continue
        elif choice == '4': # Kelola data mobil for superadmin
            if is_superadmin():
                clear_screen()
                car_menu()
            else:
                clear_screen()
                print(MessageEnum.CHOICE_NOT_EXIST.value)
                continue
        elif choice == '5': # Kelola akun user for superadmin
            if is_superadmin():
                clear_screen()
                user_menu()
            else:
                clear_screen()
                print(MessageEnum.CHOICE_NOT_EXIST.value)
                continue
        elif choice == '0': # Keluar
            clear_screen()
            print(MessageEnum.EXIT_MESSAGE.value)
            exit()
        else:
            print(MessageEnum.CHOICE_NOT_EXIST.value)
            continue

# Login function
def login():
    global logged_in_user
    while True:
        clear_screen()

        # Login input section
        print(f"{MessageEnum.LOGIN_HEADER.value}\n")
        username = input(f"Masukkan {MessageEnum.USERNAME.value}: ")
        password = input(f"Masukkan {MessageEnum.PASSWORD.value}: ")

        # Call UserManager for login
        logged_in_user = userManager.login(username, password)

        # Check login success if logged_in_user exist
        if logged_in_user:
            clear_screen()
            break
        else:
            choice = input("Apakah Anda ingin mencoba lagi? (y/n): ")
            if choice.lower() != "y":
                clear_screen()
                print(MessageEnum.EXIT_MESSAGE.value)
                exit()

# Compose main menu function
def main_menu():
    global logged_in_user
    if logged_in_user['role'] == 'superadmin':
        # Update main menu items for superadmin
        main_menu_attributes.update(superadmin_menu_attributes)
    print("\nMenu Utama:")
    for key, value in main_menu_attributes.items():
        print(f"{key}. {value}")
    print("0. Keluar")

# Rent menu function
def rent_menu():
    while True:
        
        # Get needed dictionaries
        cars = carManager.read_data_set()
        customers = customerManager.read_data_set()
        rents = rentManager.read_data_set()

        print(f"Menu Penyewaan Mobil:")
        for key, value in rent_menu_attributes.items():
            print(f"{key}. {value}")
        choice = input(f"\n{choose_option}")
        if choice == '1': # Filter Data Penyewaan
            clear_screen()
            show_table_data(rents, rent_header_attributes, rent_data_attributes, True)
            continue
        elif choice == '2': # Buat Penyewaan Baru
            clear_screen()
            rentManager.add_new_rent_data(cars, customers)
            continue
        elif choice == '3': # Pengembalian Mobil
            clear_screen()
            rentManager.return_rented_car(cars)
            continue
        elif choice == '0': # Kembali ke Menu Utama
            clear_screen()
            return
        else:
            print(f"{MessageEnum.CHOICE_NOT_EXIST.value}\n")
            continue
        
# Car menu function
def car_menu():
    while True:

        # Get cars dictionary data for manipulate
        cars = carManager.read_data_set()

        print(f"Menu Kelola Data Mobil:")
        
        # Loop the car's menu attribute from config and input the value
        for key, value in car_menu_attributes.items():
            print(f"{key}. {value}")
        choice = input(f"\n{choose_option}")
        if choice == '1': # Filter Data Mobil
            clear_screen()
            show_table_data(cars, car_header_attributes, car_data_attributes, True)
            continue
        elif choice == '2': # Tambah Data Mobil
            clear_screen()
            carManager.add_new_data()
            continue
        elif choice == '3': # Ubah Data Mobil
            clear_screen()
            carManager.update_data()
            continue
        elif choice == '4': # Hapus Data Mobil
            clear_screen()
            carManager.delete_data()
            continue
        elif choice == '0': # Kembali ke Menu Utama
            clear_screen()
            return
        else:
            print(f"{MessageEnum.CHOICE_NOT_EXIST.value}\n")
            continue


# User menu function
def user_menu():
    while True:
        
        # Get user dictionary data for manipulate
        users = userManager.read_data_set()
    
        print(f"Menu Kelola Data User:")

        # Loop the user's menu attribute from config and input the value
        for key, value in user_menu_attributes.items():
            print(f"{key}. {value}")
        choice = input(f"\n{choose_option}")
        if choice == '1': # Filter Data User
            clear_screen()
            show_table_data(users, user_header_attributes, user_data_attributes, True)
            continue
        elif choice == '2': # Tambah Data User
            clear_screen()
            userManager.add_new_data()
            continue
        elif choice == '3': # Ubah Data User
            clear_screen()
            userManager.update_data()
            continue
        elif choice == '4': # Hapus Data User
            clear_screen()
            userManager.delete_data()
            continue
        elif choice == '0': # Kembali ke Menu Utama
            clear_screen()
            return
        else:
            print(f"{MessageEnum.CHOICE_NOT_EXIST.value}\n")
            continue


# Compose customer menu function
def customer_menu():
    while True:

        # Get customers dictionary data for manipulate
        customers = customerManager.read_data_set()

        print(f"Menu Kelola Data Customer:")

        # Loop the car's menu attribute from config and input the value
        for key, value in customer_menu_attributes.items():
            print(f"{key}. {value}")
        choice = input(f"\n{choose_option}")
        if choice == '1': # Filter Data Customer
            clear_screen()
            show_table_data(customers, customer_header_attributes, customer_data_attributes, True)
            continue
        elif choice == '2': # Tambah Data Customer
            clear_screen()
            customerManager.add_new_data()
            continue
        elif choice == '3': # Ubah Data Customer
            clear_screen()
            customerManager.update_data()
            continue
        elif choice == '4': # Hapus Data Customer
            clear_screen()
            customerManager.delete_data()
            continue
        elif choice == '0': # Kembali ke Menu Utama
            clear_screen()
            return
        else:
            print(f"{MessageEnum.CHOICE_NOT_EXIST.value}\n")
            continue

# Check is user is superadmin function
def is_superadmin():
    global logged_in_user
    if logged_in_user['role'] == 'superadmin':
        return True
    else:
        return False

# Init main class
if __name__ == "__main__":
    main()
