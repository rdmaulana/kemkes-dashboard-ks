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