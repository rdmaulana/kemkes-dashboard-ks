import psycopg2

import time

import json

# buka file JSON
file_json = open("config/config.json")

# prsing data JSON
database = json.loads(file_json.read())

# ==============================
#       Connect to DB
# ==============================

def connectDB():
    db_conn = psycopg2.connect(f"dbname={database['db_name']} user={database['user']} password={database['pass']} host={database['host']} port={database['port']}")
    cursor = db_conn.cursor()
    return (db_conn, cursor)

# ==============================
#         Read ID SQL
# ==============================

def readSQL(cursor, waktu):
    ID = "SELECT survei_individu_survei_individu_detail_id FROM public.raw_survei where survei_individu_created_at " \
         "BETWEEN '%s' AND '%s' OR survei_individu_updated_at BETWEEN '%s' AND '%s' ORDER BY " \
         "survei_individu_created_at;" % (waktu[1], waktu[2], waktu[1], waktu[2])
    cursor.execute(ID)
    id_from_query = cursor.fetchall()
    return id_from_query

# ==============================
#         Check ID
# ==============================

def checkIdSurveiIndividu(cursor, id_individu): # fungsi untuk memeriksa apakah id_individu tersedia pada tabel survei individu
    sql_check_survei_individu = "SELECT EXISTS(select survei_individu_survei_individu_detail_id FROM raw_survei " \
                                "where survei_individu_survei_individu_detail_id = '%s');" % (id_individu)
    cursor.execute(sql_check_survei_individu)
    status_id_survei_individu = cursor.fetchone()

    if status_id_survei_individu == (1,):
        return 1 # mengembalikan nilai 1 jika id_individu tersedia
    else:
        return 0 # mengembalikan nilai 0 jika id_individu tidak tersedia

# ==============================
#         Template Data
# ==============================

def templateData(cursor, id_individu, date): # fungsi ini untuk ambil template data
    select_Query = '''SELECT 
        survei_individu_survei_individu_detail_id, 
        survei_rt_survei_rt_id,
        survei_survei_id,
        survei_propinsi_id,
        survei_nm_propinsi,
        survei_kota_id,
        survei_nm_kota,
        survei_kecamatan_id,
        survei_nm_kecamatan,
        survei_kelurahan_id,
        survei_nm_kelurahan,
        survei_kd_puskesmas,
        survei_individu_nik,
        survei_individu_nama,
        survei_individu_tanggal_lahir,
        survei_individu_jk_id
        FROM public.raw_survei WHERE survei_individu_survei_individu_detail_id = %s;
        '''
    cursor.execute(select_Query, (id_individu,))
    query_Result = cursor.fetchone()

    if query_Result[15] == 1:
        jenis_kelamin = 'Laki-Laki'
    else:
        jenis_kelamin = 'Perempuan'

    constant_dict = {
        'survei_individu_detail_id': query_Result[0],
        'survei_rumah_tangga_id': query_Result[1],
        'survei_id': query_Result[2],
        'provinsi_id': query_Result[3],
        'nama_provinsi': query_Result[4],
        'kota_kabupaten_id': query_Result[5],
        'nama_kota_kabupaten': query_Result[6],
        'kecamatan_id': query_Result[7],
        'nama_kecamatan': query_Result[8],
        'kelurahan_id': query_Result[9],
        'nama_kelurahan': query_Result[10],
        'kd_puskesmas': query_Result[11],
        'nik': query_Result[12],
        'nama': query_Result[13],
        'tgl_lahir': query_Result[14],
        'jenis_kelamin': jenis_kelamin,
        "created_at": time.strftime("%a, %d %b %Y %H:%M:%S")
    }
    # data yang terambil akan disimpan pada tipe data dictionary
    return (constant_dict) # mengembalikan nilai pada variabel dict

# =============================
#           Gabung Data
# ==============================

def gabungData(templateData, dataTambahan): # fungsi ini untuk menggabungkan templateData dan dataTambahan
    hasil = {}
    hasil.update(templateData)
    hasil.update(dataTambahan)

    return hasil # mengembalikan nilai hasil penggabungan dua variabel

# =============================
#     Sasaran Life Cycle SPM
# ==============================

def specificDataForSasaranLifeCycleSpm(cursor, id): # fungsi ini untuk tambahan data untuk table SASARAN LIFE CYCLE SPM
    sql_select_data_for_insert_sasaran_life_cycle_spm = "SELECT survei_individu_umur_bln, survei_individu_umur_thn," \
                                                        "survei_individu_wuh FROM public.raw_survei " \
                                                        "where survei_individu_survei_individu_detail_id = %s"
                                                        # data field yang dipilih tergantung table masing-masing

    cursor.execute(sql_select_data_for_insert_sasaran_life_cycle_spm, (id,))
    data_for_sasaran_life_cycle_spm = cursor.fetchone()

    dictSasaranLifeCycleSpm = {
        'umur_bulan' : data_for_sasaran_life_cycle_spm[0],
        'umur_tahun' : data_for_sasaran_life_cycle_spm [1],
        'wanita_usia_hamil' : data_for_sasaran_life_cycle_spm[2]
    }
    # data yang diambil disimpan pada tipe data dictionary

    return dictSasaranLifeCycleSpm # mengembalikan nilai tambahan data untuk table SASARAN LIFE CYCLE SPM

def insertDataSasaranLifeCycleSpm(db_conn, cursor, sasaran_life_cycle_spm): # fungsi ini untuk insert data pada table SASARAN LIFE CYCLE SPM

    sql_insert_sasaran_life_cycle_spm = "INSERT INTO public.sasaran_life_cycle_spm values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT " \
                                        "(survei_individu_detail_id) DO UPDATE SET survei_individu_detail_id = excluded.survei_individu_detail_id, " \
                                        "survei_rumah_tangga_id = excluded.survei_rumah_tangga_id, survei_id = excluded.survei_id, provinsi_id = excluded.provinsi_id, " \
                                        "nama_provinsi = excluded.nama_provinsi, kota_kabupaten_id = excluded.kota_kabupaten_id, nama_kota_kabupaten = excluded.nama_kota_kabupaten, " \
                                        "kecamatan_id = excluded.kecamatan_id, nama_kecamatan = excluded.nama_kecamatan, kelurahan_id = excluded.kelurahan_id, " \
                                        "nama_kelurahan = excluded.nama_kelurahan,	kd_puskesmas = excluded.kd_puskesmas, nik = excluded.nik , nama = excluded.nama , " \
                                        "tgl_lahir = excluded.tgl_lahir, jenis_kelamin = excluded.jenis_kelamin, hamil = excluded.hamil, " \
                                        "usia_0_sd_59_bulan = excluded.usia_0_sd_59_bulan,	usia_7_sd_15_tahun = excluded.usia_7_sd_15_tahun, " \
                                        "usia_15_sd_59_tahun = excluded.usia_15_sd_59_tahun, usia_lbh_dari_60_tahun = excluded.usia_lbh_dari_60_tahun, " \
                                        "updated_at = excluded.updated_at;"

    if sasaran_life_cycle_spm['wanita_usia_hamil'] == 'Y':
        hamil = 1
    else:
        hamil = 0

    usia_0_sd_59_bulan = 0
    usia_7_sd_15_tahun = 0
    usia_15_sd_59_tahun = 0
    usia_lbh_dari_60_tahun = 0

    if sasaran_life_cycle_spm['umur_bulan'] >= 0 and sasaran_life_cycle_spm['umur_bulan'] <= 59 and sasaran_life_cycle_spm['umur_tahun'] < 7:
        usia_0_sd_59_bulan = 1
    else:
        if sasaran_life_cycle_spm['umur_tahun'] >= 7 and sasaran_life_cycle_spm['umur_tahun'] <= 15:
            usia_7_sd_15_tahun = 1
        elif sasaran_life_cycle_spm['umur_tahun'] >= 15 and sasaran_life_cycle_spm['umur_tahun'] <= 59:
            usia_15_sd_59_tahun = 1
        else:
            usia_lbh_dari_60_tahun = 1

    val = (
        sasaran_life_cycle_spm['survei_individu_detail_id'],
        sasaran_life_cycle_spm['survei_rumah_tangga_id'],
        sasaran_life_cycle_spm['survei_id'],
        sasaran_life_cycle_spm['provinsi_id'],
        sasaran_life_cycle_spm['nama_provinsi'],
        sasaran_life_cycle_spm['kota_kabupaten_id'],
        sasaran_life_cycle_spm['nama_kota_kabupaten'],
        sasaran_life_cycle_spm['kecamatan_id'],
        sasaran_life_cycle_spm['nama_kecamatan'],
        sasaran_life_cycle_spm['kelurahan_id'],
        sasaran_life_cycle_spm['nama_kelurahan'],
        sasaran_life_cycle_spm['kd_puskesmas'],
        sasaran_life_cycle_spm['nik'],
        sasaran_life_cycle_spm['nama'],
        sasaran_life_cycle_spm['tgl_lahir'],
        sasaran_life_cycle_spm['jenis_kelamin'],
        hamil,
        usia_0_sd_59_bulan,
        usia_7_sd_15_tahun,
        usia_15_sd_59_tahun,
        usia_lbh_dari_60_tahun,
        sasaran_life_cycle_spm['created_at'],
        sasaran_life_cycle_spm['created_at']
    )

    # variabel val adalah data yang akan di input
    cursor.execute(sql_insert_sasaran_life_cycle_spm,val)
    db_conn.commit()
    return (sasaran_life_cycle_spm['survei_individu_detail_id'])  # cuman variabel kontrol aja

# ==============================
#     Keluarga Berencana
# ==============================

def specificDataForKeluargaBerencana(cursor, id):
    sql_select_data_for_insert_keluarga_berencana = "SELECT survei_individu_umur_thn, survei_individu_stmarital_id, survei_individu_wuh," \
                                                    "survei_individu_kb FROM public.raw_survei where survei_individu_survei_individu_detail_id = %s"

    cursor.execute(sql_select_data_for_insert_keluarga_berencana, (id,))
    data_for_keluarga_berencana = cursor.fetchone()

    dictKeluargaBerencana = {
        'umur_tahun' : data_for_keluarga_berencana[0],
        'status_kawin': data_for_keluarga_berencana[1],
        'wanita_usia_hamil' : data_for_keluarga_berencana[2],
        'menggunakan_kb' : data_for_keluarga_berencana[3]
    }

    return dictKeluargaBerencana

def insertDataKeluargaBerencana(db_conn, cursor, keluarga_berencana):

    sql_insert_keluarga_berencana = "INSERT INTO public.keluarga_berencana values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) " \
                                    "ON CONFLICT (survei_individu_detail_id) DO UPDATE SET survei_individu_detail_id = excluded.survei_individu_detail_id, " \
                                    "survei_rumah_tangga_id = excluded.survei_rumah_tangga_id, survei_id = excluded.survei_id, provinsi_id = excluded.provinsi_id, " \
                                    "nama_provinsi = excluded.nama_provinsi, kota_kabupaten_id = excluded.kota_kabupaten_id, nama_kota_kabupaten = excluded.nama_kota_kabupaten, " \
                                    "kecamatan_id = excluded.kecamatan_id, nama_kecamatan = excluded.nama_kecamatan, kelurahan_id = excluded.kelurahan_id, " \
                                    "nama_kelurahan = excluded.nama_kelurahan,	kd_puskesmas = excluded.kd_puskesmas, nik = excluded.nik , nama = excluded.nama , " \
                                    "tgl_lahir = excluded.tgl_lahir, jenis_kelamin = excluded.jenis_kelamin, usia_lebih_dari_10_tahun = excluded.usia_lebih_dari_10_tahun, " \
                                    "usia_10_sd_54 = excluded.usia_10_sd_54, wanita_usia_10_sd_54_kawin = excluded.wanita_usia_10_sd_54_kawin, " \
                                    "pria_usia_lebih_dari_10_tahun_kawin = excluded.pria_usia_lebih_dari_10_tahun_kawin, " \
                                    "wanita_usia_10_sd_54_dan_pria_usia_lebih_10_sudah_kawin = excluded.wanita_usia_10_sd_54_dan_pria_usia_lebih_10_sudah_kawin," \
                                    "wanita_usia_10_sd_54_sudah_kawin_tidak_hamil = excluded.wanita_usia_10_sd_54_sudah_kawin_tidak_hamil, " \
                                    "wanita_usia_10_sd_54_sudah_kawin_tidak_hamil_ber_kb = excluded.wanita_usia_10_sd_54_sudah_kawin_tidak_hamil_ber_kb," \
                                    "wanita_usia_10_sd_54_sudahkawin_tidak_hamil_tidak_berkb = excluded.wanita_usia_10_sd_54_sudahkawin_tidak_hamil_tidak_berkb, " \
                                    "wanita_ber_kb = excluded.wanita_ber_kb, wanita_tidak_ber_kb = excluded.wanita_tidak_ber_kb, updated_at = excluded.updated_at;"

    usia_lebih_dari_10_tahun = 0
    usia_10_sd_54 = 0
    wanita_usia_10_sd_54_kawin = 0
    pria_usia_lebih_dari_10_tahun_kawin = 0
    wanita_usia_10_sd_54_dan_pria_usia_lebih_10_sudah_kawin = 0
    wanita_usia_10_sd_54_sudah_kawin_tidak_hamil = 0
    wanita_usia_10_sd_54_sudah_kawin_tidak_hamil_ber_kb = 0
    wanita_usia_10_sd_54_sudahkawin_tidak_hamil_tidak_berkb = 0
    wanita_ber_kb = 0
    wanita_tidak_ber_kb = 0

    if keluarga_berencana['umur_tahun'] > 10 :
        usia_lebih_dari_10_tahun = 1
    if keluarga_berencana['umur_tahun'] >= 10 and keluarga_berencana['umur_tahun'] <= 54:
        usia_10_sd_54 = 1
    if keluarga_berencana['jenis_kelamin'] == 'Perempuan' and usia_10_sd_54 == 1 and keluarga_berencana['status_kawin'] == 1:
        wanita_usia_10_sd_54_kawin = 1
    if keluarga_berencana['jenis_kelamin'] == 'Laki-Laki' and usia_lebih_dari_10_tahun == 1 and keluarga_berencana['status_kawin'] == 1:
        pria_usia_lebih_dari_10_tahun_kawin = 1
    if wanita_usia_10_sd_54_kawin == 1 or pria_usia_lebih_dari_10_tahun_kawin == 1:
        wanita_usia_10_sd_54_dan_pria_usia_lebih_10_sudah_kawin = 1
    if wanita_usia_10_sd_54_kawin == 1 and keluarga_berencana['wanita_usia_hamil'] == 'Y':
        wanita_usia_10_sd_54_sudah_kawin_tidak_hamil = 1
    if wanita_usia_10_sd_54_sudah_kawin_tidak_hamil == 1 and keluarga_berencana['menggunakan_kb'] == 'Y':
        wanita_usia_10_sd_54_sudah_kawin_tidak_hamil_ber_kb = 1
    if wanita_usia_10_sd_54_sudah_kawin_tidak_hamil == 1 and keluarga_berencana['menggunakan_kb'] == 'T':
        wanita_usia_10_sd_54_sudahkawin_tidak_hamil_tidak_berkb = 1
    if keluarga_berencana['jenis_kelamin'] == 'Perempuan' and keluarga_berencana['menggunakan_kb'] == 'Y':
        wanita_ber_kb = 1
    if keluarga_berencana['jenis_kelamin'] == 'Perempuan' and keluarga_berencana['menggunakan_kb'] == 'T':
        wanita_tidak_ber_kb = 1

    val = (
        keluarga_berencana['survei_individu_detail_id'],
        keluarga_berencana['survei_rumah_tangga_id'],
        keluarga_berencana['survei_id'],
        keluarga_berencana['provinsi_id'],
        keluarga_berencana['nama_provinsi'],
        keluarga_berencana['kota_kabupaten_id'],
        keluarga_berencana['nama_kota_kabupaten'],
        keluarga_berencana['kecamatan_id'],
        keluarga_berencana['nama_kecamatan'],
        keluarga_berencana['kelurahan_id'],
        keluarga_berencana['nama_kelurahan'],
        keluarga_berencana['kd_puskesmas'],
        keluarga_berencana['nik'],
        keluarga_berencana['nama'],
        keluarga_berencana['tgl_lahir'],
        keluarga_berencana['jenis_kelamin'],
        usia_lebih_dari_10_tahun,
        usia_10_sd_54,
        wanita_usia_10_sd_54_kawin,
        pria_usia_lebih_dari_10_tahun_kawin,
        wanita_usia_10_sd_54_dan_pria_usia_lebih_10_sudah_kawin,
        wanita_usia_10_sd_54_sudah_kawin_tidak_hamil,
        wanita_usia_10_sd_54_sudah_kawin_tidak_hamil_ber_kb,
        wanita_usia_10_sd_54_sudahkawin_tidak_hamil_tidak_berkb,
        wanita_ber_kb,
        wanita_tidak_ber_kb,
        keluarga_berencana['created_at'],
        keluarga_berencana['created_at']
    )

    cursor.execute(sql_insert_keluarga_berencana, val)
    db_conn.commit()

    return (keluarga_berencana['survei_individu_detail_id'])

