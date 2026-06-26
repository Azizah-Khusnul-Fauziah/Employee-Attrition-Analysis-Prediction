# Proyek Akhir: Menyelesaikan Permasalahan Departemen Human Resource (HR)

## Business Understanding
Perusahaan Jaya Jaya Maju mengalami permasalahan tingginya angka **attrition** (resign) karyawan yang berdampak pada biaya rekrutmen, produktivitas, dan stabilitas tim.


### Permasalahan Bisnis

Perusahaan Jaya Jaya Maju saat ini menghadapi tantangan serius berupa tingginya employee attrition yang mencapai angka 15%. Jika tren resign ini terus dibiarkan tanpa adanya intervensi yang tepat, perusahaan akan menghadapi berbagai risiko bisnis jangka panjang yang merugikan, antara lain:

1. Tingginya turnover memaksa perusahaan untuk terus mengeluarkan biaya ekstra yang signifikan untuk proses rekrutmen, onboarding, dan pelatihan karyawan baru.

2. Kehilangan karyawan, terutama di departemen krusial seperti Research & Development (R&D) yang memiliki tingkat resign di atas 50%, berarti hilangnya pengetahuan teknis dan melambatnya inovasi serta pengerjaan proyek perusahaan.

3. Karyawan yang sering keluar-masuk akan merusak dinamika tim. Beban kerja dari karyawan yang resign seringkali dilimpahkan kepada karyawan yang bertahan, yang pada akhirnya dapat menurunkan work-life balance dan memicu efek domino pengunduran diri massal.

4. Ketidakmampuan perusahaan mempertahankan karyawan muda (usia di bawah 25 tahun) dapat mengancam regenerasi kepemimpinan dan keberlanjutan bisnis di masa depan.

### Cakupan Proyek

-Business Understanding
-Data Understanding
-Data Preparation
-Exploratory Data Analysis (EDA)
-Pengembangan Model Machine Learning
-Pembuatan Business Dashboard

### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/employee_data.csv
Setup environment:

```
pipenv install
pipenv shell
pip install numpy pandas scipy matplotlib seaborn jupyter sqlalchemy scikit-learn joblib
pipreqsnb notebook.ipynb
```

## Business Dashboard
https://public.tableau.com/views/EmployeeAttritionRiskDashboard/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link


- Dari total populasi 1.470 karyawan, tercatat ada 221 karyawan yang telah resign. Ini menghasilkan attrition rate sebesar 15,03%.
- Rata-rata pendapatan bulanan (Monthly Income) karyawan ada di angka 6.503, dengan rata-rata masa kerja 7 tahun. Sementara itu, tingkat kepuasan kerja (Job Satisfaction) berada di angka 2,7 dari skala 4—yang berarti tingkat kepuasan karyawan saat ini berada di level menengah.
- Pada grafik Attrition berdasarkan Departemen dan treemap Karyawan Beresiko, terlihat jelas bahwa Departemen R&D (Research & Development) adalah penyumbang attrition terbesar, mendominasi lebih dari 56% dari total karyawan yang keluar.
- Jika dilihat dari sisi usia pada Attrition Rate per Kelompok Usia, terdapat tren yang sangat mencolok. Dimana Karyawan muda dengan usia di bawah 25 tahun memiliki tingkat resign yang sangat tinggi, melampaui 40%. Semakin bertambahnya usia karyawan, grafik menunjukkan bahwa probabilitas mereka untuk resign semakin menurun tajam.
- Adanya kesenjangan kompensasi pada Rata-Rata Monthly Income. Karyawan yang memilih bertahan memiliki rata-rata pendapatan sekitar 6.847, sedangkan karyawan yang memilih resign memiliki rata-rata pendapatan yang jauh lebih rendah, yaitu 4.559.

Tiga kesimpulan utama:
1. Gaji memainkan peran penting dalam keputusan karyawan untuk resign. Mereka yang bergaji di bawah rata-rata (sekitar 4.500) memiliki risiko attrition yang jauh lebih tinggi dibandingkan mereka yang gajinya di atas 6.500.
2. Perusahaan saat ini kesulitan untuk mempertahankan talenta muda. Dimana tingkat turnover di kelompok usia di bawah 25 tahun berada di level yang mengkhawatirkan dan butuh intervensi segera.
3. Departemen R&D adalah area paling kritis yang membutuhkan investigasi lebih lanjut oleh tim HR, karena mayoritas karyawan yang resign berasal dari departemen ini.

## Conclusion

Proyek HR Analytics untuk Jaya Jaya Maju yang telah dikerjakan mencakup tahap analisis data eksploratif (EDA), pembuatan business dashboard, dan pengembangan model machine learning. Berdasarkan keseluruhan proyek, dapat ditarik kesimpulan sebagai berikut:

- Proyek ini berhasil mengidentifikasi bahwa tingkat attrition perusahaan mencapai 15,03%. Faktor pendorong karyawan untuk resign dipengaruhi oleh tingkat pendapatan (gaji di bawah rata-rata), faktor demografi (usia di bawah 25 tahun), dan penempatan departemen (khususnya R&D).

- Untuk mengantisipasi attrition di masa depan, telah dibangun model klasifikasi menggunakan algoritma Random Forest. Model ini mampu memprediksi karyawan yang berisiko resign dengan tingkat akurasi AUC-ROC sebesar 0.814

- Dengan memadukan monitoring interaktif melalui dashboard dan prediksi real-time dari model machine learning, manajemen dan tim HR kini memiliki alat berbasis data yang solid. Solusi ini memungkinkan perusahaan untuk beralih dari pendekatan reaktif menjadi proaktif dalam melakukan intervensi dan strategi retensi karyawan.

### Rekomendasi Action Items (Optional)
1. Lakukan Focus Group Discussion (FGD) atau audit manajemen khusus di divisi R&D untuk mencari tahu root cause spesifiknya (misal: apakah karena load kerja penelitian terlalu berat, minimnya fasilitas, atau gaya leadership manajernya).
2. Pasangkan karyawan muda dengan mentor senior, dan berikan peta karir yang jelas agar mereka tahu proyeksi karir mereka 2-3 tahun ke depan di Jaya Jaya Maju.
3. Wajibkan exit interview yang mendalam bagi setiap karyawan yang resign (terutama dari R&D dan usia <25) untuk memvalidasi apakah gaji dan kepuasan kerja benar-benar menjadi alasan utama.

