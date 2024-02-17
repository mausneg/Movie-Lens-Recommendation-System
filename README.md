# Laporan Proyek Machine Learning - Maulana Surya Negara

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

- Membangun sistem rekomendasi film yang dapat memberikan rekomendasi yang relevan dan personal bagi setiap pengguna dengan _error_ di bawah 0.2.
- Mengidentifikasi dan mengumpulkan dataset yang diperlukan untuk membangun sistem rekomendasi film yang efektif.
- Mengevaluasi kinerja dari sistem rekomendasi film yang telah dibangun.

Semua poin di atas harus diuraikan dengan jelas. Anda bebas menuliskan berapa pernyataan masalah dan juga goals yang diinginkan.

### Solution statements

- Membangun sistem rekomendasi film berbasis _content-based filtering_ dengan menggunakan algoritma _cosine similarity_ dan juga menggunakan pendekatan _neural network_. Pendekatan dengan algoritma _cosine similarity_ akan memberikan rekomendasi film berdasarkan kemiripan genre dan tags, sedangkan pendekatan _neural network_ akan memberikan rekomendasi film berdasarkan preferensi pengguna.
- Menggunakan dataset yang berisi informasi mengenai film, seperti judul, genre, dan rating.
- Menggunakan metrik evaluasi _mean squared error_ untuk mengevaluasi kinerja dari sistem rekomendasi film yang telah dibangun. Selain itu juga, akan dilakukan evaluasi dengan melakukan prediksi terhadap pengguna baru.

## Data Understanding

### Data Loading

