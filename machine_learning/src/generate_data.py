import random
import csv
import os

# Menentukan path untuk folder 'raw'
raw_data_dir = 'machine_learning/data/raw'

# Membuat folder 'raw' jika belum ada
os.makedirs(raw_data_dir, exist_ok=True)

# Fungsi untuk mengenerate data donor
def generate_donor_data(num_donors):
    donor_data = []
    
    for i in range(num_donors):
        donor_id = f"D{i+1}"
        jenis_makanan = random.choice(['makanan', 'minuman', 'makanan_minuman'])
        jumlah_disumbangkan = random.randint(1, 50)
        lokasi_lat_penyumbang = random.uniform(-5.405901634725342, -5.365442970161212)  # Rentang koordinat lintang
        lokasi_lon_penyumbang = random.uniform(105.22551998740258, 105.29009985878861)  # Rentang koordinat bujur
        kondisi_makanan = random.choice(['layak_konsumsi', 'hampir_kadaluarsa', 'tidak_layak_konsumsi'])

        # Logika tambahan untuk kondisi 'tidak layak konsumsi'
        if kondisi_makanan == 'tidak layak konsumsi':
            is_halal = False
            is_for_child = False
            is_for_elderly = False
            is_alergan = True
        else:
            is_halal = random.choice([True, False])
            is_for_child = random.choice([True, False])
            is_for_elderly = random.choice([True, False])
            is_alergan = random.choice([True, False])
        
        donor_data.append([
            donor_id,
            jenis_makanan,
            jumlah_disumbangkan,
            lokasi_lat_penyumbang,
            lokasi_lon_penyumbang,
            kondisi_makanan,
            is_halal,
            is_for_child,
            is_for_elderly,
            is_alergan
        ])
        
    return donor_data

# Fungsi untuk mengenerate data penerima
def generate_receiver_data(num_receivers):
    receiver_data = []
    
    for i in range(num_receivers):
        receiver_id = f"T{i+1}"
        makanan_dibutuhkan = random.choice(['makanan', 'minuman', 'makanan_minuman'])
        jumlah_dibutuhkan = random.randint(1, 50)
        lokasi_lat_penerima = random.uniform(-5.405901634725342, -5.365442970161212)  # Rentang koordinat lintang
        lokasi_lon_penerima = random.uniform(105.22551998740258, 105.29009985878861)  # Rentang koordinat bujur
        frekuensi_menerima = random.randint(1, 10)
        kondisi_makanan_diterima = random.choice([
            'layak_konsumsi',
            'hampir_kadaluarsa',
            'tidak_layak konsumsi',
            'layak_konsumsi_hampir_kadaluarsa'
        ])

        # Logika tambahan untuk kondisi 'tidak layak konsumsi'
        if 'tidak layak konsumsi' in kondisi_makanan_diterima:
            is_halal = False
            is_for_child = False
            is_for_elderly = False
            is_alergan_free = False
        else:
            is_halal = random.choice([True, False])
            is_for_child = random.choice([True, False])
            is_for_elderly = random.choice([True, False])
            is_alergan_free = random.choice([True, False])
        
        status_penerima = random.choice(['mendesak', 'normal', 'tidak mendesak'])
        
        receiver_data.append([
            receiver_id,
            makanan_dibutuhkan,
            jumlah_dibutuhkan,
            lokasi_lat_penerima,
            lokasi_lon_penerima,
            frekuensi_menerima,
            kondisi_makanan_diterima,
            is_halal,
            is_for_child,
            is_for_elderly,
            is_alergan_free,
            status_penerima
        ])
        
    return receiver_data

# Mengenerate 5000 data untuk masing-masing donor dan penerima 
donor_data = generate_donor_data(5000) 
receiver_data = generate_receiver_data(5000) 

# Menyimpan data donor ke dalam CSV di folder 'raw'
with open(os.path.join(raw_data_dir, 'data_donor.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([
        'id_penyumbang', 'makanan_disumbangkan', 'jumlah_disumbangkan', 
        'lokasi_lat_penyumbang', 'lokasi_lon_penyumbang', 'kondisi_makanan', 
        'is_halal', 'is_for_child', 'is_for_elderly', 'is_alergan'
    ])
    writer.writerows(donor_data)

# Menyimpan data penerima ke dalam CSV di folder 'raw'
with open(os.path.join(raw_data_dir, 'data_penerima.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([
        'id_penerima', 'makanan_dibutuhkan', 'jumlah_dibutuhkan', 
        'lokasi_lat_penerima', 'lokasi_lon_penerima', 'frekuensi_menerima', 
        'kondisi_makanan_diterima', 'is_halal', 'is_for_child', 'is_for_elderly', 
        'is_alergan_free', 'status_penerima'
    ])
    writer.writerows(receiver_data)

print("Dataset berhasil digenerate dan disimpan di folder 'data/raw'!")
