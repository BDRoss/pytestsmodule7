import pytest
import System
import Staff

import os
os.system("python3 RestoreData.py")

#Tests if the program can handle dropping a student
def test_dropstu(grading_system):
    name = 'akend3'
    course = 'databases'
    grading_system.login('goggins','augurrox')
    usr = grading_system.users['goggins'] 
    grading_system.usr.drop_student(name, course)


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
