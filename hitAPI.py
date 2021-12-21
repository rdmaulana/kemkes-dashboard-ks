# program ini untuk hit API pemadanan data

import requests

import psycopg2

db_conn = psycopg2.connect("dbname=iks_v2 user=postgres password=pacific1904")
# Sesuaikan dbname, user, password sesuai postgres anda
cursor = db_conn.cursor()

url = "http://192.168.230.34:1323/event/akses_dukcapil"

sql = "SELECT survei_survei_id, survei_tanggal, survei_no_urut_rt, survei_no_urut_kel, survei_surveyor, survei_supervisor, survei_no_kk, survei_nama_kk, survei_alamat, survei_propinsi_id, survei_kota_id, survei_kecamatan_id, survei_kelurahan_id, survei_kd_puskesmas, survei_nm_kota, survei_nm_propinsi, survei_nm_kecamatan, survei_nm_kelurahan, survei_iks_besar, survei_iks_inti, survei_rt_new, survei_rw_new, survei_kode, survei_created_at, survei_updated_at, survei_status_pindah, survei_status_delete, survei_step_number, survei_sumber, survei_status_kepala_keluarga, survei_rt_old, survei_rw_old, survei_status_migrasi, survei_catatan_migrasi, survei_iks_inti_old, survei_iks_besar_old, survei_deleted_at, survei_survei_id_old, survei_rt_survei_rt_id, survei_rt_jml_art, survei_rt_jml_art_wawancara, survei_rt_jml_art_dewasa, survei_rt_jml_art_10_54_thn, survei_rt_jml_art_12_59_bln, survei_rt_jml_art_0_11_bln_45, survei_rt_sab, survei_rt_sat, survei_rt_jk, survei_rt_js, survei_rt_gjb, survei_rt_obat_gjb, survei_rt_pasung, survei_rt_keterangan, survei_rt_kode, survei_rt_supervisor, survei_rt_surveyor, survei_rt_indikator_8, survei_rt_indikator_11, survei_rt_indikator_12, survei_rt_status_delete, survei_rt_created_at, survei_rt_updated_at, survei_rt_deleted_at, survei_rt_status_migrasi, survei_rt_catatan_migrasi, survei_rt_kd_puskesmas, survei_rt_survei_id_old, survei_individu_survei_individu_detail_id, survei_individu_jkn, survei_individu_merokok, survei_individu_babj, survei_individu_sab, survei_individu_tb, survei_individu_obat_tb, survei_individu_batuk, survei_individu_hipertensi, survei_individu_obat_hipertensi, survei_individu_tekanan_darah, survei_individu_sistolik, survei_individu_diastolik, survei_individu_kb, survei_individu_kb_follow, survei_individu_kb_detail, survei_individu_faskes, survei_individu_asi_ekslusif, survei_individu_imunisasi, survei_individu_pantau_balita, survei_individu_keterangan, survei_individu_catatan_intervensi, survei_individu_no_urut_rt, survei_individu_no_urut_kel, survei_individu_nik, survei_individu_status_nik, survei_individu_nama, survei_individu_hub_kel_id, survei_individu_tanggal_lahir, survei_individu_umur_bln, survei_individu_umur_thn, survei_individu_jk_id, survei_individu_stmarital_id, survei_individu_wuh, survei_individu_agama_id, survei_individu_pendidikan_id, survei_individu_pekerjaan_id, survei_individu_indikator_1, survei_individu_indikator_2, survei_individu_indikator_3, survei_individu_indikator_4, survei_individu_indikator_5, survei_individu_indikator_6, survei_individu_indikator_7, survei_individu_indikator_8, survei_individu_indikator_9, survei_individu_indikator_10, survei_individu_indikator_11, survei_individu_indikator_12, survei_individu_kode, survei_individu_supervisor, survei_individu_surveyor, survei_individu_status_delete, survei_individu_created_at, survei_individu_updated_at, survei_individu_survei_id, survei_individu_status_survei, survei_individu_deleted_at, survei_individu_status_migrasi, survei_individu_catatan_migrasi, survei_individu_kd_puskesmas, survei_individu_survei_id_old FROM public.raw_survei limit 10;"
# LAKUKAN QUERY KE RAW_SURVEI
cursor.execute(sql)
query_Result = cursor.fetchall()

for data in query_Result:
    payload={'survei_individu_detail_id': data[67],
    'NIK': data[91],
    'NAMA_LGKP': data[94],
    'JENIS_KLMIN': data[98],
    'TMPT_LHR': 'JAXXXXX', #belum ada di raw survei
    'TGL_LHR': data[95],
    'STATUS_KAWIN': data[99],
    'JENIS_PKRJN': data[103],
    'NAMA_LGKP_IBU': 'SRXXXX', #belum ada di raw survei
    'ALAMAT': data[8],
    'NO_PROB': data[9],
    'NO_KAB': data[10],
    'NO_KEC': data[11],
    'NO_KEL': data[12],
    'PROB_NAME': data[15],
    'KAB_NAME': data[14],
    'KEC_NAME': data[16],
    'KEL_NAME': data[17],
    'NO_RW': data[21],
    'NO_RT': data[20],
    'TRESHOLD': '90',
    'user_id': '00_KEMENKES',
    'password': '123',
    'ip_user': '127.0.0.1'}
    files=[]
    headers = {}
    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)
