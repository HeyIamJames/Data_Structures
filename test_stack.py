import pytest
from linked_list import LinkedList
from stack import Stack

def test_stack():
    a=Stack()
    a.push('x')
    a.push('z')
    assert a._list.size()== 2
    assert a._list.display() == repr(('z', 'x'))

def test_push():
    s=Stack()
    s.push('x')
    assert s._list.size() == 1

def test_pop():
    s=Stack((1, ))
    assert s.pop() == 1
    assert s._list.size() == 0
    with pytest.raises(AttributeError): s.pop()
