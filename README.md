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

Tabel 2. Deskripsi Data _Rating_
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

Tabel 4 Statistik Deskriptif Data _Rating_
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

Gambar 1. Distribusi Data _Rating_

Dari histogram di atas, grafik terlihat _left-skewed_ yang menunjukkan bahwa mayoritas film memiliki rating di antara 3.0 - 4.0. Dengan kata lain, ada lebih sedikit film dengan rating rendah dibandingkan dengan film dengan rating tinggi.

Ini bisa menunjukkan bahwa penonton cenderung memberikan rating yang relatif tinggi untuk film yang mereka tonton, atau bisa juga menunjukkan bahwa film dengan rating rendah cenderung ditonton lebih sedikit atau kurang populer di antara penonton.

## Data Preparation

Tahapan ini membahas mengenai proses data preparation yang dilakukan. Data preparation adalah tahapan yang sangat penting dalam proses _machine learning_ karena kualitas data yang baik akan menghasilkan model yang baik pula.

### Merging Data

Langkah selanjutnya adalah menggabungkan dataset sesuai dengan kebutuhan. Data ratings akan digabungkan dengan data _movies_ dan data _movies_ juga akan digabungkan dengan data tags.

#### Data _Movies_ dan Data Tags

Penggabungan kedua dataset ini memungkinkan kita untuk mempertimbangkan lebih banyak fitur saat menghitung kesamaan antara film. Dalam hal ini, algoritma _cosine similarity_ digunakan untuk menghitung kesamaan antara film berdasarkan genre dan tag.

Langkah pertama adalah menggabungkan kedua dataset ini berdasarkan kolom `movieId`. Setelah itu, kolom `tag` akan digabungkan menjadi satu dengan menggunakan fungsi `groupby` dan `agg` untuk menggabungkan tag menjadi satu baris. Berikut merupakan hasilnya.

Tabel 5. Hasil _Join_ Tag berdasarkan `movieId`

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

Tabel 6. Hasil _Merge_ Data Movies dan Data Tags
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

Tabel 7. Hasil _Merge_ Data Movies dan Data Ratings
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

Tabel 8. Hasil _Encoding_ Data Movies dan Data Ratings
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
