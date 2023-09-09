![books](https://images.alphacoders.com/132/1326370.png)
# libshop
Singkatan dari Library Shop

Tugas 2 PBP 
**Hilmi Atha Putra (2206830050) - PBP B**
# [Link menuju LibShop](https://libshop.adaptable.app/main/)

Soal :
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

Jawab :
1. A. Untuk membuat projek Django yang baru diperlukan beberapa step di bawah
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


D. 
   
     
