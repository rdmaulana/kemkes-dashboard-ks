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