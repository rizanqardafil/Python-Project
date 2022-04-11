x = int(input('Masukkan Total Belanja'))
z = x * 0.05
if x >= 100000:
    print('Total Belanja: ', x)
    print("Diskon Belanja", z)
    print("Total Belanja dikurangin Diskon", x-z)
else:
    print("Total Belanja: ", x)
    print("Diskon Belanja: 0")
    print("Total Belanja dikurangi Diskon :", x)