# Tugas 2 PBP : Aci Rezeki Shop

Web application : [Aci Rezeki Shop](https://aci-rezeki-shop.adaptable.app/main/)

## Daftar Isi

-   Tugas 3

-   Tugas 2
    -   [Implementasi Step-by-Step](#implementasi-step-by-step-tugas-2)
    -   [Cara Kerja Implementasi Konsep MTV pada Django](#cara-kerja-implementasi-konsep-mtv-pada-django)
    -   [Alasan Penggunaan Virtual Environment](#alasan-penggunaan-virtual-environment)
    -   [Konsep MVC, MVT, dan MVVM](#konsep-mvc-mvt-dan-mvvm)

<!-- ================ TUGAS 3 BEGIN ================== -->
<details>
<summary><h1>Tugas 3</h1></summary>

## Perbedaan Form POST dan Form GET

POST dan GET, keduanya merupakan bagian dari HTTP request method. Dalam Django, hanya kedua method tersebut yang dapat digunakan saat menggunakan form. Keduanya sama-sama digunakan dalam _data delivery_. Namun, perbedaannya terdapat pada cara bagaimana data tersebut disampaikan. Method POST mengirimkan data melalui _body_ HTTP request yang mana telah melalui _encoding_ terlebih dahulu. Sedangkan, method GET mengirimkan data melalui string URL tanpa melalui proses _encoding_. Tentunya hal ini menunjukkan keduanya memiliki fungsi yang berbeda. Pengiriman data melalui method POST dinilai lebih aman karena data tidak terekspos secara langsung dan telah melalui proses _encoding_ terlebih dahulu. Biasanya form POST digunakan untuk mengirimkan _request_ yang bersifat _state changing_ seperti mengubah atau menambahkan data ke database. Adapun form GET biasa digunakan untuk mengirimkan _request_ yang bersifat _state retrieving_ seperti mengambil data dari database.

Referensi: [https://docs.djangoproject.com/en/4.2/topics/forms/#get-and-post](https://docs.djangoproject.com/en/4.2/topics/forms/#get-and-post)

## Perbedaan XML, JSON, dan HTML dalam _Data Delivery_
XML (eXtensible Markup Language) merupakan salah satu format dalam pengiriman data. Data yang diformat dalam XML akan memiliki struktur seperti berikut: `<tag>content</tag>`. Bagian `tag` merupakan nama dari data dan `content` merupakan isi dari data tersebut. Setiap `<tag>` perlu ditutup oleh tag penutupnya (`</tag>`). XML dapat digunakan untuk mengirimkan data yang memiliki struktur yang kompleks, seperti data yang memiliki hierarki. Tag XML dapat ditentukan sendiri oleh pengguna sesuai dengan kebutuhan.

JSON (JavaScript Object Notation) merupakan salah satu format dalam pengiriman data. Data yang diformat dalam JSON akan memiliki struktur key-value seperti berikut `{ "key": "value" }` yang mana `key` merupakan nama dari data dan `value` merupakan isi dari data tersebut. Seperti namanya, JSON terinspirasi/dibuat berdasarkan notasi/format objek dari bahasa pemrograman JavaScript.

HTML (Hyper Text Markup Language) merupakan format dokumen yang digunakan untuk membuat halaman web. HTML adalah kombinasi dari _markup language_ dan _hypertext_. Sebagai _markup language_, HTML memiliki syntax yang sama seperti XML, yaitu  `<tag>content</tag>`. Sebagai _hypertext_, HTML memiliki kemampuan untuk membuat _link_ yang menghubungkan satu halaman dengan halaman lainnya. Tag-tag dalam HTML pada umumnya telah ditentukan sebelumnya.

Dalam konteks pengiriman data, XML dan JSON memiliki fungsi yang sama, yaitu sebagai *format/struktur untuk menyimpan atau melakukan transfer data*. Sedangkan HTML berfungsi sebagai *reperesentasi bagaimana data ditampilkan* kepada user. 

Adapun perbedaan antara JSON dan XML terletak pada format penulisannya. JSON menggunakan format key-value, seperti pada struktur data Map. Sedangkan XML yang merupakan _markup language_ menggunakan format tag. 

Referensi: 
    - [https://www.geeksforgeeks.org/html-vs-xml/](https://www.geeksforgeeks.org/html-vs-xml/)
    - [https://aws.amazon.com/compare/the-difference-between-json-xml/](https://aws.amazon.com/compare/the-difference-between-json-xml/)

## Alasan JSON Lebih Populer Digunakan dalam _Data Delivery_
JSON lebih populer digunakan sebagai format _data delivery_ pada aplikasi web modern dibandingkan dengan XML. Hal ini karena bahasa pemrograman Javascript banyak digunakan di berbagai aplikasi web modern. Kepopuleran Javascript ini berdampak pada kepopuleran JSON karena format JSON telah di-support langsung oleh Javascript. Berbeda dengan XML yang tidak di-support langsung oleh Javascript sehingga membutuhkan proses _parsing_ terlebih dahulu sebelum dapat digunakan. Selain itu, JSON memiliki format yang *lebih ringkas* dibandingkan dengan XML sehingga lebih mudah dibaca dan ditulis oleh manusia serta dapat mengurangi ukuran data dan mempercepat proses transfer data.


## Implementasi Step-by-Step (Tugas 3)

-   Membuat input form untuk menambahkan objek model 
    -   Membuat file `forms.py` di dalam folder aplikasi `main`. Pada file tersebut, saya membuat class `ItemForm` sebagai form class untuk class `Item`. Class tersebut memiliki _innerclass_ `Meta` yang berisi model yang akan digunakan dan field yang akan ditampilkan pada form. Field yang ditampilkan pada form adalah semua field pada model class `Item`, kecuali field `id`. Berikut potongan kodenya.
    ```python
    class ItemForm(ModelForm):
        class Meta:
            model = Item
            fields = '__all__'
            exclude = ['id']
    ```
    - Membuat
</details>
<!-- ================ TUGAS 3 END ================== -->

<!-- ================ TUGAS 2 BEGIN ================== -->
<details>
<summary><h1>Tugas 2</h1></summary>

## Implementasi Step-by-Step (Tugas 2)

-   Membuat repository baru di github
-   Membuat folder baru di local dan menghubungkan dengan repository yang sudah dibuat
-   Sebelum membuat proyek Django, terlebih dahulu membuat virtual environment dengan perintah `python -m venv env`. Kemudian mengaktifkannya dengan perintah `env\Scripts\Activate.ps1` (saya menggunakan powershell)
-   Mendaftarkan seluruh package yang dibutuhkan ke dalam `requirements.txt`, kemudian menginstallnya dengan perintah `pip install -r requirements.txt`.
-   Membuat proyek Django dengan perintah `django-admin startproject aci_rezeki_shop`
-   Membuat aplikasi 'main' dengan perintah `python manage.py startapp main`
-   Untuk melakukan routing pada aplikasi, saya menambahkan path `main` pada `urls.py` di folder proyek `aci_rezeki_shop`. Selain itu, saya juga menambahkan path `main` sebagai `INSTALLED_APPS` pada `settings.py` di folder proyek.
-   Kemudian di aplikasi `main`, membuat model `Item` dan `Category` (tambahan) di dalam file `models.py` dengan spesifikasi class sebagai berikut.

```python
    -   Item
        -   name = models.CharField(max_length=255)
        -   amount = models.IntegerField()
        -   description = models.TextField()
        -   id = models.AutoField(primary_key=True)
        -   price = models.IntegerField()
        -   category = models.ForeignKey('Category', on_delete=models.DO_NOTHING, null=True)
    -   Category
        -   id = models.AutoField(primary_key=True)
        -   name = models.CharField(max_length=255)
```

-   Melakukan registrasi model `Item` dan `Category` pada `admin.py` di aplikasi `main`.
-   Membuat fungsi `show_homepage` pada `views.py` di aplikasi `main` untuk menampilkan halaman utama. Fungsi tersebut akan me-render halaman `index.html` pada folder `templates` dengan context berupa nama toko serta nama dan kelas saya.
-   Membuat file `urls.py` pada aplikasi `main` untuk melakukan routing pada aplikasi. Kemudian menambahkan root path yang akan mengarah ke fungsi `show_homepage` pada `views.py`.
-   Melakukan migrasi database dengan perintah `python manage.py makemigrations` dan `python manage.py migrate`.
-   Membuat testing
-   Melakukan `add`, `commit`, dan `push` ke repository github.
-   Melakukan deployment ke platform Adaptable.

## Cara Kerja Implementasi Konsep MTV pada Django

![Diagram Konsep MVT pada Django](img/diagram_django_flow.jpg)

1. User melakukan request HTTP ke aplikasi Django melalui browser atau aplikasi lainnya. Framework Django akan melihat URL yang diakses oleh user dan mencocokkannya dengan URL yang terdaftar pada `urls.py`.
2. `urls.py` akan meneruskan request ke `views.py` yang sesuai dengan URL yang diakses oleh user.
3. `views.py` akan memproses request yang diterima dari `urls.py`. Jika pengolahan data diperlukan, `views.py` akan meminta (_query_) data tersebut dari `model.py`.
4. `model.py` akan mengambil data dari _database_ dan mengembalikannya kepada `views.py`.
5. `views.py` akan mengolah data yang diterima dari `model.py`.
6. Jika tampilan UI diperlukan, `views.py` akan meminta bantuan kepada `template.py` untuk menampilkan data kepada user. Tampilan UI tersebut akan di-render sesuai dengan data yang telah diberikan oleh `model.py` sebelumnya.
7. `views.py` mengembalikan response HTTP kepada user.

## Alasan Penggunaan Virtual Environment

Pada umumnya, saat kita membangun sebuah aplikasi Django, kita menggunakan virtual environment. Berikut merupakan beberapa alasan mengapa kita dianjurkan menggunakan virtual environment.

-   Memungkinkan kita untuk mengisolasi package yang digunakan pada proyek kita. Ketika kita menggunakan perintah `pip install [nama_package]` tanpa virtual environment, package tersebut akan terinstall pada python global environment. Hal ini berpotensi memunculkan konflik antar package yang digunakan pada proyek yang berbeda. Oleh karena itu, kita perlu mengisolasi package yang digunakan pada proyek kita dengan virtual environment.
-   Memungkinkan kita untuk membuat development environment yang sama persis di komputer lain. Dengan menentukan versi package pada `requirement.txt`, kita dapat membuat development environment yang sama persis di komputer lain dengan perintah `pip install -r requirements.txt`. Hal ini akan memudahkan kita untuk melakukan kolaborasi dengan orang lain.

_Tanpa virtual environment, kita masih dapat membuat aplikasi berbasis Django_. Namun, hal ini tidak direkomendasikan karena berpotensi menimbulkan konflik antar package yang digunakan pada proyek yang berbeda.

## Konsep MVC, MVT, dan MVVM

### MVC (Model-View-Controller)

MVC merupakan salah satu konsep arsitektur perangkat lunak populer yang memisahkan aplikasi berdasarkan komponen utamanya. Komponen utama tersebut adalah model, view, dan controller. Berikut merupakan penjelasan dari masing-masing komponen tersebut.

-   Model merupakan komponen yang berfungsi untuk mengatur semua hal yang berkaitan dengan _data logic_ . Model akan mengatur bagaimana data disimpan, diubah, dan diakses. Model juga lah yang berinteraksi langsung dengan _database_.
-   View merupakan komponen UI aplikasi yang berfungsi untuk menampilkan data kepada user. View akan mengatur bagaimana data ditampilkan kepada pengguna. Data yang diakses user melalui view tidak diperoleh langsung melalui model, akan tetapi melalui controller.
-   Controller merupakan komponen yang berfungsi untuk mengatur _flow_ dari aplikasi. Controller akan mengatur bagaimana data yang diperoleh dari model ditampilkan kepada user melalui view. Controller juga berperan sebagai entry point dari aplikasi.

### MVT (Model-View-Template)

MVT merupakan konsep arsitektur perangkat lunak yang digunakan oleh Django. Konsep ini sedikit berbeda dari MVC. Berikut merupakan penjelasan dari masing-masing komponen tersebut.

-   Model. Model pada MVT memiliki peran dan fungsi yang sama dengan model pada MVC, yaitu mengatur semua hal yang berkaitan dengan _data logic_.
-   View. Berbeda dengan view pada MVC, view pada MVT bertanggung jawab untuk memproses _request_ user dan mengembalikan response kembali kepada user.
-   Template. Template bertanggung jawab untuk menampilkan data kepada user. Template akan mengatur bagaimana data ditampilkan kepada pengguna.

### MVVM (Model-View-ViewModel)

MVVM merupakan konsep arsitektur perangkat lunak yang memisahkan aplikasi menjadi tiga layer utama, yaitu model-view-viewmodel. Berikut merupakan penjelasan dari masing-masing komponen tersebut.

-   Model. Model pada MVVM memiliki peran dan fungsi yang sama dengan model pada MVC dan MVT, yaitu mengatur semua hal yang berkaitan dengan _data logic_.
-   View. View bertanggung jawab untuk menampilkan data kepada user. View akan mengatur bagaimana data ditampilkan kepada pengguna. Pada arsitektur ini, view berperan sebagai entry point dari aplikasi.
-   ViewModel. ViewModel bertugas sebagai penghubung antara model dan view. ViewModel akan mengatur bagaimana data yang diperoleh dari model ditampilkan kepada user melalui view.

### Perbedaan MVC, MVT, dan MVVM

-   Masing-masing arsitektur memiliki _entry point_ yang berbeda untuk berinteraksi dengan user. Pada MVC, _entry point_-nya adalah controller. Pada MVT Django, _entry point_-nya adalah aplikasi Django itu sendiri kemudian di-forward ke layer view. Sedangkan pada MVVM, _entry point_-nya adalah layer view.
-   Arsitektur MVVM cocok digunakan dalam implementasi aplikasi berbasis UI atau frontend, terutama aplikasi mobile dan desktop. Sedangkan arsitektur MVC dan MVT lebih populer diguanaan dalam implementasi aplikasi server-side, seperti aplikasi web.
-   Peran layer view pada MVT lebih mirip seperti layer controller pada arsitektur MVC, yaitu sebagai pengatur _flow_ dari aplikasi.
-   Peran layer template pada MVT lebih mirip dengan layer view pada arsitektur MVC, yaitu sebagai layer yang bertanggung jawab untuk menampilkan data kepada user.

</details>
<!-- ================ TUGAS 2 END ================== -->
