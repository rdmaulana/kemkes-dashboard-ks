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