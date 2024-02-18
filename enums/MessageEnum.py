from enum import Enum

class MessageEnum(Enum):

    # Base Enums
    LOGIN_HEADER = "Silahkan login untuk masuk Aplikasi Rental Mobil."
    CHOICE_NOT_EXIST = "Pilihan anda tidak tersedia. Silakan coba lagi.\n"
    EXIT_MESSAGE = "Terima kasih telah menggunakan Aplikasi Rental Mobil ini. Sampai jumpa!\n"
    DATA_EXIST = "sudah digunakan. Silakan coba lagi."
    USERNAME = "username"
    PASSWORD = "password"
    
    # Add Data Enums
    ADD_SUCCESS_MESSAGE = "Data berhasil ditambahkan dengan ID: "

    # Update Data Enums
    UPDATE_SUCCESS_MESSAGE = "Data berhasil diperbarui untuk ID: "
    UPDATE_CHOICE_MESSAGE = "Pilih atribut yang ingin diperbarui: "
    UPDATE_INPUT_MESSAGE = "Masukkan ID untuk data yang ingin diperbarui: "
    UPDATE_VALUE_MESSAGE = "Masukkan data baru untuk "
    
    # Delete Data ENums
    DELETE_SUCCESS_MESSAGE = "Data berhasil dihapus untuk ID: "
    DELETE_INPUT_MESSAGE = "Masukkan ID yang ingin dihapus: "

    # Warning Enums
    USERNAME_WARNING = "Username harus terdiri dari 3 hingga 16 karakter. Silakan coba lagi."
    PASSWORD_WARNING = "Password harus terdiri dari minimal 6 karakter dan mengandung setidaknya satu huruf kecil, satu huruf besar, dan satu angka. Silakan coba lagi."
    NAME_WARNING = "Nama harus berupa alphabet. Silakan coba lagi."
    PHONE_WARNING = "Nomor telepon harus berupa angka dan berjumlah 7 sampai 12 digit. Silakan coba lagi."
    KTP_WARNING = "Nomor KTP harus berupa 16 digit angka. Silakan coba lagi."
    YEAR_WARNING = "Format tahun tidak valid. Harap masukkan tahun dengan format yang benar (misal: 2022)."
    PRICE_WARNING = "Format harga tidak valid. Harus berupa angka dan di atas 0. Silakan coba lagi."
    ID_NOT_FOUND_WARNING = "ID tidak ditemukan. Silakan coba lagi."
    DURATION_WARNING = "Durasi peminjaman harus berupa angka untuk jumlah hari. Silahkan coba lagi."
