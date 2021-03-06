#!/usr/bin/env python3.6
from user import Userinfo,Credentials

def function():

        print("HI THERE")
    

function()

def create_user(user_name, password, email):
    '''
    method to create new user
    '''

    new_user = Userinfo(user_name,password,email)
    return new_user

def save_userinfo(user):
    '''
    method to save the user
    '''
    user.save_userinfo()

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

def create_credentials(account_name, account_username, account_password):
        '''
        method to creste new credential
        '''

        new_credential = Credentials(account_name,account_username,account_password)
        return new_credential

def save_credentials(credentials):
        '''
        method to save new credential
        '''
        credentials.save_credentials()

def delete_account(credentials):
        '''
        method to delete a credential
        '''

        credentials.delete_account()

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
                print('*'*50)
                print("Use the short code to navigate the app: CN - To create a new user account, LN - to log in an account, EX - exit from password ")
                short_code = input().lower()
                print ('+'*60)
        
                if short_code == "ex":
                        print("Thank you for using password locker will see you again ")
                        break
        
                if short_code == "cn":
                        print("Sign up")
                        print('-'*30)
                        user_name = input("Username: ")
                        password = input("Password: ")
                        email = input("Email: ")

                        save_userinfo(create_user(user_name,password,email))
                        print('\n')

                        
                        print('\n')
                        print('-'*50)

               
                if short_code == "ln":
                        print("Enter your User name and your password to log in:")  
                        print('*'*30)
                        user_name = input("Username : ")
                        password = input("Password: ")
                        sign_in = login_user(user_name,password)
                        
                        print(f"{user_name} You are now logged in")
                        while True:

                                print("Use the following to navigate through: CA- to create new account DL-to see the list of your accounts  EX- to exit current account \n")
                                short_code = input().lower()
                                if short_code == "ca":
                                        print("Create new account")
                                        print('='*40)
                                        account_name = input(" Site name:")
                                        account_username = input("Site user name:")
                                        print('.'*60)
                                        while True:
                                                password_option = input("You can choose between: EP - To input existing password GP - To generate your new password \n").lower()
                                                print('\n')
                                                print('*'*80)
                                        
                                                if password_option == "ep":
                                                        account_password = input("Enter your password: ")
                                                        break
                                                elif password_option == "gp":
                                                        account_password = generate_password()
                                                        break
                                                else:
                                                        print("Invalid Entry!")
                                                        break
                                                save_credentials(create_credentials(account_name,account_username,account_password))
                                print('+'*40)
                                print(f"New account created: \n Account:{account_name} \n User Name:{account_username}\n Password:{account_password}")
                                print('#' * 40)

                        if short_code == "dl":
                                if display_accounts():
                                        print("Here's your list of account(s)")

                                        print('#'*30)
                                        for account in display_accounts():
                                                print(f"Site:{account.account_name} \n Use Name:{account_username} \n Password:{account_password}")
                                                print('*'*30)
                        else:
                                print("Sorry....you do not have an account yet")

                        if short_code == "ex":
                                print("it was nice having you")
                                break
                
                                                                       
                else:
                        print("You do not have an account yet use the short codes to craete an account")

                                        

if __name__ == '__main__':
        main()
