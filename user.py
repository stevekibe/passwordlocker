import random
import string

class Userinfo:
    '''
    class that shows the user info
    '''

    user_list = [] #an empty user list
    def __init__(self,user_name,password,email):

        self.user_name = user_name
        self.password = password
        self.email = email

    def save_userinfo(self):
        '''
        method that saves the users info
        '''
        Userinfo.user_list.append(self) 

    @classmethod
    def display_users(cls):
        return cls.user_list


class Credentials:
    '''
    class that generates new instances for the  credentials object
    '''
    credential_list = []#empty object
    def __init__(self,account_name, account_username, account_password):
        self.account_name = account_name
        self.account_username = account_username
        self.account_password = account_password
    
    @classmethod
    def check_user_exist(cls,user_name,password):
        '''
        method that checks if a user is logged in
        '''
        for user in Userinfo.user_list:
            if user.user_name == user_name and password == password:
                return True
            return False


    def save_accont(self):
        '''
        method that save the account credential
        '''
        Credentials.credential_list.append(self)

    def delete_account(self):
        '''
        method to delete the accounut created
        '''
        Credentials.credential_list.remove(self)

    @classmethod
    def display_account(cls):
        '''
        method that returns the credetial list
        '''
        return cls.credential_list

    def generate_password(self):
        '''
        method that generates the passwords for the user
        '''
        char = string.ascii_uppercase + string.ascii_lowercase + string.digits + "@#$%^&*"

        gen_pass = "".join(random.choice(char) for _ in range(8))




        

        
          