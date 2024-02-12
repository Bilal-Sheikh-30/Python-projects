import json
class InvalidCredentials(Exception):
    pass
class Account:
    Account_Number = 0

    # get the previous acc number from the file:
    with open("accNo.txt") as accNo:
        AccountNo = int(accNo.read())
        Account_Number = AccountNo


    def New_Account(self):
        self._Balance = input("enter initial deposit amount: ")
        self.User_Acc_Num = Account.Account_Number
        global user_acc_no
        user_acc_no = self.User_Acc_Num
        # trackList.append(self.User_Acc_Num)
        Account.Account_Number += 1

        #save this acc number in a file:
        with open("accNo.txt", "w") as accNo:
            accNo.write(str(Account.Account_Number))
        self.saveTransction(str(self.User_Acc_Num),self._Balance,"cre")
        return self.User_Acc_Num
    def saveTransction(self,accNo,amount, type, secPersonAccNum = "", status = ""):
        from datetime import datetime
        dnt = datetime.now()
        dnt = f"{dnt.day}-{dnt.month}-{dnt.year}     {dnt.hour}:{dnt.minute}:{dnt.second}     "
        if status == "":
            if type == "cre":
                record = f"{dnt}{amount} :{type}    Balance: {self._Balance}"
            elif type == "deb":
                record = f"{dnt}{amount} :{type}    Balance: {self._Balance}"
            else:
                print("cannot find transction type")
                return
        else:
            if status == "from" and type == "cre":
                record = f"{dnt}{amount} :{type}    Balance: {self._Balance}    (received from: {secPersonAccNum})"
            elif status == "to" and type == "deb":
                record = f"{dnt}{amount} :{type}    Balance: {self._Balance}    (sent to: {secPersonAccNum})"
        with open(str(accNo), "a") as transcfile:
            transcfile.write(record + "\n")
        return
    def setDetails(self,accNo,currBalance):
        self.User_Acc_Num = accNo
        self._Balance = int(currBalance)
    def Withdraw(self,accNo):
        try:
            Withdraw_amount = int(input("Enter withdraw amount: "))
            Withdraw_amount >= 0
        except:
            print("please enter a valid amount")
        else:
            if self._Balance >= Withdraw_amount:
                confirmation = input(f"Are you sure? Yow want to withdraw {Withdraw_amount} from your account? ( y/n ): ").lower()
                if confirmation == 'y':
                    self._Balance -= Withdraw_amount
                    print(f"Transction is Successful.\nYour current balance is: {self._Balance}")
                    self.saveTransction(accNo,str(Withdraw_amount),"deb")
                    return self._Balance
                else:
                    return
            else:
                print("Insufficient Balance")
                return

    def Deposit(self,accNo):
        try:
            Deposit_amount = int(input("Enter deposit amount: "))
            Deposit_amount > 0
        except:
            print("please enter a valid amount")
        else:
            confirmation = input(f"Are you sure? Yow want to deposit {Deposit_amount} in your account? ( y/n ): ").lower()
            if confirmation == 'y':
                self._Balance += Deposit_amount
                print(f"Transction is Successful.\nYour current balance is: {self._Balance}")
                self.saveTransction(accNo, str(Deposit_amount), "cre")
                return self._Balance
            else:
                return
    def moneyTransfer(self,type):
        # t = transfer, p = bills payment
        sendingAmount = int(input("\nEnter amount you want to send: "))
        if type == "t":
            receiverAccNum = input("\nEnter recipient's Account Number: ")
            if sendingAmount > self._Balance:
                print("\n==> You have insufficient balance")
                return None
            else:
                # reflecting changes in sender's file
                confirmation = input(f'\nShould we proceed with the transction? (y/n): ').lower()
                if confirmation == 'y':
                    self._Balance -= sendingAmount
                    self.saveTransction(self.User_Acc_Num,str(sendingAmount),"deb",receiverAccNum,"to")
                    # reflecting changes in receipent's file
                    recipient_file = open(f"{receiverAccNum}data").read()
                    recipient_file = json.loads(recipient_file)
                    recipient_pre_balance = recipient_file["balance"]
                    recipient_new_balance = int(recipient_pre_balance) + sendingAmount
                    recipient_file["balance"] = recipient_new_balance
                    with open(f"{receiverAccNum}data", "w") as rec:
                        rec.write(json.dumps(recipient_file))
                    self.saveTransction(receiverAccNum, str(sendingAmount), "cre",self.User_Acc_Num,"from")
                    print("\nTransction is successful !!")
                    return self._Balance
                else:
                    return

        elif type == "p":
            billAcc = {"e": 126, "g": 127}
            billChoice = input("\nEnter 'e' for Electric bill and 'g' for gas bill ==> ").lower()
            if self._Balance >= sendingAmount:
                confirmation = input(f'\nShould we proceed with the transction? (y/n): ').lower()
                if confirmation == 'y':
                    self._Balance -= sendingAmount
                    # save transction in sender's account
                    self.saveTransction(self.User_Acc_Num, str(sendingAmount), "deb",billAcc[billChoice],"to")
                    if billChoice == "e":
                        elec = billAcc["e"]
                        recipient_file = open(f"{elec}data").read()
                        recipient_file = json.loads(recipient_file)
                        recipient_pre_balance = recipient_file["balance"]
                        recipient_new_balance = int(recipient_pre_balance) + sendingAmount
                        recipient_file["balance"] = recipient_new_balance
                        with open(f"{elec}data", "w") as rec:
                            rec.write(json.dumps(recipient_file))
                        # save transction in receiver's account
                        self.saveTransction(elec, str(sendingAmount), "cre",self.User_Acc_Num,"from")
                        print("\nTransction is successful !!")
                        return self._Balance
                    elif billChoice == "g":
                        gas = billAcc["g"]
                        recipient_file = open(f"{gas}data").read()
                        recipient_file = json.loads(recipient_file)
                        recipient_pre_balance = recipient_file["balance"]
                        recipient_new_balance = int(recipient_pre_balance) + sendingAmount
                        recipient_file["balance"] = recipient_new_balance
                        with open(f"{gas}data", "w") as rec:
                            rec.write(json.dumps(recipient_file))
                        # save transction in receiver's account
                        self.saveTransction(gas, str(sendingAmount), "cre",self.User_Acc_Num,"from")
                        print("\nTransction is successful !!")
                        return self._Balance
                else:
                    return
            else:
                print("\n You have insufficient balance !!")
                return None
        else:
            print("cannot perform operation")
            return None
    def Balance_Enquiry(self):
        print(f"\nAccount Number: {self.User_Acc_Num}\nYour current balance is: {self._Balance}")

    def Show_Details(self):
        print(f"\n\nYour account balance is: {self._Balance}\nYour account number is: {self.User_Acc_Num}")
        return self._Balance

class Checking_Account(Account):

    def createAcc(self, Credit_Limit=50000, Overdraft_Fee=3000):
        self._Credit_Limit = Credit_Limit
        self._Overdraft_Fee = Overdraft_Fee
        user_acc_no = Account.New_Account(self)
        userBalance = Account.Show_Details(self)
        info = {"type": "checking", "creditLimit":self._Credit_Limit, "overdraftFee":self._Overdraft_Fee, "balance":userBalance}
        import json
        with open(f"{user_acc_no}data", "a") as data:
            data.write(json.dumps(info))

    def Set_Credit_Limit(self):
        self._Credit_Limit = int(input("\nEnter new credit limit: "))
        print(f'\nCredit limit is changed successfully.\nYour new credit limit is: {self._Credit_Limit}')

    def Set_Overdraft_Fee(self):
        self._Overdraft_Fee = int(input("\nEnter new overdraft fee: "))
        print(f'\nOverdraft Fee is changed successfully.\nYour new Overdraft Fee is: {self._Overdraft_Fee}')

    def Show_Details(self):
        print(f"\n\nYour Credit Limit is: {self._Credit_Limit}\nYour overdraft fee is:{self._Overdraft_Fee}")


class Saving_Account(Account):
    def createAcc(self, Interest_Rate=12.56):
        self._Interest_Rate = Interest_Rate
        user_acc_no = Account.New_Account(self)
        userBalance = Account.Show_Details(self)
        info = {"type": "saving", "interestRate": self._Interest_Rate, "balance": userBalance}
        import json
        with open(f"{user_acc_no}data", "a") as data:
            data.write(json.dumps(info))


    def Set_Interest_Rate(self):
        self._Interest_Rate = float(input("Enter new interest rate: "))
        print(f"\nInterest rate is changed successfully.\nYour new interest rate is: {self._Interest_Rate}")

    def Show_Details(self):
        print(f"\n\nInterest Rate is: {self._Interest_Rate}")


class Loan_Account(Account):
    def createAcc(self):
        self._Principal_Amount = int(input("\nEnter principal amount: "))
        self._Interest_Rate = 2.5
        self._Loan_Duration = 6
        user_acc_no = Account.New_Account(self)
        userBalance = Account.Show_Details(self)
        info = {"type": "loan", "principalAmount": self._Principal_Amount, "interestRate": self._Interest_Rate, "loanDuration": self._Loan_Duration, "balance": userBalance}
        import json
        with open(f"{user_acc_no}data", "a") as data:
            data.write(json.dumps(info))

    def Set_Principal_Amount(self):
        self._Principal_Amount = int(input("\nEnter principal amount: "))
        print(f"\nPrincipal amount is changed successfully.\nYour new Principal amount is: {self._Principal_Amount}")

    def Set_Interest_Rate(self):
        self._Interest_Rate = float(input("\nEnter interest rate: "))
        print(f"\nInterest rate is changed successfully.\nYour new interest rate is: {self._Interest_Rate}")

    def Set_Loan_Duration(self):
        self._Loan_Duration = float(input("\nEnter loan duration in months: "))
        print(f"\n loan duration is changed successfully.\nYour new loan duration is: {self._Loan_Duration}")

    def Show_Details(self):
        print(f"\n\nYour principal amount: {self._Principal_Amount}\nInterest Rate: {self._Interest_Rate}\nYour Loan Duration is: {self._Loan_Duration}\nYou have to pay: {self._Principal_Amount * self._Interest_Rate} within {self._Loan_Duration} months ")
class User:
    def newUser(self):
        # checking if username and nic are unique
        with open("users-record.txt", "r") as rec:
            # database is a grand list containing each user record as a separate list
            dataBase = []
            for i in rec:
                i = i.split(":")
                dataBase.append(i)
        self._Username = input("Enter your username: ")
        self._Password = input("Enter password: ")
        self._NIC = input("Enter your NIC: ")
        try:
            for eachrecord in dataBase:
                if self._Username in eachrecord:
                    print("\nusername is already registered\n")
                    raise Exception
                elif self._NIC == eachrecord[-1].strip("\n"):
                    print("\nnic is already registered\n")
                    raise Exception
        except:
            dataBase[:] = []
            return False
        else:
            self._FirstName = input("Enter your first name: ")
            self._LastName = input("Enter your last name: ")
            self._Address = input("Enter your address: ")

            UserRecord.append(self._Username)
            UserRecord.append(self._Password)
            UserRecord.append(self._FirstName)
            UserRecord.append(self._LastName)
            UserRecord.append(self._Address)
            UserRecord.append(self._NIC)
            dataBase[:] = []
        # trackList.append(self._NIC)
        # save_user_record()

    def Reset_Username(self):
        self._Username = input("Enter your new username: ")
        print(f"\nUsername has been reset.\nYour new username is: {self._Username}")
        return self._Username

    def Reset_Password(self):
        self._Password = input("Enter new password: ")
        print(f"\nPassword has been reset.\nYour new password is: {self._Password}")
        return self._Password

    def Reset_FirstName(self):
        self._FirstName = input("Enter your first name: ")
        print(f"\nFirst name has been reset.\nYour new first name is: {self._FirstName}")
        return self._FirstName
    def Reset_LastName(self):
        self._LastName = input("Enter your last name: ")
        print(f"\nLast name has been reset.\nYour new Last name is: {self._LastName}")
        return self._LastName
    def Change_Address(self):
        self._Address = input("Enter your address: ")
        print(f"\nAddress has been reset.\nYour new address is: {self._Address}")
        return self._Address
    def changeMyInfo(self,myInfo):
        # myInfo contain a list of logged-in user's details
        print(f'Username: {myInfo[0]}\nPassword: {myInfo[1]}\nFirst Name: {myInfo[2]}\nLast Name: {myInfo[3]}\nAddress: {myInfo[4]}')
        print("""\n Enter the number corresponding to the detail you want to change:
    1. Reset Username               4. Change Last Name
    2. Reset Password               5. Change Address
    3. Change First Name""")
        editInfoChoice = input("\n>>> ")
        if editInfoChoice == "1":
            newUserName = self.Reset_Username()
            myInfo[0] = newUserName
            return myInfo
        elif editInfoChoice == "2":
            newPassword = self.Reset_Password()
            myInfo[1] = newPassword
            return myInfo
        elif editInfoChoice == "3":
            newFname = self.Reset_FirstName()
            myInfo[2] = newFname
            return myInfo
        elif editInfoChoice == "4":
            newLname = self.Reset_LastName()
            myInfo[3] = newLname
            return myInfo
        elif editInfoChoice == "5":
            newAdd = self.Change_Address()
            myInfo[4] = newAdd
            return myInfo
        else:
            print("\nInvalid input !!")
            return None
