mylist = (list(range(10)))
listganjil = []
listgenap = []
for i in mylist:
    if (i**2)%2 == 0:
        listgenap.append(i**2)
    else:
        listganjil.append(i**2)
print("List Genap", listgenap)
print("List Ganjil", listganjil)