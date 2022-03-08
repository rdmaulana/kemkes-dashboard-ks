# ==============================
#         Hipertensi
# ==============================


def specificDataForHipertensi(cursor, id):
    sql_select_data_for_KB_by_Program = "SELECT survei_individu_umur_thn, survei_individu_hipertensi, survei_individu_obat_hipertensi, survei_individu_tekanan_darah, survei_individu_sistolik, survei_individu_diastolik " \
                                        "FROM public.raw_survei " \
                                        "where survei_individu_survei_individu_detail_id = %s"

    cursor.execute(sql_select_data_for_KB_by_Program, (id,))
    data_for_Hipertensi = cursor.fetchone()

    # Yang dibutuhkan: umur_tahun, di_diagnosis_hipertensi, minum_obat_hipertensi_teratur
    # dilakukan_pengukuran_tekanan_darah, sistol, diastol

    umur_tahun = data_for_Hipertensi[0]
    di_diagnosis_hipertensi = data_for_Hipertensi[1]
    minum_obat_hipertensi_teratur = data_for_Hipertensi[2]
    dilakukan_pengukuran_tekanan_darah = data_for_Hipertensi[3]

    DIDIAGNOSIS_HIPERTENSI = 0
    INDIVIDU_DIDIAGNOSIS_TAPI_TIDAK_MINUM_OBAT_HIPERTENSI = 0
    INDIVIDU_DIDIAGNOSIS_HIPERTENSI_MINUM_OBAT_SESUAI_STANDAR = 0
    DIUKUR_TEKANAN_DARAH = 0
    SISTOL = data_for_Hipertensi[4]
    DIASTOL = data_for_Hipertensi[5]
    SUSPEK_TEKANAN_DARAH_TINGGI = 0

    # Field CT
    CO5 = 0

    if umur_tahun >= 15:
        CO5 = 1

    if CO5 == 1 and di_diagnosis_hipertensi == 'Y':
        DIDIAGNOSIS_HIPERTENSI = 1

    # Field CU
    if CO5 == 1 and DIDIAGNOSIS_HIPERTENSI == 1 and minum_obat_hipertensi_teratur == 'T':
        INDIVIDU_DIDIAGNOSIS_TAPI_TIDAK_MINUM_OBAT_HIPERTENSI = 1

    # Field CV
    if CO5 == 1 and DIDIAGNOSIS_HIPERTENSI == 1 and minum_obat_hipertensi_teratur == 'Y':
        INDIVIDU_DIDIAGNOSIS_HIPERTENSI_MINUM_OBAT_SESUAI_STANDAR = 1

    # Field CW
    if CO5 == 1 and dilakukan_pengukuran_tekanan_darah == 'Y':
        DIUKUR_TEKANAN_DARAH = 1



    # Field CZ
    if data_for_Hipertensi == 1 and SISTOL >= 140 and DIASTOL >= 90:
        SUSPEK_TEKANAN_DARAH_TINGGI = 1

    dict_Hipertensi = {
        'DIDIAGNOSIS_HIPERTENSI': DIDIAGNOSIS_HIPERTENSI,
        'INDIVIDU_DIDIAGNOSIS_TAPI_TIDAK_MINUM_OBAT_HIPERTENSI': INDIVIDU_DIDIAGNOSIS_TAPI_TIDAK_MINUM_OBAT_HIPERTENSI,
        'INDIVIDU_DIDIAGNOSIS_HIPERTENSI_MINUM_OBAT_SESUAI_STANDAR': INDIVIDU_DIDIAGNOSIS_HIPERTENSI_MINUM_OBAT_SESUAI_STANDAR,
        'DIUKUR_TEKANAN_DARAH': DIUKUR_TEKANAN_DARAH,
        'SISTOL': SISTOL,
        'DIASTOL': DIASTOL,
        'SUSPEK_TEKANAN_DARAH_TINGGI': SUSPEK_TEKANAN_DARAH_TINGGI
    }
    # data yang diambil disimpan pada tipe data dictionary

    return dict_Hipertensi


