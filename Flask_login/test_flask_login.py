import unittest
from flask_login import *

class TestFlask(unittest.TestCase):
    render_templates = False

    def setUp(self):
        app.config['SECRET_KEY']= "philip"
        self.flask_login = app.test_client()

    def test_index(self):
        self.assertEqual(request.form['password'] ,'password')

    def post(self):
    	pass

    def comment(self):
    	pass

    def login(self):
    	pass

    def logout(self):
    	pass

if __name__ == '__main__':
 unittest.main()
