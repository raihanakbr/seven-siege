# Tugas 2 PBP
Muhammad Raihan Akbar (2206827674) \
PBP-B \
Link Adaptable : https://seven-siege.adaptable.app/

## 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- [x] **Membuat sebuah proyek Django baru.**
    1. Membuat direktori `seven_siege` dan membuat *virtual environment* dengan perintah `python -m venv env`.
    2. Menginstall dependencies pada python *virtual environment* proyek ini, dependencies yang diinstall diantaranya:
    ```
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```
    3. Memulai proyek django bernama `seven_siege` dengan perintah `django-admin startproject seven_siege .`.
    4. Mengizinkan akses dari semua host dengan menambahkan `*` pada `ALLOWED_HOST` di `settings.py`.
    5. Mencoba run server dengan perintah `python manage.py runserver` pada port default di `8000` dan membuka `http://localhost:8000/` untuk melihat animasi roket.
    6. Membuat repositori git, menginisiasi git pada direktori utama `seven_siege` serta membuat berkas `.gitignore` untuk menentukan berkas-berkas yang tidak akan dimasukkan ke dalam versi kontrol Git. Selanjutnya dilakukan `add`, `commit`, dan `push` dari direktori repositori lokal.

- [x] **Membuat aplikasi dengan nama main pada proyek tersebut.**
    1. Membuat aplikasi `main` dengan menjalankan perintah
    ```
    python manage.py startapp main
    ```
    2. Mendaftarkan aplikasi main ke dalam proyek dengan menambahkan `'main'` pada list `INSTALLED_APPS`dalam berkas `settings.py`

- [x] **Melakukan *routing* pada proyek agar dapat menjalankan aplikasi main.**
    1. Menambahkan path baru pada `urls.py` proyek Seven Siege dan menambahkan kode berikut.
    ```
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```
- [x] **Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib.**
    1. Membuka berkas `models.py` pada direktori `main`.
    2. Menambahkan class Item dengan kode sebagai berikut.
    ```
    from django.db import models

    class Item(models.Model):
        name = models.CharField(max_length=255)
        date_added = models.DateField(auto_now_add=True)
        amount = models.IntegerField()
        price = models.IntegerField()
        category = models.TextField()
        description = models.TextField()
    ```
    3. Memastikan atribut wajib sudah terpenuhi dengan tipe yang sesuai dan menambahkan atribut tambahan
    4. Memigrasi model dengan perintah `python manage.py makemigrations` dan `python manage.py migrate`

- [x] **Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas.**
    1. Membuka berkas views.py pada berkas aplikasi `main` dan membuat function `show_main` yang akan mengatur permintaan HTTP dan mengembalikan tampilan yang sesuai sebagai berikut.
    ```
    from django.shortcuts import render

    def show_main(request):
        context = {
            'appl_name': 'Seven Siege',
            'name': 'Raihan Akbar',
            'class': 'PBP B'
        }

        return render(request, "main.html", context)
    ```
    2. Membuat direktori `templates` pada direktori `main` dan membuat berkas `main.html` sebagai template utama yang akan digunakan. Isinya akan menampilkan nama aplikasi, nama, dan kelas dengan kode sebagai berikut.
    ```
    <h1>{{ appl_name }} Page</h1>
    <h5>Name: </h5>
    <p>{{ name }}<p>
    <h5>Class: </h5>
    <p>{{ class }}<p>
    ```
