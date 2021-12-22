from datetime import date

from funcdash import *

def main(db_conn, cursor, id_individu, id_ada, id_tidak_ada):
    # tanggal sekarang untuk created_at
    current_date = date.today()

    status_id = checkIdSurveiIndividu(cursor, id_individu)

    if status_id == 1:
        template_data = templateData(cursor, id_individu, current_date)
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

        insertSLCS = insertDataSasaranLifeCycleSpm(db_conn, cursor, sasaran_life_cycle_spm)
        # fungsi ini untuk memasukkan data ke table SASARAN LIFE CYCLE SPM sehingga paraneternya adalah SASARAN LIFE CYCLE SPM

        # print(f"id : {insertSLCS} berhasil masuk tabel SLCS") # cetak hasil aja. buat kontrol. boleh dihapus line ini.

        # ==============================
        #     Keluarga Berencana
        # ==============================

        data_for_keluarga_berencana = specificDataForKeluargaBerencana(cursor, id_individu)

        keluarga_berencana = gabungData(template_data, data_for_keluarga_berencana)

        insertKB = insertDataKeluargaBerencana(db_conn, cursor, keluarga_berencana)
        # print(f"id : {insertKB} berhasil masuk tabel KB") # cetak hasil aja. buat kontrol. boleh dihapus line ini.

        # ==============================
        #     Persalinan di Faskes
        # ==============================

        data_for_persalinan_di_faskes = specificDataForPersalinanDiFaskes(cursor, id_individu)

        persalinan_di_faskes = gabungData(template_data, data_for_persalinan_di_faskes)

        insertPdF = insertDataPersalinanDiFaskes(db_conn, cursor, persalinan_di_faskes)

        # print(f"id : {insertPdF} berhasil masuk tabel Pdf") # cetak hasil aja. buat kontrol. boleh dihapus line ini.

        #     Created By Aldon

        #     Created By Deca

        # ==============================
        #     Imunisasi dasar Lengkap
        # ==============================

        data_for_IDL = specificDataForIDL(cursor, id_individu)

        imunisasi_dasar_lengkap = gabungData(template_data, data_for_IDL)

        insertIDL = insertDataIDL(db_conn, cursor, imunisasi_dasar_lengkap)

        # ==============================
        #        Asi Eksklusif
        # ==============================

        data_for_Asi_Eksklusif = specificDataForAsiEksklusif(cursor, id_individu)

        Asi_Eksklusif = gabungData(template_data, data_for_Asi_Eksklusif)

        insert_Asi_Eksklusif = insertDataAsiEksklusif(db_conn, cursor, Asi_Eksklusif)

        # ==============================
        #       Tumbuh Kembang
        # ==============================

        data_for_tumbuh_kembang = specificDataForTumbuhKembang(cursor, id_individu)

        tumbuh_kembang = gabungData(template_data, data_for_tumbuh_kembang)

        insert_tumbuh_kembang = insertDataTumbuhKembang(db_conn, cursor, tumbuh_kembang)

        # ==============================
        #           TB Paru
        # ==============================

        data_for_TB_Paru = specificDataForTBParu(cursor, id_individu)

        TB_Paru = gabungData(template_data, data_for_TB_Paru)

        insert_TB_Paru = insertDataTBParu(db_conn, cursor, TB_Paru)

        # ==============================
        #            Rokok
        # ==============================

        data_for_Rokok = specificDataForRokok(cursor, id_individu)

        Rokok = gabungData(template_data, data_for_Rokok)

        insert_Rokok = insertDataRokok(db_conn, cursor, Rokok)

        # ==============================
        #             JKN
        # ==============================

        data_for_JKN = specificDataForJKN(cursor, id_individu)

        JKN = gabungData(template_data, data_for_JKN)

        insert_JKN = insertDataJKN(db_conn, cursor, JKN)
        # ==============================
        #        Perilaku SAB
        # ==============================

        data_for_Perilaku_SAB = specificDataForPerilakuSAB(cursor, id_individu)

        Perilaku_SAB = gabungData(template_data, data_for_Perilaku_SAB)

        insert_Perilaku_SAB = insertDataPerilakuSAB(db_conn, cursor, Perilaku_SAB)

        # ==============================
        #       Perilaku Jamban
        # ==============================

        data_for_Perilaku_Jamban = specificDataForPerilakuJamban(cursor, id_individu)

        Perilaku_Jamban = gabungData(template_data, data_for_Perilaku_Jamban)

        insert_Perilaku_Jamban = insertDataPerilakuJamban(db_conn, cursor, Perilaku_Jamban)

        #     Created By Deca

        #     Created By Vianto

        # ==============================
        #          Hipertensi
        # ==============================

        data_for_Hipertensi = specificDataForHipertensi(cursor, id_individu)

        Hipertensi = gabungData(template_data, data_for_Hipertensi)

        insert_Hipertensi = insertDataHipertensi(db_conn, cursor, Hipertensi)

        # ==============================
        #           ROKOkS
        # ==============================

        data_for_ROKOkS = specificDataForROKOkS(cursor, id_individu)

        ROKOkS = gabungData(template_data, data_for_ROKOkS)

        insert_ROKOkS = insertDataROKOkS(db_conn, cursor, ROKOkS)

        #     Created By Vianto

        #     Created By Aldi

        # ==============================
        #     Karakterisik Responden
        # ==============================

        data_for_karakteristik_responden = specificDataKarakteristikResponden(cursor, id_individu)

        karakteristik_responden = gabungData(template_data, data_for_karakteristik_responden)

        insert_karakteristik_responden = insertDataKarakteristikResponden(db_conn, cursor, karakteristik_responden, current_date)

        #     Created By Aldi

        #     Created By Aldon

        # ==============================
        #       Rokok by program
        # ==============================

        data_for_rokok_by_program = specificDataForRokokByProgram(cursor, id_individu)

        rokok_by_program = gabungData(template_data, data_for_rokok_by_program)

        insertRBP = insertDataRokokByProgram(db_conn, cursor, rokok_by_program)

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

        insertDKB = insertDataDenominatorKB(db_conn, cursor, denominator_KB)

        #     Created By Aldon

        #     Created By Deca

        # ==============================
        #       KB by Program
        # ==============================
        data_for_KB_by_Program = specificDataForKBbyProgram(cursor, id_individu)

        KB_by_Program = gabungData(template_data, data_for_KB_by_Program)

        insert_KB_by_Program = insertDataKBbyProgram(db_conn, cursor, KB_by_Program)

        #     Created By Deca

        id_ada.append(id_individu)

    else:
        id_tidak_ada.append(id_individu)

    return (id_ada, id_tidak_ada)


id_ada = []
id_tidak_ada = []
readID = readTXT()  # fungsi ini untuk membaca id pada file txt

connect = connectDB()
db_conn = connect[0]
cursor = connect[1]

for id_individu in readID:
    res = main(db_conn, cursor, id_individu, id_ada, id_tidak_ada)  # fungsi main akan dipanggil sebanyak id yang tertera pada file txt

closeDB(db_conn, cursor)

print(f"{len(res[0])} id yang diproses = {res[0]}")
print(f"{len(res[1])} id yang tidak dapat diproses = {res[1]}")
print()

