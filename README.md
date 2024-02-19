# Laporan Proyek Machine Learning - Maulana Surya Negara

## Project Overview

Perkembangan era digital telah mengubah paradigma dan kebutuhan masyarakat secara global. Informasi yang dahulu terbatas pada format kertas kini telah bertransformasi menjadi bentuk digital, dengan internet menjadi kekuatan utama yang memberikan akses mudah ke sumber informasi dari berbagai perangkat teknologi informasi dan komunikasi (TIK). Perubahan ini menjadikan informasi lebih mudah diakses, cerdas, praktis, dan terintegrasi.

Dengan demikian, ledakan data (_big data_) dan informasi digital menjadi fenomena yang tak terhindarkan. Diperkuat oleh peran media sosial, proses bisnis digital, dan publikasi _online_, sehingga volume dan pertumbuhan data meningkat pesat. Contohnya, sekitar 2,5 _Exabyte_ data tercipta setiap hari, dengan perusahaan-perusahaan besar seperti Google, Facebook, Amazon, dan Netflix menjadi pemain kunci dalam pemanfaatan data dan informasi [^1^].

Industri hiburan merupakan salah satu industri yang paling berdampak dengan adanya fenomena _big data_ ini. Dengan banyaknya film yang dirilis setiap tahunnya, pengguna layanan _streaming_ seperti Netflix, Amazon Prime, dan Disney+ memiliki lebih banyak pilihan daripada sebelumnya. Namun, tidak setiap film yang dirilis akan cocok dengan selera pengguna, dan proses mencari film yang cocok dengan selera pengguna bisa menjadi proses yang memakan waktu, mengingat banyaknya pilihan yang ada dan minimnya informasi yang dimiliki penonton tentang film baru yang dirilis.

Di sinilah sistem rekomendasi film menjadi solusi yang efektif untuk menyelesaikan permasalahan ini. Sistem ini memungkinkan pengguna untuk menemukan film yang sesuai dengan selera mereka dengan lebih mudah dan efisien tanpa harus mencari secara manual. Dengan menggunakan kecerdasan buatan, sistem rekomendasi dapat memberikan rekomendasi yang relevan dan personal bagi setiap pengguna berdasarkan preferensi dan riwayat penontonannya.

## Business Understanding

Pada era digital ini, banyak perusahaan telah memanfaatkan sistem rekomendasi untuk meningkatkan interaksi pengguna dan pendapatan perusahaan. YouTube, sebagai platform video paling populer di dunia, telah berhasil meningkatkan interaksi pengguna dengan sistem rekomendasi yang kuat. Sistem ini memanfaatkan berbagai sumber data, termasuk riwayat penontonan pengguna, interaksi pengguna dengan video, dan informasi tentang video itu sendiri untuk memberikan rekomendasi yang relevan.

Selain YouTube, Netflix yang merupakan layanan _streaming_ film dan serial TV terbesar di dunia juga memanfaatkan sistem rekomendasi untuk meningkatkan _engagement_ pengguna. Mereka menggunakan berbagai algoritma dan teknik, termasuk _collaborative filtering_ dan _deep learning_, untuk memberikan rekomendasi yang paling relevan kepada pengguna mereka. Netflix bahkan pernah mengadakan kompetisi, "Netflix Prize", dengan tujuan untuk meningkatkan akurasi sistem rekomendasinya.

Tanpa adanya sistem rekomedasi, suatu bisnis yang bergerak di bidang hiburan seperti layanan _streaming_ akan mengalami penurunan _engagement_ dari pengguna yang pada akhirnya akan berdampak pada pendapatan perusahaan. Berikut adalah beberapa alasan penting mengapa sistem rekomendasi film sangat penting bagi industri hiburan.

- Personalisasi: Sistem rekomendasi memungkinkan personalisasi berdasarkan preferensi individu. Melalui analisis data pengguna, sistem dapat menyajikan rekomendasi yang sesuai dengan selera dan preferensi masing-masing pengguna.
- Mengatasi Keterbatasan Manusia: Dengan adanya fenomena _big data_, manusia sulit untuk memproses dan mengevaluasi setiap opsi secara manual. Sistem rekomendasi menggunakan kecerdasan buatan untuk mengatasi keterbatasan ini dan memberikan rekomendasi yang lebih efisien.
- Mengoptimalkan Pengalaman Pengguna: Dengan membantu pengguna menemukan konten yang sesuai dengan minat mereka, sistem rekomendasi dapat meningkatkan kepuasan pengguna dan memperkecil kemungkinan pengguna untuk melakukan _churn_. Hal ini tentu akan berdampak positif pada pendapatan perusahaan.
- Memanfaatkan Data Pengguna: Dengan mengumpulkan dan menganalisis data dari pengguna seperti rating, sistem rekomendasi dapat terus berkembang dan meningkatkan akurasi rekomendasinya seiring waktu.
- Meningkatkan Pemasaran: Dengan adanya sistem rekomendasi, perusahaan dapat mempromosikan film-film yang kurang populer atau kurang dikenal kepada pengguna. Hal ini akan membantu perusahaan untuk meningkatkan _engagement_ pengguna terhadap film-film tersebut.

Dari latar belakang dan beberapa alasan di atas, dapat ditarik _problem statements_ dan _goals_ sebagai berikut.

### Problem Statements

- Bagaimana cara membangun sistem rekomendasi film yang dapat memberikan rekomendasi yang relevan dan personal bagi setiap pengguna?
- Dataset seperti apa yang diperlukan untuk membangun sistem rekomendasi film yang efektif?
- Bagaimana cara mengevaluasi kinerja dari sistem rekomendasi film yang telah dibangun?

### Goals

- Membangun sistem rekomendasi film yang dapat memberikan rekomendasi yang relevan dan personal bagi setiap pengguna dengan _error_ di bawah 0.2.
- Mengidentifikasi dan mengumpulkan dataset yang diperlukan untuk membangun sistem rekomendasi film yang efektif.
- Mengevaluasi kinerja dari sistem rekomendasi film yang telah dibangun.

