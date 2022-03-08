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