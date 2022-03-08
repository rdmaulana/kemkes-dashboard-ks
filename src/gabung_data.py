# =============================
#           Gabung Data
# ==============================


def gabungData(templateData, dataTambahan):  # fungsi ini untuk menggabungkan templateData dan dataTambahan
    hasil = {}
    hasil.update(templateData)
    hasil.update(dataTambahan)

    return hasil  # mengembalikan nilai hasil penggabungan dua variabel