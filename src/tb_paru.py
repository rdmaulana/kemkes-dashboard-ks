# ==============================
#           TB Paru
# ==============================


def specificDataForTBParu(cursor, id):
    sql_select_data_for_TB_Paru = "SELECT survei_individu_umur_thn," \
                                  "survei_individu_tb, survei_individu_obat_tb, survei_individu_batuk FROM public.raw_survei " \
                                  "where survei_individu_survei_individu_detail_id = %s"

    # note yang dibutuhkan:
    # umur_tahun, didiagnosis_tb_baru, minum_obat_tb_teratur, batuk_berdakah_lebih_dari_Sama_Dengan_2_minggu

    cursor.execute(sql_select_data_for_TB_Paru, (id,))
    data_for_TB_Paru = cursor.fetchone()

    umur_tahun = data_for_TB_Paru[0]
    didiagnosis_tb_baru = data_for_TB_Paru[1]
    minum_obat_tb_teratur = data_for_TB_Paru[2]
    batuk_berdakah_lebih_dari_Sama_Dengan_2_minggu = data_for_TB_Paru[3]

    DIDIAGNOSIS_TAPI_TIDAK_MINUM_OBAT_TB = 0
    PENDERITA_TB_YANG_MINUM_OBAT_SESUAI_STANDAR = 0
    lebih_dari_sama_dengan_15_TAHUN = 0
    DIDIAGNOSIS_TB = 0
    SUSPEK_TB = 0

    # co
    if umur_tahun >= 15:
        lebih_dari_sama_dengan_15_TAHUN = 1

    # CP
    if lebih_dari_sama_dengan_15_TAHUN == 1 and didiagnosis_tb_baru == 'Y':
        DIDIAGNOSIS_TB = 1

    # CQ dan CR

    if lebih_dari_sama_dengan_15_TAHUN == 1 and DIDIAGNOSIS_TB == 1 and minum_obat_tb_teratur == 'T':
        DIDIAGNOSIS_TAPI_TIDAK_MINUM_OBAT_TB = 1
    if lebih_dari_sama_dengan_15_TAHUN == 1 and DIDIAGNOSIS_TB == 1 and minum_obat_tb_teratur == 'Y':
        PENDERITA_TB_YANG_MINUM_OBAT_SESUAI_STANDAR = 1

    # CS

    if lebih_dari_sama_dengan_15_TAHUN == 1 and batuk_berdakah_lebih_dari_Sama_Dengan_2_minggu == 'Y':
        SUSPEK_TB = 1

    dict_TB_Paru = {
        'lebih_dari_sama_dengan_15_TAHUN': lebih_dari_sama_dengan_15_TAHUN,
        'DIDIAGNOSIS_TB': DIDIAGNOSIS_TB,
        'DIDIAGNOSIS_TAPI_TIDAK_MINUM_OBAT_TB': DIDIAGNOSIS_TAPI_TIDAK_MINUM_OBAT_TB,
        'PENDERITA_TB_YANG_MINUM_OBAT_SESUAI_STANDAR': PENDERITA_TB_YANG_MINUM_OBAT_SESUAI_STANDAR,
        'SUSPEK_TB': SUSPEK_TB,
    }

    # data yang diambil disimpan pada tipe data dictionary

    return dict_TB_Paru


def insertDataTBParu(db_conn, cursor, TB_Paru):
    sql_insert_TB_Paru = "INSERT INTO public.tb_paru values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT " \
                         "(survei_individu_detail_id) DO UPDATE SET survei_individu_detail_id = excluded.survei_individu_detail_id, " \
                         "survei_rumah_tangga_id = excluded.survei_rumah_tangga_id, survei_id = excluded.survei_id, provinsi_id = excluded.provinsi_id, " \
                         "nama_provinsi = excluded.nama_provinsi, kota_kabupaten_id = excluded.kota_kabupaten_id, nama_kota_kabupaten = excluded.nama_kota_kabupaten, " \
                         "kecamatan_id = excluded.kecamatan_id, nama_kecamatan = excluded.nama_kecamatan, kelurahan_id = excluded.kelurahan_id, " \
                         "nama_kelurahan = excluded.nama_kelurahan,	kd_puskesmas = excluded.kd_puskesmas, nik = excluded.nik , nama = excluded.nama , " \
                         "tgl_lahir = excluded.tgl_lahir, jenis_kelamin = excluded.jenis_kelamin, lebih_dari_sama_dengan_15_TAHUN = excluded.lebih_dari_sama_dengan_15_TAHUN, " \
                         "DIDIAGNOSIS_TB = excluded.DIDIAGNOSIS_TB,	DIDIAGNOSIS_TAPI_TIDAK_MINUM_OBAT_TB = excluded.DIDIAGNOSIS_TAPI_TIDAK_MINUM_OBAT_TB, " \
                         "PENDERITA_TB_YANG_MINUM_OBAT_SESUAI_STANDAR = excluded.PENDERITA_TB_YANG_MINUM_OBAT_SESUAI_STANDAR, SUSPEK_TB = excluded.SUSPEK_TB, " \
                         "updated_at = excluded.updated_at;"

    val = (
        TB_Paru['survei_individu_detail_id'],
        TB_Paru['survei_rumah_tangga_id'],
        TB_Paru['survei_id'],
        TB_Paru['provinsi_id'],
        TB_Paru['nama_provinsi'],
        TB_Paru['kota_kabupaten_id'],
        TB_Paru['nama_kota_kabupaten'],
        TB_Paru['kecamatan_id'],
        TB_Paru['nama_kecamatan'],
        TB_Paru['kelurahan_id'],
        TB_Paru['nama_kelurahan'],
        TB_Paru['kd_puskesmas'],
        TB_Paru['nik'],
        TB_Paru['nama'],
        TB_Paru['tgl_lahir'],
        TB_Paru['jenis_kelamin'],
        TB_Paru["lebih_dari_sama_dengan_15_TAHUN"],
        TB_Paru["DIDIAGNOSIS_TB"],
        TB_Paru["DIDIAGNOSIS_TAPI_TIDAK_MINUM_OBAT_TB"],
        TB_Paru["PENDERITA_TB_YANG_MINUM_OBAT_SESUAI_STANDAR"],
        TB_Paru["SUSPEK_TB"],
        TB_Paru['created_at'],
        TB_Paru['created_at']
    )

    # variabel val adalah data yang akan di input
    cursor.execute(sql_insert_TB_Paru, val)
    db_conn.commit()