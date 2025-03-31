from src.math_operations import add,subtraction

def test_add() :
    assert add(2,3)==5
    assert add(5,7) ==12

def test_sub() :
    assert subtraction(4,2) == 2
    assert subtraction(3,3) == 0