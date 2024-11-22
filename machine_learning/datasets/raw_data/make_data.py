import pandas as pd
import random
import os

# Fungsi untuk membuat Data Donor
def generate_donor_data(n):
    data = []
    for i in range(n):
        lat = round(random.uniform(-5.439174727052239, -5.37286637048833), 14)  # Koordinat di wilayah Bandar Lampung
        lon = round(random.uniform(105.20842398470758, 105.31416739581265), 14)
        
        donor = {
            "donor_id": "D" + str(i + 1), 
            "jenis_makanan": random.sample(["makanan", "minuman"], random.randint(1, 2)),
            "jumlah_makanan": random.randint(1, 10),  # dalam kg atau porsi
            "lokasi_donor": (lat, lon),  # Lokasi dalam koordinat GPS
            "makanan_layak_konsumsi": random.choice(["layak konsumsi", "hampir kadaluarsa", "tidak layak konsumsi"]),
            "is_halal": random.choice([True, False]),
            "is_for_child": random.choice([True, False]),
            "is_for_elderly": random.choice([True, False]),
            "is_alergan": random.choice([True, False])
        }
        data.append(donor)
    return pd.DataFrame(data)

# Fungsi untuk membuat Data Penerima
def generate_receiver_data(n):
    data = []
    for i in range(n):
        lat = round(random.uniform(-5.439174727052239, -5.37286637048833), 14)  # Koordinat di wilayah Bandar Lampung
        lon = round(random.uniform(105.20842398470758, 105.31416739581265), 14)
        
        receiver = {
            "penerima_id": "R" + str(i + 1),
            "jenis_makanan_dibutuhkan": random.sample(["makanan", "minuman"], random.randint(1, 2)),  # Sekarang jenis makanan bisa banyak
            "jumlah_dibutuhkan": random.randint(1, 10),  # dalam kg atau porsi
            "lokasi_penerima": (lat, lon),  # Lokasi dalam koordinat GPS
            "jumlah_diterima": random.randint(0, 5),
            "makanan_layak_konsumsi" : random.choice(["layak konsumsi", "tidak layak konsumsi"])
        }
        
        # Jika makanan yang dibutuhkan layak konsumsi, tambahkan informasi lebih lanjut
        if receiver["makanan_layak_konsumsi"] == "layak konsumsi":
            receiver.update({
                "makanan_layak_konsumsi": random.sample(["layak konsumsi", "hampir kadaluarsa"], random.randint(1, 2)),
                "is_halal": random.choice([True, False]),
                "is_for_child": random.choice([True, False]),
                "is_for_elderly": random.choice([True, False]),
                "is_alergan_free": random.choice([True, False])
            })
        else:
            receiver.update({
                "makanan_layak_konsumsi": "tidak layak konsumsi",
                "is_halal": False,
                "is_for_child": False,
                "is_for_elderly": False,
                "is_alergan_free": False
            })
        
        data.append(receiver)
    return pd.DataFrame(data)

# Path untuk menyimpan file
donor_file_path = 'machine_learning/datasets/raw_data/data_donor.csv'
receiver_file_path = 'machine_learning/datasets/raw_data/data_receiver.csv'

# Cek keberadaan file sebelum menulis ulang
if not os.path.exists(donor_file_path):
    donor_data = generate_donor_data(2000)  # 2000 data donor
    donor_data.to_csv(donor_file_path, index=False)
    print("Data donor dibuat dan disimpan.")
else:
    print("Data donor sudah ada. Tidak menimpa file yang ada.")

if not os.path.exists(receiver_file_path):
    receiver_data = generate_receiver_data(2000)  # 2000 data penerima
    receiver_data.to_csv(receiver_file_path, index=False)
    print("Data penerima dibuat dan disimpan.")
else:
    print("Data penerima sudah ada. Tidak menimpa file yang ada.")

# Menampilkan contoh data jika file sudah ada
if os.path.exists(donor_file_path):
    donor_data = pd.read_csv(donor_file_path)
    print("\nContoh Data Donor:")
    print(donor_data.head())

if os.path.exists(receiver_file_path):
    receiver_data = pd.read_csv(receiver_file_path)
    print("\nContoh Data Penerima:")
    print(receiver_data.head())
