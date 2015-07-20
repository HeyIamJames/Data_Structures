# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from parenthetics import balanced
import pytest 

def test_open():
    text = "(((()"
    assert balanced(text) == 1

def test_cloed():
    text = "()))))"
    assert balanced(text) == -1

def test_balanced():
    text = "()"
    assert balanced(text) == 0

def test_order():
    text = ")()()()"
    assert balanced(text) == "You have started with a closed parentheses. Invalid."
