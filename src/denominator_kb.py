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