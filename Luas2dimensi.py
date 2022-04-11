 while  True:
     balance=10000
     print("   ATM   ")
     print("""
     1)         Balance
     2)         Withdraw
     3)         Deposit
     4)         Quit
     """)
     try:
         Option=int(input("Enter Option: "))
    except Exception as e:
        print("Error:", e)
        print("Enter 1, 2, 3 or 4 only")
        continue
    if Option==:
        print("Balance ")