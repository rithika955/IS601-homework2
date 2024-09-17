'''My Calculator Test'''
from calculator import add,subtract

def test_addition():
    '''Addition function'''
    assert add(2,2) == 4
def test_sutraction():
    '''Subtraction Function'''
    assert subtract(2,2) == 0
