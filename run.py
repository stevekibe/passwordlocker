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
        return Credential.display_accounts()

    def generate_password():
        '''
        method to generate passwords
        '''
        
