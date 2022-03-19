import pytest
import System

def test_submit_assignment(grading_system):
    #this test looks like it should work but because onTime does not work this would fail
    grading_system.login('akend3', '123454321')

    grading_system.usr.submit_assignment('databases',"assignment1","test_assignment","1/1/2000")
    assert(grading_system.users['akend3']['courses']['databases']['assignment1']["submission"] == "test_assignment")
    assert(grading_system.users['akend3']['courses']['databases']['assignment1']["ontime"] == True)

    grading_system.usr.submit_assignment('databases',"assignment1","test_assignment","12/31/9999")
    assert(grading_system.users['akend3']['courses']['databases']['assignment1']["submission"] == "test_assignment")
    assert(grading_system.users['akend3']['courses']['databases']['assignment1']["ontime"] == False)

def test_check_grades(grading_system):
    #I tried doing this otherways such as using slices and other things this seems to be the only way that makes sense tho :/
    grading_system.login('akend3', '123454321')
    assert(["assignment2", 46] in grading_system.usr.check_grades('databases'))

def test_check_ontime(grading_system):
    grading_system.login('akend3', '123454321')
    assert(grading_system.usr.check_ontime("1/1/2000","12/31/9999"))
    assert not(grading_system.usr.check_ontime("12/31/9999","1/1/2000"))

def test_view_assignments(grading_system):
    grading_system.login('akend3', '123454321')
    assert(["assignment1","1/6/20"] in grading_system.usr.view_assignments('databases'))

def test_view_assignments_incorrect_class(grading_system):
    grading_system.login('akend3', '123454321')
    assert([] == grading_system.usr.view_assignments("software_engineering"))



@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem