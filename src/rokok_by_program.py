# ==============================
#       Rokok by program
# ==============================


def specificDataForRokokByProgram(cursor, id):
    sql_select_data_for_insert_rokok_by_program = "SELECT survei_individu_merokok, survei_individu_umur_thn FROM public.raw_survei " \
                                                  "where survei_individu_survei_individu_detail_id = %s"

    cursor.execute(sql_select_data_for_insert_rokok_by_program, (id,))
    data_for_rokok_by_program = cursor.fetchone()

    dictRokokByProgram = {
        'merokok' : data_for_rokok_by_program[0],
        'umur_thn': data_for_rokok_by_program[1],
    }

    return dictRokokByProgram


def insertDataRokokByProgram(db_conn, cursor, rokok_by_program):  # fungsi ini untuk insert data pada table SASARAN LIFE CYCLE SPM

    sql_insert_rokok_by_program = "INSERT INTO public.rokok_by_program values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT " \
                                  "(survei_individu_detail_id) DO UPDATE SET survei_individu_detail_id = excluded.survei_individu_detail_id, " \
                                  "survei_rumah_tangga_id = excluded.survei_rumah_tangga_id, survei_id = excluded.survei_id, provinsi_id = excluded.provinsi_id, " \
                                  "nama_provinsi = excluded.nama_provinsi, kota_kabupaten_id = excluded.kota_kabupaten_id, nama_kota_kabupaten = excluded.nama_kota_kabupaten, " \
                                  "kecamatan_id = excluded.kecamatan_id, nama_kecamatan = excluded.nama_kecamatan, kelurahan_id = excluded.kelurahan_id, " \
                                  "nama_kelurahan = excluded.nama_kelurahan, kd_puskesmas = excluded.kd_puskesmas, nik = excluded.nik , nama = excluded.nama , " \
                                  "tgl_lahir = excluded.tgl_lahir, jenis_kelamin = excluded.jenis_kelamin, perokok_umur_10_sd_18_tahun = excluded.perokok_umur_10_sd_18_tahun, " \
                                  "perokok_umur_15_sd_18_tahun = excluded.perokok_umur_15_sd_18_tahun, perokok_umur_diatas_15_tahun = excluded.perokok_umur_diatas_15_tahun, " \
                                  "updated_at = excluded.updated_at;"

    perokok_umur_10_sd_18_tahun = 0
    perokok_umur_15_sd_18_tahun = 0
    perokok_umur_lebih_besar_15_tahun = 0

    if rokok_by_program['umur_thn'] >= 10 and rokok_by_program['umur_thn'] <= 18 and rokok_by_program['merokok'] == 'Y':
        perokok_umur_10_sd_18_tahun = 1
    if rokok_by_program['umur_thn'] >= 15 and rokok_by_program['umur_thn'] <= 18 and rokok_by_program['merokok'] == 'Y':
        perokok_umur_15_sd_18_tahun = 1
    if rokok_by_program['umur_thn'] >= 15 and rokok_by_program['merokok'] == 'Y':
        perokok_umur_lebih_besar_15_tahun = 1

    val = (
        rokok_by_program['survei_individu_detail_id'],
        rokok_by_program['survei_rumah_tangga_id'],
        rokok_by_program['survei_id'],
        rokok_by_program['provinsi_id'],
        rokok_by_program['nama_provinsi'],
        rokok_by_program['kota_kabupaten_id'],
        rokok_by_program['nama_kota_kabupaten'],
        rokok_by_program['kecamatan_id'],
        rokok_by_program['nama_kecamatan'],
        rokok_by_program['kelurahan_id'],
        rokok_by_program['nama_kelurahan'],
        rokok_by_program['kd_puskesmas'],
        rokok_by_program['nik'],
        rokok_by_program['nama'],
        rokok_by_program['tgl_lahir'],
        rokok_by_program['jenis_kelamin'],
        perokok_umur_10_sd_18_tahun,
        perokok_umur_15_sd_18_tahun,
        perokok_umur_lebih_besar_15_tahun,
        rokok_by_program['created_at'],
        rokok_by_program['created_at']
    )

    # variabel val adalah data yang akan di input
    cursor.execute(sql_insert_rokok_by_program, val)
    cursor.execute("ROLLBACK")
    db_conn.commit()