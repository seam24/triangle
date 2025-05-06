from triangle import triangle

def test_invalid1():
    assert triangle(-1, 0, 1) == -1

def test_isosceles():
    assert triangle(3, 2, 3) == 1

def test_equilateral():
    assert triangle(3, 3, 3) == 2  
    
def test_invalid2():
    assert triangle(1, 2, 3) == -1  # a + b <= c

def test_invalid3():
    assert triangle(10, 1, 1) == -1  # a + b < c