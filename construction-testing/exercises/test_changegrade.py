import pytest
import System
import Staff

import os
os.system("python3 RestoreData.py")

#Tests if the program can handle changing a grade
def test_changegrade(grading_system):
    username = 'akend3'
    password =  '123454321'
    course = 'comp_sci'
    assignment = 'assignment1'
    grade = '0'
    grading_system.login('goggins','augurrox')
    usr = grading_system.users['goggins'] 
    grading_system.usr.change_grade(username, course, assignment, grade)


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
