import os
import unittest
import sys

# Append the above path to allow us to relative import the below
sys.path.append('..')

from app import app

class BasicTests(unittest.TestCase):
    # executed prior to each test
    def setUp(self):
        self.app = app.test_client()
        self.assertEqual(app.debug, False)

    # executed after each test
    def tearDown(self):
        pass

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_signup_page(self):
        response = self.app.get('/showSignUp', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_signin_page(self):
        response = self.app.get('/showSignIn', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()