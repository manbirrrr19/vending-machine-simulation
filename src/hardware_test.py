import main 
import pytest


def test_check_password():
    result = main.check_password()
    ans = "1234"
    assert(result == ans)

def test_check_choice():
    result = main.check_choice()
    assert(0<result<7)

def test_restockp1():
    result = main.restocking_p1()
    assert(0<result<7)