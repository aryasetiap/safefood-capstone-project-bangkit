import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df_donor = pd.read_csv('../data/raw/data_donor.csv')
df_penerima = pd.read_csv('../data/raw/data_penerima.csv')

if not df_donor['id_penyumbang'].is_unique:
    df_donor.drop_duplicates(subset='id_penyumbang', keep='first', inplace=True)

df_donor = pd.get_dummies(df_donor, columns=['makanan_disumbangkan'], prefix='disumbangkan', prefix_sep='_')

one_hot_columns = [col for col in df_donor.columns if col.startswith('disumbangkan_')]
df_donor[one_hot_columns] = df_donor[one_hot_columns].astype(int)

df_donor['jumlah_disumbangkan'] = pd.to_numeric(df_donor['jumlah_disumbangkan'], errors='coerce').fillna(0).astype(int)

df_donor = pd.get_dummies(df_donor, columns=['kondisi_makanan'], prefix='kondisi')

one_hot_columns = [col for col in df_donor.columns if col.startswith('kondisi_')]
df_donor[one_hot_columns] = df_donor[one_hot_columns].astype(int)

df_donor['is_halal'] = df_donor['is_halal'].astype(int)
df_donor['is_for_child'] = df_donor['is_for_child'].astype(int)
df_donor['is_for_elderly'] = df_donor['is_for_elderly'].astype(int)
df_donor['is_alergan'] = df_donor['is_alergan'].astype(int)

df_donor.to_csv('../data/processed/data_donor_processed.csv', index=False)

if not df_penerima['id_penerima'].is_unique:
    df_penerima.drop_duplicates(subset='id_penerima', keep='first', inplace=True)
    
df_penerima = pd.get_dummies(df_penerima, columns=['makanan_dibutuhkan'], prefix='dibutuhkan', prefix_sep='_')

one_hot_columns = [col for col in df_penerima.columns if col.startswith('dibutuhkan_')]
df_penerima[one_hot_columns] = df_penerima[one_hot_columns].astype(int)

df_penerima['jumlah_dibutuhkan'] = pd.to_numeric(df_penerima['jumlah_dibutuhkan'], errors='coerce').fillna(0).astype(int)

df_penerima['frekuensi_menerima'] = pd.to_numeric(df_penerima['frekuensi_menerima'], errors='coerce').fillna(0).astype(int)

df_penerima = pd.get_dummies(df_penerima, columns=['kondisi_makanan_diterima'], prefix='kondisi_menerima')

one_hot_columns = [col for col in df_penerima.columns if col.startswith('kondisi_')]
df_penerima[one_hot_columns] = df_penerima[one_hot_columns].astype(int)

df_penerima['is_halal'] = df_penerima['is_halal'].astype(int)
df_penerima['is_for_child'] = df_penerima['is_for_child'].astype(int)
df_penerima['is_for_elderly'] = df_penerima['is_for_elderly'].astype(int)
df_penerima['is_alergan_free'] = df_penerima['is_alergan_free'].astype(int)

df_penerima = pd.get_dummies(df_penerima, columns=['status_penerima'], prefix='status')

one_hot_columns = [col for col in df_penerima.columns if col.startswith('status_')]
df_penerima[one_hot_columns] = df_penerima[one_hot_columns].astype(int)

df_penerima.to_csv('../data/processed/data_penerima_processed.csv', index=False)

print("Proses preprocessing selesai")