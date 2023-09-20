\
**Muhammad Raihan Akbar (2206827674)** \
**PBP-B** \
![elaina](https://media.discordapp.net/attachments/874575252808667149/1153856416126353448/elaina.gif?width=200&height=200)

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