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
                





if __name__ == '__main__':
    main()