# ==============================
#     Persalinan di Faskes
# ==============================

def specificDataForPersalinanDiFaskes(cursor, id):
    sql_select_data_for_insert_persalinan_di_faskes = "SELECT survei_individu_faskes FROM public.raw_survei " \
                                                        "where survei_individu_survei_individu_detail_id = %s"

    cursor.execute(sql_select_data_for_insert_persalinan_di_faskes, (id,))
    data_for_persalinan_di_faskes = cursor.fetchone()

    dictPersalinanDiFaskes = {
        'faskes' : data_for_persalinan_di_faskes[0],
    }

    return dictPersalinanDiFaskes

def insertDataPersalinanDiFaskes(db_conn, cursor, persalinan_di_faskes):
    sql_insert_persalinan_di_faskes = "INSERT INTO public.persalinan_di_faskes VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) " \
                                      "ON CONFLICT (survei_individu_detail_id) DO UPDATE SET survei_individu_detail_id = excluded.survei_individu_detail_id, " \
                                      "survei_rumah_tangga_id = excluded.survei_rumah_tangga_id, survei_id = excluded.survei_id, provinsi_id = excluded.provinsi_id, " \
                                      "nama_provinsi = excluded.nama_provinsi, kota_kabupaten_id = excluded.kota_kabupaten_id, nama_kota_kabupaten = excluded.nama_kota_kabupaten, " \
                                      "kecamatan_id = excluded.kecamatan_id, nama_kecamatan = excluded.nama_kecamatan, kelurahan_id = excluded.kelurahan_id, " \
                                      "nama_kelurahan = excluded.nama_kelurahan,	kd_puskesmas = excluded.kd_puskesmas, nik = excluded.nik , nama = excluded.nama , " \
                                      "tgl_lahir = excluded.tgl_lahir, jenis_kelamin = excluded.jenis_kelamin, " \
                                      "ibu_dengan_anak_usia_0_sd_11_bulan = excluded.ibu_dengan_anak_usia_0_sd_11_bulan, " \
                                      "persalinan_tidak_di_faskes = excluded.persalinan_tidak_di_faskes, updated_at = excluded.updated_at;"

    ibu_dengan_anak_usia_0_sd_11_bulan = 0
    persalinan_tidak_di_faskes = 0

    if persalinan_di_faskes['faskes'] == 'Y' or persalinan_di_faskes['faskes'] == 'T':
        ibu_dengan_anak_usia_0_sd_11_bulan = 1
    if ibu_dengan_anak_usia_0_sd_11_bulan == 1 and persalinan_di_faskes['faskes'] == 'T':
        persalinan_tidak_di_faskes = 1

    val = (
        persalinan_di_faskes['survei_individu_detail_id'],
        persalinan_di_faskes['survei_rumah_tangga_id'],
        persalinan_di_faskes['survei_id'],
        persalinan_di_faskes['provinsi_id'],
        persalinan_di_faskes['nama_provinsi'],
        persalinan_di_faskes['kota_kabupaten_id'],
        persalinan_di_faskes['nama_kota_kabupaten'],
        persalinan_di_faskes['kecamatan_id'],
        persalinan_di_faskes['nama_kecamatan'],
        persalinan_di_faskes['kelurahan_id'],
        persalinan_di_faskes['nama_kelurahan'],
        persalinan_di_faskes['kd_puskesmas'],
        persalinan_di_faskes['nik'],
        persalinan_di_faskes['nama'],
        persalinan_di_faskes['tgl_lahir'],
        persalinan_di_faskes['jenis_kelamin'],
        ibu_dengan_anak_usia_0_sd_11_bulan,
        persalinan_tidak_di_faskes,
        persalinan_di_faskes['created_at']
    )

    cursor.execute(sql_insert_persalinan_di_faskes, val)
    db_conn.commit()

    return (persalinan_di_faskes['survei_individu_detail_id'])

# ==============================
#     Imunisasi dasar Lengkap
# ==============================

def specificDataForIDL(cursor, id):
    sql_select_data_for_insert_sasaran_life_cycle_spm = "SELECT survei_individu_umur_bln, survei_individu_umur_thn," \
                                                        "survei_individu_imunisasi FROM public.raw_survei " \
                                                        "where survei_individu_survei_individu_detail_id = %s"

    cursor.execute(sql_select_data_for_insert_sasaran_life_cycle_spm, (id,))
    data_for_IDL = cursor.fetchone()

    umur_tahun = data_for_IDL[1]
    # umur_tahun = 3 for debug
    umur_bulan = data_for_IDL[0]
    status_imunisasi = data_for_IDL[2]
    di5 = 0

    MEMILIKI_BALITA_12_sd_23_BULAN = 0
    SASARAN_TIDAK_IDL = 0

    if umur_tahun < 5:
        di5 = umur_tahun * 12 + umur_bulan  # Ini logic dipertanyakan dah



    if di5 >= 12 and di5 <= 23:
        MEMILIKI_BALITA_12_sd_23_BULAN = 1

    if MEMILIKI_BALITA_12_sd_23_BULAN == 1 and status_imunisasi == 'T':
        SASARAN_TIDAK_IDL = 1

    dictIDL = {
        'MEMILIKI_BALITA_12_sd_23_BULAN': MEMILIKI_BALITA_12_sd_23_BULAN,
        'SASARAN_TIDAK_IDL': SASARAN_TIDAK_IDL
    }
    # data yang diambil disimpan pada tipe data dictionary

    return dictIDL

def insertDataIDL(db_conn, cursor, imunisasi_dasar_lengkap):
    sql_insert_imunisasi_dasar_lengkap = "INSERT INTO public.imunisasi_dasar_lengkap values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT " \
                                         "(survei_individu_detail_id) DO UPDATE SET survei_individu_detail_id = excluded.survei_individu_detail_id, " \
                                         "survei_rumah_tangga_id = excluded.survei_rumah_tangga_id, survei_id = excluded.survei_id, provinsi_id = excluded.provinsi_id, " \
                                         "nama_provinsi = excluded.nama_provinsi, kota_kabupaten_id = excluded.kota_kabupaten_id, nama_kota_kabupaten = excluded.nama_kota_kabupaten, " \
                                         "kecamatan_id = excluded.kecamatan_id, nama_kecamatan = excluded.nama_kecamatan, kelurahan_id = excluded.kelurahan_id, " \
                                         "nama_kelurahan = excluded.nama_kelurahan,	kd_puskesmas = excluded.kd_puskesmas, nik = excluded.nik , nama = excluded.nama , " \
                                         "tgl_lahir = excluded.tgl_lahir, jenis_kelamin = excluded.jenis_kelamin, memiliki_balita_12_sd_23_bulan = excluded.memiliki_balita_12_sd_23_bulan, " \
                                         "sasaran_tidak_idl = excluded.sasaran_tidak_idl, " \
                                         "updated_at = excluded.updated_at;"

    val = (
        imunisasi_dasar_lengkap['survei_individu_detail_id'],
        imunisasi_dasar_lengkap['survei_rumah_tangga_id'],
        imunisasi_dasar_lengkap['survei_id'],
        imunisasi_dasar_lengkap['provinsi_id'],
        imunisasi_dasar_lengkap['nama_provinsi'],
        imunisasi_dasar_lengkap['kota_kabupaten_id'],
        imunisasi_dasar_lengkap['nama_kota_kabupaten'],
        imunisasi_dasar_lengkap['kecamatan_id'],
        imunisasi_dasar_lengkap['nama_kecamatan'],
        imunisasi_dasar_lengkap['kelurahan_id'],
        imunisasi_dasar_lengkap['nama_kelurahan'],
        imunisasi_dasar_lengkap['kd_puskesmas'],
        imunisasi_dasar_lengkap['nik'],
        imunisasi_dasar_lengkap['nama'],
        imunisasi_dasar_lengkap['tgl_lahir'],
        imunisasi_dasar_lengkap['jenis_kelamin'],
        imunisasi_dasar_lengkap['MEMILIKI_BALITA_12_sd_23_BULAN'],
        imunisasi_dasar_lengkap['SASARAN_TIDAK_IDL'],
        imunisasi_dasar_lengkap['created_at'],
        imunisasi_dasar_lengkap['created_at']
    )

    # variabel val adalah data yang akan di input
    cursor.execute(sql_insert_imunisasi_dasar_lengkap, val)
    db_conn.commit()

    return (imunisasi_dasar_lengkap['survei_individu_detail_id'])  # cuman variabel kontrol aja

# ==============================
#        Asi Eksklusif
# ==============================

def specificDataForAsiEksklusif(cursor, id):
    sql_select_data_for_Asi_Eksklusif = "SELECT survei_individu_umur_bln, survei_individu_umur_thn," \
                                        "survei_individu_asi_ekslusif FROM public.raw_survei " \
                                        "where survei_individu_survei_individu_detail_id = %s"

    cursor.execute(sql_select_data_for_Asi_Eksklusif, (id,))
    data_for_Asi_Eksklusif = cursor.fetchone()

    umur_tahun = data_for_Asi_Eksklusif[1]
    # umur_tahun = 3 for debug
    umur_bulan = data_for_Asi_Eksklusif[0]
    asi_eksklusif = data_for_Asi_Eksklusif[2]
    di5 = 0

    MEMILIKI_BAYI_7_sd_23_BULAN = 0
    SASARAN_TIDAK_ASI_EKSLUSIF = 0

    if umur_tahun < 5:
        di5 = umur_tahun * 12 + umur_bulan  # Ini logic dipertanyakan dah



    if di5 >= 12 and di5 <= 23:
        MEMILIKI_BAYI_7_sd_23_BULAN = 1

    if MEMILIKI_BAYI_7_sd_23_BULAN == 1 and asi_eksklusif == 'T':
        SASARAN_TIDAK_ASI_EKSLUSIF = 1

    dictAsiEksklusif = {
        'MEMILIKI_BAYI_7_sd_23_BULAN': MEMILIKI_BAYI_7_sd_23_BULAN,
        'SASARAN_TIDAK_ASI_EKSLUSIF': SASARAN_TIDAK_ASI_EKSLUSIF
    }
    # data yang diambil disimpan pada tipe data dictionary

    return dictAsiEksklusif

def insertDataAsiEksklusif(db_conn, cursor, Asi_Eksklusif):
    sql_insert_Asi_Eksklusif = "INSERT INTO public.asi_eksklusif values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT " \
                               "(survei_individu_detail_id) DO UPDATE SET survei_individu_detail_id = excluded.survei_individu_detail_id, " \
                               "survei_rumah_tangga_id = excluded.survei_rumah_tangga_id, survei_id = excluded.survei_id, provinsi_id = excluded.provinsi_id, " \
                               "nama_provinsi = excluded.nama_provinsi, kota_kabupaten_id = excluded.kota_kabupaten_id, nama_kota_kabupaten = excluded.nama_kota_kabupaten, " \
                               "kecamatan_id = excluded.kecamatan_id, nama_kecamatan = excluded.nama_kecamatan, kelurahan_id = excluded.kelurahan_id, " \
                               "nama_kelurahan = excluded.nama_kelurahan,	kd_puskesmas = excluded.kd_puskesmas, nik = excluded.nik , nama = excluded.nama , " \
                               "tgl_lahir = excluded.tgl_lahir, jenis_kelamin = excluded.jenis_kelamin, MEMILIKI_BAYI_7_sd_23_BULAN = excluded.MEMILIKI_BAYI_7_sd_23_BULAN, " \
                               "SASARAN_TIDAK_ASI_EKSLUSIF = excluded.SASARAN_TIDAK_ASI_EKSLUSIF, " \
                               "updated_at = excluded.updated_at;"

    val = (
        Asi_Eksklusif['survei_individu_detail_id'],
        Asi_Eksklusif['survei_rumah_tangga_id'],
        Asi_Eksklusif['survei_id'],
        Asi_Eksklusif['provinsi_id'],
        Asi_Eksklusif['nama_provinsi'],
        Asi_Eksklusif['kota_kabupaten_id'],
        Asi_Eksklusif['nama_kota_kabupaten'],
        Asi_Eksklusif['kecamatan_id'],
        Asi_Eksklusif['nama_kecamatan'],
        Asi_Eksklusif['kelurahan_id'],
        Asi_Eksklusif['nama_kelurahan'],
        Asi_Eksklusif['kd_puskesmas'],
        Asi_Eksklusif['nik'],
        Asi_Eksklusif['nama'],
        Asi_Eksklusif['tgl_lahir'],
        Asi_Eksklusif['jenis_kelamin'],
        Asi_Eksklusif['MEMILIKI_BAYI_7_sd_23_BULAN'],
        Asi_Eksklusif['SASARAN_TIDAK_ASI_EKSLUSIF'],
        Asi_Eksklusif['created_at'],
        Asi_Eksklusif['created_at']
    )

    # variabel val adalah data yang akan di input
    cursor.execute(sql_insert_Asi_Eksklusif, val)
    db_conn.commit()

    return (Asi_Eksklusif['survei_individu_detail_id'])  # cuman variabel kontrol aja

# ==============================
#       Tumbuh Kembang
# ==============================

def specificDataForTumbuhKembang(cursor, id):
    sql_select_data_for_tumbuh_kembang = "SELECT survei_individu_umur_bln, survei_individu_umur_thn," \
                                         "survei_individu_pantau_balita FROM public.raw_survei " \
                                         "where survei_individu_survei_individu_detail_id = %s"

    cursor.execute(sql_select_data_for_tumbuh_kembang, (id,))
    data_for_Tumbuh_Kembang = cursor.fetchone()

    umur_tahun = data_for_Tumbuh_Kembang[1]
    # umur_tahun = 3 for debug
    umur_bulan = data_for_Tumbuh_Kembang[0]
    pantau_balita = data_for_Tumbuh_Kembang[2]
    di5 = 0
    USIA_2_sd_59_BULAN = 0
    SASARAN_TIDAK_PEMANTAUAN_PERTUMBUHAN = 0

    if umur_tahun < 5:
        di5 = umur_tahun * 12 + umur_bulan  # Ini logic dipertanyakan dah

    

    if di5 >= 12 and di5 <= 23:
        USIA_2_sd_59_BULAN = 1

    if USIA_2_sd_59_BULAN == 1 and pantau_balita == 'T':
        SASARAN_TIDAK_PEMANTAUAN_PERTUMBUHAN = 1

    dict_Tumbuh_Kembang = {
        'USIA_2_sd_59_BULAN': USIA_2_sd_59_BULAN,
        'SASARAN_TIDAK_PEMANTAUAN_PERTUMBUHAN': SASARAN_TIDAK_PEMANTAUAN_PERTUMBUHAN
    }
    # data yang diambil disimpan pada tipe data dictionary

    return dict_Tumbuh_Kembang

def insertDataTumbuhKembang(db_conn, cursor, tumbuh_kembang):
    sql_insert_Tumbuh_Kembang = "INSERT INTO public.tumbuh_kembang values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT " \
                                "(survei_individu_detail_id) DO UPDATE SET survei_individu_detail_id = excluded.survei_individu_detail_id, " \
                                "survei_rumah_tangga_id = excluded.survei_rumah_tangga_id, survei_id = excluded.survei_id, provinsi_id = excluded.provinsi_id, " \
                                "nama_provinsi = excluded.nama_provinsi, kota_kabupaten_id = excluded.kota_kabupaten_id, nama_kota_kabupaten = excluded.nama_kota_kabupaten, " \
                                "kecamatan_id = excluded.kecamatan_id, nama_kecamatan = excluded.nama_kecamatan, kelurahan_id = excluded.kelurahan_id, " \
                                "nama_kelurahan = excluded.nama_kelurahan,	kd_puskesmas = excluded.kd_puskesmas, nik = excluded.nik , nama = excluded.nama , " \
                                "tgl_lahir = excluded.tgl_lahir, jenis_kelamin = excluded.jenis_kelamin, USIA_2_sd_59_BULAN = excluded.USIA_2_sd_59_BULAN, " \
                                "SASARAN_TIDAK_PEMANTAUAN_PERTUMBUHAN = excluded.SASARAN_TIDAK_PEMANTAUAN_PERTUMBUHAN, " \
                                "updated_at = excluded.updated_at;"

    val = (
        tumbuh_kembang['survei_individu_detail_id'],
        tumbuh_kembang['survei_rumah_tangga_id'],
        tumbuh_kembang['survei_id'],
        tumbuh_kembang['provinsi_id'],
        tumbuh_kembang['nama_provinsi'],
        tumbuh_kembang['kota_kabupaten_id'],
        tumbuh_kembang['nama_kota_kabupaten'],
        tumbuh_kembang['kecamatan_id'],
        tumbuh_kembang['nama_kecamatan'],
        tumbuh_kembang['kelurahan_id'],
        tumbuh_kembang['nama_kelurahan'],
        tumbuh_kembang['kd_puskesmas'],
        tumbuh_kembang['nik'],
        tumbuh_kembang['nama'],
        tumbuh_kembang['tgl_lahir'],
        tumbuh_kembang['jenis_kelamin'],
        tumbuh_kembang['USIA_2_sd_59_BULAN'],
        tumbuh_kembang['SASARAN_TIDAK_PEMANTAUAN_PERTUMBUHAN'],
        tumbuh_kembang['created_at'],
        tumbuh_kembang['created_at']
    )

    # variabel val adalah data yang akan di input
    cursor.execute(sql_insert_Tumbuh_Kembang, val)
    db_conn.commit()

    return (tumbuh_kembang['survei_individu_detail_id'])  # cuman variabel kontrol aja

# ==============================
#           TB Paru
# ==============================

def specificDataForTBParu(cursor, id):
    sql_select_data_for_TB_Paru = "SELECT survei_individu_umur_thn," \
                                  "survei_individu_tb, survei_individu_obat_tb, survei_individu_batuk FROM public.raw_survei " \
                                  "where survei_individu_survei_individu_detail_id = %s"

    # note yang dibutuhkan:
    # umur_tahun, didiagnosis_tb_baru, minum_obat_tb_teratur, batuk_berdakah_lebih_dari_Sama_Dengan_2_minggu

    cursor.execute(sql_select_data_for_TB_Paru, (id,))
    data_for_TB_Paru = cursor.fetchone()

    umur_tahun = data_for_TB_Paru[0]
    didiagnosis_tb_baru = data_for_TB_Paru[1]
    minum_obat_tb_teratur = data_for_TB_Paru[2]
    batuk_berdakah_lebih_dari_Sama_Dengan_2_minggu = data_for_TB_Paru[3]

    DIDIAGNOSIS_TAPI_TIDAK_MINUM_OBAT_TB = 0
    PENDERITA_TB_YANG_MINUM_OBAT_SESUAI_STANDAR = 0
    lebih_dari_sama_dengan_15_TAHUN = 0
    DIDIAGNOSIS_TB = 0
    SUSPEK_TB = 0

    # co
    if umur_tahun >= 15:
        lebih_dari_sama_dengan_15_TAHUN = 1

    # CP
    if lebih_dari_sama_dengan_15_TAHUN == 1 and didiagnosis_tb_baru == 'Y':
        DIDIAGNOSIS_TB = 1

    # CQ dan CR

    if lebih_dari_sama_dengan_15_TAHUN == 1 and DIDIAGNOSIS_TB == 1 and minum_obat_tb_teratur == 'T':
        DIDIAGNOSIS_TAPI_TIDAK_MINUM_OBAT_TB = 1
    if lebih_dari_sama_dengan_15_TAHUN == 1 and DIDIAGNOSIS_TB == 1 and minum_obat_tb_teratur == 'Y':
        PENDERITA_TB_YANG_MINUM_OBAT_SESUAI_STANDAR = 1

    # CS

    if lebih_dari_sama_dengan_15_TAHUN == 1 and batuk_berdakah_lebih_dari_Sama_Dengan_2_minggu == 'Y':
        SUSPEK_TB = 1

    dict_TB_Paru = {
        'lebih_dari_sama_dengan_15_TAHUN': lebih_dari_sama_dengan_15_TAHUN,
        'DIDIAGNOSIS_TB': DIDIAGNOSIS_TB,
        'DIDIAGNOSIS_TAPI_TIDAK_MINUM_OBAT_TB': DIDIAGNOSIS_TAPI_TIDAK_MINUM_OBAT_TB,
        'PENDERITA_TB_YANG_MINUM_OBAT_SESUAI_STANDAR': PENDERITA_TB_YANG_MINUM_OBAT_SESUAI_STANDAR,
        'SUSPEK_TB': SUSPEK_TB,
    }

    # data yang diambil disimpan pada tipe data dictionary

    return dict_TB_Paru

def insertDataTBParu(db_conn, cursor, TB_Paru):
    sql_insert_TB_Paru = "INSERT INTO public.tb_paru values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT " \
                         "(survei_individu_detail_id) DO UPDATE SET survei_individu_detail_id = excluded.survei_individu_detail_id, " \
                         "survei_rumah_tangga_id = excluded.survei_rumah_tangga_id, survei_id = excluded.survei_id, provinsi_id = excluded.provinsi_id, " \
                         "nama_provinsi = excluded.nama_provinsi, kota_kabupaten_id = excluded.kota_kabupaten_id, nama_kota_kabupaten = excluded.nama_kota_kabupaten, " \
                         "kecamatan_id = excluded.kecamatan_id, nama_kecamatan = excluded.nama_kecamatan, kelurahan_id = excluded.kelurahan_id, " \
                         "nama_kelurahan = excluded.nama_kelurahan,	kd_puskesmas = excluded.kd_puskesmas, nik = excluded.nik , nama = excluded.nama , " \
                         "tgl_lahir = excluded.tgl_lahir, jenis_kelamin = excluded.jenis_kelamin, lebih_dari_sama_dengan_15_TAHUN = excluded.lebih_dari_sama_dengan_15_TAHUN, " \
                         "DIDIAGNOSIS_TB = excluded.DIDIAGNOSIS_TB,	DIDIAGNOSIS_TAPI_TIDAK_MINUM_OBAT_TB = excluded.DIDIAGNOSIS_TAPI_TIDAK_MINUM_OBAT_TB, " \
                         "PENDERITA_TB_YANG_MINUM_OBAT_SESUAI_STANDAR = excluded.PENDERITA_TB_YANG_MINUM_OBAT_SESUAI_STANDAR, SUSPEK_TB = excluded.SUSPEK_TB, " \
                         "updated_at = excluded.updated_at;"

    val = (
        TB_Paru['survei_individu_detail_id'],
        TB_Paru['survei_rumah_tangga_id'],
        TB_Paru['survei_id'],
        TB_Paru['provinsi_id'],
        TB_Paru['nama_provinsi'],
        TB_Paru['kota_kabupaten_id'],
        TB_Paru['nama_kota_kabupaten'],
        TB_Paru['kecamatan_id'],
        TB_Paru['nama_kecamatan'],
        TB_Paru['kelurahan_id'],
        TB_Paru['nama_kelurahan'],
        TB_Paru['kd_puskesmas'],
        TB_Paru['nik'],
        TB_Paru['nama'],
        TB_Paru['tgl_lahir'],
        TB_Paru['jenis_kelamin'],
        TB_Paru["lebih_dari_sama_dengan_15_TAHUN"],
        TB_Paru["DIDIAGNOSIS_TB"],
        TB_Paru["DIDIAGNOSIS_TAPI_TIDAK_MINUM_OBAT_TB"],
        TB_Paru["PENDERITA_TB_YANG_MINUM_OBAT_SESUAI_STANDAR"],
        TB_Paru["SUSPEK_TB"],
        TB_Paru['created_at'],
        TB_Paru['created_at']
    )

    # variabel val adalah data yang akan di input
    cursor.execute(sql_insert_TB_Paru, val)
    db_conn.commit()

    return (TB_Paru['survei_individu_detail_id'])  # cuman variabel kontrol aja

# ==============================
#         Hipertensi
# ==============================

def specificDataForHipertensi(cursor, id):
    sql_select_data_for_KB_by_Program = "SELECT survei_individu_umur_thn, survei_individu_hipertensi, survei_individu_obat_hipertensi, survei_individu_tekanan_darah, survei_individu_sistolik, survei_individu_diastolik " \
                                        "FROM public.raw_survei " \
                                        "where survei_individu_survei_individu_detail_id = %s"

    cursor.execute(sql_select_data_for_KB_by_Program, (id,))
    data_for_Hipertensi = cursor.fetchone()

    # Yang dibutuhkan: umur_tahun, di_diagnosis_hipertensi, minum_obat_hipertensi_teratur
    # dilakukan_pengukuran_tekanan_darah, sistol, diastol

    umur_tahun = data_for_Hipertensi[0]
    di_diagnosis_hipertensi = data_for_Hipertensi[1]
    minum_obat_hipertensi_teratur = data_for_Hipertensi[2]
    dilakukan_pengukuran_tekanan_darah = data_for_Hipertensi[3]

    DIDIAGNOSIS_HIPERTENSI = 0
    INDIVIDU_DIDIAGNOSIS_TAPI_TIDAK_MINUM_OBAT_HIPERTENSI = 0
    INDIVIDU_DIDIAGNOSIS_HIPERTENSI_MINUM_OBAT_SESUAI_STANDAR = 0
    DIUKUR_TEKANAN_DARAH = 0
    SISTOL = data_for_Hipertensi[4]
    DIASTOL = data_for_Hipertensi[5]
    SUSPEK_TEKANAN_DARAH_TINGGI = 0

    # Field CT
    CO5 = 0

    if umur_tahun >= 15:
        CO5 = 1

    if CO5 == 1 and di_diagnosis_hipertensi == 'Y':
        DIDIAGNOSIS_HIPERTENSI = 1

    # Field CU
    if CO5 == 1 and DIDIAGNOSIS_HIPERTENSI == 1 and minum_obat_hipertensi_teratur == 'T':
        INDIVIDU_DIDIAGNOSIS_TAPI_TIDAK_MINUM_OBAT_HIPERTENSI = 1

    # Field CV
    if CO5 == 1 and DIDIAGNOSIS_HIPERTENSI == 1 and minum_obat_hipertensi_teratur == 'Y':
        INDIVIDU_DIDIAGNOSIS_HIPERTENSI_MINUM_OBAT_SESUAI_STANDAR = 1

    # Field CW
    if CO5 == 1 and dilakukan_pengukuran_tekanan_darah == 'Y':
        DIUKUR_TEKANAN_DARAH = 1



    # Field CZ
    if data_for_Hipertensi == 1 and SISTOL >= 140 and DIASTOL >= 90:
        SUSPEK_TEKANAN_DARAH_TINGGI = 1

    dict_Hipertensi = {
        'DIDIAGNOSIS_HIPERTENSI': DIDIAGNOSIS_HIPERTENSI,
        'INDIVIDU_DIDIAGNOSIS_TAPI_TIDAK_MINUM_OBAT_HIPERTENSI': INDIVIDU_DIDIAGNOSIS_TAPI_TIDAK_MINUM_OBAT_HIPERTENSI,
        'INDIVIDU_DIDIAGNOSIS_HIPERTENSI_MINUM_OBAT_SESUAI_STANDAR': INDIVIDU_DIDIAGNOSIS_HIPERTENSI_MINUM_OBAT_SESUAI_STANDAR,
        'DIUKUR_TEKANAN_DARAH': DIUKUR_TEKANAN_DARAH,
        'SISTOL': SISTOL,
        'DIASTOL': DIASTOL,
        'SUSPEK_TEKANAN_DARAH_TINGGI': SUSPEK_TEKANAN_DARAH_TINGGI
    }
    # data yang diambil disimpan pada tipe data dictionary

    return dict_Hipertensi


