mylist = (list(range(91)))
listbaru = []
for i in mylist:
    if i <= 90:
        listbaru.append(i)
    else:
        print("Error")

print("List Baru", listbaru)