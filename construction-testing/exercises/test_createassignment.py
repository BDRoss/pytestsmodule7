import pytest
import System
import Staff

import os
os.system("python3 RestoreData.py")

#Tests if the program can handle creating an assignment w/out permission
def test_createasi(grading_system):
    assignment = 'test_assignment'
    due = '01/01/1970'
    course = 'software_engineering'
    grading_system.login('akend3','123454321')
    usr = grading_system.users['goggins'] 
    grading_system.usr.create_assignment(assignment, due, course)


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
