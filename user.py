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
        