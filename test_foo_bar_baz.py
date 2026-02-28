import pytest

from foo_bar_baz import foo_bar_baz

def test_basic_inputs():
    from foo_bar_baz import foo_bar_baz
    
    assert foo_bar_baz(0) == ''
    
    assert foo_bar_baz(1) == '1'
    
    assert foo_bar_baz(3) == '1 2 Foo'
    
    assert foo_bar_baz(5) == '1 2 Foo 4 Bar'
    
    assert foo_bar_baz(15) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz"

def test_negative_numbers():
    negatives = [-1, -10, -1000, -1000000, -10000000]
    for n in negatives:
        assert foo_bar_baz(n) == ""

def test_format_string_15():
    n = 15
    result = foo_bar_baz(n)

    assert result[0] != " "
    assert result[-1] != " "

    for i in range(len(result) - 1):
        assert not (result[i] == " " and result[i + 1] == " ")

    space_count = 0
    for ch in result:
        if ch == " ":
            space_count += 1

    assert space_count == n - 1
        
        
def test_bad_arguments():
    from foo_bar_baz import foo_bar_baz

    with pytest.raises(TypeError):
        foo_bar_baz(6.7) 

    with pytest.raises(TypeError):
        foo_bar_baz("") 
    
    with pytest.raises(TypeError):
        foo_bar_baz(bool)
        
    with pytest.raises(TypeError):
        foo_bar_baz(bytes)
        
    with pytest.raises(TypeError):
        foo_bar_baz(list)