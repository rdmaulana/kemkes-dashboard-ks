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