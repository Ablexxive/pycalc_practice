from main import calculate_input
# Functional Tests - AAA Model - Arrange, Act, Assert
# Fixtures - gives you explicit dependency declarations

def test_simple():
    inpt = "1+1"
    ans = calculate_input(inpt)
    assert ans == 2

    inpt = "5+1"
    ans = calculate_input(inpt)
    assert ans == 6

    inpt = "5-1"
    ans = calculate_input(inpt)
    assert ans == 4


def test_simple_2():
    inpt = "5+1+10"
    ans = calculate_input(inpt)
    assert ans == 16

    inpt = "5-9-1"
    ans = calculate_input(inpt)
    assert ans == -5

def test_mult_div():
    inpt = "5*2"
    ans = calculate_input(inpt)
    assert ans == 10

    inpt = "6/2"
    ans = calculate_input(inpt)
    assert ans == 3

def test_mult_div_2():
    inpt = "5*10*2"
    ans = calculate_input(inpt)
    assert ans == 100

def test_complex():
    inpt = "5*2-1"
    ans = calculate_input(inpt)
    assert ans == 9

    inpt = "20+20/4"
    ans = calculate_input(inpt)
    assert ans == 25

def test_long():
    inpt = "5+1*2-6/2"
    ans = calculate_input(inpt)
    assert ans == 4

    inpt = "8+100+28-198/20*2+1381"
    ans = calculate_input(inpt)
    assert ans == 1497.2