# trackList = []

def Login():
    LoginUser = input("Enter username: ")
    LoginPw = input("Enter Password: ")
    with open("users-record.txt", "r") as rec:
        # database is a grand list containing each user record as a separate list
        dataBase = []
        for i in rec:
            i = i.split(":")
            dataBase.append(i)
        found = False
        # dataBaseIndex: contains the index of the list having info of logined user in the database list
        dataBaseIndex = -1
        # found user contain the recoed of the logined user
        foundUser = []
        for j in dataBase:
            if LoginUser == j[0] and LoginPw == j[1]:
                print("\n**********   SUCCESSFULLY LOGINED    **********\n")
                dataBaseIndex = dataBase.index(j)
                found = True
                foundUser = j
        try:
            if found == False and dataBaseIndex < 0:
                raise InvalidCredentials
        except InvalidCredentials:
            print("\nINCORRECT CREDENTIALS")
            tryAgain = input("Do you want to try again? (y/n): ").lower()
            if tryAgain == "y":
                Login()
            else:
                return
        else:
            print(f"Welcome: {foundUser[2].upper()} {foundUser[3].upper()}")
            print("\nYou have following accounts.")
            getAllAccInfo = open(foundUser[-1].strip("\n")).read()
            getAllAccInfo = json.loads(getAllAccInfo)
            print()
            # getAllAccInfoDict => json dict: getAllAccInfo is converted into classic dict in this variable since json dict does not have much methods
            getAllAccInfoDict = {}
            for i in getAllAccInfo:
                print(f"{i} : {getAllAccInfo[i]}")
                getAllAccInfoDict.update({i: getAllAccInfo[i]})
            loginAccNo = input("\nEnter acc number to log into: ")
            if loginAccNo in getAllAccInfoDict.keys():
                try:
                    output_file = open(f"{loginAccNo}data").read()
                except:
                    print("\ncannot find file. Please report to the bank\n")
                else:
                    output_json = json.loads(output_file)
                    print()
                    for i in output_json:
                        print(f"{i} : {output_json[i]}")
                    print()
                    def afterLoginOperations():
                        print("-"*200,'\n')
                        print("""SELECT YOUR OPERATION:
                  
    1.  SHOW BALANCE                6.  CHANGE MY DETAILS
    2.  WITHDRAW                    7.  GET YOUR ACCOUNTS' DETAILS
    3.  DEPOSIT                     8.  CREATE / CLOSE ACCOUNT
    4.  TRANSFER / PAYMENTS         9.  LOG OUT
    5.  GET ACCOUNT STATEMENT            
    """)
                        operationChoice = input(">>> ")
                        if operationChoice == "1":
                            print(f"\n-----  BALANCE INQUIRY   -----\nCurrent Balance: {output_json['balance']}\n")
                            afterLoginOperations()
                        elif operationChoice == "2":
                            print("\n-----  WITHDRAWL   -----\n")
                            operate = Account()
                            operate.setDetails(loginAccNo,output_json["balance"])
                            updatedBalance = operate.Withdraw(loginAccNo)
                            if updatedBalance == None:
                                pass
                            else:
                                output_json['balance']= updatedBalance
                            afterLoginOperations()
                        elif operationChoice == "3":
                            print("\n-----  DEPOSIT   -----\n")
                            operate = Account()
                            operate.setDetails(loginAccNo, output_json["balance"])
                            updatedBalance = operate.Deposit(loginAccNo)
                            if updatedBalance == None:
                                pass
                            else:
                                output_json['balance']= updatedBalance
                            afterLoginOperations()
                        elif operationChoice == "4":
                            print("\n-----  TRANSFER / PAYMENTS   -----\n")
                            print("press 't' for money transfer and 'p' for bill payment\n")
                            operate = Account()
                            operate.setDetails(loginAccNo, output_json["balance"])
                            t_pChoice = input("==> ").lower()
                            if t_pChoice == "t" or t_pChoice == "p":
                                updatedBalance = operate.moneyTransfer(t_pChoice)
                                if updatedBalance == None:
                                    pass
                                else:
                                    # update balance
                                    output_json['balance'] = updatedBalance
                            else:
                                print("Invalid Input")
                            afterLoginOperations()
                        elif operationChoice == "5":
                            print("\n-----  ACCOUNT STATEMENT   -----\n")
                            with open(loginAccNo) as statement:
                                for transction in statement:
                                    print(transction)
                            afterLoginOperations()
                        elif operationChoice == "6":
                            print("\n-----  CHANGE MY DETAILS   -----\n")
                            edit = User()
                            updatedRecord = edit.changeMyInfo(foundUser)
                            if updatedRecord == None:
                                pass
                            else:
                                dataBase[dataBaseIndex] = updatedRecord
                                with open("users-record.txt", "w") as file:
                                    for singleRecord in dataBase:
                                        for singleItem in singleRecord:
                                            if singleItem == singleRecord[-1]:
                                                file.write(singleItem)
                                            else:
                                                file.write(singleItem + ":")
                            afterLoginOperations()

                        elif operationChoice == "7":
                            print("\n-----  GET ACCOUNTS' DETAILS   -----\n")
                            for i in getAllAccInfo:
                                AccFile = open(f"{i}data").read()
                                AccFile = json.loads(AccFile)
                                currBalance = AccFile["balance"]
                                print(f"Account# {i} => Type: {getAllAccInfo[i]} => Current Balance : PKR {currBalance}")
                            afterLoginOperations()
                        elif operationChoice == "8":
                            print("\n-----  CREATE / CLOSE ACCOUNT   -----\n")
                            AccChoice = input("""Select your operation:
    1. Create Another Account
    2. Close this Account
>> """)
                            if AccChoice == "1":
                                def createAnotherAccount():
                                    print("""SELECT THE TYPE OF ACCOUNT:
    1. CHECKING ACCOUNT
    2. SAVING ACCOUNT
    3. LOAN ACCOUNT""")
                                    accChoice = input("ENTER: ")
                                    global user_acc_no
                                    if accChoice == "1":
                                        AnotherAcc = Checking_Account()
                                        AnotherAcc.createAcc()
                                        AnotherAcc.Show_Details()
                                        getAllAccInfoDict.update({user_acc_no: "checking"})
                                        with open(foundUser[-1].strip("\n"), "w") as accRecord:
                                            accRecord.write(json.dumps(getAllAccInfoDict))
                                        user_acc_no = 0
                                        afterLoginOperations()
                                    elif accChoice == "2":
                                        AnotherAcc = Saving_Account()
                                        AnotherAcc.createAcc()
                                        AnotherAcc.Show_Details()
                                        getAllAccInfoDict.update({user_acc_no: "saving"})
                                        with open(foundUser[-1].strip("\n"), "w") as accRecord:
                                            accRecord.write(json.dumps(getAllAccInfoDict))
                                        user_acc_no = 0
                                        afterLoginOperations()
                                    elif accChoice == "3":
                                        AnotherAcc = Loan_Account()
                                        AnotherAcc.createAcc()
                                        AnotherAcc.Show_Details()
                                        getAllAccInfoDict.update({user_acc_no: "loan"})
                                        with open(foundUser[-1].strip("\n"), "w") as accRecord:
                                            accRecord.write(json.dumps(getAllAccInfoDict))
                                        user_acc_no = 0
                                        afterLoginOperations()
                                    else:
                                        print("\n\nPLEASE ENTER THE CORRECT OPTION")
                                        createAnotherAccount()
                                createAnotherAccount()
                            elif AccChoice == "2":
                                confirm = input(f"Are you sure?\nDo you want to close Acc# {loginAccNo} (y for yes) ? >> ").lower()
                                if confirm == "y":
                                    getAllAccInfoDict.pop(loginAccNo)
                                    import os
                                    if len(getAllAccInfoDict) == 0:
                                        # remove record form main database cuz if getAllAccInfoDict is empty it means that user has no record any more
                                        nicFile = foundUser[-1].strip("\n")
                                        os.remove(nicFile)
                                        del dataBase[dataBaseIndex]
                                        with open("users-record.txt", "w") as file:
                                            for singleRecord in dataBase:
                                                for singleItem in singleRecord:
                                                    if singleItem == singleRecord[-1]:
                                                        file.write(singleItem)
                                                    else:
                                                        file.write(singleItem + ":")
                                    else:
                                        # user has other accounts
                                        # remove acc info from nic file
                                        with open(foundUser[-1].strip("\n"), "w") as accRecord:
                                            accRecord.write(json.dumps(getAllAccInfoDict))
                                    os.remove(f"{loginAccNo}data")
                                    os.remove(f"{loginAccNo}")
                                    print(f"\n***   Your Account has been closed successfully   ***\n")
                                else:
                                    print('Operation failed\n')
                                    afterLoginOperations()
                            else:
                                print("\nInvalid Input")
                                afterLoginOperations()
                        elif operationChoice == "9":
                            print("\n-----  LOGGING OUT !!!   -----\n")
                            with open(f"{loginAccNo}data", "w") as rec:
                                rec.write(json.dumps(output_json))
                            return
                        else:
                            print("\nplease select from the given operations\n")
                            afterLoginOperations()
                        return
                    afterLoginOperations()
            else:
                print("\nEnter correct Account number!!\n")




