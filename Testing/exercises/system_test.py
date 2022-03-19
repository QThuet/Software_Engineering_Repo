import pytest
import System

def test_login(grading_system):
    #Test that student works
    grading_system.login('hdjsr7', 'pass1234')
    name = grading_system.usr.name
    assert(grading_system.usr.users[name]['role'] == 'student')
    #Test TA works
    grading_system.login('cmhbf5', 'bestTA')
    name = grading_system.usr.name
    assert(grading_system.usr.users[name]['role'] == 'ta')
    #Test Teacher works
    grading_system.login('goggins', 'augurrox')
    name = grading_system.usr.name
    assert(grading_system.usr.users[name]['role'] == 'professor')

def test_Password(grading_system):
    #Test that student works
    grading_system.login('hdjsr7', 'pass1234')
    name = grading_system.usr.name
    assert(grading_system.check_password(name, 'pass1234'))
    #Test TA works
    grading_system.login('cmhbf5', 'bestTA')
    name = grading_system.usr.name
    assert(grading_system.check_password(name, 'bestTA'))
    #Test Teacher works
    grading_system.login('goggins', 'augurrox')
    name = grading_system.usr.name
    assert(grading_system.check_password(name, 'augurrox'))
    assert not any([grading_system.check_password(name, 'WrongPassword'),grading_system.check_password(name, '129846129'),grading_system.check_password(name, '')])

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem