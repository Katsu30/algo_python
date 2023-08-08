def get_fizzbuzz(number):
    is_fizz = number % 3 == 0
    is_bazz = number % 5 == 0
    if is_fizz and is_bazz:
        return 'FizzBazz'
    elif is_fizz: return 'Fizz'
    elif is_bazz: return 'Bazz'
    return number

def test_fizzbuzz():
    assert get_fizzbuzz(3) == 'Fizz'
    assert get_fizzbuzz(5) == 'Bazz'
    assert get_fizzbuzz(15) == 'FizzBazz'
    assert get_fizzbuzz(2) == 2