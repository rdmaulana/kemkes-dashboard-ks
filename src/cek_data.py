def readSQL(cursor, waktu):
    ID = "SELECT survei_individu_survei_individu_detail_id FROM public.raw_survei where survei_individu_created_at " \
         "BETWEEN '%s' AND '%s' OR survei_individu_updated_at BETWEEN '%s' AND '%s' ORDER BY " \
         "survei_individu_created_at;" % (waktu[1], waktu[2], waktu[1], waktu[2])
    cursor.execute(ID)
    id_from_query = cursor.fetchall()
    return id_from_query

def checkIdSurveiIndividu(cursor, id_individu): # fungsi untuk memeriksa apakah id_individu tersedia pada tabel survei individu
    sql_check_survei_individu = "SELECT EXISTS(select survei_individu_survei_individu_detail_id FROM raw_survei " \
                                "where survei_individu_survei_individu_detail_id = '%s');" % (id_individu)
    cursor.execute(sql_check_survei_individu)
    status_id_survei_individu = cursor.fetchone()

    if status_id_survei_individu == (1,):
        return 1 # mengembalikan nilai 1 jika id_individu tersedia
    else:
        return 0 # mengembalikan nilai 0 jika id_individu tidak tersedia


def cekUmur(cursor, id_individu):
    sql_cek_umur = "SELECT survei_individu_umur_thn, survei_individu_umur_bln FROM public.raw_survei where survei_individu_survei_individu_detail_id = %s"

    cursor.execute(sql_cek_umur, (id_individu,))
    data_cek = cursor.fetchone()

    if data_cek == None:
        return 404
    elif data_cek[0] == None and data_cek[1] == None:
        return 400

    return 200