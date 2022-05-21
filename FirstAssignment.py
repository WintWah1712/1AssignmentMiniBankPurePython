#for first assingment
import random
import sys
class MiniBank:
    main_userInfo:dict = {}

    def firstOption(self):
            option: int = int(input('\nPress 1 to Login/ Press 2 to Register : '))
            if(option == 1):
                self.login()
            else:
                self.register()
               
        
    def checkString(self,username):
        flag = False
        for i in username:
            if i >= chr(61) and i <= chr(122) or i>=chr(64) and i<=chr(90):
                flag = True
            else:
                flag = False
                break
        if flag == False:
            print('Your input is invalid!')
        return flag

    def checkDigit(self,passcode):
        flag = False
        for i in passcode:
            if i >= chr(48) and i<= chr(57):
                flag = True
            else:
                flag = False
                break
        if flag == False:
            print('Your input is invalid!')
        return flag

    def returnId(self, transfer_username):
        userInfo_length : int = len(self.main_userInfo)
        for i in range(1, userInfo_length+1):
            if self.main_userInfo[i]["r_username"] == transfer_username:
                return i
        return None

    def detailAccount(self,login_id):
        print("\n----------ACCOUNT DETAIL----------")
        print("Account Holder: ",self.main_userInfo[login_id]["r_username"].upper())
        print("Account Password: ",self.main_userInfo[login_id]["r_passcode"])
        print("Available balance: $",self.main_userInfo[login_id]["amount"])
    
    def depositMoney(self, login_id, deposit_amount):
        my_balance :int = self.main_userInfo[login_id]['amount']
        self.main_userInfo[login_id]['amount'] = my_balance + deposit_amount
        print('Current account balance: $',self.main_userInfo[login_id]['amount'])
        print(self.main_userInfo[login_id])

    
    def transferMoney(self,login_id, transfer_id, transfer_amount):
        my_balance :int = self.main_userInfo[login_id]['amount']
        receiver_balance :int = self.main_userInfo[transfer_id]['amount'] 
        if(my_balance >= transfer_amount):
            self.main_userInfo[login_id]['amount'] = my_balance - transfer_amount
            self.main_userInfo[transfer_id]['amount'] = receiver_balance + transfer_amount
            print(self.main_userInfo[login_id])
            print(self.main_userInfo[transfer_id])
        else:
             print("Insufficient fund!")
             print("Your balance is ${0} only.".format(self.main_userInfo[login_id]['amount']))
             print("Try with lesser amount than balance.")

    def withdrawMoney(self,login_id, withdraw_amount):
        my_balance :int = self.main_userInfo[login_id]['amount']
        if my_balance >= withdraw_amount:
            self.main_userInfo[login_id]['amount'] = my_balance-withdraw_amount
            print('${0} withdraw successful!'.format(withdraw_amount))
            print('Current account balance: $',self.main_userInfo[login_id]['amount'])
        else:
            print("Insufficient fund!")
            print("Your balance is ${0} only.".format(self.main_userInfo[login_id]['amount']))
            print("Try with lesser amount than balance.")
            print()

    def updateName (self,login_id, newName):
         self.main_userInfo[login_id].update({"r_username" : newName})
         print(self.main_userInfo[login_id])
             

    def updatePw (self, login_id, newPw):
         self.main_userInfo[login_id].update({"r_passcode" : newPw})
         print(self.main_userInfo[login_id])
             
    def updateAmount(self,login_id,newAmount):
        self.main_userInfo[login_id].update({"amount" : newAmount})
        print(self.main_userInfo[login_id])
    
    def menu(self,login_id):
                print("""
                        TRANSACTION 
                    *******************
                        Menu:
                        1. Account Detail
                        2. Deposit
                        3. Transfer
                        4. Withdraw
                        5. Update
                        6. Exit
                    *******************
                    """)
                while True:
                        menu_input  = input('\nEnter 1,2,3,4,5 or 6 : ')
                        flag :bool = self.checkDigit(menu_input)
                        if flag:
                                if int(menu_input) == 1:
                                    self.detailAccount(login_id)
                                elif int(menu_input) == 2:
                                    print("\n----------Deposit Money----------")
                                    deposit_amount: int = int(input('How much you want to deposit : $'))
                                    self.depositMoney(login_id, deposit_amount)
                                elif int(menu_input) == 3:
                                    print("\n----------Transfer Money----------")
                                    transfer_username: str = input('Pls enter username to transfer : ')
                                    transfer_id: int = self.returnId(transfer_username)
                                    transfer_amount: int = int(input('How much you want to transfer : $'))
                                    print("\n We get to transfer ID : ", transfer_id)
                                    print("\n My ID : ", login_id)
                                    self.transferMoney(login_id, transfer_id, transfer_amount)
                                elif int(menu_input) == 4:
                                    print("\n----------Withdraw Money----------")
                                    withdraw_amount: int = int(input("How much you want to withdraw : $"))
                                    self.withdrawMoney(login_id, withdraw_amount)
                                elif int(menu_input) == 5:
                                    print("""
                        Update Account
                    *****************
                         Menu:
                         1. Change name
                         2. Change password
                         3. Change amount
                    *****************
                                        """
                                          )
                                    while True:
                                        menu = int(input('Enter 1,2 or 3 : '))
                                        if (menu == 1):
                                            newName = input('Enter you want to change name : ')
                                            self.updateName(login_id, newName)
                                        elif (menu == 2):
                                            newPw = int(input('Enter you want to change password : '))
                                            self.updatePw(login_id, newPw)
                                        elif (menu == 3):
                                            newAmount = int(input('Enter you want to change amount : $'))
                                            self.updateAmount(login_id, newAmount)
                                        else:
                                            break
                                elif int(menu_input) == 6:
                                    # formatted string literals
                                    print(f"""     
                         printing receipt..............
                    ****************************************
                          Transaction is now complete.                         
                          Transaction number: {random.randint(10000, 1000000)} 
                          Account holder: {self.main_userInfo[login_id]['r_username'].upper()}                  
                          Account password: {self.main_userInfo[login_id]['r_passcode']}                
                          Available balance: ${self.main_userInfo[login_id]['amount']}                    

                          Thanks for choosing us as your bank                  
                    ****************************************
                                """)
                                    sys.exit()
                                else:
                                    print("Error: Enter 1, 2, 3, 4,5 or 6 only!\n")




    def login(self):
        print('\n-----------This is Login Form---------\n')
        while True:
            l_username = input('Pls enter user name to login : ')
            flagName = self.checkString(l_username)
            if flagName:
                while True:  
                    l_passcode = input('Pls enter user passcode to login : ')
                    flagPw = self.checkDigit(l_passcode)
                    if flagPw:
                        exitUser : bool = self.exitUser(l_username, l_passcode)
                        print(exitUser)
                        if(exitUser):
                            print('Login Successful...\n')
                            login_id:int = self.returnId(l_username)
                            self.menu(login_id)
                        else:
                            print('You cannot login!')
                        break

                    else:
                        continue
                    break
                break
            else:
                continue
            break

    def exitUser(self,l_username,l_passcode):
        user_count = len(self.main_userInfo)
        for i in range(1,user_count+1):
            if self.main_userInfo[i]["r_username"] == l_username and self.main_userInfo[i]["r_passcode"]== l_passcode:
                return True
        return False

    def register(self):
        print('\n-----------This is Register Form---------\n')
        while True:
            r_username = input('Pls enter user name to register : ')
            flagName = self.checkString(r_username)
            if flagName:
                while True:
                    r_passcode1 = input('Pls enter user passcode to register : ')
                    flagPw = self.checkDigit(r_passcode1)
                    if flagPw:
                        r_passcode2 = input('Pls enter again passcode to comfirm : ')
                        if(r_passcode1 == r_passcode2):
                            exit_register : bool = self.exitUser(r_username,r_passcode1)
                            if not exit_register:
                                id: int = self.checkingUserCount()
                                userInfoForm :dict = {id:{"r_username":r_username, "r_passcode":r_passcode1, "amount":0}}
                                self.main_userInfo.update(userInfoForm)
                                print("########### Success Registered! ##########\n\n")
                                print(self.main_userInfo)
                            else:
                                print('Data is already exit!')
                        break
                    else:
                        continue
                    break
                break
            else:
                continue
            break

    def checkingUserCount(self):
        count = len(self.main_userInfo)
        return count+1

     

print("\n*******WELCOME TO BANK OF MYBANK*******")
print("___________________________________________________________\n")
print("----------ACCOUNT CREATION----------")
if __name__ == "__main__":
    miniBank : MiniBank = MiniBank()
    while True:
        miniBank.firstOption()
     