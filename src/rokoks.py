# ==============================
#           ROKOkS
# ==============================


def specificDataForROKOkS(cursor, id_individu):
    sql_select_data_for_ROKOkS = "SELECT  survei_individu_umur_thn, survei_individu_merokok " \
                                 "FROM public.raw_survei " \
                                 "where survei_individu_survei_individu_detail_id = %s"

    cursor.execute(sql_select_data_for_ROKOkS, (id_individu,))
    data_for_ROKOkS = cursor.fetchone()

    umur_tahun = data_for_ROKOkS[0]
    individu_merokok = data_for_ROKOkS[1]

    kategori_umur_tahun = ""

    Umur_5_9_tahun = 0
    Umur_10_14_tahun = 0
    Umur_15_24_tahun = 0
    Umur_25_34_tahun = 0
    Umur_35_44_tahun = 0
    Umur_45_54_tahun = 0
    Umur_55_64_tahun = 0
    Umur_65_tahun_keatas = 0

    # Variable DK5 = kategori_umur_tahun
    if umur_tahun >= 5 and umur_tahun <= 9:
        kategori_umur_tahun = "5-9 tahun"
    elif umur_tahun >= 10 and umur_tahun <= 14:
        kategori_umur_tahun = "10-14 tahun"
    elif (umur_tahun >= 15 and umur_tahun <= 24):
        kategori_umur_tahun = "15-24 tahun"
    elif (umur_tahun >= 25 and umur_tahun <= 34):
        kategori_umur_tahun = "25-34 tahun"
    elif (umur_tahun >= 35 and umur_tahun <= 44):
        kategori_umur_tahun = "35-44 tahun"
    elif (umur_tahun >= 45 and umur_tahun <= 54):
        kategori_umur_tahun = "45-54 tahun"
    elif (umur_tahun >= 55 and umur_tahun <= 64):
        kategori_umur_tahun = "55-64 tahun"
    elif umur_tahun >= 65:
        kategori_umur_tahun = "65 tahun keatas"



    # Field DV
    if kategori_umur_tahun == "5-9 tahun" and individu_merokok == 'Y':
        Umur_5_9_tahun = 1
    elif kategori_umur_tahun == "10-14 tahun" and individu_merokok == 'Y':
        Umur_10_14_tahun = 1
    elif kategori_umur_tahun == "15-24 tahun" and individu_merokok == 'Y':
        Umur_15_24_tahun = 1
    elif kategori_umur_tahun == "25-34 tahun" and individu_merokok == 'Y':
        Umur_25_34_tahun = 1
    elif kategori_umur_tahun == "35-44 tahun" and individu_merokok == 'Y':
        Umur_35_44_tahun = 1
    elif kategori_umur_tahun == "45-54 tahun" and individu_merokok == 'Y':
        Umur_45_54_tahun = 1
    elif kategori_umur_tahun == "55-64 tahun" and individu_merokok == 'Y':
        Umur_55_64_tahun = 1
    elif kategori_umur_tahun == "65 tahun keatas" and individu_merokok == 'Y':
        Umur_65_tahun_keatas = 1

    dict_ROKOkS = {
        'Umur_5_9_tahun': Umur_5_9_tahun,
        'Umur_10_14_tahun': Umur_10_14_tahun,
        'Umur_15_24_tahun': Umur_15_24_tahun,
        'Umur_25_34_tahun': Umur_25_34_tahun,
        'Umur_35_44_tahun': Umur_35_44_tahun,
        'Umur_45_54_tahun': Umur_45_54_tahun,
        'Umur_55_64_tahun': Umur_55_64_tahun,
        'Umur_65_tahun_keatas': Umur_65_tahun_keatas
    }
    # data yang diambil disimpan pada tipe data dictionary

    return dict_ROKOkS


def insertDataROKOkS(db_conn, cursor, ROKOkS):
    sql_insert_ROKOkS = "INSERT INTO public.ROKOkS values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT " \
                        "(survei_individu_detail_id) DO UPDATE SET survei_individu_detail_id = excluded.survei_individu_detail_id, " \
                        "survei_rumah_tangga_id = excluded.survei_rumah_tangga_id, survei_id = excluded.survei_id, provinsi_id = excluded.provinsi_id, " \
                        "nama_provinsi = excluded.nama_provinsi, kota_kabupaten_id = excluded.kota_kabupaten_id, nama_kota_kabupaten = excluded.nama_kota_kabupaten, " \
                        "kecamatan_id = excluded.kecamatan_id, nama_kecamatan = excluded.nama_kecamatan, kelurahan_id = excluded.kelurahan_id, " \
                        "nama_kelurahan = excluded.nama_kelurahan,	kd_puskesmas = excluded.kd_puskesmas, nik = excluded.nik , nama = excluded.nama , " \
                        "tgl_lahir = excluded.tgl_lahir, jenis_kelamin = excluded.jenis_kelamin, Umur_5_9_tahun = excluded.Umur_5_9_tahun, " \
                        "Umur_10_14_tahun = excluded.Umur_10_14_tahun,	Umur_15_24_tahun = excluded.Umur_15_24_tahun, " \
                        "Umur_25_34_tahun = excluded.Umur_25_34_tahun, Umur_35_44_tahun = excluded.Umur_35_44_tahun, " \
                        "Umur_45_54_tahun = excluded.Umur_45_54_tahun, Umur_55_64_tahun = excluded.Umur_55_64_tahun, " \
                        "Umur_65_tahun_keatas = excluded.Umur_65_tahun_keatas, updated_at = excluded.updated_at;"

    val = (
        ROKOkS['survei_individu_detail_id'],
        ROKOkS['survei_rumah_tangga_id'],
        ROKOkS['survei_id'],
        ROKOkS['provinsi_id'],
        ROKOkS['nama_provinsi'],
        ROKOkS['kota_kabupaten_id'],
        ROKOkS['nama_kota_kabupaten'],
        ROKOkS['kecamatan_id'],
        ROKOkS['nama_kecamatan'],
        ROKOkS['kelurahan_id'],
        ROKOkS['nama_kelurahan'],
        ROKOkS['kd_puskesmas'],
        ROKOkS['nik'],
        ROKOkS['nama'],
        ROKOkS['tgl_lahir'],
        ROKOkS['jenis_kelamin'],
        ROKOkS["Umur_5_9_tahun"],
        ROKOkS["Umur_10_14_tahun"],
        ROKOkS["Umur_15_24_tahun"],
        ROKOkS["Umur_25_34_tahun"],
        ROKOkS["Umur_35_44_tahun"],
        ROKOkS["Umur_45_54_tahun"],
        ROKOkS["Umur_55_64_tahun"],
        ROKOkS["Umur_65_tahun_keatas"],
        ROKOkS['created_at'],
        ROKOkS['created_at']
    )

    # variabel val adalah data yang akan di input
    cursor.execute(sql_insert_ROKOkS, val)
    db_conn.commit()