def insertDataHipertensi(db_conn, cursor, Hipertensi):
    sql_insert_Hipertensi = "INSERT INTO public.HIPERTENSI values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT " \
                            "(survei_individu_detail_id) DO UPDATE SET survei_individu_detail_id = excluded.survei_individu_detail_id, " \
                            "survei_rumah_tangga_id = excluded.survei_rumah_tangga_id, survei_id = excluded.survei_id, provinsi_id = excluded.provinsi_id, " \
                            "nama_provinsi = excluded.nama_provinsi, kota_kabupaten_id = excluded.kota_kabupaten_id, nama_kota_kabupaten = excluded.nama_kota_kabupaten, " \
                            "kecamatan_id = excluded.kecamatan_id, nama_kecamatan = excluded.nama_kecamatan, kelurahan_id = excluded.kelurahan_id, " \
                            "nama_kelurahan = excluded.nama_kelurahan,	kd_puskesmas = excluded.kd_puskesmas, nik = excluded.nik , nama = excluded.nama , " \
                            "tgl_lahir = excluded.tgl_lahir, jenis_kelamin = excluded.jenis_kelamin, DIDIAGNOSIS_HIPERTENSI = excluded.DIDIAGNOSIS_HIPERTENSI, " \
                            "INDIVIDU_DIDIAGNOSIS_TAPI_TIDAK_MINUM_OBAT_HIPERTENSI = excluded.INDIVIDU_DIDIAGNOSIS_TAPI_TIDAK_MINUM_OBAT_HIPERTENSI,	INDIVIDU_DIDIAGNOSIS_HIPERTENSI_MINUM_OBAT_SESUAI_STANDAR = excluded.INDIVIDU_DIDIAGNOSIS_HIPERTENSI_MINUM_OBAT_SESUAI_STANDAR, " \
                            "DIUKUR_TEKANAN_DARAH = excluded.DIUKUR_TEKANAN_DARAH, SISTOL = excluded.SISTOL, DIASTOL = excluded.DIASTOL, " \
                            "SUSPEK_TEKANAN_DARAH_TINGGI = excluded.SUSPEK_TEKANAN_DARAH_TINGGI, updated_at = excluded.updated_at;"

    val = (
        Hipertensi['survei_individu_detail_id'],
        Hipertensi['survei_rumah_tangga_id'],
        Hipertensi['survei_id'],
        Hipertensi['provinsi_id'],
        Hipertensi['nama_provinsi'],
        Hipertensi['kota_kabupaten_id'],
        Hipertensi['nama_kota_kabupaten'],
        Hipertensi['kecamatan_id'],
        Hipertensi['nama_kecamatan'],
        Hipertensi['kelurahan_id'],
        Hipertensi['nama_kelurahan'],
        Hipertensi['kd_puskesmas'],
        Hipertensi['nik'],
        Hipertensi['nama'],
        Hipertensi['tgl_lahir'],
        Hipertensi['jenis_kelamin'],
        Hipertensi["DIDIAGNOSIS_HIPERTENSI"],
        Hipertensi["INDIVIDU_DIDIAGNOSIS_TAPI_TIDAK_MINUM_OBAT_HIPERTENSI"],
        Hipertensi["INDIVIDU_DIDIAGNOSIS_HIPERTENSI_MINUM_OBAT_SESUAI_STANDAR"],
        Hipertensi["DIUKUR_TEKANAN_DARAH"],
        Hipertensi["SISTOL"],
        Hipertensi["DIASTOL"],
        Hipertensi["SUSPEK_TEKANAN_DARAH_TINGGI"],
        Hipertensi['created_at'],
        Hipertensi['created_at']
    )

    # variabel val adalah data yang akan di input
    cursor.execute(sql_insert_Hipertensi, val)
    db_conn.commit()

    return (Hipertensi['survei_individu_detail_id'])  # cuman variabel kontrol aja


# ==============================
#            Rokok
# ==============================

def specificDataForRokok(cursor, id):
    sql_select_data_for_Rokok = "SELECT survei_individu_merokok " \
                                "FROM public.raw_survei " \
                                "where survei_individu_survei_individu_detail_id = %s"

    cursor.execute(sql_select_data_for_Rokok, (id,))
    data_for_Rokok = cursor.fetchone()

    merokok = data_for_Rokok[0]
    INDIVIDU_MEROKOK = 0

    if merokok == 'Y':
        INDIVIDU_MEROKOK = 1

    dict_Rokok = {
        'INDIVIDU_MEROKOK': INDIVIDU_MEROKOK
    }
    # data yang diambil disimpan pada tipe data dictionary

    return dict_Rokok

def insertDataRokok(db_conn, cursor, Rokok):
    sql_insert_Rokok = "INSERT INTO public.rokok values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT " \
                       "(survei_individu_detail_id) DO UPDATE SET survei_individu_detail_id = excluded.survei_individu_detail_id, " \
                       "survei_rumah_tangga_id = excluded.survei_rumah_tangga_id, survei_id = excluded.survei_id, provinsi_id = excluded.provinsi_id, " \
                       "nama_provinsi = excluded.nama_provinsi, kota_kabupaten_id = excluded.kota_kabupaten_id, nama_kota_kabupaten = excluded.nama_kota_kabupaten, " \
                       "kecamatan_id = excluded.kecamatan_id, nama_kecamatan = excluded.nama_kecamatan, kelurahan_id = excluded.kelurahan_id, " \
                       "nama_kelurahan = excluded.nama_kelurahan,	kd_puskesmas = excluded.kd_puskesmas, nik = excluded.nik , nama = excluded.nama , " \
                       "tgl_lahir = excluded.tgl_lahir, jenis_kelamin = excluded.jenis_kelamin, INDIVIDU_MEROKOK = excluded.INDIVIDU_MEROKOK, " \
                       "updated_at = excluded.updated_at;"

    val = (
        Rokok['survei_individu_detail_id'],
        Rokok['survei_rumah_tangga_id'],
        Rokok['survei_id'],
        Rokok['provinsi_id'],
        Rokok['nama_provinsi'],
        Rokok['kota_kabupaten_id'],
        Rokok['nama_kota_kabupaten'],
        Rokok['kecamatan_id'],
        Rokok['nama_kecamatan'],
        Rokok['kelurahan_id'],
        Rokok['nama_kelurahan'],
        Rokok['kd_puskesmas'],
        Rokok['nik'],
        Rokok['nama'],
        Rokok['tgl_lahir'],
        Rokok['jenis_kelamin'],
        Rokok['INDIVIDU_MEROKOK'],
        Rokok['created_at'],
        Rokok['created_at']
    )

    # variabel val adalah data yang akan di input
    cursor.execute(sql_insert_Rokok, val)
    db_conn.commit()

    return (Rokok['survei_individu_detail_id'])  # cuman variabel kontrol aja

# ==============================
#             JKN
# ==============================

def specificDataForJKN(cursor, id):
    sql_select_data_for_tumbuh_kembang = "SELECT survei_individu_jkn " \
                                         "FROM public.raw_survei " \
                                         "where survei_individu_survei_individu_detail_id = %s"

    cursor.execute(sql_select_data_for_tumbuh_kembang, (id,))
    data_for_JKN = cursor.fetchone()

    kepersertaan_jkn = data_for_JKN[0]

    BELUM_MENJADI_PESERTA_JKN = 0
    PESERTA_JKN = 0

    if kepersertaan_jkn == 'T':
        BELUM_MENJADI_PESERTA_JKN = 1
    else:
        PESERTA_JKN = 1

    dict_JKN = {
        'BELUM_MENJADI_PESERTA_JKN': BELUM_MENJADI_PESERTA_JKN,
        'PESERTA_JKN': PESERTA_JKN
    }
    # data yang diambil disimpan pada tipe data dictionary

    return dict_JKN

def insertDataJKN(db_conn, cursor, JKN):
    sql_insert_JKN = "INSERT INTO public.jkn values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT " \
                     "(survei_individu_detail_id) DO UPDATE SET survei_individu_detail_id = excluded.survei_individu_detail_id, " \
                     "survei_rumah_tangga_id = excluded.survei_rumah_tangga_id, survei_id = excluded.survei_id, provinsi_id = excluded.provinsi_id, " \
                     "nama_provinsi = excluded.nama_provinsi, kota_kabupaten_id = excluded.kota_kabupaten_id, nama_kota_kabupaten = excluded.nama_kota_kabupaten, " \
                     "kecamatan_id = excluded.kecamatan_id, nama_kecamatan = excluded.nama_kecamatan, kelurahan_id = excluded.kelurahan_id, " \
                     "nama_kelurahan = excluded.nama_kelurahan,	kd_puskesmas = excluded.kd_puskesmas, nik = excluded.nik , nama = excluded.nama , " \
                     "tgl_lahir = excluded.tgl_lahir, jenis_kelamin = excluded.jenis_kelamin, BELUM_MENJADI_PESERTA_JKN = excluded.BELUM_MENJADI_PESERTA_JKN, " \
                     "PESERTA_JKN = excluded.PESERTA_JKN, " \
                     "updated_at = excluded.updated_at;"

    val = (
        JKN['survei_individu_detail_id'],
        JKN['survei_rumah_tangga_id'],
        JKN['survei_id'],
        JKN['provinsi_id'],
        JKN['nama_provinsi'],
        JKN['kota_kabupaten_id'],
        JKN['nama_kota_kabupaten'],
        JKN['kecamatan_id'],
        JKN['nama_kecamatan'],
        JKN['kelurahan_id'],
        JKN['nama_kelurahan'],
        JKN['kd_puskesmas'],
        JKN['nik'],
        JKN['nama'],
        JKN['tgl_lahir'],
        JKN['jenis_kelamin'],
        JKN['BELUM_MENJADI_PESERTA_JKN'],
        JKN['PESERTA_JKN'],
        JKN['created_at'],
        JKN['created_at']
    )

    # variabel val adalah data yang akan di input
    cursor.execute(sql_insert_JKN, val)
    db_conn.commit()

    return (JKN['survei_individu_detail_id'])  # cuman variabel kontrol aja

# ==============================
#        Perilaku SAB
# ==============================

def specificDataForPerilakuSAB(cursor, id):
    sql_select_data_for_Perilaku_SAB = "SELECT survei_rt_sab, survei_rt_sat, survei_individu_sab " \
                                       "FROM public.raw_survei " \
                                       "where survei_individu_survei_individu_detail_id = %s"

    cursor.execute(sql_select_data_for_Perilaku_SAB, (id,))
    data_for_Perilaku_SAB = cursor.fetchone()

    tersedia_sarana_air_bersih = data_for_Perilaku_SAB[0]
    jenis_sumber_air_terlindungi = data_for_Perilaku_SAB[1]
    perilaku_penggunaan_air_bersih = data_for_Perilaku_SAB[2]

    IND_SARANA_AIR_BERSIH_TERLINDUNG_PERILAKU = 0

    if tersedia_sarana_air_bersih == 'Y' and jenis_sumber_air_terlindungi == 'Y' and perilaku_penggunaan_air_bersih == 'T':
        IND_SARANA_AIR_BERSIH_TERLINDUNG_PERILAKU = 1

    dict_Perilaku_SAB = {
        'IND_SARANA_AIR_BERSIH_TERLINDUNG_PERILAKU': IND_SARANA_AIR_BERSIH_TERLINDUNG_PERILAKU
    }
    # data yang diambil disimpan pada tipe data dictionary

    return dict_Perilaku_SAB

