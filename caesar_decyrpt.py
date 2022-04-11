d=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
a = input("Masukkan Kata = ")
b = ""
c = int(input("Masukkan Kunci = "))
for x in range(len(a)):
    p = d.index(a[x])+c
    b=b+d[p%26]
for y in ""+b:
    print(y)