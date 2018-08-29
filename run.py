#!/usr/bin/env python3.6
from user import Userinfo,Credentials

def function():
    print(" __      __   ___  ")
print("|  |    |  | |   | ")
print("|  |    |  | |   | ")
print("|  |    |  | |   | ")
print("|  |    |  | |   | ")
print("|  |____|  | |   | ")
print("|          | |   | ") 
print("|   ____   | |   | ")
print("|  |    |  | |   | ")
print("|  |    |  | |   | ")
print("|  |    |  | |   | ")
print("|__|    |__| |___| ")
print("            ")

function()

def create_user(user_name, Password, email):
    '''
    function to create new user
    '''

    new_user = Userinfo(user_name,password,email)
    return new_user

def save_user(user):
    '''
    method to save the user
    '''
    user.save_user()

def display_users():
        '''
        method to save the user
        '''

        return Userinfo.display_users()

def login_user(user_name,password):
        '''
        method that checks if the user exixts
        '''

        check_user_exist = Credentials.check_user_exist(user_name,password)
        return check_user_exist

def create_credential(account_name, account_username, account_password):
        '''
        method to creste new credential
        '''

        new_credential = Credentials(account_name,account_username,account_password)
        return new_credential

def save_credential(credential):
        '''
        method to save new credential
        '''
        credential.save_credential()

def delete_account(credential):
        '''
        method to delete a credential
        '''

        credential.delete_account()

def display_accounts():
        '''
        method to display the credentials
        '''
        return Credentials.display_account()

def generate_password():
        '''
        method to generate passwords
        '''

        password_gen = Credentials.generate_password()

        return password_gen

        #end of the methods
    
    #layout 

def main():
        print("Welcome to password locker....Feel safe to use our services")
        print("\n")
        while True:
                print('*'*150)
                short_code = input("Use the following short codes: CU- create a new user account,  LN - to log in if you have an account ,  EX - exit from password locker \n ").lower().strip()
                print ('+'*60)
        
                if short_code == "EX":
                        print("Thank you for using password locker will see you again ")
                        break
        
                elif short_code == "CA":
                        print("Sign up")
                        print('-'*30)
                        user_name = input("Username: ")
                        password = input("Password: ")
                        email = input("Email: ")

                        save_user(create_user(user_name,password,email))
                        print('\n')
                        print(f"{user_name} Your account has been created successfully")

                elif code == "LN":
                        print("Enter your User name and your password to log in:")  
                        print('*'*30)
                        user_name = input("Username : ")
                        password = input("Password: ")
                        sign_in = login_user(user_name,password)
                        if sign_in == True:
                                print(f"{user_name} You are now logged in")
                                while True:
                                        print("Use the follwing to navigate through: CA-to create new account DL- to see the list of your accounts EX - toexit current account")
                                        if code == "CA":
                                                print("Create new account")
                                                print('='*40)
                                                account_name = input("Account name \ Site name: ")
                                                account_username = input("Site user name: ")
                                                print('.'*60)
                                                password_option = input("You can choose between: EP- to input existing password GP- to generate new password")
                                                print('*'*80)
                                                while True:
                                                        if password_option == "EP":
                                                                account_password = input("Enter your password: ")
                                                                break
                                                        elif password_option == "GP":
                                                                account_password = generate_password()
                                                                break
                                                        else:
                                                                print("Invalid Entry!")
                                                                break
                                                        save_profileinfo(create_profileinfo(account_name,account_username, account_password))
                                                        print('+'*40)
                                                        print(f"New account created: \n Account:{account_name}\n User Name:{account_username}\n Password:{account_password}")
                                                        print('*' * 40)

                                                if short_code == "da":
                                                        if display_accounts():
                                                        print("Here's your list of accounts(s): ")

                                                        print('#'* 30)
                                                        for account in display_accounts():
                                                                print(f"Site:{account.account_name} \n User Name:{account_username} \n Password:{account_password}")
                                                                print('*'*30)
                                                        else:
                                                        print("Sorry ... you do not have an account yet")

                                        


                        

                        






if __name__ == '__main__':
    main()
