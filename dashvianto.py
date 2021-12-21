#table hi[ertensi mulai
#fielddiagnosisi hipertensi
def insertdiagnosisihipertensi():
  if tb_paru['15_tahun'] == '1' and keterangan_survei_individu['didagnosisi_hipertensi'] == 'y':
    didagnosisi_hipertensi = '1'
  else:
    didagnosisi_hipertensi = '0'

#tidakminumobat
def individudiagnosisitapitidakminumobat():
  if tb_paru['15_tahun'] == '1' and hipertensi['didiagnosis_hipertensi'] == '1' and keterangan_survei_individu['minum_obat_hipertensi_teratur'] == 't':
    didagnosisi_tapi_tidak_minum_obat = '1'
  else:
    didagnosisi_tapi_tidak_minum_obat = '0'

#tapiminumobat
def individudiagnosisitapiminumobat():
  if tb_paru['15_tahun'] == '1' and hipertensi['didiagnosis_hipertensi'] == '1' and keterangan_survei_individu['minum_obat_hipertensi_teratur'] == 'y':
    didagnosisi_tapi_minum_obat = '1'
  else:
    didagnosisi_tapi_minum_obat = '0'
    
def diukur_tekanan_darah():
  if tb_paru['15_tahun'] == '1' and keterangan_survei_individu['diukur_tekanan_darah'] == 'y':
    diukur_tekanan_darah = '1'
  else:
    diukur_tekanan_darah = '0'
    
def sistol():
  sistol = keterangan_survei_individu['sistolik']

def distolic():
  distolic = keterangan_survei_individu['distolic']

def suspektekanandarahtinggi():
  if hipertensi['diukur_tekanan_darah']=='1' and hipertensi['sistol'] > 140 and hipertensi['distolic'] > 90:
    suspektekanandarahtinggi = '1'
  else:
    suspektekanandarahtinggi = '0'
#end hipertensi

#start rokoks 
def umur5sampai9():
  if karakteristik_responden['kategori_umur'] == '5-9 tahun' and rokok['individu_merokok'] == '1':
    umur5sampai9 = '1'
  else:
    umur5sampai9 = '0'

def umur10sampai14():
  if karakteristik_responden['kategori_umur'] == '10-14 tahun' and rokok['individu_merokok'] == '1':
    umur10sampai14 = '1'
  else:
    umur10sampai14 = '0'

def umur15sampai24():
  if karakteristik_responden['kategori_umur'] == '15-24 tahun' and rokok['individu_merokok'] == '1':
    umur15sampai24 = '1'
  else:
    umur15sampai24 = '0'
    
def umur25sampai34():
  if karakteristik_responden['kategori_umur'] == '25-34 tahun' and rokok['individu_merokok'] == '1':
    umur25sampai34 = '1'
  else:
    umur25sampai34 = '0'

def umur35sampai44():
  if karakteristik_responden['kategori_umur'] == '35-44 tahun' and rokok['individu_merokok'] == '1':
    umur35sampai44 = '1'
  else:
    umur35sampai44 = '0'

def umur45sampai54():
  if karakteristik_responden['kategori_umur'] == '45-54 tahun' and rokok['individu_merokok'] == '1':
    umur45sampai54 = '1'
  else:
    umur45sampai54 = '0'
    
def umur55sampai64():
  if karakteristik_responden['kategori_umur'] == '55-64 tahun' and rokok['individu_merokok'] == '1':
    umur55sampai64 = '1'
  else:
    umur55sampai64 = '0'

def umur65keatas():
  if karakteristik_responden['kategori_umur'] == '65 tahun ke atas' and rokok['individu_merokok'] == '1':
    umur65keatas = '1'
  else:
    umur65keatas = '0'
