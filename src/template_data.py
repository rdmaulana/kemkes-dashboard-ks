import time


def ambil_data_template(cursor, id_individu): # fungsi ini untuk ambil template data
    select_Query = '''SELECT 
        survei_individu_survei_individu_detail_id, 
        survei_rt_survei_rt_id,
        survei_survei_id,
        survei_propinsi_id,
        survei_nm_propinsi,
        survei_kota_id,
        survei_nm_kota,
        survei_kecamatan_id,
        survei_nm_kecamatan,
        survei_kelurahan_id,
        survei_nm_kelurahan,
        survei_kd_puskesmas,
        survei_individu_nik,
        survei_individu_nama,
        survei_individu_tanggal_lahir,
        survei_individu_jk_id
        FROM public.raw_survei WHERE survei_individu_survei_individu_detail_id = %s;
        '''
    cursor.execute(select_Query, (id_individu,))
    query_Result = cursor.fetchone()

    if query_Result[15] == 1:
        jenis_kelamin = 'Laki-Laki'
    else:
        jenis_kelamin = 'Perempuan'

    constant_dict = {
        'survei_individu_detail_id': query_Result[0],
        'survei_rumah_tangga_id': query_Result[1],
        'survei_id': query_Result[2],
        'provinsi_id': query_Result[3],
        'nama_provinsi': query_Result[4],
        'kota_kabupaten_id': query_Result[5],
        'nama_kota_kabupaten': query_Result[6],
        'kecamatan_id': query_Result[7],
        'nama_kecamatan': query_Result[8],
        'kelurahan_id': query_Result[9],
        'nama_kelurahan': query_Result[10],
        'kd_puskesmas': query_Result[11],
        'nik': query_Result[12],
        'nama': query_Result[13],
        'tgl_lahir': query_Result[14],
        'jenis_kelamin': jenis_kelamin,
        "created_at": time.strftime("%a, %d %b %Y %H:%M:%S")
    }
    # data yang terambil akan disimpan pada tipe data dictionary
    return constant_dict  # mengembalikan nilai pada variabel dict
