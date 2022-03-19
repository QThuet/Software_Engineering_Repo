import pytest
import System

def test_add_student(grading_system):
    grading_system.login('goggins', 'augurrox')
    grading_system.usr.add_student('Test_User', 'databases')
    assert(grading_system.users['yted91']['courses']['databases'] != None)

def test_drop_student(grading_system):
    grading_system.login('calyam','#yeet')
    grading_system.usr.drop_student("yted91","cloud_computing")
    assert("cloud_computing" not in grading_system.users["yted91"]['courses'])

def test_drop_student_wrong_teacher(grading_system):
    grading_system.login('goggins','augurrox')
    grading_system.usr.drop_student("hdjsr7","cloud_computing")
    assert("cloud_computing" in grading_system.users["hdjsr7"]['courses'])

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem