from datetime import date

import datetime

import sys

from src.connection_db import *
from src.cek_data import *
from src.template_data import *
from src.sasaran_life_cycle_spm import *
from src.gabung_data import *
from src.keluarga_berencana import *
from src.persalinan_di_faskes import *
from src.imunisasi_dasar_lengkap import *
from src.asi_eksklusif import *
from src.tumbuh_kembang import *
from src.tb_paru import *
from src.rokok import *
from src.jkn import *
from src.perilaku_sab import *
from src.perilaku_jamban import *
from src.hipertensi import *
from src.karakteristik_responden import *
from src.rokoks import *
from src.rokok_by_program import *
from src.rokok_by_program_umur import *
from src.denominator_kb import *
from src.kb_by_program import *
from src.log import *


def dashboard(db_conn, cursor, id_individu, id_ada, id_gagal):
    # tanggal sekarang untuk created_at
    current_date = date.today()

    print(f"id {id_individu} diproses")

    status_id = checkIdSurveiIndividu(cursor, id_individu)
    status_umur = cekUmur(cursor, id_individu)

    if status_id == 1 and status_umur == 200:
        template_data = ambil_data_template(cursor, id_individu)
        # fungsi ini digunakan untuk template data yang akan digunakan pada semua table. Ini data pada field tambahan yang ada pada seluruh table
        # fungsi ini dikasih paramater karena data diambil berdasarkan id_individu
        # variabel template_data akan digunakan untuk seluruh table jadi jangan diapa-apain

        #     Created By Aldon

        # =============================
        #     Sasaran Life Cycle SPM
        # ==============================

        data_for_sasaran_life_cycle_spm = specificDataForSasaranLifeCycleSpm(cursor, id_individu)
        # fungsi ini digunakan untuk tambahan data yang spesifik untuk table SasaranLifeCycleSpm
        # fungsi ini dikasih paramater karena data diambil berdasarkan id_individu


        sasaran_life_cycle_spm = gabungData(template_data, data_for_sasaran_life_cycle_spm)
        # fungsi ini digunakan untuk menggabungkan template data dan data_for_sasaran_life_cycle_spm jadi parameternya dua itu
        # variabel sasaran_life_cycle_spm adalah record untuk table SASARAN LIFE CYCLE SPM

        insertDataSasaranLifeCycleSpm(db_conn, cursor, sasaran_life_cycle_spm)
        # fungsi ini untuk memasukkan data ke table SASARAN LIFE CYCLE SPM sehingga paraneternya adalah SASARAN LIFE CYCLE SPM

        # print(f"id : {insertSLCS} berhasil masuk tabel SLCS") # cetak hasil aja. buat kontrol. boleh dihapus line ini.

        # ==============================
        #     Keluarga Berencana
        # ==============================

        data_for_keluarga_berencana = specificDataForKeluargaBerencana(cursor, id_individu)

        keluarga_berencana = gabungData(template_data, data_for_keluarga_berencana)

        insertDataKeluargaBerencana(db_conn, cursor, keluarga_berencana)
        # print(f"id : {insertKB} berhasil masuk tabel KB") # cetak hasil aja. buat kontrol. boleh dihapus line ini.

        # ==============================
        #     Persalinan di Faskes
        # ==============================

        data_for_persalinan_di_faskes = specificDataForPersalinanDiFaskes(cursor, id_individu)

        persalinan_di_faskes = gabungData(template_data, data_for_persalinan_di_faskes)

        insertDataPersalinanDiFaskes(db_conn, cursor, persalinan_di_faskes)

        # print(f"id : {insertPdF} berhasil masuk tabel Pdf") # cetak hasil aja. buat kontrol. boleh dihapus line ini.

        #     Created By Aldon

        #     Created By Deca

        # ==============================
        #     Imunisasi dasar Lengkap
        # ==============================

        data_for_IDL = specificDataForIDL(cursor, id_individu)

        imunisasi_dasar_lengkap = gabungData(template_data, data_for_IDL)

        insertDataIDL(db_conn, cursor, imunisasi_dasar_lengkap)

        # ==============================
        #        Asi Eksklusif
        # ==============================

        data_for_Asi_Eksklusif = specificDataForAsiEksklusif(cursor, id_individu)

        Asi_Eksklusif = gabungData(template_data, data_for_Asi_Eksklusif)

        insertDataAsiEksklusif(db_conn, cursor, Asi_Eksklusif)

        # ==============================
        #       Tumbuh Kembang
        # ==============================

        data_for_tumbuh_kembang = specificDataForTumbuhKembang(cursor, id_individu)

        tumbuh_kembang = gabungData(template_data, data_for_tumbuh_kembang)

        insertDataTumbuhKembang(db_conn, cursor, tumbuh_kembang)

        # ==============================
        #           TB Paru
        # ==============================

        data_for_TB_Paru = specificDataForTBParu(cursor, id_individu)

        TB_Paru = gabungData(template_data, data_for_TB_Paru)

        insertDataTBParu(db_conn, cursor, TB_Paru)

        # ==============================
        #            Rokok
        # ==============================

        data_for_Rokok = specificDataForRokok(cursor, id_individu)

        Rokok = gabungData(template_data, data_for_Rokok)

        insertDataRokok(db_conn, cursor, Rokok)

        # ==============================
        #             JKN
        # ==============================

        data_for_JKN = specificDataForJKN(cursor, id_individu)

        JKN = gabungData(template_data, data_for_JKN)

        insertDataJKN(db_conn, cursor, JKN)
        # ==============================
        #        Perilaku SAB
        # ==============================

        data_for_Perilaku_SAB = specificDataForPerilakuSAB(cursor, id_individu)

        Perilaku_SAB = gabungData(template_data, data_for_Perilaku_SAB)

        insertDataPerilakuSAB(db_conn, cursor, Perilaku_SAB)

        # ==============================
        #       Perilaku Jamban
        # ==============================

        data_for_Perilaku_Jamban = specificDataForPerilakuJamban(cursor, id_individu)

        Perilaku_Jamban = gabungData(template_data, data_for_Perilaku_Jamban)

        insertDataPerilakuJamban(db_conn, cursor, Perilaku_Jamban)

        #     Created By Deca

        #     Created By Vianto

        # ==============================
        #          Hipertensi
        # ==============================

        data_for_Hipertensi = specificDataForHipertensi(cursor, id_individu)

        Hipertensi = gabungData(template_data, data_for_Hipertensi)

        insertDataHipertensi(db_conn, cursor, Hipertensi)

        # ==============================
        #           ROKOkS
        # ==============================

        data_for_ROKOkS = specificDataForROKOkS(cursor, id_individu)

        ROKOkS = gabungData(template_data, data_for_ROKOkS)

        insertDataROKOkS(db_conn, cursor, ROKOkS)

        #     Created By Vianto

        #     Created By Aldi

        # ==============================
        #     Karakterisik Responden
        # ==============================

        data_for_karakteristik_responden = specificDataKarakteristikResponden(cursor, id_individu)

        karakteristik_responden = gabungData(template_data, data_for_karakteristik_responden)

        insertDataKarakteristikResponden(db_conn, cursor, karakteristik_responden, current_date)

        #     Created By Aldi

        #     Created By Aldon

        # ==============================
        #       Rokok by program
        # ==============================

        data_for_rokok_by_program = specificDataForRokokByProgram(cursor, id_individu)

        rokok_by_program = gabungData(template_data, data_for_rokok_by_program)

        insertDataRokokByProgram(db_conn, cursor, rokok_by_program)

        # ==============================
        #    Rokok by prorgram (Umur)
        # ==============================

        data_for_rokok_by_program_umur = specificDataForRokokByProgramUmur(cursor, id_individu)

        rokok_by_program_umur = gabungData(template_data, data_for_rokok_by_program_umur)

        insertRBPU = insertDataRokokByProgramUmur(db_conn, cursor, rokok_by_program_umur)

        # ==============================
        #       Denominator KB
        # ==============================

        data_for_rokok_by_denominator_KB = specificDataForDenominatorKB(cursor, id_individu)

        denominator_KB = gabungData(template_data, data_for_rokok_by_denominator_KB)

        insertDataDenominatorKB(db_conn, cursor, denominator_KB)

        #     Created By Aldon

        #     Created By Deca

        # ==============================
        #       KB by Program
        # ==============================
        data_for_KB_by_Program = specificDataForKBbyProgram(cursor, id_individu)

        KB_by_Program = gabungData(template_data, data_for_KB_by_Program)

        insertDataKBbyProgram(db_conn, cursor, KB_by_Program)

        #     Created By Deca

        id_ada += 1
        print(f"id {id_individu} berhasil, Jumlah id yang berhasil diproses : {id_ada}")
        insertUpdateLog(db_conn, cursor, id_individu, True, True, time.strftime("%a, %d %b %Y %H:%M:%S"))

    else:
        id_gagal += 1
        print(f"id {id_individu} tidak dapat diproses, Jumlah id yang gagal diproses : {id_gagal}")
        exist = False
        if status_umur == 400:
            exist = True
        insertUpdateLog(db_conn, cursor, id_individu, exist, False, time.strftime("%a, %d %b %Y %H:%M:%S"))

    return id_ada, id_gagal


id_ada = 0
id_gagal = 0
start = datetime.datetime.now()

db_conn, cursor = connect_db()

id = readSQL(cursor, sys.argv)
for x in id:
    for id_individu in x:
        id_ada, id_gagal = dashboard(db_conn, cursor, id_individu, id_ada, id_gagal)  # fungsi main akan dipanggil sebanyak id yang tertera pada file txt


closeDB(db_conn, cursor)
finish = datetime.datetime.now()

print()
print(f"Jumlah id yang berhasil diproses = {id_ada}")
print(f"Jumlah id yang gagal diproses = {id_gagal}")
print()
print(f'Data yang diproses adalah data dari tanggal {(sys.argv[1])} hingga {(sys.argv[2])}')
print(f"Lama Proses {finish - start}")