UserRecord = []
def save_user_record():
    with open("users-record.txt","a") as file:
        for i in UserRecord:
            if i == UserRecord[-1]:
                file.write(i+"\n")
            else:
                file.write(i+":")
        UserRecord[:] = []
# def save_account_details():
#  contain acc number assigned to new user
user_acc_no = 0
def SignUp():
    tempObj = User()
    tempObj= tempObj.newUser()
    if tempObj == False:
        return
    # FUNCTION FOR CHOICE OF ACCOUNT
    def AccChoice():
        print("""SELECT THE TYPE OF ACCOUNT:
        1. CHECKING ACCOUNT
        2. SAVING ACCOUNT
        3. LOAN ACCOUNT""")
        accChoice = input("ENTER: ")
        global user_acc_no
        if accChoice == "1":
            tempAcc = Checking_Account()
            tempAcc.createAcc()
            tempAcc.Show_Details()
            accDict = {user_acc_no: "checking"}
            with open(UserRecord[-1],"a") as accRecord:
                accRecord.write(json.dumps(accDict))
            save_user_record()
            accDict.clear()
            user_acc_no = 0
        elif accChoice == "2":
            tempAcc = Saving_Account()
            tempAcc.createAcc()
            tempAcc.Show_Details()
            accDict = {user_acc_no: "saving"}
            with open(UserRecord[-1],"a") as accRecord:
                accRecord.write(json.dumps(accDict))
            save_user_record()
            accDict.clear()
            user_acc_no = 0
        elif accChoice == "3":
            tempAcc = Loan_Account()
            tempAcc.createAcc()
            tempAcc.Show_Details()
            accDict = {user_acc_no: "loan"}
            with open(UserRecord[-1],"a") as accRecord:
                accRecord.write(json.dumps(accDict))
            save_user_record()
            accDict.clear()
            user_acc_no = 0
        else:
            print("\n\nPLEASE ENTER THE CORRECT OPTION")
            AccChoice()

    AccChoice()


