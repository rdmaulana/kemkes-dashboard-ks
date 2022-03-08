# =============================
#     Sasaran Life Cycle SPM
# ==============================


def specificDataForSasaranLifeCycleSpm(cursor, id): # fungsi ini untuk tambahan data untuk table SASARAN LIFE CYCLE SPM
    sql_select_data_for_insert_sasaran_life_cycle_spm = "SELECT survei_individu_umur_bln, survei_individu_umur_thn," \
                                                        "survei_individu_wuh FROM public.raw_survei " \
                                                        "where survei_individu_survei_individu_detail_id = %s"
                                                        # data field yang dipilih tergantung table masing-masing

    cursor.execute(sql_select_data_for_insert_sasaran_life_cycle_spm, (id,))
    data_for_sasaran_life_cycle_spm = cursor.fetchone()

    dictSasaranLifeCycleSpm = {
        'umur_bulan' : data_for_sasaran_life_cycle_spm[0],
        'umur_tahun' : data_for_sasaran_life_cycle_spm [1],
        'wanita_usia_hamil' : data_for_sasaran_life_cycle_spm[2]
    }
    # data yang diambil disimpan pada tipe data dictionary

    return dictSasaranLifeCycleSpm  # mengembalikan nilai tambahan data untuk table SASARAN LIFE CYCLE SPM


def insertDataSasaranLifeCycleSpm(db_conn, cursor, sasaran_life_cycle_spm): # fungsi ini untuk insert data pada table SASARAN LIFE CYCLE SPM

    sql_insert_sasaran_life_cycle_spm = "INSERT INTO public.sasaran_life_cycle_spm values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT " \
                                        "(survei_individu_detail_id) DO UPDATE SET survei_individu_detail_id = excluded.survei_individu_detail_id, " \
                                        "survei_rumah_tangga_id = excluded.survei_rumah_tangga_id, survei_id = excluded.survei_id, provinsi_id = excluded.provinsi_id, " \
                                        "nama_provinsi = excluded.nama_provinsi, kota_kabupaten_id = excluded.kota_kabupaten_id, nama_kota_kabupaten = excluded.nama_kota_kabupaten, " \
                                        "kecamatan_id = excluded.kecamatan_id, nama_kecamatan = excluded.nama_kecamatan, kelurahan_id = excluded.kelurahan_id, " \
                                        "nama_kelurahan = excluded.nama_kelurahan,	kd_puskesmas = excluded.kd_puskesmas, nik = excluded.nik , nama = excluded.nama , " \
                                        "tgl_lahir = excluded.tgl_lahir, jenis_kelamin = excluded.jenis_kelamin, hamil = excluded.hamil, " \
                                        "usia_0_sd_59_bulan = excluded.usia_0_sd_59_bulan,	usia_7_sd_15_tahun = excluded.usia_7_sd_15_tahun, " \
                                        "usia_15_sd_59_tahun = excluded.usia_15_sd_59_tahun, usia_lbh_dari_60_tahun = excluded.usia_lbh_dari_60_tahun, " \
                                        "updated_at = excluded.updated_at;"

    if sasaran_life_cycle_spm['wanita_usia_hamil'] == 'Y':
        hamil = 1
    else:
        hamil = 0

    usia_0_sd_59_bulan = 0
    usia_7_sd_15_tahun = 0
    usia_15_sd_59_tahun = 0
    usia_lbh_dari_60_tahun = 0

    if sasaran_life_cycle_spm['umur_bulan'] >= 0 and sasaran_life_cycle_spm['umur_bulan'] <= 59 and sasaran_life_cycle_spm['umur_tahun'] < 7:
        usia_0_sd_59_bulan = 1
    else:
        if sasaran_life_cycle_spm['umur_tahun'] >= 7 and sasaran_life_cycle_spm['umur_tahun'] <= 15:
            usia_7_sd_15_tahun = 1
        elif sasaran_life_cycle_spm['umur_tahun'] >= 15 and sasaran_life_cycle_spm['umur_tahun'] <= 59:
            usia_15_sd_59_tahun = 1
        else:
            usia_lbh_dari_60_tahun = 1

    val = (
        sasaran_life_cycle_spm['survei_individu_detail_id'],
        sasaran_life_cycle_spm['survei_rumah_tangga_id'],
        sasaran_life_cycle_spm['survei_id'],
        sasaran_life_cycle_spm['provinsi_id'],
        sasaran_life_cycle_spm['nama_provinsi'],
        sasaran_life_cycle_spm['kota_kabupaten_id'],
        sasaran_life_cycle_spm['nama_kota_kabupaten'],
        sasaran_life_cycle_spm['kecamatan_id'],
        sasaran_life_cycle_spm['nama_kecamatan'],
        sasaran_life_cycle_spm['kelurahan_id'],
        sasaran_life_cycle_spm['nama_kelurahan'],
        sasaran_life_cycle_spm['kd_puskesmas'],
        sasaran_life_cycle_spm['nik'],
        sasaran_life_cycle_spm['nama'],
        sasaran_life_cycle_spm['tgl_lahir'],
        sasaran_life_cycle_spm['jenis_kelamin'],
        hamil,
        usia_0_sd_59_bulan,
        usia_7_sd_15_tahun,
        usia_15_sd_59_tahun,
        usia_lbh_dari_60_tahun,
        sasaran_life_cycle_spm['created_at'],
        sasaran_life_cycle_spm['created_at']
    )

    # variabel val adalah data yang akan di input
    cursor.execute(sql_insert_sasaran_life_cycle_spm, val)
    db_conn.commit()