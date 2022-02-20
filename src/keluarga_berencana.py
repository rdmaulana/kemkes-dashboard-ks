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