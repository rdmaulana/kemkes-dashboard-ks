Catatan :

**Semua program berada pada branch master**

Tools yang dibutuhkan :

1. Python atleast version 3
2. Postgres
3. Postman

Cara menjalankan program

Langkah - Langkah menjalankan program :

1. Buatlah sebuah database dengan nama tertentu (disarankan = iks_v2).
2. Jalankan script sql pada file create_table_dashboard.sql pada database tersebut. (Jika blm ada table-table dashboard)
3. Jalankan script sql pada folder raw survei (Jika belum ada tabel raw survei):
    - create_table_raw_survei.sql
    - insert_table_raw_survei.sql
4. Edit pada file funcdash.py line ke-3 sesuai dengan postgres anda. (atur nama dbname, user, password)
5. Run file cobadash.py
    Jika berhasil outputnya seperti ini

    1 id yang diproses = ['acc44eb7-2f0d-5f10-88b4-f357e9f289f1']
    2 id yang tidak dapat diproses = ['ae', 'ed']