import pytest
import System

import os
os.system("python RestoreData.py")

#Tests if the program can handle a wrong username
def test_login(grading_system):
    username = 'yted92'
    password =  'imoutofpasswordnames'
    grading_system.login(username,password)
    usr = grading_system.users['yted91'] 
    


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