def insertDataHipertensi(db_conn, cursor, Hipertensi):
    sql_insert_Hipertensi = "INSERT INTO public.HIPERTENSI values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT " \
                            "(survei_individu_detail_id) DO UPDATE SET survei_individu_detail_id = excluded.survei_individu_detail_id, " \
                            "survei_rumah_tangga_id = excluded.survei_rumah_tangga_id, survei_id = excluded.survei_id, provinsi_id = excluded.provinsi_id, " \
                            "nama_provinsi = excluded.nama_provinsi, kota_kabupaten_id = excluded.kota_kabupaten_id, nama_kota_kabupaten = excluded.nama_kota_kabupaten, " \
                            "kecamatan_id = excluded.kecamatan_id, nama_kecamatan = excluded.nama_kecamatan, kelurahan_id = excluded.kelurahan_id, " \
                            "nama_kelurahan = excluded.nama_kelurahan,	kd_puskesmas = excluded.kd_puskesmas, nik = excluded.nik , nama = excluded.nama , " \
                            "tgl_lahir = excluded.tgl_lahir, jenis_kelamin = excluded.jenis_kelamin, DIDIAGNOSIS_HIPERTENSI = excluded.DIDIAGNOSIS_HIPERTENSI, " \
                            "INDIVIDU_DIDIAGNOSIS_TAPI_TIDAK_MINUM_OBAT_HIPERTENSI = excluded.INDIVIDU_DIDIAGNOSIS_TAPI_TIDAK_MINUM_OBAT_HIPERTENSI,	INDIVIDU_DIDIAGNOSIS_HIPERTENSI_MINUM_OBAT_SESUAI_STANDAR = excluded.INDIVIDU_DIDIAGNOSIS_HIPERTENSI_MINUM_OBAT_SESUAI_STANDAR, " \
                            "DIUKUR_TEKANAN_DARAH = excluded.DIUKUR_TEKANAN_DARAH, SISTOL = excluded.SISTOL, DIASTOL = excluded.DIASTOL, " \
                            "SUSPEK_TEKANAN_DARAH_TINGGI = excluded.SUSPEK_TEKANAN_DARAH_TINGGI, updated_at = excluded.updated_at;"

    val = (
        Hipertensi['survei_individu_detail_id'],
        Hipertensi['survei_rumah_tangga_id'],
        Hipertensi['survei_id'],
        Hipertensi['provinsi_id'],
        Hipertensi['nama_provinsi'],
        Hipertensi['kota_kabupaten_id'],
        Hipertensi['nama_kota_kabupaten'],
        Hipertensi['kecamatan_id'],
        Hipertensi['nama_kecamatan'],
        Hipertensi['kelurahan_id'],
        Hipertensi['nama_kelurahan'],
        Hipertensi['kd_puskesmas'],
        Hipertensi['nik'],
        Hipertensi['nama'],
        Hipertensi['tgl_lahir'],
        Hipertensi['jenis_kelamin'],
        Hipertensi["DIDIAGNOSIS_HIPERTENSI"],
        Hipertensi["INDIVIDU_DIDIAGNOSIS_TAPI_TIDAK_MINUM_OBAT_HIPERTENSI"],
        Hipertensi["INDIVIDU_DIDIAGNOSIS_HIPERTENSI_MINUM_OBAT_SESUAI_STANDAR"],
        Hipertensi["DIUKUR_TEKANAN_DARAH"],
        Hipertensi["SISTOL"],
        Hipertensi["DIASTOL"],
        Hipertensi["SUSPEK_TEKANAN_DARAH_TINGGI"],
        Hipertensi['created_at'],
        Hipertensi['created_at']
    )

    # variabel val adalah data yang akan di input
    cursor.execute(sql_insert_Hipertensi, val)
    db_conn.commit()