- [x] **Membuat sebuah *routing* pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`.**
    1. Membuka berkas `urls.py` pada direktori proyek `seven_siege` dan menambakan URL *pattern* untuk mengarah ke `main` dengan kode sebagai berikut.
    ```
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('main/', include('main.urls')),
    ]
    ```
- [x] **Melakukan *deployment* ke Adaptable terhadap aplikasi yang sudah dibuat**
    1. Membuka [Adaptable](https://adaptable.io/) dan sign in menggunakan akun GitHub.
    2. Membuat App baru dengan menekan tombol `New App` serta menghubungkan dengan repositori `seven-siege` pada branch main
    3. Memilih `Python App Template` sebagai template dan `PostgreSQL` sebagai database.
    4. Memilih versi python sesuai *virtual environment* (3.10) dan menggunakan start command `python manage.py migrate && gunicorn seven_siege.wsgi`
    5. Mencentang bagian `HTTP Listener on PORT` dan memulai proses *deploy* aplikasi.

## 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![Bagan Django](https://cdn.discordapp.com/attachments/1054028087551078452/1151125519421681745/image.png)
1. User: URL Request dengan method HTTP, seperti mengakses halaman web atau mengirim data melalui formulir.
2. URLconfig (urls.py): Berkas ini mendefinisikan pola URL yang akan digunakan dalam aplikasi. Pola-pola ini mengarahkan permintaan user ke fungsi tampilan (views) yang sesuai.
3. Views (views.py): Fungsi tampilan mengelola permintaan yang masuk dari URL. Mereka dapat mengakses data dari database melalui models.py jika diperlukan, dan mereka juga bertanggung jawab untuk merender berkas HTML yang sesuai.
4. Models (models.py): Berkas ini mendefinisikan struktur database dan mengelola data yang disimpan dalam database. Fungsi tampilan (views) dapat berinteraksi dengan models.py untuk mengambil atau menyimpan data.
5. Database: berperan sebagai penyimpanan persisten untuk data yang digunakan oleh aplikasi.
6. Template (HTML): Berkas-berkas ini mengatur tampilan halaman web dan menerima data dari fungsi tampilan (views). Template engine Django digunakan untuk mengintegrasikan data ke dalam HTML.

## 3. Jelaskan mengapa kita menggunakan *virtual environment*? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan *virtual environment*
*virtual environment* adalah alat penting dalam pengembangan perangkat lunak yang digunakan untuk mengisolasi proyek-proyek Python yang berbeda. Ini memiliki beberapa tujuan penting:
1. Isolasi Proyek
*virtual environment* memungkinkan kita untuk membuat lingkungan yang terisolasi untuk setiap proyek Python yang berbeda. Ini berarti kita dapat menginstal paket dan dependensi yang diperlukan hanya untuk proyek tertentu tanpa memengaruhi instalasi Python global atau proyek lain.
2. Pengujian
Misalnya, jika kita ingin memindahkan aplikasi web Django dari 1.5 ke 1.9, kita dapat dengan mudah melakukannya dengan membuat *virtual environment* yang berbeda dan menginstal versi Django yang berbeda.
3. Mengelola Versi Python
Mengelola Versi Python: *virtual environment* juga memungkinkan kita untuk mengelola versi Python yang berbeda di berbagai proyek. Ini berguna jika kita perlu mengembangkan proyek yang berjalan di versi Python yang berbeda.
Meskipun demikian, kita masih bisa menjalankan proyek Django tanpa menggunakan *virtual environment*. Namun, hal ini mungkin akan menimbulkan masalah jika ada dependensi proyek yang berbeda dan memerlukan versi pustaka yang berbeda. Oleh karena itu, penggunaan *virtual environment* sangat disarankan untuk memastikan isolasi dan manajemen dependensi yang tepat.


## 4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
1. MVC (Model-View-Controller):
MVC adalah pola desain yang memisahkan aplikasi menjadi tiga komponen utama: Model, View, dan Controller. Model mewakili data aplikasi, View menampilkan data, dan Controller memperbarui View saat data berubah. Perbedaan utama dengan pola lain adalah penggunaan Controller sebagai pengendali antara Model dan View. MVC memisahkan perubahan data dari tampilan dan memungkinkan aplikasi untuk lebih mudah dikembangkan dan dikelola.

2. MVT (Model-View-Template):
MVT adalah variasi dari MVC yang digunakan dalam kerangka kerja Django. Dalam MVT, Template menggantikan Controller. Template adalah bagian yang menangani bagian presentasi dalam arsitektur MVT. Perbedaan utama MVT dengan MVC adalah penggunaan Template yang memisahkan kode HTML dari logika tampilan, sementara MVC biasanya menggunakan View untuk mengelola tampilan.

3. MVVM (Model-View-ViewModel):
MVVM adalah pola desain yang memisahkan pengembangan antarmuka pengguna (GUI) dari pengembangan logika bisnis atau back-end. Dalam MVVM, ViewModel bertindak sebagai penghubung antara Model dan View. Perbedaan utama MVVM adalah penggunaan ViewModel yang mengelola komunikasi antara Model dan View. Ini memungkinkan pengembang untuk lebih terfokus pada logika tampilan tanpa perlu menggabungkan banyak kode bisnis di dalam View.