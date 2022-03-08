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