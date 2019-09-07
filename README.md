## Django ile kodlanmış basit bir portfolyo projesi


<hr>

 # Kurulum
 
 ### Sanal ortam oluşturma

```
python -m venv myvenv
```

### Sanal ortamı çalıştırma


* **git kullanarak**
```
source .\myvenv\Scripts\activate
```

* **powershell kullanarak**
```
.\myvenv\Scripts\activate
```

* **cmd kullanarak**
```
call .\myvenv\Scripts\activate
```
### Gerekli modüllerin kurulumu
```
pip install -r .\requirements.txt
```


### Veritabanı kurulumu
* [Postresql](https://www.postgresql.org/download/) kurulduktan sonra [settings.py](https://github.com/mustafadalga/portfolio/blob/master/portfolio/settings.py) içerisinden veritabanı bilgileri istenildiği gibi değiştirilebilip veritabanı oluşturulabilir.

* **Varsayılan isimle veritabanını oluşturma**
```
CREATE DATABASE portfoliodb;
```

### Veritabanı tablolarını oluşturma
```
python .\manage.py makemigrations
python .\manage.py migrate
```

### Statik dosyaları oluşturma

```
python manage.py collectstatic
```

### Projeyi çalıştırma

```
python manage.py runserver
```

<hr>


### Notlar
* Python versiyonu:3.7.2

<hr>


### Uygulama Görüntüsü

* **Anasayfa** 

![1](https://user-images.githubusercontent.com/25087769/64475618-9ca28000-d18d-11e9-9687-cd309209bc40.png)

* **Blog**  

![2](https://user-images.githubusercontent.com/25087769/64475617-9ca28000-d18d-11e9-8b9b-ff5e61b66190.png)


