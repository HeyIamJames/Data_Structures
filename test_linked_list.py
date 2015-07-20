from linked_list import LinkedList
import pytest 

def test_constructor():
    items=("duck", 3, [2, 3, 4], object())
    ll=LinkedList(items)
    ll2=LinkedList()
    for i in items[::-1]:
        ll2.insert(i)
    for i in items:
        assert ll.pop() == ll2.pop()


def test_insert():
    ll = LinkedList()
    ll.insert(5)
    assert ll.pop() == 5

        
def test_pop():
    LL = LinkedList(("dog", 3, "fish taco", object(), "house"))
    assert  "dog" == LL.pop()
    
def test_size():
    LL = LinkedList(("dog", 3, "fish taco", object(), "house"))
    assert LL.size() == 5

def test_search():
    LL = LinkedList(("dog", 3, "fish taco", object(), "house"))
    print LL.first.value, LL.first.nextNode.value , LL.first.nextNode.nextNode.value 
    assert LL.search('fish taco') is LL.first.nextNode.nextNode
    assert LL.search(10) == None
    
def test_remove():
    LL = LinkedList(("dog", 3, "fish taco", object(), "house"))
    LL.remove(LL.search("fish taco"))
    assert LL.size() == 4

def test_display():
    items = ("duck", 3, [2, 3, 4], object())
    ll=LinkedList(items)
    assert repr(items) == ll.display()

