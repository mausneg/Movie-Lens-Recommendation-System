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
