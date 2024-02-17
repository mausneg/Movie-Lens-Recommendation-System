# Laporan Proyek Machine Learning - Nama Anda

## Project Overview

Perkembangan era digital telah mengubah paradigma dan kebutuhan masyarakat secara global. Informasi yang dahulu terbatas pada format kertas kini telah bertransformasi menjadi bentuk digital, dengan internet menjadi kekuatan utama yang memberikan akses mudah ke sumber informasi dari berbagai perangkat teknologi informasi dan komunikasi (TIK). Perubahan ini menjadikan informasi lebih mudah diakses, cerdas, praktis, dan terintegrasi.

Dengan demikian, ledakan data dan informasi digital menjadi fenomena yang tak terhindarkan. Diperkuat oleh peran media sosial, proses bisnis digital, dan publikasi _online_, volume dan pertumbuhan data meningkat pesat. Contohnya, sekitar 2,5 _Exabyte_ data tercipta setiap hari, dengan perusahaan-perusahaan besar seperti Google, Facebook, Amazon, dan Netflix menjadi pemain kunci dalam pemanfaatan data dan informasi [^1^].

Film merupakan yang merupakan salah satu bentuk hiburan masyaratkat juga terdampak oleh perubahan ini. Ribuan film baru dirilis setiap tahunnya, menghadirkan keragaman genre, tema, dan cerita yang menarik. Namun, dengan banyaknya pilihan ini, masyarakat sering kali menghadapi kesulitan dalam mencari film yang sesuai dengan kriteria dan selera mereka.

Di sinilah sistem rekomendasi film menjadi solusi yang efektif. Sistem ini memanfaatkan opini dan rating dari pengguna lain terhadap suatu film untuk membantu pengguna menemukan film yang mungkin tidak pernah terpikirkan sebelumnya, namun sesuai dengan selera mereka. Dengan menganalisis preferensi dan penilaian film yang telah diberikan oleh pengguna lain dengan selera serupa, sistem ini mampu memberikan rekomendasi yang relevan dan personal bagi setiap pengguna.

## Business Understanding

Dengan banyaknya film yang dirilis setiap tahunnya, tanpa adanya sistem rekomedasi film, suatu bisnis yang bergerak di bidang hiburan seperti layanan _streaming_ akan mengalami penurunan _engagement_ dari pengguna yang pada akhirnya akan berdampak pada pendapatan perusahaan. Berikut merupakan akibat dari tidak adanya sistem rekomendasi film:

- Kesulitan dalam Menjangkau Pelanggan: Tanpa sistem rekomendasi, bisnis mungkin kesulitan menjangkau pelanggan dengan produk atau layanan yang paling relevan bagi mereka. Ini bisa berarti peluang penjualan yang hilang.
- Pengalaman Pelanggan yang Kurang Memuaskan: Pelanggan mungkin merasa kewalahan dengan banyaknya pilihan dan kesulitan menemukan produk atau layanan yang mereka cari. Ini bisa berdampak negatif pada kepuasan pelanggan dan retensi.
- Pemasaran yang Kurang Efektif: Tanpa sistem rekomendasi, bisnis mungkin kesulitan menargetkan pemasaran mereka dengan efektif. Ini bisa berarti pengeluaran pemasaran yang lebih tinggi dan ROI yang lebih rendah.

Dari alasan-alasan di atas, maka didapatkan _problem statement_ dan _goals_ dari proyek ini sebagai berikut:

### Problem Statements

- Bagaimana cara membangun sistem rekomendasi film yang dapat memberikan rekomendasi yang relevan dan personal bagi setiap pengguna?
- Dataset seperti apa yang diperlukan untuk membangun sistem rekomendasi film yang efektif?
- Bagaimana cara mengevaluasi kinerja dari sistem rekomendasi film yang telah dibangun?

### Goals

- Membangun sistem rekomendasi film yang dapat memberikan rekomendasi yang relevan dan personal bagi setiap pengguna.
- Mengidentifikasi dan mengumpulkan dataset yang diperlukan untuk membangun sistem rekomendasi film yang efektif.
- Mengevaluasi kinerja dari sistem rekomendasi film yang telah dibangun.

Semua poin di atas harus diuraikan dengan jelas. Anda bebas menuliskan berapa pernyataan masalah dan juga goals yang diinginkan.

### Solution statements

- Membangun sistem rekomendasi film berbasis _content-based filtering_ dengan menggunakan algoritma _cosine similarity_ dan juga menggunakan pendekatan _neural network_. Pendekatan dengan algoritma _cosine similarity_ akan memberikan rekomendasi film berdasarkan kemiripan genre dan tags, sedangkan pendekatan _neural network_ akan memberikan rekomendasi film berdasarkan preferensi pengguna.
- Menggunakan dataset yang berisi informasi mengenai film, seperti judul, genre, dan rating. 
- Menggunakan metrik evaluasi _mean squared error_ untuk mengevaluasi kinerja dari sistem rekomendasi film yang telah dibangun. Selain itu juga, akan dilakukan evaluasi dengan melakukan prediksi terhadap pengguna baru.

## Data Understanding




**Rubrik/Kriteria Tambahan (Opsional)**:

- Melakukan beberapa tahapan yang diperlukan untuk memahami data, contohnya teknik visualisasi data beserta insight atau exploratory data analysis.

## Data Preparation

Pada bagian ini Anda menerapkan dan menyebutkan teknik data preparation yang dilakukan. Teknik yang digunakan pada notebook dan laporan harus berurutan.

**Rubrik/Kriteria Tambahan (Opsional)**:

- Menjelaskan proses data preparation yang dilakukan
- Menjelaskan alasan mengapa diperlukan tahapan data preparation tersebut.

## Modeling

Tahapan ini membahas mengenai model sisten rekomendasi yang Anda buat untuk menyelesaikan permasalahan. Sajikan top-N recommendation sebagai output.

**Rubrik/Kriteria Tambahan (Opsional)**:

- Menyajikan dua solusi rekomendasi dengan algoritma yang berbeda.
- Menjelaskan kelebihan dan kekurangan dari solusi/pendekatan yang dipilih.

## Evaluation

Pada bagian ini Anda perlu menyebutkan metrik evaluasi yang digunakan. Kemudian, jelaskan hasil proyek berdasarkan metrik evaluasi tersebut.

Ingatlah, metrik evaluasi yang digunakan harus sesuai dengan konteks data, problem statement, dan solusi yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**:

- Menjelaskan formula metrik dan bagaimana metrik tersebut bekerja.

## References

[^1^]: [Wahyudi, Indah Survyana, "Mesin Rekomendasi Film Menggunakan Metode Kemiripan Genre Berbasis Collaborative Filtering"](https://repository.its.ac.id/42018/1/2215206701-Master-Thesis.pdf)
