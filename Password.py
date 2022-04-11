import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "123456790"
symbol = "!@#$%^&*()-<>?,./':[]{}"
all = lower + upper + numbers + symbol
length = 5
password = "".join(random.sample(all,length))
print(password)