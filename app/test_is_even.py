def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(4) == True
    assert is_even(5) == False

def is_even(n):
    return n % 2 == 0
