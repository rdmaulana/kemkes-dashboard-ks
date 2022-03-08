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