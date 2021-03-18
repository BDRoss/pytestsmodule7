import pytest
import System
import Staff

import os


#Tests if the program can handle a non-existant student submitting an assignment
def test_submit(grading_system):
    name = 'janedoe'
    password = '123454321'
    course = 'databases'
    assignment = 'assignment1'
    submission = 'TestData'
    #Running RestoreData before every test to make sure the integrity of sample data is 
    #consistent between tests.  However, this DOES make it more difficult to verify data is 
    #being changed between tests while using pytest without arguments
    os.system("python3 RestoreData.py")
    #Not the appropriate date time format, but it should clearly be populated from this test
    submissiondate = "now"
    grading_system.login(name, password)
    grading_system.usr.submit_assignment(course, assignment,submission, submissiondate)


@pytest.fixture
def grading_system():
    os.system("python3 RestoreData.py")
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
