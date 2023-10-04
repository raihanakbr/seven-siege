**Muhammad Raihan Akbar (2206827674)** \
**PBP-B** \
![elaina](https://media.discordapp.net/attachments/874575252808667149/1153856416126353448/elaina.gif?width=200&height=200)

# Tugas 5 PBP

## 1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.

1. **Selektor Tag:** Selektor ini memilih elemen berdasarkan nama tag. Misalnya, p `{ color: red; }` akan memilih semua elemen `<p>` dan mengatur warna teksnya menjadi merah. Selektor tag sangat berguna saat ingin menerapkan gaya yang sama ke semua elemen dengan tag tertentu.

2. **Selektor Class:** Selektor ini memilih elemen berdasarkan nama class yang diberikan. Misalnya, `.blue { color: white; background: blue; padding: 5px; }` akan memilih semua elemen dengan class `blue` dan menerapkan gaya tersebut. Selektor class sangat berguna untuk menerapkan gaya yang sama ke sekelompok elemen yang memiliki class yang sama.

2. **Selektor ID:** Selektor ini hampir sama dengan class, tetapi ID bersifat unik dan hanya boleh digunakan oleh satu elemen saja. Misalnya, `#header { background: teal; color: white; height: 100px; padding: 50px; }` akan memilih elemen dengan id `header` dan menerapkan gaya tersebut1. Selektor ID sangat berguna untuk menerapkan gaya khusus ke satu elemen tertentu.

3. **Selektor Atribut:** Selektor ini memilih elemen berdasarkan atribut1. Misalnya, `input[type=text] { background: none; color: cyan; padding: 10px; border: 2px solid cyan; }` akan memilih semua elemen `<input>` yang memiliki atribut `type=‘text’` dan menerapkan gaya tersebut. Selektor atribut sangat berguna untuk menerapkan gaya khusus ke elemen dengan atribut tertentu.

4. **Selektor Universal:** Selektor ini digunakan untuk menyeleksi semua elemen pada jangkauan *(scope)* tertentu. Misalnya, `{ border: 2px solid grey; }` akan memberikan garis solid dengan ukuran `2px` dan berwarna grey ke semua elemen. Selektor universal biasanya digunakan untuk me-reset CSS.

## 2. Jelaskan HTML5 Tag yang kamu ketahui.

- `<!DOCTYPE>`: Mendefinisikan tipe dokumen dan versi HTML.
- `<html>`: Mendefinisikan akar dari dokumen HTML.
- `<head>`: Mengandung metadata/informasi untuk dokumen.
- `<title>`: Mendefinisikan judul untuk dokumen.
- `<body>`: Mendefinisikan badan dokumen.
- `<h1>` sampai `<h6>`: Mendefinisikan judul HTML.
- `<p>`: Mendefinisikan paragraf.
- `<br>`: Mendefinisikan jeda baris tunggal.
- `<a>`: Mendefinisikan *hyperlink*.
- `<img>`: Digunakan untuk menyisipkan gambar.
- `<div>`: Mendefinisikan bagian dalam dokumen.
- `<span>`: Digunakan untuk mengelompokkan elemen inline dalam dokumen.
- `<ul>`, `<ol>`, dan `<li>`: Digunakan untuk membuat daftar.
- `<table>`, `<tr>`, `<td>`, dan `<th>`: Digunakan untuk membuat tabel.
- `<form>`, `<input>`, `<textarea>`, `<button>`, dll.: Digunakan untuk membuat form.
- `<header>` dan `<footer>`: Mendefinisikan header dan footer dari dokumen atau bagian
- `<nav>`: Digunakan untuk mendefinisikan navigasi link

## 3. Jelaskan perbedaan antara *margin* dan *padding*.

1. **Margin:**
    -  Margin adalah ruang di luar batas luar elemen HTML. Ini adalah jarak antara elemen HTML dan elemen-elemen lain yang berada di sekitarnya.
    - Margin digunakan untuk mengendalikan jarak antara elemen HTML dengan elemen-elemen lain yang ada di sekitarnya, seperti elemen tetangga atau batas dari elemen yang berbeda.
    - Margin tidak memiliki latar belakang atau warna, dan tidak dapat digunakan untuk mengatur tampilan elemen HTML itu sendiri.

2. **Padding:**
    - Padding adalah ruang di dalam batas luar elemen HTML. Ini adalah jarak antara batas elemen HTML dan kontennya sendiri.
    - Padding digunakan untuk mengendalikan jarak antara konten elemen HTML dan batasnya sendiri. Ini memengaruhi tampilan elemen HTML itu sendiri.
    - Padding dapat memiliki latar belakang atau warna yang berbeda dari elemen HTML, sehingga dapat digunakan untuk mengatur tampilan elemen, misalnya, memberikan ruang di sekitar teks dalam sebuah kotak.

## 4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?

| Tailwind | Bootstrap |
| -------- | --------- |
| Tailwind CSS membangun tampilan dengan menggabungkan kelas-kelas utilitas yang telah didefinisikan sebelumnya.     | Bootstrap menggunakan gaya dan komponen yang telah didefinisikan, yang memiliki tampilan yang sudah jadi dan dapat digunakan secara langsung.      |
| Tailwind CSS memiliki *file* CSS yang lebih kecil sedikit dibandingkan Bootstrap dan hanya akan memuat kelas-kelas utilitas yang ada | Bootstrap memiliki *file* CSS yang lebih besar dibandingkan dengan Tailwind CSS karena termasuk banyak komponen yang telah didefinisikan. |
| Tailwind CSS memiliki memberikan fleksibilitas dan adaptabilitas tinggi terhadap proyek | Bootstrap sering kali menghasilkan tampilan yang lebih konsisten di seluruh proyek karena menggunakan komponen yang telah didefinisikan. |
| Tailwind CSS memiliki pembelajaran yang lebih curam karena memerlukan pemahaman terhadap kelas-kelas utilitas yang tersedia dan bagaimana menggabungkannya untuk mencapai tampilan yang diinginkan. | Bootstrap memiliki pembelajaran yang lebih cepat untuk pemula karena dapat mulai dengan komponen yang telah didefinisikan. |

Pilihan antara Bootstrap dan Tailwind tergantung pada kebutuhan proyek, preferensi desain, dan tingkat fleksibilitas yang diinginkan:

- Gunakan Bootstrap jika: Anda membutuhkan kerangka kerja yang stabil dan mudah digunakan untuk proyek dengan desain tradisional. Bootstrap juga bagus untuk situs web responsif cepat.
- Gunakan Tailwind jika: Anda ingin memiliki kendali penuh atas gaya dan tata letak dengan kombinasi class utilitas yang spesifik. Tailwind lebih baik untuk desain khusus.

Baik Bootstrap maupun Tailwind memiliki ekosistem pengembangan yang kuat, sehingga kita dapat dengan mudah menemukan sumber daya dan dukungan yang diperlukan dalam proses pengembangan.

## 5. Implementasi Checklist

1. Menambahkan Bootstrap pada Aplikasi dengan membuka `base.html` pada `templates` dan menambahkan kode sebagai berikut.
    ```html
        <head>
            ...
            {% endblock meta %}
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
            <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha384-KyZXEAg3QhqLMpG8r+J4jsl5c9zdLKaUk5Ae5f5b1bw6AUn5f5v8FZJoMxm6f5cH1" crossorigin="anonymous"></script>
            <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js" integrity="sha384-BBtl+eGJRgqQAUMxJ7pMwbEyER4l1g+O15P+16Ep7Q9Q+zqX6gSbd85u4mG4QzX+" crossorigin="anonymous"></script>
        </head>
    ```
2. Menbamahkan `navbar` pada halaman `main` dan `create_item` sebagai berikut.
    ```html
    {% extends 'base.html' %}

    {% block content %}
    <nav class="navbar navbar-expand-lg bg-dark">
        <div class="container-fluid">
        <a class="navbar-brand text-white" href="#">Seven Siege</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
            <div class="navbar-nav">
            <a class="nav-link active text-white" aria-current="page" href="/">Home</a>
            <a class="nav-link text-white" href="{% url 'main:logout' %}">Logout</a>
            </div>
        </div>
        </div>
    </nav>
    ...
    ```
3. Membuka `main.html` dan membuat `div` dengan class `cards` untuk menampung semua item dan menaruhnya pada `container` sebagai berikut.
    ```html
    <div class="container mt-5">
        <h1 class="text-black">{{ appl_name }} Page</h1>
        <h5 class="text-black">Name:</h5>
        <p class="text-black">{{name}}</p>
        <h5 class="text-black">Class:</h5>
        <p class="text-black">{{class}}</p>
        <h4 class="text-black">Jumlah Item</h4>
        <p class="text-black">Kamu menyimpan {{ item_count }} item pada applikasi ini</p>

        <div class="card-group">
            {% for item in items %}
            <div class="card bg-secondary text-white{% if forloop.last %} last-card{% endif %}">
                <!-- <img src="..." class="card-img-top" alt="..."> -->
                <div class="card-body">
                    <h5 class="card-title">{{ item.name }}</h5>
                    <p class="card-text">Amount: {{ item.amount }}</p>
                    <p class="card-text">Price: {{ item.price }}</p>
                    <p class="card-text">Category: {{ item.category }}</p>
                    <p class="card-text">Description: {{ item.description }}</p>
                    <p class="card-text">Date Added: {{ item.date_added }}</p>
                    <div class="d-flex">
                        <form action="{% url 'main:add_amount' item.id %}" method="post">
                            {% csrf_token %}
                            <button type="submit" class="btn btn-primary me-2" name="Increment">+</button>
                        </form>
                        <form action="{% url 'main:subtract_amount' item.id %}" method="post">
                            {% csrf_token %}
                            <button type="submit" class="btn btn-primary me-2" name="Decrement">-</button>
                        </form>
                        <form action="{% url 'main:remove_item' item.id %}" method="post">
                            {% csrf_token %}
                            <button type="submit" class="btn btn-danger" name="Remove">X</button>
                        </form>
                    </div>                               
                </div>
            </div>
            {% endfor %}
        </div>
        
        <br />
        
        <a href="{% url 'main:create_item' %}" class="btn btn-success">Add New Item</a>
        <h5 class="text-white">Sesi terakhir login: {{ last_login }}</h5>    
    </div>
    ```

4. Membuat `login page` lebih rapi dengan membuat elemen-elemen yang ada menjadi di tengah dan menambahkan *margin* sebagai berikut.
    ```html
    {% block content %}

    <div class="container d-flex justify-content-center align-items-center" style="min-height: 100vh;">
        <div class="login">
            <h1>Login</h1>

            <form method="POST" action="">
                {% csrf_token %}
                <div class="mb-3">
                    <label for="username" class="form-label">Username:</label>
                    <input type="text" name="username" id="username" class="form-control" placeholder="Username">
                </div>

                <div class="mb-3">
                    <label for="password" class="form-label">Password:</label>
                    <input type="password" name="password" id="password" class="form-control" placeholder="Password">
                </div>

                <div class="text-center">
                    <input class="btn btn-primary" type="submit" value="Login">
                </div>
            </form>

            <p class="mt-3">Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a></p>
        </div>
    </div>

    {% endblock content %}
    ```

5. Mendesain halaman `create_item.html` dengan menambahkan *container* dan memberikan warna sebagai berikut.
    ```html
    <div class="container mt-5">

        <div class="card bg-dark text-white">
            <div class="card-header">
                <h1 class="card-title">Add New Item</h1>
            </div>
            <div class="card-body">
                <form method="POST">
                    {% csrf_token %}
                    <div class="mb-3">
                        <div class="card bg-secondary">
                            <div class="card-body">
                                {{ form.name.label_tag }}
                                {{ form.name }}
                            </div>
                        </div>
                    </div>
                    <div class="mb-3">
                        <div class="card bg-secondary">
                            <div class="card-body">
                                {{ form.amount.label_tag }}
                                {{ form.amount }}
                            </div>
                        </div>
                    </div>
                    <div class="mb-3">
                        <div class="card bg-secondary">
                            <div class="card-body">
                                {{ form.price.label_tag }}
                                {{ form.price }}
                            </div>
                        </div>
                    </div>
                    <div class="mb-3">
                        <div class="card bg-secondary">
                            <div class="card-body">
                                {{ form.category.label_tag }}
                                {{ form.category }}
                            </div>
                        </div>
                    </div>
                    <div class="mb-3">
                        <div class="card bg-secondary">
                            <div class="card-body">
                                {{ form.description.label_tag }}
                                {{ form.description }}
                            </div>
                        </div>
                    </div>
                    <div class="text-center">
                        <button type="submit" class="btn btn-success">Add Item</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
    ```

# Tugas 4 PBP

## 1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
UserCreationForm adalah impor formulir bawaan yang memudahkan pembuatan formulir pendaftaran pengguna dalam aplikasi web. Dengan formulir ini, pengguna baru dapat mendaftar dengan mudah di situs web Anda tanpa harus menulis kode dari awal.

- **Kelebihan:**
    - Mudah Digunakan: UserCreationForm sudah terintegrasi dengan baik dengan Django, sehingga memudahkan pengembang dalam membuat fitur pendaftaran pengguna tanpa harus menulis kode formulir dari awal.

    - Validasi Otomatis: Formulir ini menyertakan validasi otomatis untuk memastikan bahwa data yang dimasukkan oleh pengguna sesuai dengan aturan yang ditentukan, seperti panjang minimal kata sandi, kecocokan antara kata sandi dan konfirmasi kata sandi, dan lainnya.

    - Integrasi dengan Authentication System: UserCreationForm bekerja secara langsung dengan sistem otentikasi yang sudah ada di Django, sehingga memungkinkan pengguna untuk dengan mudah masuk ke dalam aplikasi setelah mendaftar.

    - Dukungan untuk Customisasi: Meskipun UserCreationForm mencakup bidang yang umum digunakan seperti username dan password, Anda dapat dengan mudah menyesuaikannya dengan kebutuhan aplikasi Anda dengan menambahkan atau menghapus bidang atau dengan mengganti perilaku validasi.

- **Kekurangan:**
    - Terbatas dalam Fungsionalitas: UserCreationForm hanya menyediakan formulir dasar untuk pendaftaran pengguna. Jika Anda memerlukan informasi tambahan seperti alamat email, nama lengkap, atau data profil tambahan, Anda perlu menyesuaikan atau memperluas formulir ini atau membuat formulir kustom sendiri.

    - Tidak Mendukung Fitur Tambahan: Jika aplikasi Anda memerlukan fitur-fitur khusus seperti pendaftaran dengan akun media sosial atau otentikasi dua faktor, Anda perlu menambahkan fungsionalitas ini secara manual.

    - Tampilan Bawaan Mungkin Tidak Sesuai: Tampilan bawaan dari UserCreationForm mungkin tidak sesuai sepenuhnya dengan desain atau tampilan aplikasi Anda, sehingga Anda perlu menyesuaikannya dengan gaya UI Anda.

    - Keamanan: Meskipun UserCreationForm memberikan validasi otomatis, Anda tetap perlu memastikan keamanan aplikasi Anda dengan melakukan langkah-langkah tambahan seperti melindungi terhadap serangan brute force dan memastikan kata sandi yang aman.

## 2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

- **Autentikasi**
adalah proses verifikasi identitas pengguna. Dalam konteks Django, ini biasanya melibatkan pengguna yang memasukkan nama pengguna dan kata sandi, yang kemudian dibandingkan dengan data yang disimpan dalam database. Jika data cocok, pengguna dianggap autentik.
Contoh sederhananya, misal ada A sebagai pengirim dokumen elektronik ke si B di internet. Kemudian pada kasus ini sistem berperan tentang bagaimana mengidentifikasi bahwa pengirim A telah mengirim pesan ke penerima B.

- **Otorisasi**
adalah proses penentuan apa yang dapat diakses oleh pengguna setelah mereka diautentikasi. Dalam Django, ini biasanya melibatkan pengecekan terhadap peran atau hak akses pengguna untuk menentukan apakah mereka memiliki izin untuk melakukan tindakan tertentu (misalnya, melihat halaman tertentu atau mengubah data tertentu)
Contoh sederhananya adalah pengguna A ingin mengakses file tertentu pada server.

Kedua proses ini penting karena mereka membantu menjaga keamanan aplikasi. Autentikasi membantu mencegah akses yang tidak sah dengan memastikan bahwa hanya pengguna yang memiliki kredensial yang valid yang dapat masuk. Sementara itu, otorisasi membantu mencegah penyalahgunaan akses dengan membatasi apa yang dapat dilakukan pengguna setelah mereka masuk.

## 3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
Cookies dalam konteks aplikasi web adalah file teks berukuran kecil yang diletakkan di komputer pengguna oleh server web ketika pengguna mengunjungi situs web.  Cookies biasanya digunakan untuk menyimpan informasi yang berkaitan dengan sesi pengguna atau preferensi pengguna, sehingga aplikasi web dapat mengenali pengguna yang sudah login atau mengingat preferensi pengguna pada kunjungan berikutnya.

Berikut adalah beberapa cara Django menggunakan cookies:

- **Menyimpan Informasi Login:** Cookies dapat digunakan untuk menyimpan informasi login pengguna, sehingga pengguna tidak perlu memasukkan kembali nama pengguna dan kata sandi mereka setiap kali mereka mengunjungi situs.

- **Menyimpan Pengaturan Situs Web:** Cookies juga dapat digunakan untuk menyimpan preferensi dan pengaturan situs web pengguna. Misalnya, jika pengguna memilih bahasa tertentu pada situs web, cookies dapat “mengingat” pilihan ini dan secara otomatis menampilkan konten dalam bahasa yang dipilih saat pengguna kembali ke situs.

- **Menyediakan Konten yang Lebih Personal:** Dengan menggunakan cookies, Django dapat menyediakan konten yang lebih personal kepada pengguna. Misalnya, jika pengguna sering mencari produk tertentu di situs e-commerce, cookies dapat “mengingat” preferensi ini dan menampilkan produk serupa saat pengguna kembali ke situs.

## 4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Penggunaan cookies dalam pengembangan web bisa menjadi alat yang aman jika diimplementasikan dengan benar, tetapi juga bisa memiliki risiko potensial jika tidak diwaspadai. Berikut adalah beberapa risiko potensial yang harus diperhatikan saat menggunakan cookies dalam aplikasi web:

- **Cross-Site Scripting (XSS):** Serangan XSS digunakan untuk mencuri cookie, penyebaran malware session hijacking / pembajakan session, dan pembelokkan tujuan / malicious redirects
- **Cross-Site Request Forgery (CSRF):** CSRF adalah serangan eksploitasi web yang membuat pengguna tanpa sadar mengirim sebuah permintaan atau request ke website melalui website yang sedang digunakan saat itu
- **Cookie Theft:** Cookie theft atau pencurian cookie adalah risiko lainnya. Jika penyerang dapat mengakses cookie pengguna, mereka dapat mencuri informasi sensitif atau bahkan mengambil alih sesi pengguna
- **Insecure Transmission:** Cookies dikirimkan antara perangkat pengguna dan server dalam teks terbuka, jika tidak dienkripsi. Jika cookies mengandung informasi sensitif, seperti kata sandi, maka ada risiko intercept cookies dalam serangan Man-in-the-Middle (MITM).
- **Cookie Sniffing:** Penyerang yang memiliki akses fisik atau akses ke jaringan dapat mencoba untuk mencuri cookies dengan teknik seperti packet sniffing.

Untuk mengatasi risiko-risiko ini, kita harus mengambil langkah-langkah keamanan tertentu dalam pengembangan web.

## 5. Checklist Tugas
- [x]  Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
    1. Membuat fungsi `register` dengan formulir registrasi secara otomatis dan menghasilkan akun pengguna ketika data di-submit dari form sebagai berikut, fungsi `login_user` untuk melakukan autentikasi dan login jika autentikasi berhasil, dan `logout_user` untuk menghapus sesi pengguna yang saat ini masuk dan mengarahkan pengguna ke halaman login dalam aplikasi Django. Serta mengimpor module yang diperlukan sebagai berikut.

        ```py
        from django.shortcuts import redirect
        from django.contrib.auth.forms import UserCreationForm
        from django.contrib import messages  
        from django.contrib.auth import authenticate, login, logout
        ...

        ...
        def register(request):
        form = UserCreationForm()

        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your account has been successfully created!')
                return redirect('main:login')
        context = {'form':form}
        return render(request, 'register.html', context)

        def login_user(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main:show_main')
            else:
                messages.info(request, 'Sorry, incorrect username or password. Please try again.')
        context = {}
        return render(request, 'login.html', context)

        def logout_user(request):
            logout(request)
            return redirect('main:login')
        ```

    2. Membuat berkas HTML baru yaitu `register.html` dan `login.html` pada folder `main/templates` untuk halaman register dan login sebagai berikut

        - `register.html`
        ```
        html
        {% extends 'base.html' %}

        {% block meta %}
            <title>Register</title>
        {% endblock meta %}

        {% block content %}  

        <div class = "login">
            
            <h1>Register</h1>  

                <form method="POST" >  
                    {% csrf_token %}  
                    <table>  
                        {{ form.as_table }}  
                        <tr>  
                            <td></td>
                            <td><input type="submit" name="submit" value="Daftar"/></td>  
                        </tr>  
                    </table>  
                </form>

            {% if messages %}  
                <ul>   
                    {% for message in messages %}  
                        <li>{{ message }}</li>  
                        {% endfor %}  
                </ul>   
            {% endif %}

        </div>  

        {% endblock content %}
        ```

        - `login.html`
        ```
        html
        {% extends 'base.html' %}

        {% block meta %}
            <title>Login</title>
        {% endblock meta %}

        {% block content %}

        <div class = "login">

            <h1>Login</h1>

            <form method="POST" action="">
                {% csrf_token %}
                <table>
                    <tr>
                        <td>Username: </td>
                        <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
                    </tr>
                            
                    <tr>
                        <td>Password: </td>
                        <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
                    </tr>

                    <tr>
                        <td></td>
                        <td><input class="btn login_btn" type="submit" value="Login"></td>
                    </tr>
                </table>
            </form>

            {% if messages %}
                <ul>
                    {% for message in messages %}
                        <li>{{ message }}</li>
                    {% endfor %}
                </ul>
            {% endif %}     
                
            Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

        </div>

        {% endblock content %}
        ```

    3. Membuka `urls.py` dan mengimpor fungsi-fungsi yang sudah dibuat sebelumnya dari `views.py` sebagai berikut

        ```py
        from main.views import register, login_user, logout_user
        ```
    
    4. Menambahkan fungsi-fungsi tersebut ke dalam `urlpatterns` sebagai berikut

        ```py
        path('register/', register, name='register'),
        path('login/', login_user, name='login'),
        path('logout/', logout_user, name='logout'),
        ```

- [x] Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.

    - **First Account**
    ![a1](https://media.discordapp.net/attachments/1054028087551078452/1155862907050008667/image.png?width=1040&height=585)
    - **Second Account**
    ![a2](https://media.discordapp.net/attachments/1054028087551078452/1155863279323840582/image.png?width=1040&height=585)

- [x] Menghubungkan model `Item` dengan `User`
    1. Membuka `models.py` dan menambahkan atribut user pada class `Item` di mana atribut tersebut menghubungkan satu produk dengan satu user melalui sebuah relationship, dimana sebuah produk pasti terasosiasikan dengan seorang user.

    ```py
    from django.contrib.auth.models import User
    ...

    ...
    class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ```

    2. Melakukan migaasi dengan `python manage.py makemigrations`.

- [x] Menampilkan detail informasi pengguna yang sedang *logged in*

    1. Mengimpor `datetime` dan lainnya untuk menyimpan waktu saat *user* *log in* sebagai berikut
        ```py
        import datetime
        from django.http import HttpResponseRedirect
        from django.urls import reverse
        ```

    2. Mengubah fungsi `login_user` sehingga kita bisa tahu kapan terakhir kali pengguna login
        ```py
        ...
        if user is not None:
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main")) 
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
        ...
        ```

    3. Menambahkan potongan kode `'last_login': request.COOKIES['last_login']` ke dalam context untuk menambahkan informasi *cookie last_login* yang akan ditampilkan pada halaman `main` sebagai berikut
        ```py
        context = {
            'appl_name': 'Seven Siege',
            'name': request.user.username,
            'class': 'PBP B',
            'items': items,
            'item_count': item_count,
            'last_login': request.COOKIES['last_login'],
        }
        ```

    4. Mengubah fungsi `logout_user` sehingga *cookie* *last_login* terhapus saat `logout`
        ```py
        def logout_user(request):
            logout(request)
            response = HttpResponseRedirect(reverse('main:login'))
            response.delete_cookie('last_login')
            return response
        ```

    5. Menampilkan last_login pada `main.html` sebagai berikut
        ```html
        ...
        <h5>Sesi terakhir login: {{ last_login }}</h5>
        ...
        ```

# Tugas 3 PBP

## 1. Apa perbedaan antara form POST dan form GET dalam Django?
- **Pengiriman Data:**
Method POST akan mengirimkan data atau nilai langsung ke action untuk ditampung, tanpa menampilkan pada URL. Sedangkan method GET akan menampilkan data/nilai pada URL, kemudian akan ditampung oleh action.
- **Batasan Data:**
Method POST data yang dikirim tidak terbatas. Sedangkan method GET tidak boleh lebih dari 2047 karakter.
- **Penggunaan:**
Form POST biasanya digunakan untuk mengirimkan data yang akan mengubah state di server, seperti membuat atau memperbarui data. Form GET biasanya digunakan untuk meminta data dari server tanpa mengubah state di server.
- **Keamanan:**
Karena form POST tidak menampilkan data pada URL, metode ini lebih aman untuk mengirimkan data sensitif seperti password

## 2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
- **XML (eXtensible Markup Language)**: XML digunakan untuk menyusun dan mengirimkan data terstruktur, serta mendefinisikan aturan sendiri untuk markup data. XML menggunakan struktur pohon dalam membentuk datanya dengan menggunakan tag dan atribut. Ini membuatnya cocok untuk merepresentasikan data terstruktur, seperti data dalam dokumen konfigurasi atau pertukaran data antara aplikasi yang berbeda.

- **JSON (JavaScript Object Notation):** Ini adalah format pertukaran data terbuka yang dapat dibaca baik oleh manusia maupun mesin. JSON menggunakan struktur data yang mirip dengan objek-objek JavaScript. Data disimpan dalam bentuk pasangan *key*-*value*, yang bisa menjadi array atau *nested objects*. JSON biasanya digunakan dalam aplikasi web dan mobile untuk mengirim data dari server ke client.

- **HTML (HyperText Markup Language):** Berbeda dengan JSON dan XML, HTML lebih difokuskan pada penyajian data daripada transfer data. HTML didorong oleh format dan digunakan untuk membuat struktur dan tampilan halaman web.

## 3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
- **Keterbacaan:** JSON dapat dengan mudah dibaca oleh manusia dan mesin. Formatnya sederhana dan intuitif, yang memudahkan pengembang dalam memahami dan memanipulasi data.

- **Ringan:** JSON memiliki ukuran yang lebih kecil dibandingkan dengan XML, sehingga mengurangi beban jaringan dan waktu transfer data.

- **Kemudahan:** JSON bersifat independen dari bahasa pemrograman tertentu, sehingga dapat digunakan di berbagai platform dan teknologi.

- **Kompatibilitas:** JSON didukung oleh hampir semua browser dan sebagian besar teknologi backend, membuatnya menjadi format yang ideal untuk pertukaran data antara aplikasi web modern.

- **Pemrosesan:** JSON mudah diproses menggunakan JavaScript, yang merupakan bahasa pemrograman yang umum digunakan dalam pengembangan aplikasi web.

- **API:** JSON adalah format umum yang digunakan dalam API (Application Programming Interface) untuk pertukaran data antara aplikasi. Banyak layanan web modern menyediakan API dengan output JSON.

- **Fleksibilitas:** JSON mendukung struktur data yang kompleks dan dapat dengan mudah diperluas untuk memenuhi kebutuhan pengembangan aplikasi web.

## 4. Implementasi Checklist
- [x] **Membuat input form untuk menambahkan objek model pada app sebelumnya.**
    1. Membuat berkas `forms.py` pada direktori `main` untuk membuat struktur *form* yang dapat menerima data item baru dengan kode berikut
    ```py
    from django.forms import ModelForm
    from main.models import Item

    class ItemForm(ModelForm):
        class Meta:
            model = Item
            fields = ["name", "amount", "price", "category", "description"]
    ```
    2. Membuat fungsi `create_item` pada `views.py` pada folder `main` untuk menambahkan data ketika data di-*submit* dari form.
    ```py
    from django.http import HttpResponseRedirect
    from main.forms import ProductForm
    from django.urls import reverse

    def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)
    ```
    3. Menambahkan semua `object` `Item` yang tersimpan dalam`database` pada context dalam fungsi `show_main` pada berkas `views.py `
    ```py
    def show_main(request):

    items = Item.objects.all()

    context = {
        'appl_name': 'Seven Siege',
        'name': 'Muhammad Raihan Akbar',
        'class': 'PBP B',
        'items': items,
        'item_count': item_count,
    }

    return render(request, "main.html", context)
    ```
    4. Menambahkan *path url* ke dalam `urlpatterns` pada `urls.py` di `main`
    ```py
    from main.views import show_main, create_item
    path('create-item', create_item, name='create_item'),
    ```
    5. Membuat berkas HTML baru dengan nama `create_item.html` pada direktori `main/templates` dengan menggunakan *form* metode POST sebagai berikut.
    ```html
    {% extends 'base.html' %} 

    {% block content %}
    <h1>Add New Item</h1>

    <form method="POST">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td>
                    <input type="submit" value="Add Item"/>
                </td>
            </tr>
        </table>
    </form>

    {% endblock %}
    ```
    6. Menambahkan `{% block content %}` dalam `main.html` untuk menampilkan data produk dalam bentuk *table* dan *button* untuk *redirect* ke halaman *form*
    ```html
            <table>
            <tr>
                <th>Name</th>
                <th>Amount</th>
                <th>Price</th>
                <th>Category</th>
                <th>Description</th>
                <th>Date Added</th>
            </tr>
        
            {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}
        
            {% for item in items %}
                <tr>
                    <td>{{item.name}}</td>
                    <td>{{item.amount}}</td>
                    <td>{{item.price}}</td>
                    <td>{{item.category}}</td>
                    <td>{{item.description}}</td>
                    <td>{{item.date_added}}</td>
                </tr>
            {% endfor %}
        </table>
        
        <br />
        
        <a href="{% url 'main:create_item' %}">
            <button>
                Add New Item
            </button>
        </a>    
    {% endblock content %}
    ``` 
- [x] **Menambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.**
    1. Membuka `views.py` yang ada dalam folder `main` dan menambahkan import `HttpResponse` dan `Serializer` sebagai berikut
    ```py
    from django.http import HttpResponse
    from django.core import serializers
    ```
    2. Membuat 5 views untuk melihat objek dalam format berbeda-beda
    ```py
    def show_html(request):
        data = Item.objects.all().values()
        return HttpResponse(data)

    def show_xml(request):
        data = Item.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json(request):
        data = Item.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")

    def show_xml_by_id(request, id):
        data = Item.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json_by_id(request, id):
        data = Item.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```
    Fungsi `show_html` tidak menggunakan *serializer* karena mengirimkan data tanpa mengubah formatnya, sementara `show_xml` dan `show_json` menggunakan *serializer* untuk mengonversi data ke dalam format yang lebih terstruktur dan standar (XML atau JSON) untuk memudahkan pengolahan dan pertukaran data.
    
    3. Membuka `urls.py` dan Mengimpor fungsi yang sudah dibuat
    ```py
    from main.views import show_main, create_item, show_html, show_xml, show_json, show_xml_by_id, show_json_by_id
    ```
    4. Menambahkan *path url* ke dalam `urlpatterns` untuk mengakses fungsi-fungsi tersebut.
    ```py
    ...
    path('html/', show_html, name='show_html'), 
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    ...
    ```

## 5. Screenshot hasil akses URL pada Postman
- **HTML**
![HTML](https://media.discordapp.net/attachments/1054028087551078452/1153688921176297533/image.png?width=1040&height=585)
- **XML**
![XML](https://media.discordapp.net/attachments/1054028087551078452/1153854506765914132/Screenshot_40.png?width=1040&height=585)
- **JSON**
![JSON](https://media.discordapp.net/attachments/1054028087551078452/1153854507076288604/Screenshot_41.png?width=1040&height=585)
- **XML by ID**
![XML/ID](https://media.discordapp.net/attachments/1054028087551078452/1153854506048688218/Screenshot_38.png?width=1040&height=585)
- **JSON by ID**
![JSON/ID](https://media.discordapp.net/attachments/1054028087551078452/1153854506442965012/Screenshot_39.png?width=1040&height=585)

# Tugas 2 PBP

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
    ```py
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
    ```py
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
    ```py
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
    ```html
    <h1>{{ appl_name }} Page</h1>
    <h5>Name: </h5>
    <p>{{ name }}<p>
    <h5>Class: </h5>
    <p>{{ class }}<p>
    ```
- [x] **Membuat sebuah *routing* pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`.**
    1. Membuka berkas `urls.py` pada direktori proyek `seven_siege` dan menambakan URL *pattern* untuk mengarah ke `main` dengan kode sebagai berikut.
    ```py
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

*virtual environment* juga memungkinkan kita untuk mengelola versi Python yang berbeda di berbagai proyek. Ini berguna jika kita perlu mengembangkan proyek yang berjalan di versi Python yang berbeda.

Meskipun demikian, kita masih bisa menjalankan proyek Django tanpa menggunakan *virtual environment*. Namun, hal ini mungkin akan menimbulkan masalah jika ada dependensi proyek yang berbeda dan memerlukan versi pustaka yang berbeda. Oleh karena itu, penggunaan *virtual environment* sangat disarankan untuk memastikan isolasi dan manajemen dependensi yang tepat.


## 4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
1. MVC (Model-View-Controller):

MVC adalah pola desain yang memisahkan aplikasi menjadi tiga komponen utama: Model, View, dan Controller. Model mewakili data aplikasi, View menampilkan data, dan Controller memperbarui View saat data berubah. Perbedaan utama dengan pola lain adalah penggunaan Controller sebagai pengendali antara Model dan View. MVC memisahkan perubahan data dari tampilan dan memungkinkan aplikasi untuk lebih mudah dikembangkan dan dikelola.

2. MVT (Model-View-Template):

MVT adalah variasi dari MVC yang digunakan dalam kerangka kerja Django. Dalam MVT, Template menggantikan Controller. Template adalah bagian yang menangani bagian presentasi dalam arsitektur MVT. Perbedaan utama MVT dengan MVC adalah penggunaan Template yang memisahkan kode HTML dari logika tampilan, sementara MVC biasanya menggunakan View untuk mengelola tampilan.

3. MVVM (Model-View-ViewModel):

MVVM adalah pola desain yang memisahkan pengembangan antarmuka pengguna (GUI) dari pengembangan logika bisnis atau back-end. Dalam MVVM, ViewModel bertindak sebagai penghubung antara Model dan View. Perbedaan utama MVVM adalah penggunaan ViewModel yang mengelola komunikasi antara Model dan View. Ini memungkinkan pengembang untuk lebih terfokus pada logika tampilan tanpa perlu menggabungkan banyak kode bisnis di dalam View.