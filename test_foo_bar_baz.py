import pytest

from foo_bar_baz import foo_bar_baz

#Add testcases Here

def test_basic_inputs():
    from foo_bar_baz import foo_bar_baz
    
    assert foo_bar_baz(0) == ''
    
    assert foo_bar_baz(1) == '1'
    
    assert foo_bar_baz(3) == '1 2 Foo'
    
    assert foo_bar_baz(5) == '1 2 Foo 4 Bar'
    
    assert foo_bar_baz(15) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz"

def test_less_basic():
    pass

def test_negative_numbers():
    negatives = [-1, -10, -1000, -1000000, -10000000]
    for n in negatives:
        assert foo_bar_baz(n) == ""
        
