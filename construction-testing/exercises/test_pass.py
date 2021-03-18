import pytest
import System

import os
os.system("python RestoreData.py")

#Tests if the program can handle incorrectly formatted passwords
def test_pass(grading_system):
    username = 'goggins'
    password = None
    grading_system.check_password(username, password)
    username = 'yted91'
    password =  'imoutofpasswordnames'
    grading_system.check_password(username, password)
    grading_system.login(username,password)
    username = 'akend3'
    password = -654
    grading_system.login(username,password)
    usr = grading_system.users['akend3']
    username = 'hdjsr7'
    password = '222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222'
    usr = grading_system.users['hdjsr7'] 
    username = 'goggins'
    password = 'aaaaaaaaaaaaaaaaaaaa\xef\xbe\xad\xde'
    grading_system.login(username,password)
    usr = grading_system.users['goggins']
    grading_system.check_password(username,password)



@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