def insertDataPerilakuSAB(db_conn, cursor, Perilaku_SAB):
    sql_insert_Perilaku_SAB = "INSERT INTO public.perilaku_sab values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT " \
                              "(survei_individu_detail_id) DO UPDATE SET survei_individu_detail_id = excluded.survei_individu_detail_id, " \
                              "survei_rumah_tangga_id = excluded.survei_rumah_tangga_id, survei_id = excluded.survei_id, provinsi_id = excluded.provinsi_id, " \
                              "nama_provinsi = excluded.nama_provinsi, kota_kabupaten_id = excluded.kota_kabupaten_id, nama_kota_kabupaten = excluded.nama_kota_kabupaten, " \
                              "kecamatan_id = excluded.kecamatan_id, nama_kecamatan = excluded.nama_kecamatan, kelurahan_id = excluded.kelurahan_id, " \
                              "nama_kelurahan = excluded.nama_kelurahan,	kd_puskesmas = excluded.kd_puskesmas, nik = excluded.nik , nama = excluded.nama , " \
                              "tgl_lahir = excluded.tgl_lahir, jenis_kelamin = excluded.jenis_kelamin, IND_SARANA_AIR_BERSIH_TERLINDUNG_PERILAKU = excluded.IND_SARANA_AIR_BERSIH_TERLINDUNG_PERILAKU, " \
                              "updated_at = excluded.updated_at;"

    val = (
        Perilaku_SAB['survei_individu_detail_id'],
        Perilaku_SAB['survei_rumah_tangga_id'],
        Perilaku_SAB['survei_id'],
        Perilaku_SAB['provinsi_id'],
        Perilaku_SAB['nama_provinsi'],
        Perilaku_SAB['kota_kabupaten_id'],
        Perilaku_SAB['nama_kota_kabupaten'],
        Perilaku_SAB['kecamatan_id'],
        Perilaku_SAB['nama_kecamatan'],
        Perilaku_SAB['kelurahan_id'],
        Perilaku_SAB['nama_kelurahan'],
        Perilaku_SAB['kd_puskesmas'],
        Perilaku_SAB['nik'],
        Perilaku_SAB['nama'],
        Perilaku_SAB['tgl_lahir'],
        Perilaku_SAB['jenis_kelamin'],
        Perilaku_SAB['IND_SARANA_AIR_BERSIH_TERLINDUNG_PERILAKU'],
        Perilaku_SAB['created_at'],
        Perilaku_SAB['created_at']
    )

    # variabel val adalah data yang akan di input
    cursor.execute(sql_insert_Perilaku_SAB, val)
    db_conn.commit()

    return (Perilaku_SAB['survei_individu_detail_id'])  # cuman variabel kontrol aja

# ==============================
#       Perilaku Jamban
# ==============================

def specificDataForPerilakuJamban(cursor, id):
    sql_select_data_for_Perilaku_Jamban = "SELECT  survei_rt_jk, survei_rt_js, survei_individu_babj " \
                                          "FROM public.raw_survei " \
                                          "where survei_individu_survei_individu_detail_id = %s"

    cursor.execute(sql_select_data_for_Perilaku_Jamban, (id,))
    data_for_Perilaku_Jamban = cursor.fetchone()

    tersedia_jamban_keluarga = data_for_Perilaku_Jamban[0]
    jenis_jamban_saniter = data_for_Perilaku_Jamban[1]
    perilaku_bab_di_jamban = data_for_Perilaku_Jamban[2]

    IND_PUNYA_JAMBAN_SANITER_PERILAKU = 0

    if tersedia_jamban_keluarga == 'Y' and jenis_jamban_saniter == 'Y' and perilaku_bab_di_jamban == 'T':
        IND_PUNYA_JAMBAN_SANITER_PERILAKU = 1

    dict_Perilaku_Jamban = {
        'IND_PUNYA_JAMBAN_SANITER_PERILAKU': IND_PUNYA_JAMBAN_SANITER_PERILAKU
    }
    # data yang diambil disimpan pada tipe data dictionary

    return dict_Perilaku_Jamban

def insertDataPerilakuJamban(db_conn, cursor, Perilaku_Jamban):
    sql_insert_Perilaku_Jamban = "INSERT INTO public.perilaku_jamban values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT " \
                                 "(survei_individu_detail_id) DO UPDATE SET survei_individu_detail_id = excluded.survei_individu_detail_id, " \
                                 "survei_rumah_tangga_id = excluded.survei_rumah_tangga_id, survei_id = excluded.survei_id, provinsi_id = excluded.provinsi_id, " \
                                 "nama_provinsi = excluded.nama_provinsi, kota_kabupaten_id = excluded.kota_kabupaten_id, nama_kota_kabupaten = excluded.nama_kota_kabupaten, " \
                                 "kecamatan_id = excluded.kecamatan_id, nama_kecamatan = excluded.nama_kecamatan, kelurahan_id = excluded.kelurahan_id, " \
                                 "nama_kelurahan = excluded.nama_kelurahan,	kd_puskesmas = excluded.kd_puskesmas, nik = excluded.nik , nama = excluded.nama , " \
                                 "tgl_lahir = excluded.tgl_lahir, jenis_kelamin = excluded.jenis_kelamin, IND_PUNYA_JAMBAN_SANITER_PERILAKU = excluded.IND_PUNYA_JAMBAN_SANITER_PERILAKU, " \
                                 "updated_at = excluded.updated_at;"

    val = (
        Perilaku_Jamban['survei_individu_detail_id'],
        Perilaku_Jamban['survei_rumah_tangga_id'],
        Perilaku_Jamban['survei_id'],
        Perilaku_Jamban['provinsi_id'],
        Perilaku_Jamban['nama_provinsi'],
        Perilaku_Jamban['kota_kabupaten_id'],
        Perilaku_Jamban['nama_kota_kabupaten'],
        Perilaku_Jamban['kecamatan_id'],
        Perilaku_Jamban['nama_kecamatan'],
        Perilaku_Jamban['kelurahan_id'],
        Perilaku_Jamban['nama_kelurahan'],
        Perilaku_Jamban['kd_puskesmas'],
        Perilaku_Jamban['nik'],
        Perilaku_Jamban['nama'],
        Perilaku_Jamban['tgl_lahir'],
        Perilaku_Jamban['jenis_kelamin'],
        Perilaku_Jamban['IND_PUNYA_JAMBAN_SANITER_PERILAKU'],
        Perilaku_Jamban['created_at'],
        Perilaku_Jamban['created_at']
    )

    # variabel val adalah data yang akan di input
    cursor.execute(sql_insert_Perilaku_Jamban, val)
    db_conn.commit()

    return (Perilaku_Jamban['survei_individu_detail_id'])  # cuman variabel kontrol aja

# ==============================
#     Karakterisik Responden
# ==============================

def specificDataKarakteristikResponden(cursor, id):  # fungsi ini untuk tambahan data untuk table Karakteristik Responden
    sql_select_data_for_insert_karakteristik_responden = "SELECT survei_individu_umur_thn, survei_individu_umur_bln, survei_individu_pendidikan_id, " \
                                                         "survei_individu_pekerjaan_id, survei_individu_tanggal_lahir FROM public.raw_survei " \
                                                         "where survei_individu_survei_individu_detail_id = %s"
    # data field yang dipilih tergantung table masing-masing

    cursor.execute(sql_select_data_for_insert_karakteristik_responden, (id,))
    data_for_karakteristik_responden = cursor.fetchone()

    dictKarakteristikResponden = {
        'umur_tahun': data_for_karakteristik_responden[0],
        'umur_bulan': data_for_karakteristik_responden[1],
        'pendidikan_id': data_for_karakteristik_responden[2],
        'pekerjaan_id': data_for_karakteristik_responden[3],
        'tanggal_lahir': data_for_karakteristik_responden[4],
    }
    # data yang diambil disimpan pada tipe data dictionary

    return dictKarakteristikResponden  # mengembalikan nilai tambahan data untuk table Karakteristik Responden

