import uuid
from tabulate import tabulate
from datetime import date
from Config import *
from enums.MessageEnum import *

choose_option = "Pilihan: "

# Show table data function
def show_table_data(datas, data_header_atributes, data_attributes, need_filter_menu):

    # Convert the datas dictionary to table_data list for output
    table_data = []
    for id, data in datas.items():
        table_data.append([id] + list(data.values()))
    print(tabulate(table_data, headers=data_header_atributes, tablefmt='pretty'))
    
    if need_filter_menu:
        filter_datas(datas, data_header_atributes, data_attributes)

# Filter data function
def filter_datas(datas, data_header_atributes, data_attributes):
    while True:
        print("\nPilih field untuk filter:")
        for i, attribute in enumerate(data_header_atributes[1:], 1):
            print(f"{i}. {attribute.capitalize()}")
        print("0. Kembali")

        choice = input(f"\n{choose_option}")
        if choice == '0':
            clear_screen()
            return

        if choice.isdigit():
            selected_index = int(choice) - 1
            if 0 <= selected_index < len(data_attributes):
                selected_attribute = data_attributes[selected_index]
                filter_by_attribute(datas, selected_attribute, data_header_atributes)
            else:
                print(MessageEnum.CHOICE_NOT_EXIST.value)
        else:
            print(MessageEnum.CHOICE_NOT_EXIST.value)

# Show filtered data function
def filter_by_attribute(datas, attribute, data_header_atributes):
    value = input(f"Masukkan nilai untuk filter: ")
    
    # Filter datas by the selected attribute and value
    filtered_datas = {id: data for id, data in datas.items() if str(data.get(attribute, '')).lower() == str(value).lower()}

    filtered_table_data = []
    for id, data in filtered_datas.items():
        filtered_table_data.append([id] + list(data.values()))

    # Print the filtered datas using tabulate
    if filtered_table_data:
        print(tabulate(filtered_table_data, headers=data_header_atributes, tablefmt='pretty'))
    else:
        print(MessageEnum.CHOICE_NOT_EXIST.value)

# Check if id and data exist in dictionary
def is_data_exist(request_id, datas):
    # Check if request_id exists in datas
    return request_id in datas

# Set data is available
def is_data_available(request_id, datas):
    return datas[request_id]['status'] == 'available'

# Today date getter
def get_today_date_string():
    return date.today().strftime("%Y-%m-%d")

# Clear terminal function
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    return