def ForgetPassword():
    Username = input("Enter username: ")
    Nic = input("Enter nic number: ")
    with open("users-record.txt") as rec:
        foundPw = False
        for i in rec:
            i = i.split(":")
            if Username == i[0] and Nic+"\n" == i[-1]:
                print("\nYour password is:",i[1],"\n")
                foundPw = True
                break
        if foundPw == False:
            print("\n-- CANNOT FIND --\n")
def AdminLogin():
    def SearchData():
        nic = input("Enter nic: ")
        with open("users-record.txt") as rec:
            file = rec.read()
            # check if nic is present in file
            if nic in file:
                with open("users-record.txt") as rec:
                    nic = nic + "\n"
                    # search nic in every record
                    for i in rec:
                        i = i.split(":")
                        if nic in i:
                            print(f"\nName: {i[2].capitalize()} {i[3].capitalize()}\n\nAddress: {i[-2]}\n")
            else:
                print("Nic not found in data")
    def GetTransction():
        accNo = input("Enter acc no: ")
        try:
            with open(str(accNo),"r") as fil:
                for i in fil:
                    print(i)
        except:
            print("Account does not exist")
    def getInfoFromNic():
        userNic = input("Enter nic: ")
        with open(userNic) as nicfile:
            for i in nicfile:
                print(i)
    def adminOperations():
        print("""\n\nEnter the corresponding number:
        1. Search client's Data
        2. Get transction History of an Account
        3. Check accounts created on a single nic""")
        choice = input("Enter: ")
        if choice == "1":
            SearchData()
            choice = input("Do you want to continue? (y/n): ").lower()
            if choice == "y":
                adminOperations()
            else:
                return
        elif choice == "2":
            GetTransction()
            choice = input("Do you want to continue? (y/n): ").lower()
            if choice == "y":
                adminOperations()
            else:
                return
        elif choice == "3":
            getInfoFromNic()
            choice = input("Do you want to continue? (y/n): ").lower()
            if choice == "y":
                adminOperations()
            else:
                return
        else:
            print("\nSelect the appropriate option")
            adminOperations()
    AdminnUser = input("Enter username: ")
    AdminnPw = input("Enter Password: ")
    with open("admin id & pw.txt") as rec:
        for i in rec:
            i = i.split(":")
            if AdminnUser == i[0] and AdminnPw == i[1]:
                print("\n","*"*10,"LOGINED","*"*10,"\n")
                adminOperations()
            else:
                print("incorrect\n")
                runAgain = input("Enter 'a' to try again: ").lower()
                if runAgain == 'a':
                    AdminLogin()
                else:
                    break


def MainProgram():
    print("""ENTER CORRESPONDING NUMBER:
    1. LOGIN
    2. SIGN UP
    3. FORGET PASSWORD
    4. LOGIN AS ADMIN
    OR ENTER 'e' TO EXIT THE PROGRAM """)
    mainProgChoice = input("ENTER: ").lower()
    if mainProgChoice == "1":
        Login()
        MainProgram()
    elif mainProgChoice == "2":
        SignUp()
        MainProgram()
    elif mainProgChoice == "3":
        ForgetPassword()
        MainProgram()
    elif mainProgChoice == "4":
        AdminLogin()
        MainProgram()
    elif mainProgChoice == "e":
        pass
    else:
        print("\nPlease Enter correct number!!!")
        MainProgram()


MainProgram()

