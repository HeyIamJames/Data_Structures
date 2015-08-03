import pytest
from hashtable import HashTable


@pytest.fixture
def words_hashtable():
    ht = HashTable(1000)

    with open('/usr/share/dict/words', 'r') as fh:
        for line in fh.readlines():
            ht.set(line.strip(), line.strip())

    return ht

@pytest.fixture
def smaller_hashtable():
    ht = HashTable(16)
    ht.set('apple', 1)
    ht.set('tomato', 2)
    return ht


def test_slots():
    ht = HashTable(16)
    assert len(ht.hashtable) == 16


def test_hash():
    ht = HashTable(16)
    assert ht.hash('z') == 10

    assert ht.hash('zzz') == 14


def test_get(words_hashtable):
    ht = words_hashtable
    with open('/usr/share/dict/words', 'r') as fh:
        for line in fh.readlines():
            assert line.strip() == ht.get(line.strip())


def test_set(smaller_hashtable):
    ht = smaller_hashtable
    ht.set('cherry', 5)
    assert ht.hashtable[13] == [('cherry', 5)]


def test_set_non_string(smaller_hashtable):
    ht = smaller_hashtable
    with pytest.raises(TypeError):
        ht.set(1, 1)


def test_set_hash_collision(smaller_hashtable):
    ht = smaller_hashtable
    ht.set('b', 4)
    assert ht.hashtable[2] == [('apple', 1), ('b', 4)]

def test_duplicate_key(smaller_hashtable):
    ht = smaller_hashtable
    ht.set('apple', 3)
    assert ht.get('apple') == 3
