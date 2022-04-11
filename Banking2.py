print ("selamat datang di program penghitung uang pecahan")

jumlah = input("jumlah uang anda")
hasil=jumlah/100000
sisa=jumlah%100000
print ("jumlah uang pecahan anda")
print hasil, ("seratusribuan")
if (sisa>=50000):
    hasil=sisa/50000
    sisa=sisa%50000
    print hasil, ("limapuluhribuan")
if (sisa>=20000):
    hasil=sisa/20000
    sisa=sisa%20000
    print hasil, ("duapuluhribuan")
if (sisa>=10000):
    hasil=sisa/10000
    sisa=sisa%10000
    print hasil, ("sepuluhribuan")
if (sisa>=5000):
    hasil=sisa/5000
    sisa=sisa%5000
    print hasil, ("limaribuan")
if (sisa>=1000):
    hasil=sisa/1000
    sisa=sisa%1000
    print hasil, ("seribuan")
if (sisa>=500):
    hasil=sisa/500
    sisa=sisa%500
    print hasil, ("limaratusan")
if (sisa>=100): 
    hasil=sisa/100
    sisa=sisa%100
    print hasil, ("seratusan")
else:
    print ("rupiah")
