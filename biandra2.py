print("Program to print star pattern in different style: \n");
num_rows = 5
for i in range (0,num_rows):
    for j in range (num_rows,i,-1):
        print("* ", end="")
    print()