# dashboard_realestate
Untuk memenuhi Project DTSense. Saya memilih file source Real_Estate_Sales_2001-2022_GL.csv untuk di jadikan dashboard real estate sehingga di ketahui pola transaksi properti berdasarkan waktu, harga, dan valuasi.

# Library
- Python
- Pandas
- Plotly
- Streamlit

Berikut beberapa fungsi dari syntax yang saya buat ini :

# Rename Field
Karena nama field ada spasi sehingga di lakukan rename field

# Field untuk filter dan grafik
-  Bagian ini berfungsi untuk mengubah fornat data, dan bila ada data yang tidak valid maka akan di sesuaikan, Contoh
   df["date_recorded"] = pd.to_datetime(df["date_recorded"], errors="coerce")
-  Field tambahan untuk keperluan grafik dan filter :
   df["sales_ratio"] = df["assessed_value"] / df["sale_amount"]
   df["year"] = df["date_recorded"].dt.year
   df["month"] = df["date_recorded"].dt.to_period("M").dt.to_timestamp()

# Grafik yang dibuat dalam dashboard :
  # Scatter Plot
    Dengan membandingkan antara assessed_value dengan sales_amount sehingga di dapat sebuah pola kolerasi apakah assessed value properti sejalan dengan harga jual / sales amount.

  # Box Plot
    Berfungsi melihat sebaran / distribusi harga jual properti, mengetahui median harga pasar, dan variasi harga properti.

  # Histogram
    Berfungsi untuk mengetahui jumlah properti di rentang suatu harga, sehingga di dapat analisa jumlah terbanyak pembelian suatu properti dengan tipe tertentu paling laku di kisaran harga sekian.

  # Heatmap
    Berfungsi untuk mengecek kolerasi antar data, data yang di tampilkan hanya yang ber nilai value saja.

  # Trend
    Menampilkan grafik yang berfungsi untuk mengidentifikasi distribusi frekuensi transaksi berdasarkan rentang harga setiap bulannya.

Overall dashboard ini sangat jauh dari sempurna, masih banyak yang masih dapat di kembangkan kembali. Perapihan tampilan angka pada score card agar menjadi simple atau menjadi format $$ atau Rupiah, memberi background yang lebih warna warni, dan lain-lain.
Terlepas itu semua, Saya sangat berterima kasih dengan para Mentor DTSense yang telah sangat luar biasa membimbing Kami, sehingga saya bisa membuat dashboard ini.
Semoga dengan terus berlatih Saya bisa jadi lebih mahir lagi.

Terima Kasih




