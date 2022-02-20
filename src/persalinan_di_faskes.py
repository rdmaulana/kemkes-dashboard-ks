# ==============================
#     Persalinan di Faskes
# ==============================


def specificDataForPersalinanDiFaskes(cursor, id):
    sql_select_data_for_insert_persalinan_di_faskes = "SELECT survei_individu_faskes FROM public.raw_survei " \
                                                        "where survei_individu_survei_individu_detail_id = %s"

    cursor.execute(sql_select_data_for_insert_persalinan_di_faskes, (id,))
    data_for_persalinan_di_faskes = cursor.fetchone()

    dictPersalinanDiFaskes = {
        'faskes' : data_for_persalinan_di_faskes[0],
    }

    return dictPersalinanDiFaskes


def insertDataPersalinanDiFaskes(db_conn, cursor, persalinan_di_faskes):
    sql_insert_persalinan_di_faskes = "INSERT INTO public.persalinan_di_faskes VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) " \
                                      "ON CONFLICT (survei_individu_detail_id) DO UPDATE SET survei_individu_detail_id = excluded.survei_individu_detail_id, " \
                                      "survei_rumah_tangga_id = excluded.survei_rumah_tangga_id, survei_id = excluded.survei_id, provinsi_id = excluded.provinsi_id, " \
                                      "nama_provinsi = excluded.nama_provinsi, kota_kabupaten_id = excluded.kota_kabupaten_id, nama_kota_kabupaten = excluded.nama_kota_kabupaten, " \
                                      "kecamatan_id = excluded.kecamatan_id, nama_kecamatan = excluded.nama_kecamatan, kelurahan_id = excluded.kelurahan_id, " \
                                      "nama_kelurahan = excluded.nama_kelurahan,	kd_puskesmas = excluded.kd_puskesmas, nik = excluded.nik , nama = excluded.nama , " \
                                      "tgl_lahir = excluded.tgl_lahir, jenis_kelamin = excluded.jenis_kelamin, " \
                                      "ibu_dengan_anak_usia_0_sd_11_bulan = excluded.ibu_dengan_anak_usia_0_sd_11_bulan, " \
                                      "persalinan_tidak_di_faskes = excluded.persalinan_tidak_di_faskes, updated_at = excluded.updated_at;"

    ibu_dengan_anak_usia_0_sd_11_bulan = 0
    persalinan_tidak_di_faskes = 0

    if persalinan_di_faskes['faskes'] == 'Y' or persalinan_di_faskes['faskes'] == 'T':
        ibu_dengan_anak_usia_0_sd_11_bulan = 1
    if ibu_dengan_anak_usia_0_sd_11_bulan == 1 and persalinan_di_faskes['faskes'] == 'T':
        persalinan_tidak_di_faskes = 1

    val = (
        persalinan_di_faskes['survei_individu_detail_id'],
        persalinan_di_faskes['survei_rumah_tangga_id'],
        persalinan_di_faskes['survei_id'],
        persalinan_di_faskes['provinsi_id'],
        persalinan_di_faskes['nama_provinsi'],
        persalinan_di_faskes['kota_kabupaten_id'],
        persalinan_di_faskes['nama_kota_kabupaten'],
        persalinan_di_faskes['kecamatan_id'],
        persalinan_di_faskes['nama_kecamatan'],
        persalinan_di_faskes['kelurahan_id'],
        persalinan_di_faskes['nama_kelurahan'],
        persalinan_di_faskes['kd_puskesmas'],
        persalinan_di_faskes['nik'],
        persalinan_di_faskes['nama'],
        persalinan_di_faskes['tgl_lahir'],
        persalinan_di_faskes['jenis_kelamin'],
        ibu_dengan_anak_usia_0_sd_11_bulan,
        persalinan_tidak_di_faskes,
        persalinan_di_faskes['created_at']
    )

    cursor.execute(sql_insert_persalinan_di_faskes, val)
    db_conn.commit()