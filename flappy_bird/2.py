def prima(x):
    if x > 2: 
         for i in range(2, x):
            if x % i == 0:
                 return False
            return True
    return False
print(prima(1))