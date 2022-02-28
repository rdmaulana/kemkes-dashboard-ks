# ==============================
#     Karakterisik Responden
# ==============================


def specificDataKarakteristikResponden(cursor, id):  # fungsi ini untuk tambahan data untuk table Karakteristik Responden
    sql_select_data_for_insert_karakteristik_responden = "SELECT survei_individu_umur_thn, survei_individu_umur_bln, survei_individu_pendidikan_id, " \
                                                         "survei_individu_pekerjaan_id, survei_individu_tanggal_lahir FROM public.raw_survei " \
                                                         "where survei_individu_survei_individu_detail_id = %s"
    # data field yang dipilih tergantung table masing-masing

    cursor.execute(sql_select_data_for_insert_karakteristik_responden, (id,))
    data_for_karakteristik_responden = cursor.fetchone()

    dictKarakteristikResponden = {
        'umur_tahun': data_for_karakteristik_responden[0],
        'umur_bulan': data_for_karakteristik_responden[1],
        'pendidikan_id': data_for_karakteristik_responden[2],
        'pekerjaan_id': data_for_karakteristik_responden[3],
        'tanggal_lahir': data_for_karakteristik_responden[4],
    }
    # data yang diambil disimpan pada tipe data dictionary

    return dictKarakteristikResponden  # mengembalikan nilai tambahan data untuk table Karakteristik Responden


def insertDataKarakteristikResponden(db_conn, cursor, karakteristik_responden, current_date):  # fungsi ini untuk insert data pada table Karakteristik Responden

    sql_insert_karakteristik_responden = "INSERT INTO public.karakteristik_responden values (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
                                         "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT " \
                                         "(survei_individu_detail_id) DO UPDATE SET survei_individu_detail_id = excluded.survei_individu_detail_id, " \
                                         "survei_rumah_tangga_id = excluded.survei_rumah_tangga_id, survei_id = excluded.survei_id, provinsi_id = excluded.provinsi_id, " \
                                         "nama_provinsi = excluded.nama_provinsi, kota_kabupaten_id = excluded.kota_kabupaten_id, nama_kota_kabupaten = excluded.nama_kota_kabupaten, " \
                                         "kecamatan_id = excluded.kecamatan_id, nama_kecamatan = excluded.nama_kecamatan, kelurahan_id = excluded.kelurahan_id, " \
                                         "nama_kelurahan = excluded.nama_kelurahan,	kd_puskesmas = excluded.kd_puskesmas, nik = excluded.nik , nama = excluded.nama , " \
                                         "tgl_lahir = excluded.tgl_lahir, jenis_kelamin = excluded.jenis_kelamin, umur_hari_ini_tahun = excluded.umur_hari_ini_tahun, " \
                                         "umur_tahun = excluded.umur_tahun, umurbulan = excluded.umurbulan, umur_bulan = excluded.umur_bulan, " \
                                         "kategori_umur_bulan = excluded.kategori_umur_bulan, kategori_umur_tahun = excluded.kategori_umur_tahun, " \
                                         "kategori_pendidikan = excluded.kategori_pendidikan, kategori_pekerjaan = excluded.kategori_pekerjaan, " \
                                         "umur_5_sd_9_tahun = excluded.umur_5_sd_9_tahun, umur_10_sd_14_tahun = excluded.umur_10_sd_14_tahun, " \
                                         "umur_15_24_tahun = excluded.umur_15_24_tahun, umur_25_34_tahun = excluded.umur_25_34_tahun, " \
                                         "umur_35_44_tahun = excluded.umur_35_44_tahun, umur_45_54_tahun = excluded.umur_45_54_tahun, " \
                                         "umur_55_64_tahun = excluded.umur_55_64_tahun, umur_65_tahun_keatas = excluded.umur_65_tahun_keatas, updated_at = excluded.updated_at;"

    try:

        umur = (current_date.year - karakteristik_responden['tanggal_lahir'].year)

    except Exception as e:
        umur = -1

    # Field UMUR HARI INI (TAHUN)
    if umur != 0:
        umur_hari_ini = umur
    else:
        umur_hari_ini = 0

    # Field UMUR (TAHUN)
    umur_tahun = karakteristik_responden['umur_tahun']

    # Field UMUR (BULAN)
    umur_bulan_1 = karakteristik_responden['umur_bulan']

    # Field umur bulan
    if karakteristik_responden['umur_tahun'] < 5:
        umur_bulan_2 = karakteristik_responden['umur_tahun'] * 12 + karakteristik_responden['umur_bulan']
    else:
        umur_bulan_2 = None

        # Field Kategori Umur Bulan
    if umur_tahun < 5 and umur_bulan_2 >= 0 and umur_bulan_2 <= 11:
        kategori_umur_bulan = "0-11 bulan"
    elif umur_tahun < 5 and umur_bulan_2 >= 12 and umur_bulan_2 <= 23:
        kategori_umur_bulan = "12-23 bulan"
    elif umur_tahun < 5 and umur_bulan_2 >= 24 and umur_bulan_2 <= 35:
        kategori_umur_bulan = "24-35 bulan"
    elif umur_tahun < 5 and umur_bulan_2 >= 36 and umur_bulan_2 <= 47 :
        kategori_umur_bulan = "36-47 bulan"
    elif umur_tahun < 5 and umur_bulan_2 >= 48 and umur_bulan_2 <= 59:
        kategori_umur_bulan = "48-59 bulan"
    else:
        kategori_umur_bulan = ""

        # Field Kategori Umur Tahun
    if (karakteristik_responden['umur_tahun'] >= 5 and karakteristik_responden['umur_tahun'] <= 9):
        kategori_umur_tahun = "5-9 tahun"
    elif (karakteristik_responden['umur_tahun'] >= 10 and karakteristik_responden['umur_tahun'] <= 14):
        kategori_umur_tahun = "10-14 tahun"
    elif (karakteristik_responden['umur_tahun'] >= 15 and karakteristik_responden['umur_tahun'] <= 24):
        kategori_umur_tahun = "15-24 tahun"
    elif (karakteristik_responden['umur_tahun'] >= 25 and karakteristik_responden['umur_tahun'] <= 34):
        kategori_umur_tahun = "25-34 tahun"
    elif (karakteristik_responden['umur_tahun'] >= 35 and karakteristik_responden['umur_tahun'] <= 44):
        kategori_umur_tahun = "35-44 tahun"
    elif (karakteristik_responden['umur_tahun'] >= 45 and karakteristik_responden['umur_tahun'] <= 54):
        kategori_umur_tahun = "45-54 tahun"
    elif (karakteristik_responden['umur_tahun'] >= 55 and karakteristik_responden['umur_tahun'] <= 64):
        kategori_umur_tahun = "55-64 tahun"
    elif karakteristik_responden['umur_tahun'] >= 65:
        kategori_umur_tahun = "65 tahun keatas"
    else:
        kategori_umur_tahun = ""

        # Field Kategori Pendidikan
    if karakteristik_responden['pendidikan_id'] == 1:
        pendidikan = "Tidak/Belum Sekolah"
    elif karakteristik_responden['pendidikan_id'] == 2:
        pendidikan = "Belum Tamat SD/Sederajat"
    elif karakteristik_responden['pendidikan_id'] == 3:
        pendidikan = "Tamat SD/Sederajat"
    elif karakteristik_responden['pendidikan_id'] == 4:
        pendidikan = "SLTP/Sederajat"
    elif karakteristik_responden['pendidikan_id'] == 5:
        pendidikan = "SLTA/Sederajat"
    elif karakteristik_responden['pendidikan_id'] == 6:
        pendidikan = "Diploma I/II"
    elif karakteristik_responden['pendidikan_id'] == 7:
        pendidikan = "Diploma I/II"
    elif karakteristik_responden['pendidikan_id'] == 8:
        pendidikan = "Diploma I/II"
    elif karakteristik_responden['pendidikan_id'] == 9:
        pendidikan = "Diploma I/II"
    elif karakteristik_responden['pendidikan_id'] == 10:
        pendidikan = "Diploma I/II"
    else:
        pendidikan = ""

        # Field Kategori Pekerjaan
    if karakteristik_responden['pekerjaan_id'] == 1:
        pekerjaan = 'Belum/Tidak Bekerja'
    elif karakteristik_responden['pekerjaan_id'] == 2:
        pekerjaan = 'Mengurus Rumah Tangga'
    elif karakteristik_responden['pekerjaan_id'] == 3:
        pekerjaan = 'Pelajar/Mahasiswa'
    elif karakteristik_responden['pekerjaan_id'] == 4:
        pekerjaan = 'Pensiunan'
    elif karakteristik_responden['pekerjaan_id'] == 5:
        pekerjaan = 'Pegawai Negeri Sipil (PNS)'
    elif karakteristik_responden['pekerjaan_id'] == 6:
        pekerjaan = 'Tentara Nasional Indonesia (TNI)'
    elif karakteristik_responden['pekerjaan_id'] == 7:
        pekerjaan = 'Kepolisian RI (POLRI)'
    elif karakteristik_responden['pekerjaan_id'] == 8:
        pekerjaan = 'Perdagangan'
    elif karakteristik_responden['pekerjaan_id'] == 9:
        pekerjaan = 'Petani/Pekebun'
    elif karakteristik_responden['pekerjaan_id'] == 10:
        pekerjaan = 'Peternak'
    elif karakteristik_responden['pekerjaan_id'] == 11:
        pekerjaan = 'Nelayan/Perikanan'
    elif karakteristik_responden['pekerjaan_id'] == 12:
        pekerjaan = 'Industri'
    elif karakteristik_responden['pekerjaan_id'] == 13:
        pekerjaan = 'Konstruksi'
    elif karakteristik_responden['pekerjaan_id'] == 14:
        pekerjaan = 'Transportasi'
    elif karakteristik_responden['pekerjaan_id'] == 15:
        pekerjaan = 'Karyawan Swasta'
    elif karakteristik_responden['pekerjaan_id'] == 16:
        pekerjaan = 'Karyawan BUMN'
    elif karakteristik_responden['pekerjaan_id'] == 17:
        pekerjaan = 'Karyawan BUMD'
    elif karakteristik_responden['pekerjaan_id'] == 18:
        pekerjaan = 'Karyawan Honorer'
    elif karakteristik_responden['pekerjaan_id'] == 19:
        pekerjaan = 'Buruh Harian Lepas'
    elif karakteristik_responden['pekerjaan_id'] == 20:
        pekerjaan = 'Buruh Tani/Perkebunan'
    elif karakteristik_responden['pekerjaan_id'] == 21:
        pekerjaan = 'Buruh Nelayan/Perikanan'
    elif karakteristik_responden['pekerjaan_id'] == 22:
        pekerjaan = 'Buruh Peternakan'
    elif karakteristik_responden['pekerjaan_id'] == 23:
        pekerjaan = 'Pembantu Rumah Tangga'
    elif karakteristik_responden['pekerjaan_id'] == 24:
        pekerjaan = 'Tukang Cukur'
    elif karakteristik_responden['pekerjaan_id'] == 25:
        pekerjaan = 'Tukang Listrik'
    elif karakteristik_responden['pekerjaan_id'] == 26:
        pekerjaan = 'Tukang Batu'
    elif karakteristik_responden['pekerjaan_id'] == 27:
        pekerjaan = 'Tukang Kayu'
    elif karakteristik_responden['pekerjaan_id'] == 28:
        pekerjaan = 'Tukang Sol Sepatu'
    elif karakteristik_responden['pekerjaan_id'] == 29:
        pekerjaan = 'Tukang Las/Pandai Besi'
    elif karakteristik_responden['pekerjaan_id'] == 30:
        pekerjaan = 'Tukang Jahit'
    elif karakteristik_responden['pekerjaan_id'] == 31:
        pekerjaan = 'Tukang Gigi'
    elif karakteristik_responden['pekerjaan_id'] == 32:
        pekerjaan = 'Penata Rias'
    elif karakteristik_responden['pekerjaan_id'] == 33:
        pekerjaan = 'Penata Busana'
    elif karakteristik_responden['pekerjaan_id'] == 34:
        pekerjaan = 'Penata Rambut'
    elif karakteristik_responden['pekerjaan_id'] == 35:
        pekerjaan = 'Mekanik'
    elif karakteristik_responden['pekerjaan_id'] == 36:
        pekerjaan = 'Seniman'
    elif karakteristik_responden['pekerjaan_id'] == 37:
        pekerjaan = 'Tabib'
    elif karakteristik_responden['pekerjaan_id'] == 38:
        pekerjaan = 'Paraji'
    elif karakteristik_responden['pekerjaan_id'] == 39:
        pekerjaan = 'Perancang Busana'
    elif karakteristik_responden['pekerjaan_id'] == 40:
        pekerjaan = 'Penterjemah'
    elif karakteristik_responden['pekerjaan_id'] == 41:
        pekerjaan = 'Imam Masjid'
    elif karakteristik_responden['pekerjaan_id'] == 42:
        pekerjaan = 'Pendeta'
    elif karakteristik_responden['pekerjaan_id'] == 43:
        pekerjaan = 'Pastor'
    elif karakteristik_responden['pekerjaan_id'] == 44:
        pekerjaan = 'Wartawan'
    elif karakteristik_responden['pekerjaan_id'] == 45:
        pekerjaan = 'Ustadz/Mubaligh'
    elif karakteristik_responden['pekerjaan_id'] == 46:
        pekerjaan = 'Juru Masak'
    elif karakteristik_responden['pekerjaan_id'] == 47:
        pekerjaan = 'Promotor Acara'
    elif karakteristik_responden['pekerjaan_id'] == 48:
        pekerjaan = 'Anggota DPR-RI'
    elif karakteristik_responden['pekerjaan_id'] == 49:
        pekerjaan = 'Anggota DPD'
    elif karakteristik_responden['pekerjaan_id'] == 50:
        pekerjaan = 'Anggota BPK'
    elif karakteristik_responden['pekerjaan_id'] == 51:
        pekerjaan = 'Presiden'
    elif karakteristik_responden['pekerjaan_id'] == 52:
        pekerjaan = 'Wakil Presiden'
    elif karakteristik_responden['pekerjaan_id'] == 53:
        pekerjaan = 'Anggota Mahkamah Konstitusi'
    elif karakteristik_responden['pekerjaan_id'] == 54:
        pekerjaan = 'Anggota Kabinet/Kementrian'
    elif karakteristik_responden['pekerjaan_id'] == 55:
        pekerjaan = 'Duta Besar'
    elif karakteristik_responden['pekerjaan_id'] == 56:
        pekerjaan = 'Gubernur'
    elif karakteristik_responden['pekerjaan_id'] == 57:
        pekerjaan = 'Wakil Gubernur'
    elif karakteristik_responden['pekerjaan_id'] == 58:
        pekerjaan = 'Bupati'
    elif karakteristik_responden['pekerjaan_id'] == 59:
        pekerjaan = 'Wakil Bupati'
    elif karakteristik_responden['pekerjaan_id'] == 60:
        pekerjaan = 'Walikota'
    elif karakteristik_responden['pekerjaan_id'] == 61:
        pekerjaan = 'Wakil Walikota'
    elif karakteristik_responden['pekerjaan_id'] == 62:
        pekerjaan = 'Anggota DPRD Prop.'
    elif karakteristik_responden['pekerjaan_id'] == 63:
        pekerjaan = 'Anggota DPRD Kab./Kota'
    elif karakteristik_responden['pekerjaan_id'] == 64:
        pekerjaan = 'Dosen'
    elif karakteristik_responden['pekerjaan_id'] == 65:
        pekerjaan = 'Guru'
    elif karakteristik_responden['pekerjaan_id'] == 66:
        pekerjaan = 'Pilot'
    elif karakteristik_responden['pekerjaan_id'] == 67:
        pekerjaan = 'Pengacara'
    elif karakteristik_responden['pekerjaan_id'] == 68:
        pekerjaan = 'Notaris'
    elif karakteristik_responden['pekerjaan_id'] == 69:
        pekerjaan = 'Arsitek'
    elif karakteristik_responden['pekerjaan_id'] == 70:
        pekerjaan = 'Akuntan'
    elif karakteristik_responden['pekerjaan_id'] == 71:
        pekerjaan = 'Konsultan'
    elif karakteristik_responden['pekerjaan_id'] == 72:
        pekerjaan = 'Dokter'
    elif karakteristik_responden['pekerjaan_id'] == 73:
        pekerjaan = 'Bidan'
    elif karakteristik_responden['pekerjaan_id'] == 74:
        pekerjaan = 'Perawat'
    elif karakteristik_responden['pekerjaan_id'] == 75:
        pekerjaan = 'Apoteker'
    elif karakteristik_responden['pekerjaan_id'] == 76:
        pekerjaan = 'Psikiater/Psikolog'
    elif karakteristik_responden['pekerjaan_id'] == 77:
        pekerjaan = 'Penyiar Televisi'
    elif karakteristik_responden['pekerjaan_id'] == 78:
        pekerjaan = 'Penyiar Radio'
    elif karakteristik_responden['pekerjaan_id'] == 79:
        pekerjaan = 'Pelaut'
    elif karakteristik_responden['pekerjaan_id'] == 80:
        pekerjaan = 'Peneliti'
    elif karakteristik_responden['pekerjaan_id'] == 81:
        pekerjaan = 'Sopir'
    elif karakteristik_responden['pekerjaan_id'] == 82:
        pekerjaan = 'Pialang'
    elif karakteristik_responden['pekerjaan_id'] == 83:
        pekerjaan = 'Paranormal'
    elif karakteristik_responden['pekerjaan_id'] == 84:
        pekerjaan = 'Pedagang'
    elif karakteristik_responden['pekerjaan_id'] == 85:
        pekerjaan = 'Perangkat Desa'
    elif karakteristik_responden['pekerjaan_id'] == 86:
        pekerjaan = 'Kepala Desa'
    elif karakteristik_responden['pekerjaan_id'] == 87:
        pekerjaan = 'Biarawati'
    elif karakteristik_responden['pekerjaan_id'] == 88:
        pekerjaan = 'Wiraswasta'
    elif karakteristik_responden['pekerjaan_id'] == 89:
        pekerjaan = 'Lainnya'
    else:
        pekerjaan = 'Tidak Menajawab'

    # Field Umur 5_sd_9 Tahun
    if kategori_umur_tahun == "5-9 tahun":
        umur_5_sd_9_tahun = 1
    else:
        umur_5_sd_9_tahun = 0

    # Field Umur 10_sd_14 Tahun
    if kategori_umur_tahun == "10-14 tahun":
        umur_10_sd_9_tahun = 1
    else:
        umur_10_sd_9_tahun = 0

    # Field Umur 15_sd_24 Tahun
    if kategori_umur_tahun == "15-24 tahun":
        umur_15_sd_24_tahun = 1
    else:
        umur_15_sd_24_tahun = 0

    # Field Umur 25_sd_34 Tahun
    if kategori_umur_tahun == "25-34 tahun":
        umur_25_sd_34_tahun = 1
    else:
        umur_25_sd_34_tahun = 0

    # Field Umur 35_sd_44 Tahun
    if kategori_umur_tahun == "35-44 tahun":
        umur_35_sd_44_tahun = 1
    else:
        umur_35_sd_44_tahun = 0

    # Field Umur 45_sd_54 Tahun
    if kategori_umur_tahun == "45-54 tahun":
        umur_45_sd_54_tahun = 1
    else:
        umur_45_sd_54_tahun = 0

    # Field Umur 55_sd_64 Tahun
    if kategori_umur_tahun == "55-64 tahun":
        umur_55_sd_64_tahun = 1
    else:
        umur_55_sd_64_tahun = 0

    # Field Umur 65 Tahun Keatas
    if kategori_umur_tahun == "65 tahun keatas":
        umur_65_tahun_keatas = 1
    else:
        umur_65_tahun_keatas = 0

    val = (
        karakteristik_responden['survei_individu_detail_id'],
        karakteristik_responden['survei_rumah_tangga_id'],
        karakteristik_responden['survei_id'],
        karakteristik_responden['provinsi_id'],
        karakteristik_responden['nama_provinsi'],
        karakteristik_responden['kota_kabupaten_id'],
        karakteristik_responden['nama_kota_kabupaten'],
        karakteristik_responden['kecamatan_id'],
        karakteristik_responden['nama_kecamatan'],
        karakteristik_responden['kelurahan_id'],
        karakteristik_responden['nama_kelurahan'],
        karakteristik_responden['kd_puskesmas'],
        karakteristik_responden['nik'],
        karakteristik_responden['nama'],
        karakteristik_responden['tgl_lahir'],
        karakteristik_responden['jenis_kelamin'],
        umur_hari_ini,
        umur_tahun,
        umur_bulan_1,
        umur_bulan_2,
        kategori_umur_bulan,
        kategori_umur_tahun,
        pendidikan,
        pekerjaan,
        umur_5_sd_9_tahun,
        umur_10_sd_9_tahun,
        umur_15_sd_24_tahun,
        umur_25_sd_34_tahun,
        umur_35_sd_44_tahun,
        umur_45_sd_54_tahun,
        umur_55_sd_64_tahun,
        umur_65_tahun_keatas,
        karakteristik_responden['created_at'],
        karakteristik_responden['created_at']
    )

    cursor.execute(sql_insert_karakteristik_responden, val)
    db_conn.commit()