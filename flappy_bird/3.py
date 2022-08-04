def fibonacci(x):
    if x<2:
        return x
    else:
        return fibonacci(x-2)+fibonacci(x-1)
n = int(input("Fibonacci Number"))
a = []
if n <= 0:
    print("Not Found Please enter A positif Interger")
else:
    print("Bilangan Fibonaci")
    for i in range(1, n+1):
        a.append(fibonacci(i))
        print(fibonacci(i))
print(a[-1])