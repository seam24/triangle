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
    
def test_right_triangle1():
    assert triangle(3, 4, 5) == 3 # 3**2 + 4**2 = 5**2

def test_right_triangle2():
    assert triangle(5, 12, 13) == 3 # 5**2 + 12**2 = 13**2
