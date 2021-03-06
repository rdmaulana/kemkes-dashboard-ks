# Proses Pembuatan Dashboard

## Maintainer
Aldon Manuel ( [GitHub](https://github.com/aldonmanuel) | [GitLab](https://gitlab.com/aldonmanuel) )

## Acknowledgements
- Andreas Hadiyono ( [GitLab](https://gitlab.com/Hadiyono) )
- Fikri Fadlillah ( [GitLab](https://gitlab.com/fikrifadlillah) )

Catatan :

**Semua program berada pada branch master**

## Prerequisites

Tools yang dibutuhkan :

1. Operating System     = linux ubuntu 21.04
2. Bahasa pemrograman   = python (3.9.5)
3. Database 		= postgres(13.5)
4. Text Editor          (VScode, Pycharm, Sublime, Notepad DLL)

## Library pyhton yang dibutuhkan

1. psycopg2
2. date
3. datetime
4. sys
5. time
6. json

## Cara install library python

1. Buka CMD
2. Ketik --> pip install {nama library}

## Inisialisasi Database dan membuat koneksi dengan database

1. Buatlah sebuah database di postgres sql dengan nama tertentu.
2. Jalankan script sql pada file create_table_dashboard.sql pada database tersebut.
3. Jalankan script sql pada folder raw survei di database yang anda buat:
    - create_table_raw_survei.sql
    - insert_table_raw_survei.sql
4. Buka file config.json pada folder config sesuai dengan postgres anda. (atur nama dbname, user, password)

## Cara menjalankan program

1. Run file cobadash.py
- Buka terminal di OS anda
- Jalankan program dengan statement (python main.py tanggal awal tanggal akhir)
    contoh : python3 cobadash.py 2019-01-01 2019-12-31 (Linux)
