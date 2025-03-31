from src.math_operations import addition,subtraction

def test_add() :
    assert addition(2,3)==5
    assert addition(5,7) ==12

def test_sub() :
    assert subtraction(4,2) == 2
    assert subtraction(3,3) == 0