def insertDataKarakteristikResponden(db_conn, cursor, karakteristik_responden, current_date):  # fungsi ini untuk insert data pada table Karakteristik Responden

    sql_insert_karakteristik_responden = "INSERT INTO public.karakteristik_responden values (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
                                         "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT " \
                                         "(survei_individu_detail_id) DO UPDATE SET survei_individu_detail_id = excluded.survei_individu_detail_id, " \
                                         "survei_rumah_tangga_id = excluded.survei_rumah_tangga_id, survei_id = excluded.survei_id, provinsi_id = excluded.provinsi_id, " \
                                         "nama_provinsi = excluded.nama_provinsi, kota_kabupaten_id = excluded.kota_kabupaten_id, nama_kota_kabupaten = excluded.nama_kota_kabupaten, " \
                                         "kecamatan_id = excluded.kecamatan_id, nama_kecamatan = excluded.nama_kecamatan, kelurahan_id = excluded.kelurahan_id, " \
                                         "nama_kelurahan = excluded.nama_kelurahan,	kd_puskesmas = excluded.kd_puskesmas, nik = excluded.nik , nama = excluded.nama , " \
                                         "tgl_lahir = excluded.tgl_lahir, jenis_kelamin = excluded.jenis_kelamin, umur_hari_ini_tahun = excluded.umur_hari_ini_tahun, " \
                                         "umur_tahun = excluded.umur_tahun, umurbulan = excluded.umurbulan, umur_bulan = excluded.umur_bulan, " \
                                         "kategori_umur_bulan = excluded.kategori_umur_bulan, kategori_umur_tahun = excluded.kategori_umur_tahun, " \
                                         "kategori_pendidikan = excluded.kategori_pendidikan, kategori_pekerjaan = excluded.kategori_pekerjaan, " \
                                         "umur_5_sd_9_tahun = excluded.umur_5_sd_9_tahun, umur_10_sd_14_tahun = excluded.umur_10_sd_14_tahun, " \
                                         "umur_15_24_tahun = excluded.umur_15_24_tahun, umur_25_34_tahun = excluded.umur_25_34_tahun, " \
                                         "umur_35_44_tahun = excluded.umur_35_44_tahun, umur_45_54_tahun = excluded.umur_45_54_tahun, " \
                                         "umur_55_64_tahun = excluded.umur_55_64_tahun, umur_65_tahun_keatas = excluded.umur_65_tahun_keatas, updated_at = excluded.updated_at;"

    try:

        umur = (current_date.year - karakteristik_responden['tanggal_lahir'].year)

    except Exception as e:
        umur = -1

    # Field UMUR HARI INI (TAHUN)
    if umur != 0:
        umur_hari_ini = umur
    else:
        umur_hari_ini = 0

    # Field UMUR (TAHUN)
    umur_tahun = karakteristik_responden['umur_tahun']

    # Field UMUR (BULAN)
    umur_bulan_1 = karakteristik_responden['umur_bulan']

    # Field umur bulan
    if karakteristik_responden['umur_tahun'] < 5:
        umur_bulan_2 = karakteristik_responden['umur_tahun'] * 12 + karakteristik_responden['umur_bulan']
    else:
        umur_bulan_2 = None

        # Field Kategori Umur Bulan
    if umur_tahun < 5 and umur_bulan_2 >= 0 and umur_bulan_2 <= 11:
        kategori_umur_bulan = "0-11 bulan"
    elif umur_tahun < 5 and umur_bulan_2 >= 12 and umur_bulan_2 <= 23:
        kategori_umur_bulan = "12-23 bulan"
    elif umur_tahun < 5 and umur_bulan_2 >= 24 and umur_bulan_2 <= 35:
        kategori_umur_bulan = "24-35 bulan"
    elif umur_tahun < 5 and umur_bulan_2 >= 36 and umur_bulan_2 <= 47 :
        kategori_umur_bulan = "36-47 bulan"
    elif umur_tahun < 5 and umur_bulan_2 >= 48 and umur_bulan_2 <= 59:
        kategori_umur_bulan = "48-59 bulan"
    else:
        kategori_umur_bulan = ""

        # Field Kategori Umur Tahun
    if (karakteristik_responden['umur_tahun'] >= 5 and karakteristik_responden['umur_tahun'] <= 9):
        kategori_umur_tahun = "5-9 tahun"
    elif (karakteristik_responden['umur_tahun'] >= 10 and karakteristik_responden['umur_tahun'] <= 14):
        kategori_umur_tahun = "10-14 tahun"
    elif (karakteristik_responden['umur_tahun'] >= 15 and karakteristik_responden['umur_tahun'] <= 24):
        kategori_umur_tahun = "15-24 tahun"
    elif (karakteristik_responden['umur_tahun'] >= 25 and karakteristik_responden['umur_tahun'] <= 34):
        kategori_umur_tahun = "25-34 tahun"
    elif (karakteristik_responden['umur_tahun'] >= 35 and karakteristik_responden['umur_tahun'] <= 44):
        kategori_umur_tahun = "35-44 tahun"
    elif (karakteristik_responden['umur_tahun'] >= 45 and karakteristik_responden['umur_tahun'] <= 54):
        kategori_umur_tahun = "45-54 tahun"
    elif (karakteristik_responden['umur_tahun'] >= 55 and karakteristik_responden['umur_tahun'] <= 64):
        kategori_umur_tahun = "55-64 tahun"
    elif karakteristik_responden['umur_tahun'] >= 65:
        kategori_umur_tahun = "65 tahun keatas"
    else:
        kategori_umur_tahun = ""

        # Field Kategori Pendidikan
    if karakteristik_responden['pendidikan_id'] == 1:
        pendidikan = "Tidak/Belum Sekolah"
    elif karakteristik_responden['pendidikan_id'] == 2:
        pendidikan = "Belum Tamat SD/Sederajat"
    elif karakteristik_responden['pendidikan_id'] == 3:
        pendidikan = "Tamat SD/Sederajat"
    elif karakteristik_responden['pendidikan_id'] == 4:
        pendidikan = "SLTP/Sederajat"
    elif karakteristik_responden['pendidikan_id'] == 5:
        pendidikan = "SLTA/Sederajat"
    elif karakteristik_responden['pendidikan_id'] == 6:
        pendidikan = "Diploma I/II"
    elif karakteristik_responden['pendidikan_id'] == 7:
        pendidikan = "Diploma I/II"
    elif karakteristik_responden['pendidikan_id'] == 8:
        pendidikan = "Diploma I/II"
    elif karakteristik_responden['pendidikan_id'] == 9:
        pendidikan = "Diploma I/II"
    elif karakteristik_responden['pendidikan_id'] == 10:
        pendidikan = "Diploma I/II"
    else:
        pendidikan = ""

        # Field Kategori Pekerjaan
    if karakteristik_responden['pekerjaan_id'] == 1:
        pekerjaan = 'Belum/Tidak Bekerja'
    elif karakteristik_responden['pekerjaan_id'] == 2:
        pekerjaan = 'Mengurus Rumah Tangga'
    elif karakteristik_responden['pekerjaan_id'] == 3:
        pekerjaan = 'Pelajar/Mahasiswa'
    elif karakteristik_responden['pekerjaan_id'] == 4:
        pekerjaan = 'Pensiunan'
    elif karakteristik_responden['pekerjaan_id'] == 5:
        pekerjaan = 'Pegawai Negeri Sipil (PNS)'
    elif karakteristik_responden['pekerjaan_id'] == 6:
        pekerjaan = 'Tentara Nasional Indonesia (TNI)'
    elif karakteristik_responden['pekerjaan_id'] == 7:
        pekerjaan = 'Kepolisian RI (POLRI)'
    elif karakteristik_responden['pekerjaan_id'] == 8:
        pekerjaan = 'Perdagangan'
    elif karakteristik_responden['pekerjaan_id'] == 9:
        pekerjaan = 'Petani/Pekebun'
    elif karakteristik_responden['pekerjaan_id'] == 10:
        pekerjaan = 'Peternak'
    elif karakteristik_responden['pekerjaan_id'] == 11:
        pekerjaan = 'Nelayan/Perikanan'
    elif karakteristik_responden['pekerjaan_id'] == 12:
        pekerjaan = 'Industri'
    elif karakteristik_responden['pekerjaan_id'] == 13:
        pekerjaan = 'Konstruksi'
    elif karakteristik_responden['pekerjaan_id'] == 14:
        pekerjaan = 'Transportasi'
    elif karakteristik_responden['pekerjaan_id'] == 15:
        pekerjaan = 'Karyawan Swasta'
    elif karakteristik_responden['pekerjaan_id'] == 16:
        pekerjaan = 'Karyawan BUMN'
    elif karakteristik_responden['pekerjaan_id'] == 17:
        pekerjaan = 'Karyawan BUMD'
    elif karakteristik_responden['pekerjaan_id'] == 18:
        pekerjaan = 'Karyawan Honorer'
    elif karakteristik_responden['pekerjaan_id'] == 19:
        pekerjaan = 'Buruh Harian Lepas'
    elif karakteristik_responden['pekerjaan_id'] == 20:
        pekerjaan = 'Buruh Tani/Perkebunan'
    elif karakteristik_responden['pekerjaan_id'] == 21:
        pekerjaan = 'Buruh Nelayan/Perikanan'
    elif karakteristik_responden['pekerjaan_id'] == 22:
        pekerjaan = 'Buruh Peternakan'
    elif karakteristik_responden['pekerjaan_id'] == 23:
        pekerjaan = 'Pembantu Rumah Tangga'
    elif karakteristik_responden['pekerjaan_id'] == 24:
        pekerjaan = 'Tukang Cukur'
    elif karakteristik_responden['pekerjaan_id'] == 25:
        pekerjaan = 'Tukang Listrik'
    elif karakteristik_responden['pekerjaan_id'] == 26:
        pekerjaan = 'Tukang Batu'
    elif karakteristik_responden['pekerjaan_id'] == 27:
        pekerjaan = 'Tukang Kayu'
    elif karakteristik_responden['pekerjaan_id'] == 28:
        pekerjaan = 'Tukang Sol Sepatu'
    elif karakteristik_responden['pekerjaan_id'] == 29:
        pekerjaan = 'Tukang Las/Pandai Besi'
    elif karakteristik_responden['pekerjaan_id'] == 30:
        pekerjaan = 'Tukang Jahit'
    elif karakteristik_responden['pekerjaan_id'] == 31:
        pekerjaan = 'Tukang Gigi'
    elif karakteristik_responden['pekerjaan_id'] == 32:
        pekerjaan = 'Penata Rias'
    elif karakteristik_responden['pekerjaan_id'] == 33:
        pekerjaan = 'Penata Busana'
    elif karakteristik_responden['pekerjaan_id'] == 34:
        pekerjaan = 'Penata Rambut'
    elif karakteristik_responden['pekerjaan_id'] == 35:
        pekerjaan = 'Mekanik'
    elif karakteristik_responden['pekerjaan_id'] == 36:
        pekerjaan = 'Seniman'
    elif karakteristik_responden['pekerjaan_id'] == 37:
        pekerjaan = 'Tabib'
    elif karakteristik_responden['pekerjaan_id'] == 38:
        pekerjaan = 'Paraji'
    elif karakteristik_responden['pekerjaan_id'] == 39:
        pekerjaan = 'Perancang Busana'
    elif karakteristik_responden['pekerjaan_id'] == 40:
        pekerjaan = 'Penterjemah'
    elif karakteristik_responden['pekerjaan_id'] == 41:
        pekerjaan = 'Imam Masjid'
    elif karakteristik_responden['pekerjaan_id'] == 42:
        pekerjaan = 'Pendeta'
    elif karakteristik_responden['pekerjaan_id'] == 43:
        pekerjaan = 'Pastor'
    elif karakteristik_responden['pekerjaan_id'] == 44:
        pekerjaan = 'Wartawan'
    elif karakteristik_responden['pekerjaan_id'] == 45:
        pekerjaan = 'Ustadz/Mubaligh'
    elif karakteristik_responden['pekerjaan_id'] == 46:
        pekerjaan = 'Juru Masak'
    elif karakteristik_responden['pekerjaan_id'] == 47:
        pekerjaan = 'Promotor Acara'
    elif karakteristik_responden['pekerjaan_id'] == 48:
        pekerjaan = 'Anggota DPR-RI'
    elif karakteristik_responden['pekerjaan_id'] == 49:
        pekerjaan = 'Anggota DPD'
    elif karakteristik_responden['pekerjaan_id'] == 50:
        pekerjaan = 'Anggota BPK'
    elif karakteristik_responden['pekerjaan_id'] == 51:
        pekerjaan = 'Presiden'
    elif karakteristik_responden['pekerjaan_id'] == 52:
        pekerjaan = 'Wakil Presiden'
    elif karakteristik_responden['pekerjaan_id'] == 53:
        pekerjaan = 'Anggota Mahkamah Konstitusi'
    elif karakteristik_responden['pekerjaan_id'] == 54:
        pekerjaan = 'Anggota Kabinet/Kementrian'
    elif karakteristik_responden['pekerjaan_id'] == 55:
        pekerjaan = 'Duta Besar'
    elif karakteristik_responden['pekerjaan_id'] == 56:
        pekerjaan = 'Gubernur'
    elif karakteristik_responden['pekerjaan_id'] == 57:
        pekerjaan = 'Wakil Gubernur'
    elif karakteristik_responden['pekerjaan_id'] == 58:
        pekerjaan = 'Bupati'
    elif karakteristik_responden['pekerjaan_id'] == 59:
        pekerjaan = 'Wakil Bupati'
    elif karakteristik_responden['pekerjaan_id'] == 60:
        pekerjaan = 'Walikota'
    elif karakteristik_responden['pekerjaan_id'] == 61:
        pekerjaan = 'Wakil Walikota'
    elif karakteristik_responden['pekerjaan_id'] == 62:
        pekerjaan = 'Anggota DPRD Prop.'
    elif karakteristik_responden['pekerjaan_id'] == 63:
        pekerjaan = 'Anggota DPRD Kab./Kota'
    elif karakteristik_responden['pekerjaan_id'] == 64:
        pekerjaan = 'Dosen'
    elif karakteristik_responden['pekerjaan_id'] == 65:
        pekerjaan = 'Guru'
    elif karakteristik_responden['pekerjaan_id'] == 66:
        pekerjaan = 'Pilot'
    elif karakteristik_responden['pekerjaan_id'] == 67:
        pekerjaan = 'Pengacara'
    elif karakteristik_responden['pekerjaan_id'] == 68:
        pekerjaan = 'Notaris'
    elif karakteristik_responden['pekerjaan_id'] == 69:
        pekerjaan = 'Arsitek'
    elif karakteristik_responden['pekerjaan_id'] == 70:
        pekerjaan = 'Akuntan'
    elif karakteristik_responden['pekerjaan_id'] == 71:
        pekerjaan = 'Konsultan'
    elif karakteristik_responden['pekerjaan_id'] == 72:
        pekerjaan = 'Dokter'
    elif karakteristik_responden['pekerjaan_id'] == 73:
        pekerjaan = 'Bidan'
    elif karakteristik_responden['pekerjaan_id'] == 74:
        pekerjaan = 'Perawat'
    elif karakteristik_responden['pekerjaan_id'] == 75:
        pekerjaan = 'Apoteker'
    elif karakteristik_responden['pekerjaan_id'] == 76:
        pekerjaan = 'Psikiater/Psikolog'
    elif karakteristik_responden['pekerjaan_id'] == 77:
        pekerjaan = 'Penyiar Televisi'
    elif karakteristik_responden['pekerjaan_id'] == 78:
        pekerjaan = 'Penyiar Radio'
    elif karakteristik_responden['pekerjaan_id'] == 79:
        pekerjaan = 'Pelaut'
    elif karakteristik_responden['pekerjaan_id'] == 80:
        pekerjaan = 'Peneliti'
    elif karakteristik_responden['pekerjaan_id'] == 81:
        pekerjaan = 'Sopir'
    elif karakteristik_responden['pekerjaan_id'] == 82:
        pekerjaan = 'Pialang'
    elif karakteristik_responden['pekerjaan_id'] == 83:
        pekerjaan = 'Paranormal'
    elif karakteristik_responden['pekerjaan_id'] == 84:
        pekerjaan = 'Pedagang'
    elif karakteristik_responden['pekerjaan_id'] == 85:
        pekerjaan = 'Perangkat Desa'
    elif karakteristik_responden['pekerjaan_id'] == 86:
        pekerjaan = 'Kepala Desa'
    elif karakteristik_responden['pekerjaan_id'] == 87:
        pekerjaan = 'Biarawati'
    elif karakteristik_responden['pekerjaan_id'] == 88:
        pekerjaan = 'Wiraswasta'
    elif karakteristik_responden['pekerjaan_id'] == 89:
        pekerjaan = 'Lainnya'
    else:
        pekerjaan = 'Tidak Menajawab'

    # Field Umur 5_sd_9 Tahun
    if kategori_umur_tahun == "5-9 tahun":
        umur_5_sd_9_tahun = 1
    else:
        umur_5_sd_9_tahun = 0

    # Field Umur 10_sd_14 Tahun
    if kategori_umur_tahun == "10-14 tahun":
        umur_10_sd_9_tahun = 1
    else:
        umur_10_sd_9_tahun = 0

    # Field Umur 15_sd_24 Tahun
    if kategori_umur_tahun == "15-24 tahun":
        umur_15_sd_24_tahun = 1
    else:
        umur_15_sd_24_tahun = 0

    # Field Umur 25_sd_34 Tahun
    if kategori_umur_tahun == "25-34 tahun":
        umur_25_sd_34_tahun = 1
    else:
        umur_25_sd_34_tahun = 0

    # Field Umur 35_sd_44 Tahun
    if kategori_umur_tahun == "35-44 tahun":
        umur_35_sd_44_tahun = 1
    else:
        umur_35_sd_44_tahun = 0

    # Field Umur 45_sd_54 Tahun
    if kategori_umur_tahun == "45-54 tahun":
        umur_45_sd_54_tahun = 1
    else:
        umur_45_sd_54_tahun = 0

    # Field Umur 55_sd_64 Tahun
    if kategori_umur_tahun == "55-64 tahun":
        umur_55_sd_64_tahun = 1
    else:
        umur_55_sd_64_tahun = 0

    # Field Umur 65 Tahun Keatas
    if kategori_umur_tahun == "65 tahun keatas":
        umur_65_tahun_keatas = 0
    else:
        umur_65_tahun_keatas = 0

    val = (
        karakteristik_responden['survei_individu_detail_id'],
        karakteristik_responden['survei_rumah_tangga_id'],
        karakteristik_responden['survei_id'],
        karakteristik_responden['provinsi_id'],
        karakteristik_responden['nama_provinsi'],
        karakteristik_responden['kota_kabupaten_id'],
        karakteristik_responden['nama_kota_kabupaten'],
        karakteristik_responden['kecamatan_id'],
        karakteristik_responden['nama_kecamatan'],
        karakteristik_responden['kelurahan_id'],
        karakteristik_responden['nama_kelurahan'],
        karakteristik_responden['kd_puskesmas'],
        karakteristik_responden['nik'],
        karakteristik_responden['nama'],
        karakteristik_responden['tgl_lahir'],
        karakteristik_responden['jenis_kelamin'],
        umur_hari_ini,
        umur_tahun,
        umur_bulan_1,
        umur_bulan_2,
        kategori_umur_bulan,
        kategori_umur_tahun,
        pendidikan,
        pekerjaan,
        umur_5_sd_9_tahun,
        umur_10_sd_9_tahun,
        umur_15_sd_24_tahun,
        umur_25_sd_34_tahun,
        umur_35_sd_44_tahun,
        umur_45_sd_54_tahun,
        umur_55_sd_64_tahun,
        umur_65_tahun_keatas,
        karakteristik_responden['created_at'],
        karakteristik_responden['created_at']
    )

    cursor.execute(sql_insert_karakteristik_responden, val)
    db_conn.commit()

    return (karakteristik_responden['survei_individu_detail_id'])

# ==============================
#           ROKOkS
# ==============================

def specificDataForROKOkS(cursor, id_individu):
    sql_select_data_for_ROKOkS = "SELECT  survei_individu_umur_thn, survei_individu_merokok " \
                                 "FROM public.raw_survei " \
                                 "where survei_individu_survei_individu_detail_id = %s"

    cursor.execute(sql_select_data_for_ROKOkS, (id_individu,))
    data_for_ROKOkS = cursor.fetchone()

    umur_tahun = data_for_ROKOkS[0]
    individu_merokok = data_for_ROKOkS[1]

    kategori_umur_tahun = ""

    Umur_5_9_tahun = 0
    Umur_10_14_tahun = 0
    Umur_15_24_tahun = 0
    Umur_25_34_tahun = 0
    Umur_35_44_tahun = 0
    Umur_45_54_tahun = 0
    Umur_55_64_tahun = 0
    Umur_65_tahun_keatas = 0

    # Variable DK5 = kategori_umur_tahun
    if umur_tahun >= 5 and umur_tahun <= 9:
        kategori_umur_tahun = "5-9 tahun"
    elif umur_tahun >= 10 and umur_tahun <= 14:
        kategori_umur_tahun = "10-14 tahun"
    elif (umur_tahun >= 15 and umur_tahun <= 24):
        kategori_umur_tahun = "15-24 tahun"
    elif (umur_tahun >= 25 and umur_tahun <= 34):
        kategori_umur_tahun = "25-34 tahun"
    elif (umur_tahun >= 35 and umur_tahun <= 44):
        kategori_umur_tahun = "35-44 tahun"
    elif (umur_tahun >= 45 and umur_tahun <= 54):
        kategori_umur_tahun = "45-54 tahun"
    elif (umur_tahun >= 55 and umur_tahun <= 64):
        kategori_umur_tahun = "55-64 tahun"
    elif umur_tahun >= 65:
        kategori_umur_tahun = "65 tahun keatas"



    # Field DV
    if kategori_umur_tahun == "5-9 tahun" and individu_merokok == 'Y':
        Umur_5_9_tahun = 1
    elif kategori_umur_tahun == "10-14 tahun" and individu_merokok == 'Y':
        Umur_10_14_tahun = 1
    elif kategori_umur_tahun == "15-24 tahun" and individu_merokok == 'Y':
        Umur_15_24_tahun = 1
    elif kategori_umur_tahun == "25-34 tahun" and individu_merokok == 'Y':
        Umur_25_34_tahun = 1
    elif kategori_umur_tahun == "35-44 tahun" and individu_merokok == 'Y':
        Umur_35_44_tahun = 1
    elif kategori_umur_tahun == "45-54 tahun" and individu_merokok == 'Y':
        Umur_45_54_tahun = 1
    elif kategori_umur_tahun == "55-64 tahun" and individu_merokok == 'Y':
        Umur_55_64_tahun = 1
    elif kategori_umur_tahun == "65 tahun keatas" and individu_merokok == 'Y':
        Umur_65_tahun_keatas = 1

    dict_ROKOkS = {
        'Umur_5_9_tahun': Umur_5_9_tahun,
        'Umur_10_14_tahun': Umur_10_14_tahun,
        'Umur_15_24_tahun': Umur_15_24_tahun,
        'Umur_25_34_tahun': Umur_25_34_tahun,
        'Umur_35_44_tahun': Umur_35_44_tahun,
        'Umur_45_54_tahun': Umur_45_54_tahun,
        'Umur_55_64_tahun': Umur_55_64_tahun,
        'Umur_65_tahun_keatas': Umur_65_tahun_keatas
    }
    # data yang diambil disimpan pada tipe data dictionary

    return dict_ROKOkS


