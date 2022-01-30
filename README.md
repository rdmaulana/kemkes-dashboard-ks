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

1. Python atleast version 3
2. Postgres
3. Postman

## Library pyhton yang dibutuhkan

1. psycopg2
2. date

## Cara install library python

1. Buka CMD
2. Ketik --> pip install {nama library}

## Cara menjalankan program

Langkah - Langkah menjalankan program :

1. Buatlah sebuah database di postgres sql dengan nama tertentu.
2. Jalankan script sql pada file create_table_dashboard.sql pada database tersebut.
3. Jalankan script sql pada folder raw survei di database yang anda buat:
    - create_table_raw_survei.sql
    - insert_table_raw_survei.sql
4. Buka file config.json pada folder config sesuai dengan postgres anda. (atur nama dbname, user, password)
5. Run file cobadash.py
    - Buka terminal di OS anda
    - Jalankan program dengan statement (python main.py tanggal awal tanggal akhir) --> contoh : python cobadash.py 2019-01-01 2019-12-31