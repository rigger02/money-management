import csv
from datetime import datetime
import os

# Folder untuk penyimpanan file CSV
folder_path = r'C:\Users\user\Downloads\anotherday'

# Pastikan folder ada
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Fungsi untuk membaca data dari file CSV
def read_csv(filename):
    data = []
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        pass
    return data

# Fungsi untuk menulis data ke file CSV
def write_csv(filename, data, fieldnames):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# List untuk penyimpanan sementara transaksi
transactions = []

# HashMap (Dictionary) untuk kategori pengeluaran
categories = {
    "food": "Makanan",
    "transport": "Transportasi",
    "entertainment": "Hiburan",
    "other": "Lain-lain"
}

# Fungsi untuk menambah transaksi
def add_transaction(date, type, amount, category, description):
    transaction = {
        "date": date,
        "type": type,
        "amount": float(amount),
        "category": category,
        "description": description
    }
    transactions.append(transaction)

# Fungsi untuk membaca semua transaksi
def read_transactions():
    return transactions

# Fungsi untuk memperbarui transaksi
def update_transaction(index, date, type, amount, category, description):
    transactions[index] = {
        "date": date,
        "type": type,
        "amount": float(amount),
        "category": category,
        "description": description
    }

# Fungsi untuk menghapus transaksi
def delete_transaction(index):
    transactions.pop(index)

# Fungsi untuk menghasilkan laporan bulanan
def monthly_report(month, year):
    monthly_transactions = [t for t in transactions if datetime.strptime(t["date"], '%Y-%m-%d').month == month and datetime.strptime(t["date"], '%Y-%m-%d').year == year]
    return monthly_transactions

# Fungsi untuk menghasilkan laporan tahunan
def yearly_report(year):
    yearly_transactions = [t for t in transactions if datetime.strptime(t["date"], '%Y-%m-%d').year == year]
    return yearly_transactions

# Fungsi untuk menyimpan data sementara ke file CSV
def save_data():
    file_name = input("Masukkan nama file untuk disimpan (tanpa ekstensi .csv): ") + '.csv'
    filename = os.path.join(folder_path, file_name)
    fieldnames = ["date", "type", "amount", "category", "description"]
    write_csv(filename, transactions, fieldnames)
    print(f"Data telah disimpan ke {filename}")

# Fungsi untuk memuat data dari file CSV
def load_data():
    file_name = input("Masukkan nama file untuk dimuat (tanpa ekstensi .csv): ") + '.csv'
    filename = os.path.join(folder_path, file_name)
    global transactions
    transactions = read_csv(filename)
    print(f"Data telah dimuat dari {filename}")

# Main program
def main():
    while True:
        print("\n" + "="*30)
        print("\nManajemen Keuangan Pribadi")
        print("1. Tambah Transaksi")
        print("2. Tampilkan Semua Transaksi")
        print("3. Perbarui Transaksi")
        print("4. Hapus Transaksi")
        print("5. Laporan Bulanan")
        print("6. Laporan Tahunan")
        print("7. Simpan Data Sementara (format CSV)")
        print("8. Load Data (format CSV)")
        print("9. Keluar")

        choice = input("Pilih opsi: ")

        if choice == '1':
            date = input("Tanggal (YYYY-MM-DD): ")
            type = input("Tipe (income/expense): ")
            amount = input("Jumlah: ")
            category = input("Kategori: ")
            description = input("Deskripsi: ")
            add_transaction(date, type, amount, category, description)

        elif choice == '2':
            for i, t in enumerate(read_transactions()):
                print(f"{i}. {t['date']} | {t['type']} | {t['amount']} | {t['category']} | {t['description']}")

        elif choice == '3':
            index = int(input("Index transaksi yang akan diperbarui: "))
            date = input("Tanggal (YYYY-MM-DD): ")
            type = input("Tipe (income/expense): ")
            amount = input("Jumlah: ")
            category = input("Kategori: ")
            description = input("Deskripsi: ")
            update_transaction(index, date, type, amount, category, description)

        elif choice == '4':
            index = int(input("Index transaksi yang akan dihapus: "))
            delete_transaction(index)

        elif choice == '5':
            month = int(input("Bulan (1-12): "))
            year = int(input("Tahun (YYYY): "))
            report = monthly_report(month, year)
            for t in report:
                print(f"{t['date']} | {t['type']} | {t['amount']} | {t['category']} | {t['description']}")

        elif choice == '6':
            year = int(input("Tahun (YYYY): "))
            report = yearly_report(year)
            for t in report:
                print(f"{t['date']} | {t['type']} | {t['amount']} | {t['category']} | {t['description']}")

        elif choice == '7':
            save_data()

        elif choice == '8':
            load_data()

        elif choice == '9':
            if input("Apakah Anda ingin menyimpan data terlebih dahulu? (y/n): ") == 'y':
                save_data()
            else:
                print("terimakasih, sampai bertemu lagi")
                break

        else:
            print("Opsi tidak valid, coba lagi.")

if __name__ == "__main__":
    main()
