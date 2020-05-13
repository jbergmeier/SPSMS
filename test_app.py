import os
import unittest
import json
import random
from flask_sqlalchemy import flask_sqlalchemy
from app import create_app
from models import setup_db, App_User


class SpsmsTestCases(unittest.TestCase):
    '''This class represents the test cases for SPSMS App'''

    def setUp(self):
        '''Define test variables and initialize web app'''
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = spsms_test
        self.database_path = os.environ['']
