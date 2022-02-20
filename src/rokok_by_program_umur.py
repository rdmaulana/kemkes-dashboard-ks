# ==============================
#    Rokok by prorgram (Umur)
# ==============================


def specificDataForRokokByProgramUmur(cursor, id):
    sql_select_data_for_insert_rokok_by_program_umur = "SELECT survei_individu_umur_thn FROM public.raw_survei where survei_individu_survei_individu_detail_id = %s"

    cursor.execute(sql_select_data_for_insert_rokok_by_program_umur, (id,))
    data_for_rokok_by_program_umur = cursor.fetchone()

    dictRokokByProgramUmur = {
        'umur_thn': data_for_rokok_by_program_umur[0]
    }

    return dictRokokByProgramUmur


def insertDataRokokByProgramUmur(db_conn, cursor, rokok_by_program_umur):  # fungsi ini untuk insert data pada table SASARAN LIFE CYCLE SPM

    sql_insert_rokok_by_program_umur = "INSERT INTO public.rokok_by_program_umur values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT " \
                                       "(survei_individu_detail_id) DO UPDATE SET survei_individu_detail_id = excluded.survei_individu_detail_id, " \
                                       "survei_rumah_tangga_id = excluded.survei_rumah_tangga_id, survei_id = excluded.survei_id, provinsi_id = excluded.provinsi_id, " \
                                       "nama_provinsi = excluded.nama_provinsi, kota_kabupaten_id = excluded.kota_kabupaten_id, nama_kota_kabupaten = excluded.nama_kota_kabupaten, " \
                                       "kecamatan_id = excluded.kecamatan_id, nama_kecamatan = excluded.nama_kecamatan, kelurahan_id = excluded.kelurahan_id, " \
                                       "nama_kelurahan = excluded.nama_kelurahan, kd_puskesmas = excluded.kd_puskesmas, nik = excluded.nik , nama = excluded.nama, " \
                                       "tgl_lahir = excluded.tgl_lahir, jenis_kelamin = excluded.jenis_kelamin, jumlah_umur_10_sd_18_tahun = excluded.jumlah_umur_10_sd_18_tahun, " \
                                       "jumlah_umur_15_sd_18_tahun = excluded.jumlah_umur_15_sd_18_tahun, jumlah_umur_diatas_15_tahun = excluded.jumlah_umur_diatas_15_tahun, " \
                                       "updated_at = excluded.updated_at;"

    umur_10_sd_18_tahun = 0
    umur_15_sd_18_tahun = 0
    umur_lebih_besar_15_tahun = 0

    if rokok_by_program_umur['umur_thn'] >= 10 and rokok_by_program_umur['umur_thn'] <= 18:
        umur_10_sd_18_tahun = 1
    if rokok_by_program_umur['umur_thn'] >= 15 and rokok_by_program_umur['umur_thn'] <= 18:
        umur_15_sd_18_tahun = 1
    if rokok_by_program_umur['umur_thn'] >= 15:
        umur_lebih_besar_15_tahun = 1

    val = (
        rokok_by_program_umur['survei_individu_detail_id'],
        rokok_by_program_umur['survei_rumah_tangga_id'],
        rokok_by_program_umur['survei_id'],
        rokok_by_program_umur['provinsi_id'],
        rokok_by_program_umur['nama_provinsi'],
        rokok_by_program_umur['kota_kabupaten_id'],
        rokok_by_program_umur['nama_kota_kabupaten'],
        rokok_by_program_umur['kecamatan_id'],
        rokok_by_program_umur['nama_kecamatan'],
        rokok_by_program_umur['kelurahan_id'],
        rokok_by_program_umur['nama_kelurahan'],
        rokok_by_program_umur['kd_puskesmas'],
        rokok_by_program_umur['nik'],
        rokok_by_program_umur['nama'],
        rokok_by_program_umur['tgl_lahir'],
        rokok_by_program_umur['jenis_kelamin'],
        umur_10_sd_18_tahun,
        umur_15_sd_18_tahun,
        umur_lebih_besar_15_tahun,
        rokok_by_program_umur['created_at'],
        rokok_by_program_umur['created_at']
    )

    # variabel val adalah data yang akan di input
    cursor.execute(sql_insert_rokok_by_program_umur, val)
    db_conn.commit()