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
    class that generates new instances for the class credentials
    '''
    credential_list = []#empty object
    def __init__(self,user_name,password,email):
        self.user_name = user_name
        self.password = password
        self.email = email
        

        
          