total1=0
total2=0
totalsemua=0
jenis1=""
jenis2=""

print("=== Selamat Datang di Restoran Pacu Jalur ===")
nama = input("Masukkan nama Konsumen: ")
print ("Nama Konsumen :", nama)
print("")
print ("Menu Makanan")
    
def pilihan(i):
        switcher={
                1:'----Spaghetti Bolognaise 20001----',
                2:'----French Fries 17273----',
                3:'----Mie Ayam Teriyaki 28182----',
                4:'----Nasi + Mie Ayam Teriyaki Saos 30000----',
                5:'----Nasi + Sapo Tahu Seafood 34364----',
                6:'----Chicken Cordon Bleu 	41819----',
                7:'----Chicken Steak Chessy 34819----',
                8:'----Fish & Chips 47273----',
                9:'----Kwetiau Ayam 24545----',
                10:'----Kwetiau Ayam Bakso 29091----',
                11:'----Kwetiau Goreng Ayame 17273----',
                12:'----French Fries 17273----',
                13:'----French Fries 17273----',
                14:'----French Fries 17273----',
                15:'----French Fries 17273----',
                16:'----French Fries 17273----',
                17:'----French Fries 17273----',
                18:'----French Fries 17273----',
                19:'----French Fries 17273----',
                20:'----French Fries 17273----',
             }
        return switcher.get(i,"Masukan Pilihan yang Benar!")

print("1. Nasi Goreng")
print("2. Soto")
print("3. Mie Ayam")
nomor=int(input("Masukan Pilihan: "))
menu=pilihan(nomor)
print (menu)
porsi1= int(input("Berapa Porsi: "))

if nomor==1:
    total1=total1+porsi1*12000
    print ("Hasilnya = ", total1)
    jenis1=("Nasi Goreng")
if nomor==2:
    total1=total1+porsi1*10000
    print ("Hasilnya = ", total1)
    jenis1=("Soto")
if nomor==3:
    total1=total1+porsi1*9000
    print ("Hasilnya = ", total1)
    jenis1=("Mie Ayam")

def pilihan(i):
        switcher={
                1:'----Es Teh 3000----',
                2:'----Es Jeruk 4000----',
                3:'----Es Kopi 3000----'
             }
        return switcher.get(i,"Masukan Pilihan yang Benar!")
print("\nMenu Minuman")
print("1. Es teh")
print("2. Es jeruk")
print("3. Es kopi")
nomor=int(input("Masukan Pilihan: "))
menu=pilihan(nomor)
print (menu)
porsi2= int(input("Berapa Gelas: "))
if nomor==1:
    total2=total2+(porsi2*3000)
    print ("Hasilnya = ", total2)
    jenis2=("Es Teh")
if nomor==2:
    total2=total2+(porsi2*4000)
    print ("Hasilnya = ", total2)
    jenis2=("Es Jeruk")
if nomor==3:
    total2=total2+(porsi2*3000)
    print ("Hasilnya = ", total2)
    jenis2=("Es Kopi")
    
uang=int(input("\nUang Tunai: Rp."))
totalsemua=total1+total2    
print("\n=========================")
print("======= S T R U K =======")
print("=========================")
print ("=== Nama      :",nama)
print ("=== Beli      :",porsi1,jenis1)
print ("===            ",porsi2,jenis2)
print ("=== Tagihan   :Rp.",totalsemua)
print ("=== Uang      :Rp.",uang)
akhir=int(uang-totalsemua)
print ("=== Kembalian :Rp.",akhir)
print("=========================")
print("=========================")