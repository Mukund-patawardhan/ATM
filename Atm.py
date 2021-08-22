class User (object):
    def __init__(self , name , age , pin , contactNo , email ):
        self.name = name
        self.age = age
        self.balance = 0
        self.pin = pin
        self.contactNo = contactNo
        self.email = email

    def showBalance(self):
        print("The balance is" , self.balance)
    
    def withdrawCash(self , amount):
        if self.balance - amount >= 0:
            self.balance = self.balance - amount
            print("Cash withdrawn successfully")
        else:
            print("Account does not have sufficient funds")

    def depositCash(self , amount):
        self.balance = self.balance + amount
        print("Cash depositted successfully")

    def showDetails(self):
        print( "Name :- " , self.name )
        print( "Age :- " , self.age )
        print( "Pin :- " , self.pin )
        print( "Contact Number :- " , self.contactNo )
        print( "Email :- " , self.email )

    def changeDetails(self , name , age , contactNo , email , currentPin , newPin):
        if currentPin == self.pin :
            self.name = name
            self.age = age
            self.pin = newPin
            self.contactNo = contactNo
            self.email = email
        else:
            print( "Enter the correct pin" )

user1 = User ("Santosh" , "34" , 1234 , 12345678 , 'santosh@gmail.com')
user2 = User ("Padmini" , "76" , 4321 , 12345678 , 'santosh@gmail.com')
user3 = User ("Srinivas" , "50" , 1111 , 12345678 , 'santosh@gmail.com')

while True :

    userPin =  int ( input("Enter the Card Pin number [ Type 0 to close ]:- " ) )

    if userPin == user1.pin:
        while True:
            print()
            print("Hello" , user1.name , ". What would you like to do ?")

            selection = input('''
    Type 1 to Withdraw Cash 
    Type 2 to Deposit Cash 
    Type 3 to See your Balance
    Type 4 to Transfer Money
    Type 5 to Change User Details
    Type 6 to See User Details
    Type 7 to Cancel

    ''')
            print()

            if selection == '1':
                amount = int ( input('Enter the amount to be withdrawn :- ') )
                user1.withdrawCash(amount)
            elif selection == '2':
                amount = int ( input('Enter the amount to be deposited :- ') )
                user1.depositCash(amount)
            elif selection == '3':
                user1.showBalance()
            elif selection == '4':
                pin = int(input("Enter Pin of the person to transfer money to :- "))
                if pin == user2.pin :
                    amount = int( input ( "Enter amount to be transferred :- " ) )
                    user1.withdrawCash(amount)
                    user2.depositCash(amount)
                elif pin == user3.pin :
                    amount = int( input ( "Enter amount to be transferred :- " ) )
                    user1.withdrawCash(amount)
                    user3.depositCash(amount)
                else:
                    print( "Enter the correct pin" )
            elif selection == '5':
                name = input ( "Enter your New Name :- " )
                age = input ( "Enter your New Age :- " )
                contactNo = int ( input ( "Enter your New Contact Number :- " ) )
                email = input ( "Enter your New Email :- " )
                currentPin = int ( input ( "Enter the Current Pin :- " ) )
                newPin = int ( input( "Enter the New Pin :-" ) )

                user1.changeDetails(name,age,contactNo,email,currentPin,newPin)
            elif selection == '6':
                user1.showDetails()
            elif selection == '7':
                print("Thank you for visiting !")
                break
            else:
                print("Incorrect Number")
    elif userPin == user2.pin:
        while True:
            print()
            print("Hello" , user2.name , ". What would you like to do ?")

            selection = input('''
    Type 1 to Withdraw Cash 
    Type 2 to Deposit Cash 
    Type 3 to See your Balance
    Type 4 to Transfer Money
    Type 5 to Change User Details
    Type 6 to See User Details
    Type 7 to Cancel

    ''')
            print()

            if selection == '1':
                amount = int ( input('Enter the amount to be withdrawn :- ') )
                user2.withdrawCash(amount)
            elif selection == '2':
                amount = int ( input('Enter the amount to be deposited :- ') )
                user2.depositCash(amount)
            elif selection == '3':
                user2.showBalance()
            elif selection == '4':
                pin = int(input("Enter Pin of the person to transfer money to :- "))
                if pin == user1.pin :
                    amount = int( input ( "Enter amount to be transferred :- " ) )
                    user2.withdrawCash(amount)
                    user1.depositCash(amount)
                elif pin == user3.pin :
                    amount = int( input ( "Enter amount to be transferred :- " ) )
                    user2.withdrawCash(amount)
                    user3.depositCash(amount)
                else:
                    print( "Enter the correct pin" )
            elif selection == '5':
                name = input ( "Enter your New Name :- " )
                age = input ( "Enter your New Age :- " )
                contactNo = int ( input ( "Enter your New Contact Number :- " ) )
                email = input ( "Enter your New Email :- " )
                currentPin = int ( input ( "Enter the Current Pin :- " ) )
                newPin = int ( input( "Enter the New Pin :-" ) )

                user2.changeDetails(name,age,contactNo,email,currentPin,newPin)
            elif selection == '6':
                user2.showDetails()
            elif selection == '7':
                print("Thank you for visiting !")
                break
            else:
                print("Incorrect Number")
    elif userPin == user3.pin:
        while True:
            print()
            print("Hello" , user3.name , ". What would you like to do ?")

            selection = input('''
    Type 1 to Withdraw Cash 
    Type 2 to Deposit Cash 
    Type 3 to See your Balance
    Type 4 to Transfer Money
    Type 5 to Change User Details
    Type 6 to See User Details
    Type 7 to Cancel

    ''')
            print()

            if selection == '1':
                amount = int ( input('Enter the amount to be withdrawn :- ') )
                user3.withdrawCash(amount)
            elif selection == '2':
                amount = int ( input('Enter the amount to be deposited :- ') )
                user3.depositCash(amount)
            elif selection == '3':
                user3.showBalance()
            elif selection == '4':
                pin = int(input("Enter Pin of the person to transfer money to :- "))
                if pin == user2.pin :
                    amount = int( input ( "Enter amount to be transferred :- " ) )
                    user3.withdrawCash(amount)
                    user2.depositCash(amount)
                elif pin == user1.pin :
                    amount = int( input ( "Enter amount to be transferred :- " ) )
                    user3.withdrawCash(amount)
                    user1.depositCash(amount)
                else:
                    print( "Enter the correct pin" )
            elif selection == '5':
                name = input ( "Enter your New Name :- " )
                age = input ( "Enter your New Age :- " )
                contactNo = int ( input ( "Enter your New Contact Number :- " ) )
                email = input ( "Enter your New Email :- " )
                currentPin = int ( input ( "Enter the Current Pin :- " ) )
                newPin = int ( input( "Enter the New Pin :-" ) )

                user3.changeDetails(name,age,contactNo,email,currentPin,newPin)
            elif selection == '6':
                user3.showDetails()
            elif selection == '7':
                print("Thank you for visiting !")
                break
            else:
                print("Incorrect Number")
    elif userPin == 0 :
        break
    else:
        print("Incorrect Pin")