def insertDataROKOkS(db_conn, cursor, ROKOkS):
    sql_insert_ROKOkS = "INSERT INTO public.ROKOkS values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT " \
                        "(survei_individu_detail_id) DO UPDATE SET survei_individu_detail_id = excluded.survei_individu_detail_id, " \
                        "survei_rumah_tangga_id = excluded.survei_rumah_tangga_id, survei_id = excluded.survei_id, provinsi_id = excluded.provinsi_id, " \
                        "nama_provinsi = excluded.nama_provinsi, kota_kabupaten_id = excluded.kota_kabupaten_id, nama_kota_kabupaten = excluded.nama_kota_kabupaten, " \
                        "kecamatan_id = excluded.kecamatan_id, nama_kecamatan = excluded.nama_kecamatan, kelurahan_id = excluded.kelurahan_id, " \
                        "nama_kelurahan = excluded.nama_kelurahan,	kd_puskesmas = excluded.kd_puskesmas, nik = excluded.nik , nama = excluded.nama , " \
                        "tgl_lahir = excluded.tgl_lahir, jenis_kelamin = excluded.jenis_kelamin, Umur_5_9_tahun = excluded.Umur_5_9_tahun, " \
                        "Umur_10_14_tahun = excluded.Umur_10_14_tahun,	Umur_15_24_tahun = excluded.Umur_15_24_tahun, " \
                        "Umur_25_34_tahun = excluded.Umur_25_34_tahun, Umur_35_44_tahun = excluded.Umur_35_44_tahun, " \
                        "Umur_45_54_tahun = excluded.Umur_45_54_tahun, Umur_55_64_tahun = excluded.Umur_55_64_tahun, " \
                        "Umur_65_tahun_keatas = excluded.Umur_65_tahun_keatas, updated_at = excluded.updated_at;"

    val = (
        ROKOkS['survei_individu_detail_id'],
        ROKOkS['survei_rumah_tangga_id'],
        ROKOkS['survei_id'],
        ROKOkS['provinsi_id'],
        ROKOkS['nama_provinsi'],
        ROKOkS['kota_kabupaten_id'],
        ROKOkS['nama_kota_kabupaten'],
        ROKOkS['kecamatan_id'],
        ROKOkS['nama_kecamatan'],
        ROKOkS['kelurahan_id'],
        ROKOkS['nama_kelurahan'],
        ROKOkS['kd_puskesmas'],
        ROKOkS['nik'],
        ROKOkS['nama'],
        ROKOkS['tgl_lahir'],
        ROKOkS['jenis_kelamin'],
        ROKOkS["Umur_5_9_tahun"],
        ROKOkS["Umur_10_14_tahun"],
        ROKOkS["Umur_15_24_tahun"],
        ROKOkS["Umur_25_34_tahun"],
        ROKOkS["Umur_35_44_tahun"],
        ROKOkS["Umur_45_54_tahun"],
        ROKOkS["Umur_55_64_tahun"],
        ROKOkS["Umur_65_tahun_keatas"],
        ROKOkS['created_at'],
        ROKOkS['created_at']
    )

    # variabel val adalah data yang akan di input
    cursor.execute(sql_insert_ROKOkS, val)
    db_conn.commit()

    return (ROKOkS['survei_individu_detail_id'])  # cuman variabel kontrol aja


# ==============================
#       Rokok by program
# ==============================

def specificDataForRokokByProgram(cursor, id):
    sql_select_data_for_insert_rokok_by_program = "SELECT survei_individu_merokok, survei_individu_umur_thn FROM public.raw_survei " \
                                                  "where survei_individu_survei_individu_detail_id = %s"

    cursor.execute(sql_select_data_for_insert_rokok_by_program, (id,))
    data_for_rokok_by_program = cursor.fetchone()

    dictRokokByProgram = {
        'merokok' : data_for_rokok_by_program[0],
        'umur_thn': data_for_rokok_by_program[1],
    }

    return dictRokokByProgram

def insertDataRokokByProgram(db_conn, cursor, rokok_by_program):  # fungsi ini untuk insert data pada table SASARAN LIFE CYCLE SPM

    sql_insert_rokok_by_program = "INSERT INTO public.rokok_by_program values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT " \
                                  "(survei_individu_detail_id) DO UPDATE SET survei_individu_detail_id = excluded.survei_individu_detail_id, " \
                                  "survei_rumah_tangga_id = excluded.survei_rumah_tangga_id, survei_id = excluded.survei_id, provinsi_id = excluded.provinsi_id, " \
                                  "nama_provinsi = excluded.nama_provinsi, kota_kabupaten_id = excluded.kota_kabupaten_id, nama_kota_kabupaten = excluded.nama_kota_kabupaten, " \
                                  "kecamatan_id = excluded.kecamatan_id, nama_kecamatan = excluded.nama_kecamatan, kelurahan_id = excluded.kelurahan_id, " \
                                  "nama_kelurahan = excluded.nama_kelurahan, kd_puskesmas = excluded.kd_puskesmas, nik = excluded.nik , nama = excluded.nama , " \
                                  "tgl_lahir = excluded.tgl_lahir, jenis_kelamin = excluded.jenis_kelamin, perokok_umur_10_sd_18_tahun = excluded.perokok_umur_10_sd_18_tahun, " \
                                  "perokok_umur_15_sd_18_tahun = excluded.perokok_umur_15_sd_18_tahun, perokok_umur_diatas_15_tahun = excluded.perokok_umur_diatas_15_tahun, " \
                                  "updated_at = excluded.updated_at;"

    perokok_umur_10_sd_18_tahun = 0
    perokok_umur_15_sd_18_tahun = 0
    perokok_umur_lebih_besar_15_tahun = 0

    if rokok_by_program['umur_thn'] >= 10 and rokok_by_program['umur_thn'] <= 18 and rokok_by_program['merokok'] == 'Y':
        perokok_umur_10_sd_18_tahun = 1
    if rokok_by_program['umur_thn'] >= 15 and rokok_by_program['umur_thn'] <= 18 and rokok_by_program['merokok'] == 'Y':
        perokok_umur_15_sd_18_tahun = 1
    if rokok_by_program['umur_thn'] >= 15 and rokok_by_program['merokok'] == 'Y':
        perokok_umur_lebih_besar_15_tahun = 1

    val = (
        rokok_by_program['survei_individu_detail_id'],
        rokok_by_program['survei_rumah_tangga_id'],
        rokok_by_program['survei_id'],
        rokok_by_program['provinsi_id'],
        rokok_by_program['nama_provinsi'],
        rokok_by_program['kota_kabupaten_id'],
        rokok_by_program['nama_kota_kabupaten'],
        rokok_by_program['kecamatan_id'],
        rokok_by_program['nama_kecamatan'],
        rokok_by_program['kelurahan_id'],
        rokok_by_program['nama_kelurahan'],
        rokok_by_program['kd_puskesmas'],
        rokok_by_program['nik'],
        rokok_by_program['nama'],
        rokok_by_program['tgl_lahir'],
        rokok_by_program['jenis_kelamin'],
        perokok_umur_10_sd_18_tahun,
        perokok_umur_15_sd_18_tahun,
        perokok_umur_lebih_besar_15_tahun,
        rokok_by_program['created_at'],
        rokok_by_program['created_at']
    )

    # variabel val adalah data yang akan di input
    cursor.execute(sql_insert_rokok_by_program, val)
    cursor.execute("ROLLBACK")
    db_conn.commit()

    return (rokok_by_program['survei_individu_detail_id'])  # cuman variabel kontrol aja

# ==============================
#    Rokok by prorgram (Umur)
# ==============================

def specificDataForRokokByProgramUmur(cursor, id):
    sql_select_data_for_insert_rokok_by_program_umur = "SELECT survei_individu_umur_thn FROM public.raw_survei where survei_individu_survei_individu_detail_id = %s"

    cursor.execute(sql_select_data_for_insert_rokok_by_program_umur, (id,))
    data_for_rokok_by_program_umur = cursor.fetchone()

    dictRokokByProgramUmur = {
        'umur_thn': data_for_rokok_by_program_umur[0]
    }

    return dictRokokByProgramUmur

def insertDataRokokByProgramUmur(db_conn, cursor, rokok_by_program_umur):  # fungsi ini untuk insert data pada table SASARAN LIFE CYCLE SPM

    sql_insert_rokok_by_program_umur = "INSERT INTO public.rokok_by_program_umur values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT " \
                                       "(survei_individu_detail_id) DO UPDATE SET survei_individu_detail_id = excluded.survei_individu_detail_id, " \
                                       "survei_rumah_tangga_id = excluded.survei_rumah_tangga_id, survei_id = excluded.survei_id, provinsi_id = excluded.provinsi_id, " \
                                       "nama_provinsi = excluded.nama_provinsi, kota_kabupaten_id = excluded.kota_kabupaten_id, nama_kota_kabupaten = excluded.nama_kota_kabupaten, " \
                                       "kecamatan_id = excluded.kecamatan_id, nama_kecamatan = excluded.nama_kecamatan, kelurahan_id = excluded.kelurahan_id, " \
                                       "nama_kelurahan = excluded.nama_kelurahan, kd_puskesmas = excluded.kd_puskesmas, nik = excluded.nik , nama = excluded.nama, " \
                                       "tgl_lahir = excluded.tgl_lahir, jenis_kelamin = excluded.jenis_kelamin, jumlah_umur_10_sd_18_tahun = excluded.jumlah_umur_10_sd_18_tahun, " \
                                       "jumlah_umur_15_sd_18_tahun = excluded.jumlah_umur_15_sd_18_tahun, jumlah_umur_diatas_15_tahun = excluded.jumlah_umur_diatas_15_tahun, " \
                                       "updated_at = excluded.updated_at;"

    umur_10_sd_18_tahun = 0
    umur_15_sd_18_tahun = 0
    umur_lebih_besar_15_tahun = 0

    if rokok_by_program_umur['umur_thn'] >= 10 and rokok_by_program_umur['umur_thn'] <= 18:
        umur_10_sd_18_tahun = 1
    if rokok_by_program_umur['umur_thn'] >= 15 and rokok_by_program_umur['umur_thn'] <= 18:
        umur_15_sd_18_tahun = 1
    if rokok_by_program_umur['umur_thn'] >= 15:
        umur_lebih_besar_15_tahun = 1

    val = (
        rokok_by_program_umur['survei_individu_detail_id'],
        rokok_by_program_umur['survei_rumah_tangga_id'],
        rokok_by_program_umur['survei_id'],
        rokok_by_program_umur['provinsi_id'],
        rokok_by_program_umur['nama_provinsi'],
        rokok_by_program_umur['kota_kabupaten_id'],
        rokok_by_program_umur['nama_kota_kabupaten'],
        rokok_by_program_umur['kecamatan_id'],
        rokok_by_program_umur['nama_kecamatan'],
        rokok_by_program_umur['kelurahan_id'],
        rokok_by_program_umur['nama_kelurahan'],
        rokok_by_program_umur['kd_puskesmas'],
        rokok_by_program_umur['nik'],
        rokok_by_program_umur['nama'],
        rokok_by_program_umur['tgl_lahir'],
        rokok_by_program_umur['jenis_kelamin'],
        umur_10_sd_18_tahun,
        umur_15_sd_18_tahun,
        umur_lebih_besar_15_tahun,
        rokok_by_program_umur['created_at'],
        rokok_by_program_umur['created_at']
    )

    # variabel val adalah data yang akan di input
    cursor.execute(sql_insert_rokok_by_program_umur, val)
    db_conn.commit()

    return (rokok_by_program_umur['survei_individu_detail_id'])  # cuman variabel kontrol aja

# ==============================
#       Denominator KB
# ==============================

def specificDataForDenominatorKB(cursor, id):
    sql_select_data_for_insert_denominator_KB = "SELECT survei_individu_umur_thn, survei_individu_stmarital_id " \
                                                "FROM public.raw_survei where survei_individu_survei_individu_detail_id = %s"

    cursor.execute(sql_select_data_for_insert_denominator_KB, (id,))
    data_for_keluarga_berencana = cursor.fetchone()

    dictDenominatorKB = {
        'umur_tahun' : data_for_keluarga_berencana[0],
        'status_kawin': data_for_keluarga_berencana[1]
    }

    return dictDenominatorKB