### Solution statements

- Membangun sistem rekomendasi film berbasis _content-based filtering_ dengan menggunakan algoritma _cosine similarity_ dan juga menggunakan pendekatan _neural network_. Pendekatan dengan algoritma _cosine similarity_ akan memberikan rekomendasi film berdasarkan kemiripan genre dan tags, sedangkan pendekatan _neural network_ akan memberikan rekomendasi film berdasarkan preferensi pengguna.
- Menggunakan dataset yang berisi informasi mengenai film, seperti judul, genre, dan rating.
- Menggunakan metrik evaluasi _mean squared error_ untuk mengevaluasi kinerja dari sistem rekomendasi film yang telah dibangun. Selain itu juga, akan dilakukan evaluasi dengan melakukan prediksi terhadap pengguna baru.

## Data Understanding

### Data Loading

Dataset yang digunakan dalam proyek ini adalah [MovieLens Latest](https://grouplens.org/datasets/movielens/latest/). Dataset ini terdiri dari 33.832.162 rating, 2.328.315 _tags_, dan 86.537 _movies_. Data ini terdiri dari empat file, yaitu links.csv, movies.csv, ratings.csv, dan tags.csv.

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
| movieId    | 86537 non-null | int64  |
| title      | 86537 non-null | object |
| genres     | 86537 non-null | object |

Dari Tabel 1 didapatkan informasi sebagai berikut.

- Dataset terdiri dari 9742 baris dan 3 kolom.
- Terdapat 1 kolom bertipe `int64` yaitu `movieId`.
- Terdapat 2 kolom bertipe `object` yaitu `title` dan `genres`.

Tabel 2. Deskripsi Data Rating
| Nama Kolom | Non-Null Count | Dtype |
|------------|----------------|-------|
| userId | 33832162 non-null| int64 |
| movieId | 33832162 non-null| int64 |
| rating | 33832162 non-null| float64|
| timestamp | 33832162 non-null| int64 |

Dari Tabel 2 didapatkan informasi sebagai berikut.

- Dataset terdiri dari 100836 baris dan 4 kolom.
- Terdapat 3 kolom bertipe `int64` yaitu `userId`, `movieId`, dan `timestamp`.
- Terdapat 1 kolom bertipe `float64` yaitu `rating`.

Tabel 3. Deskripsi Data _Tags_
| Nama Kolom | Non-Null Count | Dtype |
|------------|----------------|-------|
| userId | 2328315 non-null | int64 |
| movieId | 2328315 non-null | int64 |
| tag | 2328315 non-null | object|
| timestamp | 2328315 non-null | int64 |

Dari Tabel 3 didapatkan informasi sebagai berikut.

- Dataset terdiri dari 2328315 baris dan 4 kolom.
- Terdapat 2 kolom bertipe `int64` yaitu `userId`, `movieId`, dan `timestamp`.
- Terdapat 1 kolom bertipe `object` yaitu `tag`.

Tabel 4 Statistik Deskriptif Data Rating

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>userId</th>
      <th>movieId</th>
      <th>rating</th>
      <th>timestamp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>3.383216e+07</td>
      <td>3.383216e+07</td>
      <td>3.383216e+07</td>
      <td>3.383216e+07</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>1.654380e+05</td>
      <td>2.831348e+04</td>
      <td>3.542540e+00</td>
      <td>1.269362e+09</td>
    </tr>
    <tr>
      <th>std</th>
      <td>9.534122e+04</td>
      <td>4.992865e+04</td>
      <td>1.063959e+00</td>
      <td>2.541023e+08</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000e+00</td>
      <td>1.000000e+00</td>
      <td>5.000000e-01</td>
      <td>7.896520e+08</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>8.295300e+04</td>
      <td>1.219000e+03</td>
      <td>3.000000e+00</td>
      <td>1.046718e+09</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>1.661290e+05</td>
      <td>3.263000e+03</td>
      <td>4.000000e+00</td>
      <td>1.264740e+09</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>2.474500e+05</td>
      <td>4.049100e+04</td>
      <td>4.000000e+00</td>
      <td>1.496919e+09</td>
    </tr>
    <tr>
      <th>max</th>
      <td>3.309750e+05</td>
      <td>2.889830e+05</td>
      <td>5.000000e+00</td>
      <td>1.689843e+09</td>
    </tr>
  </tbody>
</table>

Dari Tabel 4 didapatkan informasi sebagai berikut.

- Rata-rata dari kolom `ratings` adalah 3.54
- Standar deviasi dari kolom `ratings` adalah 1.06
- Nilai minimum dari kolom `ratings` adalah 0.50
- Nilai 25% dari kolom `ratings` adalah 3.00
- Nilai 50% dari kolom `ratings` adalah 4.00
- Nilai 75% dari kolom `ratings` adalah 4.00
- Nilai maksimum dari kolom `ratings` adalah 5.00

Sehingga dapat disimpulkan bahwa distribusi data dari kolom ratings cenderung menumpuk di nilai 3.00 - 4.00. Hal ini bukanlah menjadi masalah karena data rating merupakan data yang bersifat subjektif dan dapat bervariasi.

Untuk memastikan distribusi data dari kolom ratings, akan dilakukan visualisasi distribusi data dari kolom ratings.

![alt text](https://github.com/mausneg/Movie-Lens-Recommendation-System/blob/main/images/image.png?raw=True)

Gambar 1. Histogram Data Rating

Dari histogram di atas, grafik terlihat _left-skewed_ yang menunjukkan bahwa mayoritas film memiliki rating di antara 3.0 - 4.0. Dengan kata lain, ada lebih sedikit film dengan rating rendah dibandingkan dengan film dengan rating tinggi.

Ini bisa menunjukkan bahwa penonton cenderung memberikan rating yang relatif tinggi untuk film yang mereka tonton, atau bisa juga menunjukkan bahwa film dengan rating rendah cenderung ditonton lebih sedikit atau kurang populer di antara penonton.

![alt text](https://github.com/mausneg/Movie-Lens-Recommendation-System/blob/main/images/image-4.png/?raw=True)

Gambar 2. _Boxplot_ Data Rating

Dapat dilihat pada Gambar 2, jika nilai rating menumpuk pada 3.0 - 4.0, dapat mengakibatkan _value_ dari rating yang rendah akan dianggap sebagai _outlier_ oleh model.

Sehingga dengan data _skewed_ ini, dapat mengakibatkan beberapa hal pada model yaitu sebagai berikut.

- Bias dalam Prediksi: Jika mayoritas film memiliki rating tinggi, model mungkin akan "belajar" untuk memprediksi rating yang lebih tinggi secara umum. Ini bisa berarti bahwa model mungkin kurang akurat dalam memprediksi rating rendah.
- Kesulitan dalam Pembelajaran: _Neural network_, seperti banyak model machine learning lainnya, bekerja paling baik ketika data yang digunakan untuk melatih model memiliki variasi yang cukup. Jika sebagian besar rating berada dalam kisaran yang sempit (misalnya, antara 3.0 dan 4.0), model mungkin akan kesulitan untuk "belajar" dari data tersebut.
- Pentingnya _Preprocessing_: Mengingat distribusi rating yang tidak merata, penting untuk melakukan _preprocessing_ data sebelum melatih model. Ini bisa mencakup normalisasi atau standarisasi rating, atau mungkin melakukan transformasi pada rating (misalnya, transformasi log) untuk membuat distribusi lebih simetris. Atau dapat juga melakukan _downsample_ pada rating yang tinggi.
- Pertimbangan dalam Evaluasi Model: Ketika mengevaluasi model, penting untuk mempertimbangkan distribusi rating. Misalnya, jika model cenderung memprediksi rating yang lebih tinggi, metrik evaluasi seperti _Mean Squared Error_ (MSE) mungkin akan rendah, tetapi ini mungkin tidak mencerminkan kinerja model dalam memprediksi rating rendah.

## Data Preparation

Tahapan ini membahas mengenai proses data preparation yang dilakukan. Data preparation adalah tahapan yang sangat penting dalam proses _machine learning_ karena kualitas data yang baik akan menghasilkan model yang baik pula.

### Downsample Data

Langkah pertama yang dilakukan adalah melakukan _downsample_ pada data rating. Hal ini bertujuan untuk mengatasi distribusi data yang tidak seimbang pada kolom rating. Selain itu juga, _downsample_ akan mengurangi jumlah data yang akan diolah oleh model, sehingga dapat mempercepat proses _training_ model. Berikut merupakan hasil dari _downsample_ data rating.

![alt text](https://github.com/mausneg/Movie-Lens-Recommendation-System/blob/main/images/image-5.png?raw=True)

Gambar 3. Histogram Data Rating Setelah _Downsample_

Dari Gambar 3 didapatkan informasi bahwa setelah dilakukan _downsampling_, distribusi data dari kolom ratings menjadi lebih seimbang. Untuk memastikan akan dilakukan visualisasi distribusi data dari kolom ratings setelah dilakukan _downsampling_.

Setelah melakukannya pada kolom ratings, selanjutnya akan dilakukan _downsampling_ pada data _movies_ dan tags. Selain untuk mengurangi ukuran data, hal ini bertujuan menghindari data _movies_ dan tags yang tidak terdapat pada data ratings.

### Merging Data

Langkah selanjutnya adalah menggabungkan dataset sesuai dengan kebutuhan. Data ratings akan digabungkan dengan data _movies_ dan data _movies_ juga akan digabungkan dengan data tags. Seperti yang diketahui, data tags berisi informasi mengenai tag yang diberikan oleh pengguna untuk setiap film yang ditonton, sehingga data ini dapat digunakan untuk memberikan rekomendasi film berdasarkan pendapat yang diberikan oleh pengguna. Penggabungan kedua dataset bertujuan untuk mendapatkan deskripsi film yang lebih lengkap, sehingga dapat digunakan untuk memberikan rekomendasi film berdasarkan kemiripan genre dan tags. Sedangkan data ratings dan data _movies_ digabungkan bertujuan untuk mendapatkan informasi lengkap terkait rating yang diberikan oleh pengguna untuk setiap film yang ditonton, sehingga dapat digunakan untuk memberikan rekomendasi film berdasarkan preferensi rating pengguna terhadap suatu genre film.

#### Data Movies dan Data Tags

Langkah pertama adalah menggabungkan kedua dataset ini berdasarkan kolom `movieId`. Setelah itu, kolom `tag` akan digabungkan menjadi satu dengan menggunakan fungsi `groupby` dan `agg` untuk menggabungkan tag menjadi satu baris. Hal ini bertujuan untuk menggabungkan pendapat yang diberikan oleh beberapa pengguna terhadap suatu film menjadi satu baris. Berikut merupakan hasilnya, berikut merupakan hasilnya.

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
      <td>animation friendship toys animation Disney Pix...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>animals based on a book fantasy magic board ga...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>sequel moldy old old age old men wedding old p...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>characters chick flick girl movie characters c...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>family pregnancy wedding 4th wall aging baby d...</td>
    </tr>
  </tbody>
</table>

Selanjutnya akan dilakukan _merge_ antara data movies dan data _tags_, sehingga akan dapat terlihat jelas ke _film_ yang mana _tag_ tersebut diberikan. Setelah itu, akan dilakukan penggabungan antara kolom `tag` dengan kolom `genres` untuk mendapatkan deskripsi film yang lebih lengkap. Hal ini karena genre dan _tag_ sendiri merupakan bagian dari identitas film. Berikut merupakan hasilnya.

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

Langkah pertama adalah menggabungkan kedua dataset ini berdasarkan kolom `movieId` untuk melihat lebih lengkap identitas lengkap dari film yang diberikan rating oleh pengguna. Berikut merupakan hasilnya.

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
      <td>7</td>
      <td>3396</td>
      <td>2.0</td>
      <td>Muppet Movie, The (1979)</td>
      <td>Adventure Children Comedy Musical</td>
    </tr>
    <tr>
      <th>1</th>
      <td>7</td>
      <td>1960</td>
      <td>2.0</td>
      <td>Last Emperor, The (1987)</td>
      <td>Drama</td>
    </tr>
    <tr>
      <th>2</th>
      <td>14</td>
      <td>19</td>
      <td>0.5</td>
      <td>Ace Ventura: When Nature Calls (1995)</td>
      <td>Comedy</td>
    </tr>
    <tr>
      <th>3</th>
      <td>17</td>
      <td>93510</td>
      <td>5.0</td>
      <td>21 Jump Street (2012)</td>
      <td>Action Comedy Crime</td>
    </tr>
    <tr>
      <th>4</th>
      <td>22</td>
      <td>33794</td>
      <td>3.5</td>
      <td>Batman Begins (2005)</td>
      <td>Action Crime IMAX</td>
    </tr>
  </tbody>
</table>

Pada Tabel 7 data movies dan data ratings sudah digabungkan berdasarkan `movieId`. Langkah selanjutnya yaitu melakukan _encoding_ dengan menjabarkan kolom genres menjadi beberapa kolom berdasarkan nilai yang ada pada kolom genres yang berisi nilai 1 atau 0. Yang mana nilai 1 menunjukkan bahwa film tersebut memiliki genre tersebut dan nilai 0 menunjukkan bahwa film tersebut tidak memiliki genre tersebut. Hal ini bertujuan, untuk melihat preferensi rating pengguna terhadap suatu genre film bukan lagi berdasarkan rating film secara keseluruhan. Berikut merupakan hasilnya.

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
      <th>Children</th>
      <th>Comedy</th>
      <th>Musical</th>
      <th>Drama</th>
      <th>Action</th>
      <th>...</th>
      <th>Romance</th>
      <th>Western</th>
      <th>Fantasy</th>
      <th>Thriller</th>
      <th>Horror</th>
      <th>Mystery</th>
      <th>Animation</th>
      <th>War</th>
      <th>Documentary</th>
      <th>Film-Noir</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>7</td>
      <td>3396</td>
      <td>2.0</td>
      <td>Muppet Movie, The (1979)</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
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
      <th>1</th>
      <td>7</td>
      <td>1960</td>
      <td>2.0</td>
      <td>Last Emperor, The (1987)</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
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
      <th>2</th>
      <td>14</td>
      <td>19</td>
      <td>0.5</td>
      <td>Ace Ventura: When Nature Calls (1995)</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
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
      <td>17</td>
      <td>93510</td>
      <td>5.0</td>
      <td>21 Jump Street (2012)</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
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
      <th>4</th>
      <td>22</td>
      <td>33794</td>
      <td>3.5</td>
      <td>Batman Begins (2005)</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
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
  </tbody>
</table>

Pada Tabel 8 dapat dilihat kolom `genres` sudah dijabarkan dengan masing-masing jenis _genre_ menjadi kolom tersendiri. Sehingga dapat dilihat preferensi rating pengguna terhadap genre film apa saja yang lebih disukai.

### Data Transformation

Setelah melakukan penggabungan data, langkah selanjutnya adalah melakukan _data transformation_ . Pada tahap ini, data yang berisi rating dan _movie_ akan di-_tranform_ menjadi data _user_, data _movie_, dan data rating. Hal ini bertujuan untuk membentuk data _features_ dan _target_ yang akan digunakan untuk membangun model rekomendasi.

#### Data User (Preferences)

Tahap ini dimulai dengan membuang kolom-kolom yang tidak diperlukan untuk data _user_ seperti `movieId` dan `title`, hal ini karena suatu preferensi tidak tergantung pada film tertentu, melainkan pada _genre_ film itu sendiri. Selanjutnya akan dibentuk data _preferences user_ berdasarkan nilai rata-rata dari rating yang diberikan oleh _user_ untuk setiap _genre_ dari film yang **pernah** ditonton oleh _user_. Hal ini karena beberapa _user_ mungkin pernah menonton film dengan _genre_ yang sama dengan sebelumnya, sehingga dapat dilihat preferensi _user_ terhadap _genre_ film yang lebih spesifik. Berikut merupakan hasilnya.

Tabel 9. Sampel Data _Preferences User_

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>userId</th>
      <th>Comedy</th>
      <th>Romance</th>
      <th>Adventure</th>
      <th>Animation</th>
      <th>Children</th>
      <th>Fantasy</th>
      <th>Drama</th>
      <th>Action</th>
      <th>Sci-Fi</th>
      <th>Mystery</th>
      <th>Thriller</th>
      <th>Crime</th>
      <th>War</th>
      <th>IMAX</th>
      <th>Horror</th>
      <th>Musical</th>
      <th>Film-Noir</th>
      <th>Western</th>
      <th>Documentary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>7</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>14</td>
      <td>0.5</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>17</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>22</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>3.5</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>3.5</td>
      <td>0.0</td>
      <td>3.5</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>24</td>
      <td>4.5</td>
      <td>1.5</td>
      <td>4.5</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>4.5</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.5</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>

Pada Tabel 9 dapat dilihat bahwa data _preferences user_ berisi seberapa tertarik _user_ terhadap setiap _genre_ film yang pernah ditonton oleh _user_. Dengan demikian, data _preferences user_ ini akan digunakan untuk memberikan rekomendasi film berdasarkan preferensi _user_ terhadap _genre_ film.

Langkah selanjutnya yaitu mengaplikasikan data _preferences user_ tersebut ke dalam data _user_ yang sudah di-_drop_ kolom-kolom yang tidak diperlukan. Dengan

Tabel 10. Data _User_ yang Telah di-_Transform_

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>userId</th>
      <th>Adventure</th>
      <th>Children</th>
      <th>Comedy</th>
      <th>Musical</th>
      <th>Drama</th>
      <th>Action</th>
      <th>Crime</th>
      <th>IMAX</th>
      <th>Sci-Fi</th>
      <th>Romance</th>
      <th>Western</th>
      <th>Fantasy</th>
      <th>Thriller</th>
      <th>Horror</th>
      <th>Mystery</th>
      <th>Animation</th>
      <th>War</th>
      <th>Documentary</th>
      <th>Film-Noir</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>7</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>7</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>14</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.5</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>17</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>22</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>3.5</td>
      <td>3.5</td>
      <td>3.5</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>99798</th>
      <td>330951</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>99799</th>
      <td>330956</td>
      <td>4.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>4.0</td>
      <td>4.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>99800</th>
      <td>330961</td>
      <td>0.5</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.5</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.5</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>99801</th>
      <td>330964</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>99802</th>
      <td>330971</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.5</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.5</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.5</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
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
      <th>Children</th>
      <th>Comedy</th>
      <th>Musical</th>
      <th>Drama</th>
      <th>Action</th>
      <th>Crime</th>
      <th>IMAX</th>
      <th>Sci-Fi</th>
      <th>Romance</th>
      <th>Western</th>
      <th>Fantasy</th>
      <th>Thriller</th>
      <th>Horror</th>
      <th>Mystery</th>
      <th>Animation</th>
      <th>War</th>
      <th>Documentary</th>
      <th>Film-Noir</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3396</td>
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
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1960</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
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
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>19</td>
      <td>0</td>
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
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>93510</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
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
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>33794</td>
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
      <th>Children</th>
      <th>Comedy</th>
      <th>Musical</th>
      <th>Drama</th>
      <th>Action</th>
      <th>Crime</th>
      <th>IMAX</th>
      <th>Sci-Fi</th>
      <th>Romance</th>
      <th>Western</th>
      <th>Fantasy</th>
      <th>Thriller</th>
      <th>Horror</th>
      <th>Mystery</th>
      <th>Animation</th>
      <th>War</th>
      <th>Documentary</th>
      <th>Film-Noir</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>7</td>
      <td>0.502246</td>
      <td>1.261085</td>
      <td>0.301016</td>
      <td>1.952713</td>
      <td>0.086485</td>
      <td>-0.900659</td>
      <td>-0.630384</td>
      <td>-0.324194</td>
      <td>-0.674925</td>
      <td>-0.653672</td>
      <td>-0.220667</td>
      <td>-0.547285</td>
      <td>-0.84067</td>
      <td>-0.485891</td>
      <td>-0.445567</td>
      <td>-0.39607</td>
      <td>-0.329605</td>
      <td>-0.210187</td>
      <td>-0.157444</td>
    </tr>
    <tr>
      <th>1</th>
      <td>7</td>
      <td>0.502246</td>
      <td>1.261085</td>
      <td>0.301016</td>
      <td>1.952713</td>
      <td>0.086485</td>
      <td>-0.900659</td>
      <td>-0.630384</td>
      <td>-0.324194</td>
      <td>-0.674925</td>
      <td>-0.653672</td>
      <td>-0.220667</td>
      <td>-0.547285</td>
      <td>-0.84067</td>
      <td>-0.485891</td>
      <td>-0.445567</td>
      <td>-0.39607</td>
      <td>-0.329605</td>
      <td>-0.210187</td>
      <td>-0.157444</td>
    </tr>
    <tr>
      <th>2</th>
      <td>14</td>
      <td>-0.782566</td>
      <td>-0.457927</td>
      <td>-0.660158</td>
      <td>-0.300952</td>
      <td>-1.073048</td>
      <td>-0.900659</td>
      <td>-0.630384</td>
      <td>-0.324194</td>
      <td>-0.674925</td>
      <td>-0.653672</td>
      <td>-0.220667</td>
      <td>-0.547285</td>
      <td>-0.84067</td>
      <td>-0.485891</td>
      <td>-0.445567</td>
      <td>-0.39607</td>
      <td>-0.329605</td>
      <td>-0.210187</td>
      <td>-0.157444</td>
    </tr>
    <tr>
      <th>3</th>
      <td>17</td>
      <td>-0.782566</td>
      <td>-0.457927</td>
      <td>2.223363</td>
      <td>-0.300952</td>
      <td>-1.073048</td>
      <td>2.289615</td>
      <td>2.625576</td>
      <td>-0.324194</td>
      <td>-0.674925</td>
      <td>-0.653672</td>
      <td>-0.220667</td>
      <td>-0.547285</td>
      <td>-0.84067</td>
      <td>-0.485891</td>
      <td>-0.445567</td>
      <td>-0.39607</td>
      <td>-0.329605</td>
      <td>-0.210187</td>
      <td>-0.157444</td>
    </tr>
    <tr>
      <th>4</th>
      <td>22</td>
      <td>-0.782566</td>
      <td>-0.457927</td>
      <td>-0.980549</td>
      <td>-0.300952</td>
      <td>-1.073048</td>
      <td>1.332533</td>
      <td>1.648788</td>
      <td>3.369889</td>
      <td>-0.674925</td>
      <td>-0.653672</td>
      <td>-0.220667</td>
      <td>-0.547285</td>
      <td>-0.84067</td>
      <td>-0.485891</td>
      <td>-0.445567</td>
      <td>-0.39607</td>
      <td>-0.329605</td>
      <td>-0.210187</td>
      <td>-0.157444</td>
    </tr>
  </tbody>
</table>

Setelah melakukan _transformasi_, data _user_ dan data _item_ akan di _scalling_ dengan menggunakan _Standard Scaler_. Alasan _Standard Scaler_ digunakan yaitu karena akan dilakukan pembagian rentang rating, jika _value_ genre bernilai positif menandakan user menyukai film tersebut, sedangkan jika _value_ genre bernilai negatif menandakan user tidak menyukai film tersebut. Atau jika pada data item, _value_ genre bernilai positif menandakan film tersebut memiliki genre tersebut, sedangkan jika _value_ genre bernilai negatif menandakan film tersebut tidak memiliki genre tersebut. Sedangkan untuk data rating akan di _scalling_ dengan menggunakan _Min Max Scaler_ dikarenakan untuk memastikan bahwa rentang nilai rating dari setiap pengguna adalah antara 0 dan 1, sehingga dapat lebih mudah membandingkan preferensi rating dari berbagai pengguna tanpa adanya bias akibat skala yang berbeda.

### Data Splitting

Selanjutnya, data _user_, data _item_, dan data rating akan di _split_ menjadi data _train_, data _test_, dan data _validation_. Hal ini bertujuan agar dapat dilakukan evaluasi model machine learning yang akan dibuat. Perbandingan data _train_, data _test_, dan data _validation_ yang digunakan adalah 80% data _train_, 10% data _test_, dan 10% data _validation_.

## Modeling

Pada tahap ini akan dilakukan pemodelan machine learning yaitu menggunakan _content-based filtering_ dengan menggunakan _cosine similarity_ dan menggunakan _neural network_. Perbedaan dari kedua model ini yaitu sebagai berikut.

- _Content-based filtering_ dengan menggunakan _cosine similarity_ akan menghitung kemiripan antara _item_ dengan _item_ lainnya berdasarkan _genre_ dan _tags_ yang dimiliki oleh _item_ tersebut. Keuntungan dari metode ini adalah bahwa ia dapat memberikan rekomendasi yang sangat spesifik untuk setiap pengguna Namun, metode ini hanya dapat memberikan rekomendasi berdasarkan _item_ yang sudah ada dan tidak dapat memberikan rekomendasi untuk _item_.
- _Neural network_ akan mempelajari pola dari data _user_ dan data _item_ dengan data _rating_ yang akan menjadi target. Keuntungan dari metode ini adalah bahwa ia dapat memberikan rekomendasi untuk _item_ atau pengguna baru, dan dapat mempertimbangkan interaksi antara pengguna dan item. Namun, _neural network_ biasanya memerlukan lebih banyak data dan waktu pelatihan dibandingkan dengan metode cosine similarity.

### Content-Based Filtering dengan Cosine Similarity

Pada perhitungan _similarity_ antar film berdasarkan genres dan _tags_, akan digunakan _cosine similarity_. Hal ini dilakukan karena _cosine similarity_ dapat mengukur kesamaan antar film berdasarkan genres dan _tags_. Tetapi sebelum itu, akan dilakukan ekstraksi data _tags_ dengan menggunakan `CountVectorizer`. Dengan menggunakan `CountVectorizer`, akan dihitung frekuensi kemunculan setiap kata pada kolom _tags_. 

Langkah selanjutnya yaitu membuat _function_ untuk mendapatkan rekomendasi film berdasarkan film yang dipilih oleh _user_. Sehingga _user_ dapat memasukkan judul film yang ingin dicari rekomendasinya. Kemudian, _function_ tersebut akan mengembalikan 10 film yang memiliki kesamaan berdasarkan tags dan genres dengan film yang dipilih oleh _user_.

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
Gambar 4. Ilustrasi Arsitektur _Neural Network_ untuk _Content-Based Filtering_

Pada proses pelatihan model _neural network_ akan dilakukan _hyperparameter tuning_ dengan _Graduate Student Descent_ (GSD). Hal ini karena GSD merupakan metode yang paling umum digunakan untuk melakukan _hyperparameter tuning_ pada _deep learning_. Berikut merupakan _hyperparameter_ yang akan di _tuning_:

- _Optimizer_: _Optimizer_ mengontrol bagaimana model diperbarui berdasarkan data yang dilihat dan fungsi _loss_-nya. Pada kasus ini, akan dicoba menggunakan _optimizer_ _adam_ dan _adagrad_ dengan _learning rate_ 0.001 (_default_), 0.0001, dan 0.01.
- Jumlah _Neuron_ pada _Hidden Layer_: Jumlah _neuron_ dalam _hidden layer_ dapat mempengaruhi kapasitas model untuk mempelajari pola dalam data. Terlalu sedikit _neuron_ dapat menyebabkan _underfitting_, sementara terlalu banyak _neuron_ dapat menyebabkan _overfitting_. Pada kasus ini, akan dicoba menggunakan 32, 64, 128, 256, 512, dan 1024.
- Jumlah _Hidden Layer_: Jumlah _hidden layer_ dalam model _deep learning_ juga dapat mempengaruhi kapasitas model. Model dengan lebih banyak layer dapat mempelajari pola yang lebih kompleks, tetapi juga lebih berisiko _overfitting_ dan membutuhkan lebih banyak data untuk pelatihan. Pada kasus ini, akan dicoba menggunakan 2 sampai 4 _hidden layer_.
- _Epoch_: _Epoch_ adalah jumlah kali seluruh dataset melalui _neural network_ selama pelatihan. Pada kasus ini, akan dicoba menggunakan 50 dan 100 _epoch_.
- _Batch Size_: _Batch size_ adalah jumlah sampel yang diproses sebelum model diperbarui. _Batch size_ yang lebih kecil dapat menghasilkan pembaruan yang lebih sering, tetapi juga dapat menyebabkan _noise_ dalam pembaruan tersebut. Pada kasus ini, akan dicoba menggunakan _batch size_ 64, 128, dan 256.

Dari proses _tuning_ maka didapatkan arsitektur model yang terbaik terdiri dari 512 _neuron_, _layer_ kedua terdiri dari 256 _neuron_, dan _layer_ terakhir terdiri dari 64 _neuron_. Model ini menggunakan fungsi _activation_ _relu_ pada _layer_ pertama dan kedua, karena _relu_ merupakan fungsi _activation_ yang paling umum digunakan pada _hidden layer_. Pada model ini juga ditambahkan _dropout_ dengan _rate_ 0.2 pada _layer_ pertama dan kedua untuk mencegah _overfitting_. Sedangkan pada _layer_ terakhir menggunakan fungsi _activation_ _linear_ karena _linear_ merupakan fungsi _activation_ yang paling umum digunakan pada _output layer_ untuk _regression_.

Pada masing-masing model akan ditambahkan _layer input_ dengan _input shape_ yang sesuai dengan jumlah _feature_ pada data _user_ dan data _item_. Kemudian, _layer_ tersebut akan dihubungkan dengan _layer_ _dense_ dengan jumlah _neuron_ yang sudah ditentukan sebelumnya. Sebelum dilakukan _dot product_, _output_ dari masing-masing model akan di normalisasi terlebih dahulu, hal ini bertujuan agar _output_ dari masing-masing model memiliki rentang nilai yang sama. Setelah itu, _output_ dari masing-masing model akan di _dot product_ untuk mendapatkan _output_ akhir. Model akan di _compile_ dengan _optimizer_ _adam_ dengan _learning rate_ sebesar 0.001, _mean squared error_, dan _metrics_ MSE. _Optimizer_ _adam_ dipilih karena _adam_ mendapat hasil yang lebih baik dibandingkan dengan _adagrad_ pada _hyperparameter tuning_ sebelumnya. _Metrics_ yang digunakan adalah _mean squared error_ karena _mean squared error_ merupakan _metrics_ yang paling umum digunakan untuk _regression_.

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
      <td>500000</td>
      <td>4</td>
      <td>5</td>
      <td>4</td>
      <td>3</td>
      <td>4</td>
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
      <td>1</td>
      <td>1</td>
    </tr>
  </tbody>
</table>

Pada Tabel 14 terlihat user 500000 memiliki preferensi terhadap film dengan genres _Adventure_, _Animation_, _Childern_ dan _Fantasy_. Akan tetapi sebelum melakukan _prediction_ data _user_ tersebut akan di _scalling_ terlebih dahulu agar memiliki rentang nilai yang sama dengan data _user_ yang sudah di _scalling_ sebelumnya. Setelah itu, model akan melakukan _prediction_ dengan menggunakan data _user_ yang baru tersebut. Berikut merupakan hasil _prediction_ dari model tersebut.

Tabel 15. Top 10 _Movies_ yang Direkomendasikan untuk _User_ 500000

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
      <td>500000</td>
      <td>3.843387</td>
      <td>5618</td>
      <td>Spirited Away (Sen to Chihiro no kamikakushi) ...</td>
      <td>[Adventure, Animation, Fantasy]</td>
    </tr>
    <tr>
      <th>1</th>
      <td>500000</td>
      <td>3.843387</td>
      <td>102720</td>
      <td>Epic (2013)</td>
      <td>[Adventure, Animation, Fantasy]</td>
    </tr>
    <tr>
      <th>2</th>
      <td>500000</td>
      <td>3.843387</td>
      <td>52806</td>
      <td>Tales from Earthsea (Gedo Senki) (2006)</td>
      <td>[Adventure, Animation, Fantasy]</td>
    </tr>
    <tr>
      <th>3</th>
      <td>500000</td>
      <td>3.817176</td>
      <td>65261</td>
      <td>Ponyo (Gake no ue no Ponyo) (2008)</td>
      <td>[Adventure, Animation, Children, Fantasy]</td>
    </tr>
    <tr>
      <th>4</th>
      <td>500000</td>
      <td>3.817176</td>
      <td>4366</td>
      <td>Atlantis: The Lost Empire (2001)</td>
      <td>[Adventure, Animation, Children, Fantasy]</td>
    </tr>
    <tr>
      <th>5</th>
      <td>500000</td>
      <td>3.817176</td>
      <td>6536</td>
      <td>Sinbad: Legend of the Seven Seas (2003)</td>
      <td>[Adventure, Animation, Children, Fantasy]</td>
    </tr>
    <tr>
      <th>6</th>
      <td>500000</td>
      <td>3.817176</td>
      <td>2116</td>
      <td>Lord of the Rings, The (1978)</td>
      <td>[Adventure, Animation, Children, Fantasy]</td>
    </tr>
    <tr>
      <th>7</th>
      <td>500000</td>
      <td>3.817176</td>
      <td>2033</td>
      <td>Black Cauldron, The (1985)</td>
      <td>[Adventure, Animation, Children, Fantasy]</td>
    </tr>
    <tr>
      <th>8</th>
      <td>500000</td>
      <td>3.817176</td>
      <td>27731</td>
      <td>Cat Returns, The (Neko no ongaeshi) (2002)</td>
      <td>[Adventure, Animation, Children, Fantasy]</td>
    </tr>
    <tr>
      <th>9</th>
      <td>500000</td>
      <td>3.817176</td>
      <td>4519</td>
      <td>Land Before Time, The (1988)</td>
      <td>[Adventure, Animation, Children, Fantasy]</td>
    </tr>
  </tbody>
</table>

Dari Tabel 15 terlihat bahwa model merekomendasikan 10 film yang memiliki kesamaan dengan preferensi _user_ 500000. Hal ini menunjukkan bahwa model dapat memberikan rekomendasi film berdasarkan preferensi _user_ yang baru.

## Evaluation

Langkah terakhir yaitu melakukan evaluasi dari model _content-based filtering_ dengan menggunakan _cosine similarity_ dan model _neural network_. Hal ini bertujuan untuk mengetahui seberapa baik model dalam memberikan rekomendasi film.

### Cosine Similarity

Pada _cosine similarity_, evaluasi dilakukan dengan menggunakan _precision_. Hal itu dilakukan dengan cara membandingkan jumlah film yang relevan dengan jumlah film yang direkomendasikan.

Tabel 16. Data dari Film "Toy Story (1995)"

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>movieId</th>
      <th>title</th>
      <th>genres</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Toy Story (1995)</td>
      <td>Adventure Animation Children Comedy Fantasy</td>
    </tr>
  </tbody>
</table>

Tabel 17. Top 10 _Movies_ yang Direkomendasikan untuk "Toy Story (1995)" berdasarkan _Cosine Similarity_

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>movieId</th>
      <th>title</th>
      <th>genres</th>
      <th>similarity_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3114</td>
      <td>Toy Story 2 (1999)</td>
      <td>Adventure Animation Children Comedy Fantasy</td>
      <td>0.884884</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2355</td>
      <td>Bug's Life, A (1998)</td>
      <td>Adventure Animation Children Comedy</td>
      <td>0.822110</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4886</td>
      <td>Monsters, Inc. (2001)</td>
      <td>Adventure Animation Children Comedy Fantasy</td>
      <td>0.746792</td>
    </tr>
    <tr>
      <th>3</th>
      <td>157296</td>
      <td>Finding Dory (2016)</td>
      <td>Adventure Animation Comedy</td>
      <td>0.734941</td>
    </tr>
    <tr>
      <th>4</th>
      <td>6377</td>
      <td>Finding Nemo (2003)</td>
      <td>Adventure Animation Children Comedy</td>
      <td>0.720650</td>
    </tr>
    <tr>
      <th>5</th>
      <td>78499</td>
      <td>Toy Story 3 (2010)</td>
      <td>Adventure Animation Children Comedy Fantasy IMAX</td>
      <td>0.713188</td>
    </tr>
    <tr>
      <th>6</th>
      <td>8961</td>
      <td>Incredibles, The (2004)</td>
      <td>Action Adventure Animation Children Comedy</td>
      <td>0.707904</td>
    </tr>
    <tr>
      <th>7</th>
      <td>201588</td>
      <td>Toy Story 4 (2019)</td>
      <td>Adventure Animation Children Comedy</td>
      <td>0.682795</td>
    </tr>
    <tr>
      <th>8</th>
      <td>5218</td>
      <td>Ice Age (2002)</td>
      <td>Adventure Animation Children Comedy</td>
      <td>0.682532</td>
    </tr>
    <tr>
      <th>9</th>
      <td>45517</td>
      <td>Cars (2006)</td>
      <td>Animation Children Comedy</td>
      <td>0.675936</td>
    </tr>
  </tbody>
</table>

Dari Tabel 16 dapat dilihat data dari film yang dicari yaitu "Toy Story (1995)", maka dapat dilihat pada Tabel 17 terdapat _top_ 10 film yang direkomendasikan berdasarkan _cosine similarity_. Dari 10 film yang direkomendasikan, jika dilihat dari konten film "Toy Story (1995)" maka semua film yang direkomendasikan memiliki relevansi dengan film "Toy Story (1995)". Sehingga jika dihitung _precision_ dari model _cosine similarity_ maka didapatkan _precision_ sebesar 1.0 atau 100%. Hasil ini menunjukkan bahwa _cosine similarity_ sangat efektif dalam memberikan rekomendasi film yang relevan berdasarkan genre ataupun berdasarkan tag. Dengan kata lain, jika seorang pengguna menyukai film dengan konten tertentu, model ini dapat dengan akurat merekomendasikan film lain dengan konten yang sama.

Namun, perlu diingat bahwa relevansi film tidak hanya ditentukan oleh konten. Faktor lain seperti rating juga dapat mempengaruhi sejauh mana film relevan bagi pengguna. Meskipun metode ini berhasil dalam merekomendasikan film dengan konten yang sama, itu tidak selalu berarti bahwa film-film tersebut akan disukai oleh pengguna. Untuk itu, pada projek ini terdapat juga model _neural network_ yang akan mempertimbangkan faktor lain seperti rating.

### Neural Network

Pada tahap ini, model akan dievaluasi dengan menggunakan data _testing_ dan data _validation_. Evaluasi dilakukan dengan menggunakan metrik _MSE_ (_Mean Squared Error_). _MSE_ digunakan karena _MSE_ dapat mengukur seberapa baik model dalam memprediksi data _rating_ yang diberikan oleh _user_. Berikut merupakan hasil evaluasi dari model _neural network_.

![alt text](https://github.com/mausneg/Movie-Lens-Recommendation-System/blob/main/images/image-3.png?raw=True)

Gambar 5. _MSE_ dari Model _Neural Network_

Dari Gambar 5, dapat diamati bahwa:

- Model memiliki _Mean Squared Error_ (MSE) kurang dari 0.06 pada data _training_, _testing_, dan _validation_. MSE adalah metrik yang mengukur rata-rata dari kuadrat _error_. Nilai MSE yang rendah menunjukkan bahwa model mampu memprediksi rating film dengan akurasi yang tinggi. Nilai ini juga menunjukkan bahwa model memiliki kemampuan generalisasi yang baik, yang berarti model mampu memberikan prediksi yang akurat tidak hanya pada data yang digunakan untuk melatih model, tetapi juga pada data baru.
- Model memiliki MSE yang konsisten di antara data _training_, _testing_, dan _validation_. Ini adalah indikasi kuat bahwa model tidak _overfitting_ atau _underfitting_. _Overfitting_ terjadi ketika model terlalu kompleks dan mempelajari data _training_ terlalu detail, yang mengakibatkan performa yang buruk pada data _testing_ atau _validation_. _Underfitting_ terjadi ketika model terlalu sederhana dan tidak mampu menangkap pola penting dalam data. Fakta bahwa model memiliki MSE yang konsisten menunjukkan bahwa model memiliki kompleksitas yang tepat untuk data ini atau disebut sebagai _good fit_.
- Model memiliki _error_ di bawah 0.06 , yang berarti bahwa prediksi rating film oleh model biasanya hanya berbeda sekitar 0.06 dari rating sebenarnya. Ini menunjukkan bahwa model mampu memberikan rekomendasi yang sangat akurat.

Secara keseluruhan, hasil evaluasi ini menunjukkan bahwa model _neural network_ berhasil dalam proyek ini. Model mampu memberikan rekomendasi film yang akurat, yang bisa sangat berguna bagi pengguna dalam memilih film untuk ditonton. Sehingga, model _neural network_ ini dapat dijadikan sebagai solusi yang baik untuk membangun sistem rekomendasi film.

## References

[^1^]: [Wahyudi, I. S. (2017). Mesin rekomendasi film menggunakan metode kemiripan genre berbasis collaborative filtering. Institut Teknologi Sepuluh Nopember.](https://repository.its.ac.id/42018/1/2215206701-Master-Thesis.pdf)
