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
        
