# Sistem antrian rumah sakit 
antrian = []

def tambah_pasien(nama, poli):
    "Menambahkan pasien ke dalam antrian"
    antrian.append((nama, poli))
    print(f"Pasien {nama} dengan poli {poli} telah terdaftar dalam antrian.")

def layani_pasien(nama, status, poli):
    "Prioritaskan pasien darurat"
    print(f"Pasien {nama} dengan status {status} dan poli {poli} sedang dilayani.")

def hitung_waktu_tunggu():
    "Perkiraan waktu tunggu berdasarkan pasien dalam antrian"
    waktu_per_pasien = 15  # Anggap tiap pasien membutuhkan waktu 15 menit
    return waktu_per_pasien * len(antrian)

def tambah_dokter_poli(poli, dokter):
    "Menambahkan poli dan dokter"
    print(f"Poli {poli} dengan dokter {dokter} ditambahkan.")

def proses_pasien():
    "Proses pasien dari antrian sesuai dengan prioritas"
    if antrian:
        pasien = antrian.pop(0)  # Mengambil pasien pertama dalam antrian
        print(f"Pasien {pasien[0]} sedang diperiksa di poli {pasien[1]}.")
    else:
        print("Antrian kosong, tidak ada pasien yang dapat diproses.")

def status_antrian():
    "Menampilkan status antrian"
    print(f"Jumlah pasien dalam antrian: {len(antrian)}")

def menu():
    "Menampilkan menu dan menjalankan pilihan pengguna"
    while True:
        print("\n--- Menu Antrian Rumah Sakit ---")
        print("1. Tambah pasien")
        print("2. Layani pasien")
        print("3. Hitung waktu tunggu")
        print("4. Tambah dokter poli")
        print("5. Proses pasien")
        print("6. Status antrian")
        print("7. Keluar")

        pilihan = input("Masukkan pilihan (1-7): ")

        if pilihan == '1':
            nama_pasien = input("Masukkan nama pasien: ")
            poli_pasien = input("Masukkan poli pasien: ")
            tambah_pasien(nama_pasien, poli_pasien)
        elif pilihan == '2':
            nama_pasien = input("Masukkan nama pasien: ")
            status_pasien = input("Masukkan status pasien (darurat/biasa): ")
            poli_pasien = input("Masukkan poli pasien: ")
            layani_pasien(nama_pasien, status_pasien, poli_pasien)
        elif pilihan == '3':
            waktu_tunggu = hitung_waktu_tunggu()
            print(f"Waktu tunggu estimasi: {waktu_tunggu} menit.")
        elif pilihan == '4':
            poli = input("Masukkan nama poli: ")
            dokter = input("Masukkan nama dokter: ")
            tambah_dokter_poli(poli, dokter)
        elif pilihan == '5':
            proses_pasien()
        elif pilihan == '6':
            status_antrian()
        elif pilihan == '7':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

# Menjalankan program
if __name__ == "__main__":
    menu()
