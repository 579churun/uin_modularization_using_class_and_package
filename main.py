nama = 'Churun Jauharoh A'
program = 'Elektrostatika'

print(f'program {program} oleh {nama}')

def hitung_arus(muatan, waktu):
    arus = muatan / waktu
    print(f'muatan = {muatan}Coulomb mengalir pada kawat penghantar selama = {waktu}detik')
    print(f'sehingga arus = {arus} A')
    return arus

# muatan = 360
# waktu = 60
arus = hitung_arus(360, 60)
arus = hitung_arus(5 * 10, 120)

def hitung_usaha(gaya, perpindahan):
    usaha = gaya * perpindahan
    print(f'gaya = {gaya}Newton bekerja pada materi sejauh = {perpindahan}meter')
    print(f'sehingga usaha = {usaha} Nm')
    return usaha

# gaya = 10
# perpindahan = 27
usaha = hitung_usaha(10, 27)
usaha = hitung_usaha(5 * 10, 70)

def hitung_daya(usaha, waktu):
    daya = usaha / waktu
    print(f'usaha = {usaha}Joule bekerja pada materi selama selang waktu = {waktu}detik')
    print(f'sehingga daya = {daya} Js')
    return daya

# usaha = 480
# waktu = 120
daya = hitung_daya(480, 120)
daya = hitung_daya(6 * 10, 30)