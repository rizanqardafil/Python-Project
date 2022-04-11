class BankAcc(object):
    def __init__(self, name, pin, balance=10000.0): #If you want to give default balance if not provided explicitly do this
        self.name = name                    #variable where value is stored = expression
        self.pin = pin
        self.balance = balance
    def CheckUser(self, name, pin):       #A function to check wheather the user is valid or not
        try:
            if name != self.name or pin != self.pin:
                raise ValueError
            print("Name and Pin Matches")
        except ValueError:
            print("Name or Password is not correct")
            exit(0)

    def __str__(self):
        return "{}'s Bank Account with Balance {}".format(self.name, self.balance) #using only one substition in the string but providing 2 variables

    def checkbalance(self):
        return '$' + str(self.balance) #self is the instance of the class for printing balance use self.balance

    def deposit(self, amount):
        self.balance += amount        #self.ammount will create a new property but i think you want to increase your balance

    def withdraw(self, amount):
        try:                          #use try catct if raising an excpetion
            if self.balance >= amount:    #balance should be greater than and equal to the ammount 
                self.balance -= amount
            else:
                raise ValueError
        except ValueError:                #Handle your exception 
                print("Cannot be done. You have insufficient funds.")

    def filedata(self):              #An extra function for writing in the file.
        return "{},{},{}".format(self.name,self.pin,self.balance)

accountfile = open("ATMACC.txt", "r+") #"r+" should be used becuase you are reading and writing
accountfiledata=accountfile.read().split(",")  #Can be done in the class it self
BankUser = BankAcc(accountfiledata[0],accountfiledata[1],float(accountfiledata[2])) #For simplicity i used comma seperated data and created an instance of it 
name=input("What is your name? ")
pin=input("What is your Pin #? ")
BankUser.CheckUser(name, pin)
#accountfile.write("Name: " + name + "\n" + "PIN: " + pin + "\n") #You did not specify that you want to write in file as well
#USER_BALANCE = 10000          it is not needed

while True:    #For multiple options use numbers instead of words such as 1 for deposit etc
    answer=input("Would you like to deposit, withdraw, check balance, or exit? ")
    if answer=="deposit" or answer== "Deposit":
        x= input("How much would you like to deposit? ")
        BankUser.deposit(float(x))   #use your deposit function
        print ("Your new balance is: " + BankUser.checkbalance())
        #continue  #Why using continue, no need for it
    elif answer== "withdraw" or answer== "Withdraw":
        y= input("How much would you like to withdraw? ")
        BankUser.withdraw(float(y))         #Use Your withdraw function why reapeating your self
    elif answer== "check balance" or answer== "Check Balance":
        print(BankUser.checkbalance())
    elif answer== "exit" or answer== "Exit":
        print ("Goodbye!")
        accountfile.close()
        exit(0)
    else:
        print ("I'm sorry, that is not an option")
    accountfile.seek(0)               #I dont know whether you want to record all tranction or a single one 
    accountfile.truncate()            #perform write function at the last
    accountfile.write(BankUser.filedata())
