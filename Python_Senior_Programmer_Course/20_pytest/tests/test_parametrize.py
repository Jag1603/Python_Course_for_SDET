import pytest
@pytest.mark.parametrize("a,b,result", [(1,2,3),(2,3,5),(5,5,10)])
def test_add(a,b,result):
    assert a+b == result