def insertDataDenominatorKB(db_conn, cursor, denominator_KB):
    sql_insert_rokok_by_denominator_KB = "INSERT INTO public.denominator_kb values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT " \
                                       "(survei_individu_detail_id) DO UPDATE SET survei_individu_detail_id = excluded.survei_individu_detail_id, " \
                                       "survei_rumah_tangga_id = excluded.survei_rumah_tangga_id, survei_id = excluded.survei_id, provinsi_id = excluded.provinsi_id, " \
                                       "nama_provinsi = excluded.nama_provinsi, kota_kabupaten_id = excluded.kota_kabupaten_id, nama_kota_kabupaten = excluded.nama_kota_kabupaten, " \
                                       "kecamatan_id = excluded.kecamatan_id, nama_kecamatan = excluded.nama_kecamatan, kelurahan_id = excluded.kelurahan_id, " \
                                       "nama_kelurahan = excluded.nama_kelurahan, kd_puskesmas = excluded.kd_puskesmas, nik = excluded.nik , nama = excluded.nama, " \
                                       "tgl_lahir = excluded.tgl_lahir, jenis_kelamin = excluded.jenis_kelamin, wanita_kawin_tidak_hamil_umur_10_sd_14 = excluded.wanita_kawin_tidak_hamil_umur_10_sd_14, " \
                                       "wanita_kawin_tidak_hamil_umur_15_sd_49 = excluded.wanita_kawin_tidak_hamil_umur_15_sd_49, " \
                                        "wanita_kawin_tidak_hamil_umur_50_sd_54 = excluded.wanita_kawin_tidak_hamil_umur_50_sd_54, " \
                                       "updated_at = excluded.updated_at;"

    wanita_kawin_tidak_hamil_umur_10_sd_14 = 0
    wanita_kawin_tidak_hamil_umur_15_sd_49 = 0
    wanita_kawin_tidak_hamil_umur_50_sd_54 = 0

    if denominator_KB['umur_tahun'] >= 10 and denominator_KB['umur_tahun'] <= 14 and denominator_KB[
        'jenis_kelamin'] == 'Perempuan' and denominator_KB['status_kawin'] == 1:
        wanita_kawin_tidak_hamil_umur_10_sd_14 = 1

    if denominator_KB['umur_tahun'] >= 15 and denominator_KB['umur_tahun'] <= 49 and denominator_KB[
        'jenis_kelamin'] == 'Perempuan' and denominator_KB['status_kawin'] == 1:
        wanita_kawin_tidak_hamil_umur_15_sd_49 = 1

    if denominator_KB['umur_tahun'] >= 50 and denominator_KB['umur_tahun'] <= 54 and denominator_KB[
        'jenis_kelamin'] == 'Perempuan' and denominator_KB['status_kawin'] == 1:
        wanita_kawin_tidak_hamil_umur_50_sd_54 = 1

    val = (
            denominator_KB['survei_individu_detail_id'],
            denominator_KB['survei_rumah_tangga_id'],
            denominator_KB['survei_id'],
            denominator_KB['provinsi_id'],
            denominator_KB['nama_provinsi'],
            denominator_KB['kota_kabupaten_id'],
            denominator_KB['nama_kota_kabupaten'],
            denominator_KB['kecamatan_id'],
            denominator_KB['nama_kecamatan'],
            denominator_KB['kelurahan_id'],
            denominator_KB['nama_kelurahan'],
            denominator_KB['kd_puskesmas'],
            denominator_KB['nik'],
            denominator_KB['nama'],
            denominator_KB['tgl_lahir'],
            denominator_KB['jenis_kelamin'],
            wanita_kawin_tidak_hamil_umur_10_sd_14,
            wanita_kawin_tidak_hamil_umur_15_sd_49,
            wanita_kawin_tidak_hamil_umur_50_sd_54,
            denominator_KB['created_at'],
            denominator_KB['created_at']
        )
            # variabel val adalah data yang akan di input
    cursor.execute(sql_insert_rokok_by_denominator_KB, val)
    db_conn.commit()

    return (denominator_KB['survei_individu_detail_id'])

# ==============================
#       KB by Program
# ==============================

def specificDataForKBbyProgram(cursor, id):
    sql_select_data_for_KB_by_Program = "SELECT  survei_individu_umur_thn, survei_individu_jk_id, survei_individu_stmarital_id, survei_individu_kb " \
                                        "FROM public.raw_survei " \
                                        "where survei_individu_survei_individu_detail_id = %s"

    cursor.execute(sql_select_data_for_KB_by_Program, (id,))
    data_for_KB_by_Program = cursor.fetchone()

    umur_tahun = data_for_KB_by_Program[0]

    if data_for_KB_by_Program[1] == 1:
        jenis_kelamin = 'Laki-Laki'
    else:
        jenis_kelamin = 'Perempuan'

    if data_for_KB_by_Program[2] == 1:
        status_kawin = 'kawin'
    else:
        status_kawin = 'tidak kawin'

    status_kb = data_for_KB_by_Program[3]

    WANITA_KAWIN_TIDAK_HAMIL_UMUR_10_sd_14_BER_sd_KB = 0
    WANITA_KAWIN_TIDAK_HAMIL_UMUR_15_sd_49_BER_sd_KB = 0
    WANITA_KAWIN_TIDAK_HAMIL_UMUR_50_sd_54_BER_sd_KB = 0
    WANITA_KAWIN_TIDAK_HAMIL_UMUR_10_sd_14_TIDAK_BER_sd_KB = 0
    WANITA_KAWIN_TIDAK_HAMIL_UMUR_15_sd_49_TIDAK_BER_sd_KB = 0
    WANITA_KAWIN_TIDAK_HAMIL_UMUR_50_sd_54_TIDAK_BER_sd_KB = 0

    # Field EN
    if umur_tahun >= 10 and umur_tahun <= 14:
        if jenis_kelamin == 'Perempuan' and status_kawin == 'kawin' and status_kb == 'Y':
            WANITA_KAWIN_TIDAK_HAMIL_UMUR_10_sd_14_BER_sd_KB = 1

    # Field EO
    if umur_tahun >= 15 and umur_tahun <= 49:
        if jenis_kelamin == 'Perempuan' and status_kawin == 'kawin' and status_kb == 'Y':
            WANITA_KAWIN_TIDAK_HAMIL_UMUR_15_sd_49_BER_sd_KB = 1

    # Field EP
    if umur_tahun >= 50 and umur_tahun <= 54:
        if jenis_kelamin == 'Perempuan' and status_kawin == 'kawin' and status_kb == 'Y':
            WANITA_KAWIN_TIDAK_HAMIL_UMUR_50_sd_54_BER_sd_KB = 1

    # Field EQ
    if umur_tahun >= 10 and umur_tahun <= 14:
        if jenis_kelamin == 'Perempuan' and status_kawin == 'kawin' and status_kb == 'T':
            WANITA_KAWIN_TIDAK_HAMIL_UMUR_10_sd_14_TIDAK_BER_sd_KB = 1

    # Field ER
    if umur_tahun >= 15 and umur_tahun <= 49:
        if jenis_kelamin == 'Perempuan' and status_kawin == 'kawin' and status_kb == 'T':
            WANITA_KAWIN_TIDAK_HAMIL_UMUR_15_sd_49_TIDAK_BER_sd_KB = 1

    # Field ES
    if umur_tahun >= 50 and umur_tahun <= 54:
        if jenis_kelamin == 'Perempuan' and status_kawin == 'kawin' and status_kb == 'T':
            WANITA_KAWIN_TIDAK_HAMIL_UMUR_50_sd_54_TIDAK_BER_sd_KB = 1

    dict_KB_by_Program = {
        'WANITA_KAWIN_TIDAK_HAMIL_UMUR_10_sd_14_BER_sd_KB': WANITA_KAWIN_TIDAK_HAMIL_UMUR_10_sd_14_BER_sd_KB,
        'WANITA_KAWIN_TIDAK_HAMIL_UMUR_15_sd_49_BER_sd_KB': WANITA_KAWIN_TIDAK_HAMIL_UMUR_15_sd_49_BER_sd_KB,
        'WANITA_KAWIN_TIDAK_HAMIL_UMUR_50_sd_54_BER_sd_KB': WANITA_KAWIN_TIDAK_HAMIL_UMUR_50_sd_54_BER_sd_KB,
        'WANITA_KAWIN_TIDAK_HAMIL_UMUR_10_sd_14_TIDAK_BER_sd_KB': WANITA_KAWIN_TIDAK_HAMIL_UMUR_10_sd_14_TIDAK_BER_sd_KB,
        'WANITA_KAWIN_TIDAK_HAMIL_UMUR_15_sd_49_TIDAK_BER_sd_KB': WANITA_KAWIN_TIDAK_HAMIL_UMUR_15_sd_49_TIDAK_BER_sd_KB,
        'WANITA_KAWIN_TIDAK_HAMIL_UMUR_50_sd_54_TIDAK_BER_sd_KB': WANITA_KAWIN_TIDAK_HAMIL_UMUR_50_sd_54_TIDAK_BER_sd_KB,
    }
    # data yang diambil disimpan pada tipe data dictionary

    return dict_KB_by_Program

def insertDataKBbyProgram(db_conn, cursor, KB_by_Program):
    sql_insert_KB_by_Program = "INSERT INTO public.KB_by_Program values (%s,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT " \
                               "(survei_individu_detail_id) DO UPDATE SET survei_individu_detail_id = excluded.survei_individu_detail_id, " \
                               "survei_rumah_tangga_id = excluded.survei_rumah_tangga_id, survei_id = excluded.survei_id, provinsi_id = excluded.provinsi_id, " \
                               "nama_provinsi = excluded.nama_provinsi, kota_kabupaten_id = excluded.kota_kabupaten_id, nama_kota_kabupaten = excluded.nama_kota_kabupaten, " \
                               "kecamatan_id = excluded.kecamatan_id, nama_kecamatan = excluded.nama_kecamatan, kelurahan_id = excluded.kelurahan_id, " \
                               "nama_kelurahan = excluded.nama_kelurahan,	kd_puskesmas = excluded.kd_puskesmas, nik = excluded.nik , nama = excluded.nama , " \
                               "tgl_lahir = excluded.tgl_lahir, jenis_kelamin = excluded.jenis_kelamin, WANITA_KAWIN_TIDAK_HAMIL_UMUR_10_sd_14_BER_sd_KB = excluded.WANITA_KAWIN_TIDAK_HAMIL_UMUR_10_sd_14_BER_sd_KB, " \
                               "WANITA_KAWIN_TIDAK_HAMIL_UMUR_15_sd_49_BER_sd_KB = excluded.WANITA_KAWIN_TIDAK_HAMIL_UMUR_15_sd_49_BER_sd_KB,	WANITA_KAWIN_TIDAK_HAMIL_UMUR_50_sd_54_BER_sd_KB = excluded.WANITA_KAWIN_TIDAK_HAMIL_UMUR_50_sd_54_BER_sd_KB, " \
                               "WANITA_KAWIN_TIDAK_HAMIL_UMUR_10_sd_14_TIDAK_BER_sd_KB = excluded.WANITA_KAWIN_TIDAK_HAMIL_UMUR_10_sd_14_TIDAK_BER_sd_KB, WANITA_KAWIN_TIDAK_HAMIL_UMUR_15_sd_49_TIDAK_BER_sd_KB = excluded.WANITA_KAWIN_TIDAK_HAMIL_UMUR_15_sd_49_TIDAK_BER_sd_KB, " \
                               "WANITA_KAWIN_TIDAK_HAMIL_UMUR_50_sd_54_TIDAK_BER_sd_KB = excluded.WANITA_KAWIN_TIDAK_HAMIL_UMUR_50_sd_54_TIDAK_BER_sd_KB, updated_at = excluded.updated_at;"

    val = (
        KB_by_Program['survei_individu_detail_id'],
        KB_by_Program['survei_rumah_tangga_id'],
        KB_by_Program['survei_id'],
        KB_by_Program['provinsi_id'],
        KB_by_Program['nama_provinsi'],
        KB_by_Program['kota_kabupaten_id'],
        KB_by_Program['nama_kota_kabupaten'],
        KB_by_Program['kecamatan_id'],
        KB_by_Program['nama_kecamatan'],
        KB_by_Program['kelurahan_id'],
        KB_by_Program['nama_kelurahan'],
        KB_by_Program['kd_puskesmas'],
        KB_by_Program['nik'],
        KB_by_Program['nama'],
        KB_by_Program['tgl_lahir'],
        KB_by_Program['jenis_kelamin'],
        KB_by_Program["WANITA_KAWIN_TIDAK_HAMIL_UMUR_10_sd_14_BER_sd_KB"],
        KB_by_Program["WANITA_KAWIN_TIDAK_HAMIL_UMUR_15_sd_49_BER_sd_KB"],
        KB_by_Program["WANITA_KAWIN_TIDAK_HAMIL_UMUR_50_sd_54_BER_sd_KB"],
        KB_by_Program["WANITA_KAWIN_TIDAK_HAMIL_UMUR_10_sd_14_TIDAK_BER_sd_KB"],
        KB_by_Program["WANITA_KAWIN_TIDAK_HAMIL_UMUR_15_sd_49_TIDAK_BER_sd_KB"],
        KB_by_Program["WANITA_KAWIN_TIDAK_HAMIL_UMUR_50_sd_54_TIDAK_BER_sd_KB"],
        KB_by_Program['created_at'],
        KB_by_Program['created_at']
    )

    # variabel val adalah data yang akan di input
    cursor.execute(sql_insert_KB_by_Program, val)
    db_conn.commit()

    return (KB_by_Program['survei_individu_detail_id'])  # cuman variabel kontrol aja

# ==============================
#     Insert / update log
# ==============================

def insertUpdateLog(db_conn, cursor, survei_individu_detail_id, id_exist, execute_success, updated_at):
    sql_insert_update_log = "INSERT INTO public.log values (%s,%s, %s,%s) ON CONFLICT (survei_individu_detail_id) DO UPDATE SET " \
                            "survei_individu_detail_id = excluded.survei_individu_detail_id, id_exist = excluded.id_exist, execute_success = excluded.execute_success," \
                            "updated_at = excluded.updated_at;"
    val = (survei_individu_detail_id, id_exist, execute_success, updated_at)
    cursor.execute(sql_insert_update_log, val)
    db_conn.commit()

# ==============================
#       Cek Umur
# ==============================

def cekUmur(cursor, id_individu):
    sql_cek_umur = "SELECT survei_individu_umur_thn, survei_individu_umur_bln FROM public.raw_survei where survei_individu_survei_individu_detail_id = %s"

    cursor.execute(sql_cek_umur, (id_individu,))
    data_cek = cursor.fetchone()

    if data_cek == None:
        return 404
    elif data_cek[0] == None and data_cek[1] == None:
        return 400

    return 200

# ==============================
#       Close DB
# ==============================

def closeDB(db_conn, cursor):
    cursor.close()
    db_conn.close()