from my_code import *


def test_make_dict():
    assert {'Ten': 10, 'Twenty': 20, 'Thirty': 30} == make_dict()

def test_add_element():
    assert {'fruit': 'apple', 'veggie': 'carrot', 'grain': 'barley', 'dairy': 'yogurt'} == add_element()

def test_remove_element():
    assert {'fruit': 'apple', 'grain': 'barley'} == remove_element()

def test_merge_dict():
    assert {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50} == merge_dict()

def test_access_key():
    assert 20 == access_key()