print("=== Menentukan bahwa karakter tersebut adalajh huruf vokal")

x = (input("Masukkan Karakter: "))
vokal = ('A', 'a', 'I', 'i', 'U', 'u', 'E', 'e', 'O', 'o')

if x in vokal:
    print('Karakter ', x, 'merupakan huruf vokal')
else:
    print('Karakter ',x, 'bukan merupakan huruf vokal' )