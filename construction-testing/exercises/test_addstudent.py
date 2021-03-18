import pytest
import System
import Staff

import os
os.system("python3 RestoreData.py")

#Tests if the program can handle adding a student with wrong authentication
def test_add(grading_system):
    name = 'janedoe'
    course = 'underwater_basketweaving'
    grading_system.login('akend3','123454321')
    usr = grading_system.users['goggins'] 
    grading_system.usr.add_student(name, course)


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
