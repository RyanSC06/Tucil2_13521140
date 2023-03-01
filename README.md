# CLOSEST-PAIR PROBLEM SOLVER
## Identitas
*Nama* : Ryan Samuel Chandra<br />
*NIM* : 13521140<br />
*Angkatan* : 2021<br />
*Kelas* : K2<br />
*Semester* : 4<br />
*Mata Kuliah* : IF2211 Strategi Algoritma

## Deskripsi
<p align="justify">Permasalahan mencari pasangan titik yang jaraknya terdekat (<i>closest-pair problem</i>), adalah salah satu persoalan terdahulu pada geometri komputasional. Masalahnya adalah: diberikan himpunan Q yang berisi n ≥ 2 buah titik berdimensi tertentu, untuk kemudian dicari pasangan mana yang memiliki jarak Euclidean terdekat.</p>
<p align="center">
  <img width="1000" src="https://i.imgur.com/bm0vid8.png" alt="Ilustrasi Permasalahan <i>Closest-Pair</i>">
</p>
<p align="center">Gambar: https://codereview.stackexchange.com/questions/141976/divide-and-conquer-approach-for-finding-the-closest-pair-of-points</p><br />

<p align="justify">Solusi dari permainan tersebut dapat ditemukan dengan program komputer dengan dua pendekatan, yaitu algoritme <i>brute force</i> dan <i>divide and conquer</i>. Dari segi waktu, jumlah perhitungan, dan efektivitas komputasi, algoritme <i>divide and conquer</i> jauh lebih unggul.</p>

<p align="justify">Dengan bantuan beberapa fungsi pendukung, serta library tambahan, program <i>closest-pair problem solver</i> berhasil dibuat dalam bahasa pemrograman Python. Terdapat satu buah fail yang berisi fungsi (<b>FUNCTIONS.py</b>) dan dua buah fail yang berisi program utama. <b>CLOSEST_PAIR.py</b> berisi program untuk menyelesaikan permasalahan dengan kedua algoritme, lalu dibandingkan secara langsung. <b>CLOSEST_PAIR_GENERALIZED.py</b> berisi program yang sama, namun Anda bisa memasukkan sendiri dimensi titik yang diinginkan</p>

<p align="justify">Silakan menikmati program lengkap yang telah saya buat. Terima kasih sudah berkunjung.</p>


## Penggunaan
<p align="justify">Tidak ada instalasi tambahan yang diperlukan untuk menjalankan program ini, melainkan cukup dengan komputer yang bisa mengeksekusi bahasa pemrograman Python.</p>
<p align="justify">1. Memasukkan input: pada saat program utama dijalankan, akan muncul beberapa pertanyaan pada layar. Apabila pertanyaannya adalah dimensi atau jumlah titik, silakan masukkan sebuah angka. Dimensi ≥ 1, sedangkan jumlah titik ≥ 2. Akhiri dengan menekan tombol <b>ENTER</b>. Ada validasi yang dilakukan oleh program. </p>
<p align="justify">2. Mencetak titik: Anda cukup memasukkan '1' pada pertanyaan "Apakah Anda ingin mencetak titik-titik Anda?", maka semua titik yang dibangkitkan secara acak akan ditampilkan. Catatan: masukkan '0' untuk tidak. Akhiri dengan menekan tombol <b>ENTER</b>. Ada validasi yang dilakukan oleh program.</p>
<p align="justify">3. Menampilkan gambar: Pada fail <b>CLOSEST_PAIR.py</b>, yaitu saat solusi untuk titik tiga dimensi sudah tampil, ada sebuah fitur tambahan yang memungkinkan Anda untuk melihat gambar titik pada koordinat Cartesius tiga sumbu. Anda cukup memasukkan '1' pada pertanyaan "Apakah Anda ingin menampilkan gambar 3D?", maka semua titik yang dibangkitkan secara acak akan ditampilkan. Catatan: masukkan '0' untuk tidak. Akhiri dengan menekan tombol <b>ENTER</b>. Ada validasi yang dilakukan oleh program.</p>
