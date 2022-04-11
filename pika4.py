print("==== Menentukan angka Tahun Masehi yang merupakan tahun kabisat")

x = int(input('Masukkkan anka tahun masehi: '))

if x % 4 == 0:
    if x % 100 == 0:
        if x % 400 == 0:
            print("Tahun ", x, "merupakan tahun kabisat")
        else:
            print("Tahun", x, 'bukan tahun kabisat')
    else:
        print('Tahun', x, 'merupakan tahun kabisat')
else:
    print('Tahun', x, 'bukan tahun kabisat')