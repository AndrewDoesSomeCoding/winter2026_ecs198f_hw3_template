import pytest

from foo_bar_baz import foo_bar_baz

#Add testcases Here

def test_basic_inputs():
    from foo_bar_baz import foo_bar_baz
    
    assert foo_bar_baz(0) == ''
    
    assert foo_bar_baz(1) == '1'
    
    assert foo_bar_baz(3) == '1 2 Foo'
    
    assert foo_bar_baz(5) == '1 2 Foo 4 Bar'

def test_less_basic():
    pass
    

