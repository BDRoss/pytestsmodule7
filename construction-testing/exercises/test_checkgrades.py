import pytest
import System
import Staff
#import RestoreData

import os
os.system("python3 RestoreData.py")

#Tests if the program can handle a student submitting an assignment
def test_checkgrades(grading_system):
    name = 'akend3'
    password = '123454321'
    course = 'databases'
    assignment = 'assignment1'
    submission = 'TestData'
    #Not the appropriate date time format, but it should clearly be populated from this test
    submissiondate = "now"
    grading_system.login(name, password)
    grading_system.usr.check_grades(course)


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
