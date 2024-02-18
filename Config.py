import os

# Init project directory
project_dir = os.path.abspath(os.path.dirname(__file__))

# Late charge for return rented car
late_charge = 50000

# Regex patterns
regex_patterns = {
    "username": r"^[a-zA-Z0-9_-]{3,16}$",
    "password": r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,}$",
    "alphabet": r"^[A-Za-z\s'-]+$",
    "year": r"\b\d{4}\b",
    "price": r"^\d+$", 
    "ktp": r"^\d{16}$", 
    "phone": r"^\d{7,12}$",
    "duration": r"\d",
}

# Main Menu Attributes
main_menu_attributes = {
    1: "Penyewaan Mobil",
    2: "Kelola Data Pelanggan",
    3: "Lihat Data Mobil",
}

superadmin_menu_attributes = {
    4: "Kelola Data Mobil",
    5: "Kelola Akun User",
}

# Car Attributes
car_menu_attributes = {
    1: "Filter Data Mobil",
    2: "Tambah Data Mobil",
    3: "Ubah Data Mobil",
    4: "Hapus Data Mobil",
    0: "Kembali ke Menu Utama",
}

car_data_attributes = [
    "brand",
    "model",
    "warna",
    "tahun",
    "harga",
    "status"
]

car_header_attributes = [
    "ID Mobil",
    "Brand",
    "Model",
    "Warna",
    "Tahun",
    "Harge Sewa Per Hari",
    "Status"
]

# User Attributes
user_menu_attributes = {
    1: "Filter Data User",
    2: "Tambah Data User",
    3: "Ubah Data User",
    4: "Hapus Data User",
    0: "Kembali ke Menu Utama",
}

user_data_attributes = [
    "username",
    "password",
    "nama",
    "role"
]

user_header_attributes = [
    "ID User",
    "Username",
    "Password",
    "Nama",
    "Role"
]

# Customer Attributes
customer_menu_attributes = {
    1: "Filter Data Customer",
    2: "Tambah Data Customer",
    3: "Ubah Data Customer",
    4: "Hapus Data Customer",
    0: "Kembali ke Menu Utama",
}

customer_data_attributes = [
    "nama",
    "alamat",
    "kota",
    "telepon",
    "ktp"
]

customer_header_attributes = [
    "ID Customer",
    "Nama",
    "Alamat",
    "Kota Domisili",
    "Nomor Telepon",
    "Nomor KTP"
]

# Rent Attributes
rent_menu_attributes = {
    1: "Filter Data Penyewaan",
    2: "Buat Penyewaan Baru",
    3: "Pengembalian Mobil",
    0: "Kembali ke Menu Utama",
}

rent_data_attributes = [
    "customer_id",
    "car_id",
    "rent_date",
    "duration",
    "return_date",
    "subtotal",
    "charge",
    "total",
    "status"
]

rent_header_attributes = [
    "ID Penyewaan ",
    "ID Pelanggan ",
    "ID Mobil",
    "Tanggal Sewa",
    "Durasi Sewa",
    "Tanggal Pengembalian",
    "Subtotal",
    "Denda Keterlambatan",
    "Total Biaya Sewa",
    "Status"
]