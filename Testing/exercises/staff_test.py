import pytest
import System

def test_change_grade(grading_system):
    #check Proffessor
    grading_system.login('goggins', 'augurrox')
    grading_system.usr.change_grade('akend3',"databases",'assignment1',23)
    assert(grading_system.users['akend3']['courses']['databases']['assignment1']['grade'] == 23)

def test_create_assignment(grading_system):
    grading_system.login('goggins', 'augurrox')
    grading_system.usr.create_assignment("test_assignment","Jan 1 2022", "databases")
    #makes sure it is made
    assert("test_assignment" in grading_system.usr.all_courses['databases']['assignments'])
    #this checks both the course and date
    assert(grading_system.usr.all_courses['databases']['assignments']["test_assignment"]["due_date"] == "Jan 1 2022")

def test_change_grade_extra_bounds(grading_system):
    #I want the bounds of the change grade able to add extra points but not be able to go negative
    #check Proffessor
    grading_system.login('goggins', 'augurrox')
    grading_system.usr.change_grade('akend3',"databases",'assignment1',-10)
    assert(grading_system.users['akend3']['courses']['databases']['assignment1']['grade'] == 0)
    #extra credit is possible
    grading_system.usr.change_grade('akend3',"databases",'assignment1',110)
    assert(grading_system.users['akend3']['courses']['databases']['assignment1']['grade'] == 110)

def test_create_assignment_wrong_class(grading_system):
    grading_system.login('goggins', 'augurrox')
    grading_system.usr.create_assignment("test_assignment","Jan 1 2022", "comp_sci")
    #makes sure it is made
    assert("test_assignment" not in grading_system.usr.all_courses["comp_sci"]['assignments'])

def test_check_grades_correct_class(grading_system):
    grading_system.login('goggins', 'augurrox')
    assert([] == grading_system.usr.check_grades("akend3","comp_sci"))

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem