import unittest
from user import Userinfo

class TestUserinfo(unittest.TestCase):
    '''
    test class to define the test
    '''

    def setUp(self):
        '''
        test to se if the account can setup
        '''

        self.new_userinfo = Userinfo("stevekibe","meee","tatata")

    def test_init(self):
        '''
        initializing the test
        '''

        self.assertEqual(self.new_userinfo.user_name,"stevekibe")
        self.assertEqual(self.new_userinfo.password,"meee")
        self.assertEqual(self.new_userinfo.email,"tatata")
    

if __name__ == '__main__':
    unittest.main()