Dataset yang digunakan dalam proyek ini adalah [MovieLens Latest Small](https://grouplens.org/datasets/movielens/latest/). Dataset ini terdiri dari 100.836 rating dan 3.683 _tags_ pada 9.742 _movies_. Data ini terdiri dari empat file, yaitu links.csv, movies.csv, ratings.csv, dan tags.csv.

1. Ratings.csv
   - `userId`: ID unik dari setiap pengguna berupa _integer_.
   - `movieId`: ID unik dari setiap film berupa _integer_.
   - `rating`: Nilai rating yang diberikan oleh pengguna dengan skala 0.5 hingga 5.
   - `timestamp`: Waktu ketika rating diberikan dengan format UTC.
2. Tags.csv
   - `userId`: ID unik dari setiap pengguna berupa _integer_.
   - `movieId`: ID unik dari setiap film berupa _integer_.
   - `tag`: Tag yang diberikan oleh pengguna. Setiap tag merupakan kata atau frasa yang memiliki makna yang diberikan oleh pengguna.
   - `timestamp`: Waktu ketika tag diberikan dengan format UTC.
3. Movies.csv
   - `movieId`: ID unik dari setiap film berupa _integer_.
   - `title`: Judul dari film yang disajikan dalam bentuk string.
   - `genres`: Genre film yang disajikan dalam bentuk string dengan format `genre1|genre2|genre3|...|genre-n`.
4. Links.csv
   - `movieId`: ID unik dari setiap film berupa _integer_.
   - `imdbId`: ID unik dari setiap film di IMDb.
   - `tmdbId`: ID unik dari setiap film di TMDb.

### Exploratory Data Analysis

Tabel 1. Deskripsi Data _Movie_

| Nama Kolom | Non-Null Count | Dtype  |
| ---------- | -------------- | ------ |
| movieId    | 9742 non-null  | int64  |
| title      | 9742 non-null  | object |
| genres     | 9742 non-null  | object |

Dari Tabel 1 didapatkan informasi sebagai berikut.

- Dataset terdiri dari 9742 baris dan 3 kolom.
- Terdapat 1 kolom bertipe `int64` yaitu `movieId`.
- Terdapat 2 kolom bertipe `object` yaitu `title` dan `genres`.

Tabel 2. Deskripsi Data Rating
| Nama Kolom | Non-Null Count | Dtype |
|------------|----------------|-------|
| userId | 100836 non-null| int64 |
| movieId | 100836 non-null| int64 |
| rating | 100836 non-null| float64|
| timestamp | 100836 non-null| int64 |

Dari Tabel 2 didapatkan informasi sebagai berikut.

- Dataset terdiri dari 100836 baris dan 4 kolom.
- Terdapat 3 kolom bertipe `int64` yaitu `userId`, `movieId`, dan `timestamp`.
- Terdapat 1 kolom bertipe `float64` yaitu `rating`.

Tabel 3. Deskripsi Data _Tags_
| Nama Kolom | Non-Null Count | Dtype |
|------------|----------------|-------|
| userId | 3683 non-null | int64 |
| movieId | 3683 non-null | int64 |
| tag | 3683 non-null | object|
| timestamp | 3683 non-null | int64 |

Dari Tabel 3 didapatkan informasi sebagai berikut.

- Dataset terdiri dari 3683 baris dan 4 kolom.
- Terdapat 2 kolom bertipe `int64` yaitu `userId`, `movieId`, dan `timestamp`.
- Terdapat 1 kolom bertipe `object` yaitu `tag`.

Tabel 4 Statistik Deskriptif Data Rating
|| userId | movieId | rating | timestamp |
|-------|--------|---------|--------|-----------|
| count | 100836 | 100836 | 100836 | 100836 |
| mean | 326.13 | 19435.3 | 3.50 | 1.20591e+09|
| std | 182.62 | 35530.9 | 1.04 | 2.16261e+08|
| min | 1 | 1 | 0.5 | 8.28111e+08|
| 25% | 177 | 1199 | 3 | 1.01847e+09|
| 50% | 325 | 2991 | 3.5 | 1.18609e+09|
| 75% | 477 | 8122 | 4 | 1.44719e+09|
| max | 610 | 193609 | 5 | 1.5378e+09 |

Dari Tabel 4 didapatkan informasi sebagai berikut.

- Rata-rata dari kolom `ratings` adalah 3.50
- Standar deviasi dari kolom `ratings` adalah 1.04
- Nilai minimum dari kolom `ratings` adalah 0.50
- Nilai 25% dari kolom `ratings` adalah 3.00
- Nilai 50% dari kolom `ratings` adalah 3.50
- Nilai 75% dari kolom `ratings` adalah 4.00
- Nilai maksimum dari kolom `ratings` adalah 5.00

Sehingga dapat disimpulkan bahwa distribusi data dari kolom ratings cenderung menumpuk di nilai 3.00 - 4.00. Hal ini bukanlah menjadi masalah karena data rating merupakan data yang bersifat subjektif dan dapat bervariasi.

Untuk memastikan distribusi data dari kolom ratings, akan dilakukan visualisasi distribusi data dari kolom ratings.

![alt text](https://github.com/mausneg/Movie-Lens-Recommendation-System/blob/main/images/image.png?raw=True)

Gambar 1. Distribusi Data Rating

Dari histogram di atas, grafik terlihat _left-skewed_ yang menunjukkan bahwa mayoritas film memiliki rating di antara 3.0 - 4.0. Dengan kata lain, ada lebih sedikit film dengan rating rendah dibandingkan dengan film dengan rating tinggi.

Ini bisa menunjukkan bahwa penonton cenderung memberikan rating yang relatif tinggi untuk film yang mereka tonton, atau bisa juga menunjukkan bahwa film dengan rating rendah cenderung ditonton lebih sedikit atau kurang populer di antara penonton.

## Data Preparation

Tahapan ini membahas mengenai proses data preparation yang dilakukan. Data preparation adalah tahapan yang sangat penting dalam proses _machine learning_ karena kualitas data yang baik akan menghasilkan model yang baik pula.

### Merging Data

Langkah selanjutnya adalah menggabungkan dataset sesuai dengan kebutuhan. Data ratings akan digabungkan dengan data _movies_ dan data _movies_ juga akan digabungkan dengan data tags.

#### Data Movies dan Data Tags

Penggabungan kedua dataset ini memungkinkan kita untuk mempertimbangkan lebih banyak fitur saat menghitung kesamaan antara film. Dalam hal ini, algoritma _cosine similarity_ digunakan untuk menghitung kesamaan antara film berdasarkan genre dan tag.

Langkah pertama adalah menggabungkan kedua dataset ini berdasarkan kolom `movieId`. Setelah itu, kolom `tag` akan digabungkan menjadi satu dengan menggunakan fungsi `groupby` dan `agg` untuk menggabungkan tag menjadi satu baris. Berikut merupakan hasilnya.

Tabel 5. Sampel Hasil _Join_ Tag berdasarkan `movieId`

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>movieId</th>
      <th>tag</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>pixar pixar fun</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>fantasy magic board game Robin Williams game</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>moldy old</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5</td>
      <td>pregnancy remake</td>
    </tr>
    <tr>
      <th>4</th>
      <td>7</td>
      <td>remake</td>
    </tr>
  </tbody>
</table>

Selanjutnya akan dilakukan _merge_ antara data movies dan data tags. Setelah itu akan dilakukan _merge_ antara kolom `tag` dengan kolom `genres` untuk menggabungkan kolom tersebut menjadi satu. Berikut merupakan hasilnya.

Tabel 6. Sampel Hasil _Merge_ Data Movies dan Data Tags

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>movieId</th>
      <th>title</th>
      <th>tags</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Toy Story (1995)</td>
      <td>Adventure Animation Children Comedy Fantasy pi...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Jumanji (1995)</td>
      <td>Adventure Children Fantasy fantasy magic board...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Grumpier Old Men (1995)</td>
      <td>Comedy Romance moldy old</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Waiting to Exhale (1995)</td>
      <td>Comedy Drama Romance</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Father of the Bride Part II (1995)</td>
      <td>Comedy pregnancy remake</td>
    </tr>
  </tbody>
</table>

Pada Tabel 6 dapat dilihat kolom `tags` sudah digabungkan berdasarkan `movieId` meskipun terdapat beberapa _missing value_ pada kolom `tags`. _Missing value_ pada kolom `tags` ini akan diisi dengan _whitespace_.

Dengan demikian, data untuk melakukan _cosine similarity_ sudah siap untuk digunakan.

#### Data Movies dan Data Ratings

Pada tahap ini, akan dilakukan penggabungan data ratings dengan data movies. Hal ini dilakukan agar nantinya dapat digunakan untuk memberikan rekomendasi film berdasarkan rating yang diberikan oleh user pada movie dengan mempertimbangkan genres.

Tabel 7. Sampel Hasil _Merge_ Data Movies dan Data Ratings

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>userId</th>
      <th>movieId</th>
      <th>rating</th>
      <th>title</th>
      <th>genres</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>1</td>
      <td>4.0</td>
      <td>Toy Story (1995)</td>
      <td>Adventure Animation Children Comedy Fantasy</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>3</td>
      <td>4.0</td>
      <td>Grumpier Old Men (1995)</td>
      <td>Comedy Romance</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>6</td>
      <td>4.0</td>
      <td>Heat (1995)</td>
      <td>Action Crime Thriller</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>47</td>
      <td>5.0</td>
      <td>Seven (a.k.a. Se7en) (1995)</td>
      <td>Mystery Thriller</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>50</td>
      <td>5.0</td>
      <td>Usual Suspects, The (1995)</td>
      <td>Crime Mystery Thriller</td>
    </tr>
  </tbody>
</table>

Pada Tabel 7 data movies dan data ratings sudah digabungkan berdasarkan `movieId`. Langkah selanjutnya yaitu melakukan _encoding_ dengan menjabarkan kolom genres menjadi beberapa kolom berdasarkan nilai yang ada pada kolom genres yang berisi nilai 1 atau 0.
Hal ini dilakukan karena model machine learning hanya dapat memproses data yang berupa numerik.

Tabel 8. Sampel Hasil _Encoding_ Data Movies dan Data Ratings

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>userId</th>
      <th>movieId</th>
      <th>rating</th>
      <th>title</th>
      <th>Adventure</th>
      <th>Animation</th>
      <th>Children</th>
      <th>Comedy</th>
      <th>Fantasy</th>
      <th>Romance</th>
      <th>...</th>
      <th>Mystery</th>
      <th>Horror</th>
      <th>Drama</th>
      <th>War</th>
      <th>Western</th>
      <th>Sci-Fi</th>
      <th>Musical</th>
      <th>Film-Noir</th>
      <th>IMAX</th>
      <th>Documentary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>1</td>
      <td>4.0</td>
      <td>Toy Story (1995)</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>3</td>
      <td>4.0</td>
      <td>Grumpier Old Men (1995)</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>6</td>
      <td>4.0</td>
      <td>Heat (1995)</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>47</td>
      <td>5.0</td>
      <td>Seven (a.k.a. Se7en) (1995)</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>50</td>
      <td>5.0</td>
      <td>Usual Suspects, The (1995)</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>

Pada Tabel 8 dapat dilihat kolom `genres` sudah dijabarkan dengan masing-masing jenis _genre_ menjadi kolom tersendiri.

### Data Transformation

Setelah melakukan penggabungan data, langkah selanjutnya adalah melakukan _data transformation_ . Pada tahap ini, data yang berisi rating dan _movie_ akan di-_tranform_ menjadi data _user_, data _movie_, dan data rating. Sehingga data _user_ dan data _item_(_movie_) akan dijadikan sebagai _features_ dan data rating akan dijadikan sebagai _target_.

#### Data User

Tahap ini dimulai dengan membuang kolom-kolom yang tidak diperlukan untuk data _user_ seperti `movieId` dan `title`. Selanjutnya akan dibentuk data _preferences user_ berdasarkan nilai rata-rata dari rating yang diberikan oleh _user_ untuk setiap _genre_ dari film yang **pernah** ditonton oleh _user_. Berikut merupakan data _preferences user_ yang dihasilkan.

Tabel 9. Sampel Data _Preferences User_

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>userId</th>
      <th>Adventure</th>
      <th>Animation</th>
      <th>Children</th>
      <th>Comedy</th>
      <th>Fantasy</th>
      <th>Romance</th>
      <th>Action</th>
      <th>Crime</th>
      <th>Thriller</th>
      <th>Mystery</th>
      <th>Horror</th>
      <th>Drama</th>
      <th>War</th>
      <th>Western</th>
      <th>Sci-Fi</th>
      <th>Musical</th>
      <th>Film-Noir</th>
      <th>IMAX</th>
      <th>Documentary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>4.388235</td>
      <td>4.689655</td>
      <td>4.547619</td>
      <td>4.277108</td>
      <td>4.297872</td>
      <td>4.307692</td>
      <td>4.322222</td>
      <td>4.355556</td>
      <td>4.145455</td>
      <td>4.166667</td>
      <td>3.470588</td>
      <td>4.529412</td>
      <td>4.500000</td>
      <td>4.285714</td>
      <td>4.225000</td>
      <td>4.681818</td>
      <td>5.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>4.166667</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>4.000000</td>
      <td>0.000000</td>
      <td>4.500000</td>
      <td>3.954545</td>
      <td>3.800000</td>
      <td>3.700000</td>
      <td>4.000000</td>
      <td>3.000000</td>
      <td>3.882353</td>
      <td>4.500000</td>
      <td>3.500000</td>
      <td>3.875000</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>3.750000</td>
      <td>4.333333</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>2.727273</td>
      <td>0.500000</td>
      <td>0.500000</td>
      <td>1.000000</td>
      <td>3.375000</td>
      <td>0.500000</td>
      <td>3.571429</td>
      <td>0.500000</td>
      <td>4.142857</td>
      <td>5.000000</td>
      <td>4.687500</td>
      <td>0.750000</td>
      <td>0.500000</td>
      <td>0.000000</td>
      <td>4.200000</td>
      <td>0.500000</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>3.655172</td>
      <td>4.000000</td>
      <td>3.800000</td>
      <td>3.509615</td>
      <td>3.684211</td>
      <td>3.379310</td>
      <td>3.320000</td>
      <td>3.814815</td>
      <td>3.552632</td>
      <td>3.478261</td>
      <td>4.250000</td>
      <td>3.483333</td>
      <td>3.571429</td>
      <td>3.800000</td>
      <td>2.833333</td>
      <td>4.000000</td>
      <td>4.0</td>
      <td>3.000000</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>3.250000</td>
      <td>4.333333</td>
      <td>4.111111</td>
      <td>3.466667</td>
      <td>4.142857</td>
      <td>3.090909</td>
      <td>3.111111</td>
      <td>3.833333</td>
      <td>3.555556</td>
      <td>4.000000</td>
      <td>3.000000</td>
      <td>3.800000</td>
      <td>3.333333</td>
      <td>3.000000</td>
      <td>2.500000</td>
      <td>4.400000</td>
      <td>0.0</td>
      <td>3.666667</td>
      <td>0.000000</td>
    </tr>
  </tbody>
</table>
</div>

Pada Tabel 9 dapat dilihat bahwa data _preferences user_ berisi seberapa suka _user_ terhadap setiap _genre_ film yang pernah ditonton oleh _user_.

Langkah selanjutnya yaitu mengaplikasikan data _preferences user_ tersebut ke dalam data _user_ yang sudah di-_drop_ kolom-kolom yang tidak diperlukan. Berikut merupakan hasilnya.

Tabel 10. Sampel Data _User_ yang Telah di-_Transform_

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>userId</th>
      <th>Adventure</th>
      <th>Animation</th>
      <th>Children</th>
      <th>Comedy</th>
      <th>Fantasy</th>
      <th>Romance</th>
      <th>Action</th>
      <th>Crime</th>
      <th>Thriller</th>
      <th>Mystery</th>
      <th>Horror</th>
      <th>Drama</th>
      <th>War</th>
      <th>Western</th>
      <th>Sci-Fi</th>
      <th>Musical</th>
      <th>Film-Noir</th>
      <th>IMAX</th>
      <th>Documentary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>4.388235</td>
      <td>4.689655</td>
      <td>4.547619</td>
      <td>4.277108</td>
      <td>4.297872</td>
      <td>4.307692</td>
      <td>4.322222</td>
      <td>4.355556</td>
      <td>4.145455</td>
      <td>4.166667</td>
      <td>3.470588</td>
      <td>4.529412</td>
      <td>4.500000</td>
      <td>4.285714</td>
      <td>4.225000</td>
      <td>4.681818</td>
      <td>5.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>4.166667</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>4.000000</td>
      <td>0.000000</td>
      <td>4.500000</td>
      <td>3.954545</td>
      <td>3.800000</td>
      <td>3.700000</td>
      <td>4.000000</td>
      <td>3.000000</td>
      <td>3.882353</td>
      <td>4.500000</td>
      <td>3.500000</td>
      <td>3.875000</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>3.750000</td>
      <td>4.333333</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>2.727273</td>
      <td>0.500000</td>
      <td>0.500000</td>
      <td>1.000000</td>
      <td>3.375000</td>
      <td>0.500000</td>
      <td>3.571429</td>
      <td>0.500000</td>
      <td>4.142857</td>
      <td>5.000000</td>
      <td>4.687500</td>
      <td>0.750000</td>
      <td>0.500000</td>
      <td>0.000000</td>
      <td>4.200000</td>
      <td>0.500000</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>3.655172</td>
      <td>4.000000</td>
      <td>3.800000</td>
      <td>3.509615</td>
      <td>3.684211</td>
      <td>3.379310</td>
      <td>3.320000</td>
      <td>3.814815</td>
      <td>3.552632</td>
      <td>3.478261</td>
      <td>4.250000</td>
      <td>3.483333</td>
      <td>3.571429</td>
      <td>3.800000</td>
      <td>2.833333</td>
      <td>4.000000</td>
      <td>4.0</td>
      <td>3.000000</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>3.250000</td>
      <td>4.333333</td>
      <td>4.111111</td>
      <td>3.466667</td>
      <td>4.142857</td>
      <td>3.090909</td>
      <td>3.111111</td>
      <td>3.833333</td>
      <td>3.555556</td>
      <td>4.000000</td>
      <td>3.000000</td>
      <td>3.800000</td>
      <td>3.333333</td>
      <td>3.000000</td>
      <td>2.500000</td>
      <td>4.400000</td>
      <td>0.0</td>
      <td>3.666667</td>
      <td>0.000000</td>
    </tr>
  </tbody>
</table>

Pada Tabel 10 dapat dilihat bahwa data _user_ sudah di-_transform_ dengan menggabungkan data _preferences user_ ke dalam data _user_. Sehingga data ini berisi _preferences user_ terhadap setiap _genre_ ke setiap film yang pernah diberikan rating oleh _user_.

#### Data Item (Data Movie)

Untuk proses tranformasi data _item_ hanya dilakukan dengan cara membuang kolom-kolom yang tidak diperlukan. Berikut merupakan hasilnya.

Tabel 11. Sampel Data _Item_ yang Telah di-_Transform_

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>movieId</th>
      <th>Adventure</th>
      <th>Animation</th>
      <th>Children</th>
      <th>Comedy</th>
      <th>Fantasy</th>
      <th>Romance</th>
      <th>Action</th>
      <th>Crime</th>
      <th>Thriller</th>
      <th>Mystery</th>
      <th>Horror</th>
      <th>Drama</th>
      <th>War</th>
      <th>Western</th>
      <th>Sci-Fi</th>
      <th>Musical</th>
      <th>Film-Noir</th>
      <th>IMAX</th>
      <th>Documentary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>47</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>50</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>

Pada Tabel 11 dapat dilihat bahwa data _item_ sudah di-_transform_ dengan menghilangkan kolom-kolom yang tidak diperlukan. Jika suatu _genre_ film memiliki nilai 1, maka film tersebut memiliki _genre_ tersebut. Sebaliknya, jika suatu _genre_ film memiliki nilai 0, maka film tersebut tidak memiliki _genre_ tersebut.

#### Data Rating

Sedangkan untuk data rating hanya diambil dari kolom `rating` saja. Data rating ini akan dijadikan sebagai _target_.

### Scalling Data

Tabel 12. Sampel Data _User_ yang Telah di-_Scalling_

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>userId</th>
      <th>Adventure</th>
      <th>Animation</th>
      <th>Children</th>
      <th>Comedy</th>
      <th>Fantasy</th>
      <th>Romance</th>
      <th>Action</th>
      <th>Crime</th>
      <th>Thriller</th>
      <th>Mystery</th>
      <th>Horror</th>
      <th>Drama</th>
      <th>War</th>
      <th>Western</th>
      <th>Sci-Fi</th>
      <th>Musical</th>
      <th>Film-Noir</th>
      <th>IMAX</th>
      <th>Documentary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>1.854035</td>
      <td>1.351371</td>
      <td>1.524218</td>
      <td>1.72754</td>
      <td>1.425833</td>
      <td>1.530181</td>
      <td>1.802559</td>
      <td>1.408636</td>
      <td>1.321439</td>
      <td>0.934757</td>
      <td>0.331341</td>
      <td>1.937017</td>
      <td>1.082297</td>
      <td>0.877787</td>
      <td>1.542293</td>
      <td>1.340258</td>
      <td>1.221822</td>
      <td>-2.452027</td>
      <td>-1.422555</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>1.854035</td>
      <td>1.351371</td>
      <td>1.524218</td>
      <td>1.72754</td>
      <td>1.425833</td>
      <td>1.530181</td>
      <td>1.802559</td>
      <td>1.408636</td>
      <td>1.321439</td>
      <td>0.934757</td>
      <td>0.331341</td>
      <td>1.937017</td>
      <td>1.082297</td>
      <td>0.877787</td>
      <td>1.542293</td>
      <td>1.340258</td>
      <td>1.221822</td>
      <td>-2.452027</td>
      <td>-1.422555</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>1.854035</td>
      <td>1.351371</td>
      <td>1.524218</td>
      <td>1.72754</td>
      <td>1.425833</td>
      <td>1.530181</td>
      <td>1.802559</td>
      <td>1.408636</td>
      <td>1.321439</td>
      <td>0.934757</td>
      <td>0.331341</td>
      <td>1.937017</td>
      <td>1.082297</td>
      <td>0.877787</td>
      <td>1.542293</td>
      <td>1.340258</td>
      <td>1.221822</td>
      <td>-2.452027</td>
      <td>-1.422555</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>1.854035</td>
      <td>1.351371</td>
      <td>1.524218</td>
      <td>1.72754</td>
      <td>1.425833</td>
      <td>1.530181</td>
      <td>1.802559</td>
      <td>1.408636</td>
      <td>1.321439</td>
      <td>0.934757</td>
      <td>0.331341</td>
      <td>1.937017</td>
      <td>1.082297</td>
      <td>0.877787</td>
      <td>1.542293</td>
      <td>1.340258</td>
      <td>1.221822</td>
      <td>-2.452027</td>
      <td>-1.422555</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>1.854035</td>
      <td>1.351371</td>
      <td>1.524218</td>
      <td>1.72754</td>
      <td>1.425833</td>
      <td>1.530181</td>
      <td>1.802559</td>
      <td>1.408636</td>
      <td>1.321439</td>
      <td>0.934757</td>
      <td>0.331341</td>
      <td>1.937017</td>
      <td>1.082297</td>
      <td>0.877787</td>
      <td>1.542293</td>
      <td>1.340258</td>
      <td>1.221822</td>
      <td>-2.452027</td>
      <td>-1.422555</td>
    </tr>
  </tbody>
</table>

Setelah melakukan _transformasi_, data _user_ dan data _item_ akan di _scalling_ dengan menggunakan _Standard Scaler_. Alasan _Standard Scaler_ digunakan yaitu karena akan dilakukan pembagian rentang rating, jika _value_ genre bernilai positif menandakan user menyukai film tersebut, sedangkan jika _value_ genre bernilai negatif menandakan user tidak menyukai film tersebut. Atau jika pada data item, _value_ genre bernilai positif menandakan film tersebut memiliki genre tersebut, sedangkan jika _value_ genre bernilai negatif menandakan film tersebut tidak memiliki genre tersebut. Sedangkan untuk data rating akan di _scalling_ dengan menggunakan _MinMax Scaler_ agar rating yang diberikan oleh _user_ memiliki rentang nilai antara 0 sampai 1.

### Data Splitting

Selanjutnya, data _user_, data _item_, dan data rating akan di _split_ menjadi data _train_, data _test_, dan data _validation_. Hal ini bertujuan agar dapat dilakukan evaluasi model machine learning yang akan dibuat. Perbandingan data _train_, data _test_, dan data _validation_ yang digunakan adalah 80% data _train_, 10% data _test_, dan 10% data _validation_.

## Modeling

Pada tahap ini akan dilakukan pemodelan machine learning yaitu menggunakan _content-based filtering_ dengan menggunakan _cosine similarity_ dan menggunakan _neural network_. Perbedaan dari kedua model ini yaitu sebagai berikut.

- _Content-based filtering_ dengan menggunakan _cosine similarity_ akan menghitung kemiripan antara _item_ dengan _item lainnya berdasarkan \_genre_ dan _tags_ yang dimiliki oleh _item_ tersebut. Sedangkan _neural network_ akan mempelajari pola dari data _user_ dan data _item_ dengan data _rating_ yang akan menjadi target.
- _Content-based filtering_ dengan menggunakan _cosine similarity_ hanya dapat memberikan rekomendasi berdasarkan data _item_ yang sudah ada, sedangkan _neural network_ dapat memberikan rekomendasi berdasarkan data _user_ atau data _item_ yang belum ada, sehingga dengan menggunakan _neural network_ dapat memberikan rekomendasi terhadap _user_ yang baru.

### Content-Based Filtering dengan Cosine Similarity

Pada perhitungan _similarity_ antar film berdasarkan genres dan _tags_, akan digunakan _cosine similarity_. Hal ini dilakukan karena _cosine similarity_ dapat mengukur kesamaan antar film berdasarkan genres dan _tags_. Tetapi sebelum itu, akan dilakukan ekstraksi data _tags_ dengan menggunakan `CountVectorizer`. Dengan menggunakan `CountVectorizer`, akan dihitung frekuensi kemunculan setiap kata pada kolom _tags_. Berikut merupakan hasil dari _cosine similarity_.

![alt text](https://github.com/mausneg/Movie-Lens-Recommendation-System/blob/main/images/image-2.png?raw=True)

Gambar 2. _Heatmap_ _Cosine Similarity_ antar _Item_

Dari Gambar 2 , terlihat bahwa banyak daerah yang memiliki warna yang cendrung terang yang menunjukkan bahwa terdapat banyak kesamaan antar film berdasarkan tags dan genres. Hal ini menunjukkan bahwa _cosine similarity_ dapat digunakan untuk mengukur kesamaan antar film berdasarkan tags dan genres.

Langkah selanjutnya yaitu membuat _function_ untuk mendapatkan rekomendasi film berdasarkan film yang dipilih oleh _user_. Berikut merupakan _function_ yang digunakan.

```python
def get_recommendation_movie(title):
    index = df_movies_similarity[df_movies_similarity['title'] == title].index[0]
    similarity_score = cosine_sim[index]
    similarity_place = sorted(enumerate(similarity_score),key=lambda x: x[1],reverse=True)[1:11]
    similarity_list = []
    for i in similarity_place:
        similarity_list.append([df_movies_similarity.iloc[i[0], 1]] + [i[1]])
    return similarity_list
```

Dari _function_ di atas, _user_ dapat memasukkan judul film yang ingin dicari rekomendasinya. Kemudian, _function_ tersebut akan mengembalikan 10 film yang memiliki kesamaan berdasarkan tags dan genres dengan film yang dipilih oleh _user_.

Contoh penggunaan _function_ tersebut yaitu semisal _user_ memasukkan judul film "Toy Story (1995)" maka _function_ tersebut akan mengembalikan 10 film yang memiliki kesamaan berdasarkan tags dan genres dengan film "Toy Story (1995)". Berikut merupakan hasilnya.

Tabel 13. Top 10 _Movies_ dengan "Toy Story (1995)" berdasarkan _Cosine Similarity_
| Movie Title | Similarity Score |
| --- | --- |
| Bug's Life, A (1998) | 0.848528137423857 |
| Toy Story 2 (1999) | 0.74535599249993 |
| Antz (1998) | 0.7071067811865475 |
| Adventures of Rocky and Bullwinkle, The (2000) | 0.7071067811865475 |
| Emperor's New Groove, The (2000) | 0.7071067811865475 |
| Monsters, Inc. (2001) | 0.7071067811865475 |
| Wild, The (2006) | 0.7071067811865475 |
| Shrek the Third (2007) | 0.7071067811865475 |
| Tale of Despereaux, The (2008) | 0.7071067811865475 |
| Asterix and the Vikings (Astérix et les Vikings) (2006) | 0.7071067811865475 |

### Neural Network

Pada tahap ini akan dilakukan pemodelan _machine learning_ dengan menggunakan _neural network_. Model ini akan mempelajari pola dari data _user_ dan data _item_ dengan data _rating_ yang akan menjadi target. Secara garis besar terdapat dua model _sequential_ yang akan digunakan. Model _sequential_ pertama yaitu model untuk data _user_ dan model _sequential_ kedua yaitu model untuk data _item_. Nantinya _output_ dari kedua model tersebut akan digabungkan dengan menggunakan _dot product_.

![alt text](https://predictivehacks.com/wp-content/uploads/2022/10/content_based.png)
Gambar 3. Ilustrasi Arsitektur _Neural Network_ untuk _Content-Based Filtering_

Pada proses pelatihan model _neural network_ akan dilakukan _hyperparameter tuning_ dengan _Graduate Student Descent_ (GSD). Hal ini karena GSD merupakan metode yang paling umum digunakan untuk melakukan _hyperparameter tuning_ pada _deep learning_. Berikut merupakan _hyperparameter_ yang akan di _tuning_:

- _Optimizer_: _Optimizer_ mengontrol bagaimana model diperbarui berdasarkan data yang dilihat dan fungsi _loss_-nya. Pada kasus ini, akan dicoba menggunakan _optimizer_ _adam_ dan _adagrad_ dengan _learning rate_ 0.001 (_default_), 0.0001, dan 0.01.
- Jumlah _Neuron_ pada _Hidden Layer_: Jumlah _neuron_ dalam _hidden layer_ dapat mempengaruhi kapasitas model untuk mempelajari pola dalam data. Terlalu sedikit _neuron_ dapat menyebabkan _underfitting_, sementara terlalu banyak _neuron_ dapat menyebabkan _overfitting_. Pada kasus ini, akan dicoba menggunakan 32, 64, 128, 256, 512, dan 1024.
- Jumlah _Hidden Layer_: Jumlah _hidden layer_ dalam model _deep learning_ juga dapat mempengaruhi kapasitas model. Model dengan lebih banyak layer dapat mempelajari pola yang lebih kompleks, tetapi juga lebih berisiko _overfitting_ dan membutuhkan lebih banyak data untuk pelatihan. Pada kasus ini, akan dicoba menggunakan 2 sampai 4 _hidden layer_.
- _Epoch_: _Epoch_ adalah jumlah kali seluruh dataset melalui _neural network_ selama pelatihan. Pada kasus ini, akan dicoba menggunakan 50 dan 100 _epoch_.
- _Batch Size_: _Batch size_ adalah jumlah sampel yang diproses sebelum model diperbarui. _Batch size_ yang lebih kecil dapat menghasilkan pembaruan yang lebih sering, tetapi juga dapat menyebabkan _noise_ dalam pembaruan tersebut. Pada kasus ini, akan dicoba menggunakan _batch size_ 64, 128, dan 256.

Dari proses _tuning_ maka didapatkan model yang terbaik terdiri dari 512 _neuron_, _layer_ kedua terdiri dari 256 _neuron_, dan _layer_ terakhir terdiri dari 64 _neuron_. Model ini menggunakan fungsi _activation_ _relu_ pada _layer_ pertama dan kedua, karena _relu_ merupakan fungsi _activation_ yang paling umum digunakan pada _hidden layer_. Pada model ini juga ditambahkan _dropout_ dengan _rate_ 0.2 pada _layer_ pertama dan kedua untuk mencegah _overfitting_. Sedangkan pada _layer_ terakhir menggunakan fungsi _activation_ _linear_ karena _linear_ merupakan fungsi _activation_ yang paling umum digunakan pada _output layer_ untuk _regression_.

Pada masing-masing model akan ditambahkan _layer input_ dengan _input shape_ yang sesuai dengan jumlah _feature_ pada data _user_ dan data _item_. Kemudian, _layer_ tersebut akan dihubungkan dengan _layer_ _dense_ dengan jumlah _neuron_ yang sudah ditentukan sebelumnya. Sebelum dilakukan _dot product_, _output_ dari masing-masing model akan di normalisasi terlebih dahulu, hal ini bertujuan agar _output_ dari masing-masing model memiliki rentang nilai yang sama. Setelah itu, _output_ dari masing-masing model akan di _dot product_ untuk mendapatkan _output_ akhir. Model akan di _compile_ dengan _optimizer_ _adagrad_ dengan _learning rate_ sebesar 0.01, _mean squared error_, dan \_metrics MSE.

Setelah itu, model akan di _fit_ dengan data _train_ dan data _test_ yang sudah di _split_ sebelumnya. Model akan di _fit_ dengan _epoch_ sebanyak 100 kali dan _batch size_ sebesar 256. Lalu model akan melakukan _prediction_ dengan menggunakan data _user_ yang baru, berikut merupakan data _user_ yang baru tersebut.

Tabel 14. Data _User_ yang Baru

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>userId</th>
      <th>Adventure</th>
      <th>Animation</th>
      <th>Children</th>
      <th>Comedy</th>
      <th>Fantasy</th>
      <th>Romance</th>
      <th>Action</th>
      <th>Crime</th>
      <th>Thriller</th>
      <th>Mystery</th>
      <th>Horror</th>
      <th>Drama</th>
      <th>War</th>
      <th>Western</th>
      <th>Sci-Fi</th>
      <th>Musical</th>
      <th>Film-Noir</th>
      <th>IMAX</th>
      <th>Documentary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1000</td>
      <td>4</td>
      <td>5</td>
      <td>4</td>
      <td>3</td>
      <td>4</td>
      <td>1</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
  </tbody>
</table>

Pada Tabel 14 terlihat user 1000 memiliki preferensi terhadap film dengan genres _Adventure_, _Animation_, _Childern_, _Comedy_, _Fantasy_, dan _Action_. Akan tetapi sebelum melakukan _prediction_ data _user_ tersebut akan di _scalling_ terlebih dahulu agar memiliki rentang nilai yang sama dengan data _user_ yang sudah di _scalling_ sebelumnya. Setelah itu, model akan melakukan _prediction_ dengan menggunakan data _user_ yang baru tersebut. Berikut merupakan hasil _prediction_ dari model tersebut.

Tabel 15. Top 10 _Movies_ yang Direkomendasikan untuk _User_ 1000

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>userId</th>
      <th>predictions</th>
      <th>movieId</th>
      <th>title</th>
      <th>genres</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1000</td>
      <td>3.799577</td>
      <td>130520</td>
      <td>Home (2015)</td>
      <td>[Adventure, Animation, Children, Comedy, Fanta...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1000</td>
      <td>3.799577</td>
      <td>673</td>
      <td>Space Jam (1996)</td>
      <td>[Adventure, Animation, Children, Comedy, Fanta...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1000</td>
      <td>3.772406</td>
      <td>108932</td>
      <td>The Lego Movie (2014)</td>
      <td>[Action, Adventure, Animation, Children, Comed...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1000</td>
      <td>3.772406</td>
      <td>51939</td>
      <td>TMNT (Teenage Mutant Ninja Turtles) (2007)</td>
      <td>[Action, Adventure, Animation, Children, Comed...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1000</td>
      <td>3.772406</td>
      <td>26340</td>
      <td>Twelve Tasks of Asterix, The (Les douze travau...</td>
      <td>[Action, Adventure, Animation, Children, Comed...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1000</td>
      <td>3.761944</td>
      <td>36397</td>
      <td>Valiant (2005)</td>
      <td>[Adventure, Animation, Children, Comedy, Fanta...</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1000</td>
      <td>3.735873</td>
      <td>2294</td>
      <td>Antz (1998)</td>
      <td>[Adventure, Animation, Children, Comedy, Fantasy]</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1000</td>
      <td>3.735873</td>
      <td>3114</td>
      <td>Toy Story 2 (1999)</td>
      <td>[Adventure, Animation, Children, Comedy, Fantasy]</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1000</td>
      <td>3.735873</td>
      <td>1</td>
      <td>Toy Story (1995)</td>
      <td>[Adventure, Animation, Children, Comedy, Fantasy]</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1000</td>
      <td>3.735873</td>
      <td>53121</td>
      <td>Shrek the Third (2007)</td>
      <td>[Adventure, Animation, Children, Comedy, Fantasy]</td>
    </tr>
  </tbody>
</table>

Dari Tabel 15 terlihat bahwa model merekomendasikan 10 film yang memiliki kesamaan dengan preferensi _user_ 1000. Hal ini menunjukkan bahwa model dapat memberikan rekomendasi film berdasarkan preferensi _user_ yang baru.

## Evaluation

Pada tahap ini, model akan dievaluasi dengan menggunakan data _testing_ dan data _validation_. Evaluasi dilakukan dengan menggunakan metrik _MSE_ (_Mean Squared Error_). _MSE_ digunakan karena _MSE_ dapat mengukur seberapa baik model dalam memprediksi data _rating_ yang diberikan oleh _user_. Berikut merupakan hasil evaluasi dari model _neural network_.

![alt text](https://github.com/mausneg/Movie-Lens-Recommendation-System/blob/main/images/image-3.png?raw=True)
Gambar 4. _MSE_ dari Model _Neural Network_

Dari Gambar 4, dapat diamati bahwa:
- Model memiliki MSE sebesar kurang dari 0.16 pada data _train_, data _test_, dan data _validation_.
- Model memiliki MSE yang konsisten pada data _training_, data _testing_, dan data _validation_ sehingga model dapat dikatakan _goodfit_. Hal ini menunjukkan bahwa model tidak _overfitting_ atau _underfitting_. _Overfitting_ sendiri terjadi ketika model memiliki perbedaan MSE yang besar antara data _training_ dan data _testing_ atau antara data _testing_ dan data _validation_. Sedangkan _underfitting_ terjadi ketika model memiliki MSE yang tinggi pada data _training_, data _testing_, dan data _validation_.
- Model memiliki performa yang sangat baik dalam memberikan rekomendasi dengan _error_ di bawah 0.2.
- Dari hasil evaluasi tersebut, dapat disimpulkan bahwa model _neural network_ dapat memberikan rekomendasi film dengan baik.

## References

[^1^]: [Wahyudi, Indah Survyana, "Mesin Rekomendasi Film Menggunakan Metode Kemiripan Genre Berbasis Collaborative Filtering"](https://repository.its.ac.id/42018/1/2215206701-Master-Thesis.pdf)
