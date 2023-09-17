![books](https://images.alphacoders.com/132/1326370.png)
# libshop
Singkatan dari Library Shop

# Tugas 2 PBP 
# **Hilmi Atha Putra (2206830050) - PBP B**
# [Link menuju LibShop](https://libshop.adaptable.app/main/)

Soal :
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

Jawab :
## **NOMOR 1**
A. Untuk membuat projek Django yang baru diperlukan beberapa step di bawah
   * Saya membuat direktori lokal baru bernama libshop untuk keperluan proyek saya
   * Untuk membuat proyek Django yang baru diperlukan untuk membuat _Virtual Environment_ agar direktori tersebut terisolasi dan _dependencies_ tidak bertabrakan satu sama lain dengan versi lain di device saya. Caranya dengan membuka terminal sesuai
     dengan direktori yang saya buat kemudian masukan line
     ```
     python -m venv env
     ```
     Kemudian untuk mengaktifkan _Virtual Environment_ masukan line
     ```
     env\Scripts\activate.bat
     ```
   * Karena _Virtual Environment_ sudah aktif, kita bisa menginstall semua dependencies yang diperlukan, sebelum itu saya membuat file requirements.txt untuk diisi dengan _dependencies_ yang diperlukan seperti django, gunicorn dan lain - lain untuk diinstall terlebih
     dahulu. setelah dibuat, kembali ke terminal dengan _Virtual Environment_ dan memasukkan line di bawah untuk menginstall semua dependencies yang diperlukan untuk proses deploying.
     ```
     pip install -r requirements.txt
     ```
   * Nah, untuk membuat proyek Django yang baru saya memasukkan line `django-admin startproject libshop .`
   * Karena proyek yang dibuat masih tahap uji coba, `ALLOWED HOST` pada `settings.py` ditambahkan bintang agar setiap hosts bisa mengakses aplikasi web
     ```
     ALLOWED_HOSTS = ["*"]
     ```
   * Lalu saya menambahkan file `.gitignore` dikarenakan terdapat berkas - berkas yang tidak perlu dilacak oleh git


B. Untuk membuat aplikasi `main` kembali ke terminal dengan _Virtual Environtment_ dan jalankan command `python manage.py startapp main`. setelah itu akan terbuat direktori aplikasi bernama main `main`. Tambahkan aplikasi    di variabel `INSTALLED APPS` pada
  `settings.py` yang berada di direktori proyek `libshop`. Tambahkan direktori `templates` pada direktori main dan tambahkan file `main.html` di dalam folder tersebut. File html tersebut    digunakan untuk mengatur tampilan aplikasi main pada web aplikasi.


C. Untuk melakukan routing proyek diperlukan  step di bawah
   * untuk mengonfigurasi routing aplikasi pada proyek kita membuka file `urls.py` pada direktori proyek `libshop` kemudian mengimpor fungsi `include` dari `django.urls` dan tambahkan path menuju tampilan main pada variabel `urlpattern` yaitu
     `path('main/',include('main.urls'))`


D. Membuat model bernama `Item` di file `models.py`. pada model `item` terdapat beberapa atribut yaitu :
  * name
  * date_added
  * price
  * amount
  * description
  * genre


E. Di dalam `views.py` yang berada di direktori aplikasi `main` saya tambahkan fungsi `show_main` dengan _context_ yang berisi nama aplikasi, nama saya, dan kelas PBP saya. Pada file `main.html` saya bisa mengakses isi dari _context_. contohnya jika saya ingin mengambil
nama, saya menulis `{{name}}` di file `main.html`

F. Untuk membuat routing pada aplikasi `main` saya membuat file python baru yaitu `urls.py` pada direktori aplikasi `main`. Di dalam file tersebut import `path` dari `django.urls` dan import `show_main` dari `main.views`, kemudian buat variable appname yang diisi 
`'main'` dan buat list bernama `urlpattern` dan isi dengan `path('', show_main, name='show_main')`

G. Untuk mendeploy aplikasi baru saya ke adaptable pertama saya harus membuat repositori baru di github kemudian hubungkan repositori lokal `libshop` dengan repositori github. Setelah itu lakukan add, commit, dan push. Terakhir, saya mendeploy aplikasi ke adaptable 


## **NOMOR 2**

![image](https://github.com/hilmiatha/libshop/assets/108039453/38b14fc4-afa8-4dda-8f6a-7abde038583c)

`urls.py` berisi seluruh url yang ada dan django akan memilih url yang sesuai dengan request client, kemudian akan diteruskan ke `views.py`. View bisa berinteraksi dengan `models.py` untuk mendapatkan data /memodifikasi data yang dibutuhkan. Terakhir data tersebut 
akan disajikan melalui template/berkas html kemudian direspons ke pengguna


## **NOMOR 3**

_Virtual Environment_ sangat dianjurkan untuk digunakan saat kita ingin membuat proyek Django dikarenakan berguna untuk mengisolasi _package_ dan _dependency_. Hal itu diperlukan dikarenakan jika kita memiliki banyak proyek, masing - masing proyek akan terisolasi dan 
tidak berhubungan satu sama lain. Misalkan kita ingin mengupdate salah satu _depedency_ pada suatu proyek maka _depedency_ tersebut pada versi lain tidak akan ikut ter-update sehingga akan terhindar dari konflik antar proyek django

Kita bisa membuat proyek Django tanpa _virtual environment_ namun seperti yang dikatakan di atas, sangat tidak direkomendasikan dikarenakan bisa memicu konflik antar proyek django. contohnya adalah jika kita mempunyai proyek A yang menggunakan gunicorn versi 21.0.0,
dan kita ingin membuat proyek b yang menggunakan gunicorn versi terbaru yaitu 21.2.0, jika kita menginstall tanpa _virtual environment_, versi gunicorn pada proyek A akan berubah juga ke versi 21.2.0. _Virtual environtment_ sangat berguna untuk mengatur depedency antar 
proyek


## **NOMOR 4**

MVC, MVT, dan MVVM merupakan pola arsitektur yang umum digunakan pada pengembangan web dan aplikasi ponsel. berikut merupakan penjelasan mengenai ketiganya dan perbedaan - perbedaannya.
* MVC
  
  MVC merupakan singkatan dari Model View Controller. Model merupakan komponen yang mengatur data dan logika dari aplikasi atau web. Model juga menghubungkan aplikasi atau web dengan database. View merupakan komponen yang mengatur tampilan yang akan dilihat oleh
  pengguna. Terakhir, Controller adalah komponen yang mengatur hubungan antar Model dan View, memproses permintaan dari pengguna lalu berinteraksi dengan Model dan mengubah View

* MVT

  MVT merupakan singkatan dari Model View Template. Model merupakan komponen yang mengatur segala data dan logika inti dari aplikasi atau web. View pada MVT bertindak mirip seperti controller, mengambil data dari model dan mengatur bagaimana data tersebut ditampilkan.
  Template merupakan representasi visual dari aplikasi atau web (visual yang terlihat oleh pengguna)

* MVVM

  MVVM merupakan singkatan dari Model View ViewModel. Model merupakan komponen yang mengatur data dan logika inti. View mengatur visual yang akan dilihat pengguna. Dan terakhir, ViewModel berguna untuk _data binding_ untuk menyinkornkan penyajian fungsi dan data ke
  View serta pembaruan Model.

* Perbedaan

MVC dan MVT mirip namun pada MVT, View memiliki tugas yang mirip dengan controller untuk mengatur pengambilan data dan pada MVT terdapat komponen Template untuk menampilkan visual ke pengguna. Sedangkan pada MVVM lebih berfokus pada _data binding_, ViewModel pada MVVM
mengambil data dari Model dan mengubahnya menjadi format yang lebih mudah untuk dibaca oleh View. MVC dan MVT umum digunakan untuk kebanyakan aplikasi atau web sedangkan pada MVVM digunakan untuk aplikasi dengan UI yang lebih kompleks.


## **BONUS**

Selain tes url dan template yang ada di Tutorial 1, saya menambahkan tes baru yaitu tes model untuk mengecek apakah model yang dibuat bekerja dengan baik atau tidak



# Tugas 3

1. Apa perbedaan antara form POST dan form GET dalam Django?

   Di dalam django, form POST dan form GET memiliki peran yang berbeda
   * Form GET digunakan untuk melakukan request terhadap database untuk meminta data tanpa mengubah isi/tidak ada efek samping. Cocok untuk pencarian, tampilan data, atau operasi baca.
   * Form POST digunakan untuk mengirim data ke database/server untuk diolah sehingga mengubah isi/memiliki efek. Cocok untuk operasi penambahan, pembaruan, penghapusan, atau operasi yang memerlukan pengiriman
     data yang kompleks.

2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

   HTML merupakan struktur utama dalap web development, digunakan untuk mengatur bagaimana data ditampilkan atau halaman ditampilkan. Sedangkan XML dan JSON digunakan untuk pertukaran data dengan server.
   JSON mudah untuk dibaca dan ditulis oleh manusia dan mudah untuk diurai dan dihasilkan oleh mesin. JSON memiliki sintaks yang lebih sederhana dibandingkan XML dan membutuhkan lebih sedikit teks untuk
   menggambarkan data yang sama. JSON digunakan juga untuk integrasi dengan Javascript. Sedangkan XML  mengkodekan dokumen dalam format yang bisa dibaca oleh manusia dan mesin. XML sering digunakan dalam
   aplikasi web untuk pertukaran data karena struktur hierarkinya yang jelas(tree)

3.  Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

    JSON lebih mudah digunakan serta lebih mudah dibaca daripada XML. Tidak perlu tag , atribut, skema, dan lain - lain. JSON juga kompatibel dengan javascript sehingga lebih terintegrasi pada banyak web. JSON
    juga mudah digunakan dengan bahasa lain sehingga lebih mudah untuk pertukaran data antar sistem

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
