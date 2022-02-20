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