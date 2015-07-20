# -*- coding: utf-8 -*-
from __future__ import unicode_literals

'''
Return 1 if the string is "open" (there are open parens that are not closed)
Return 0 if the string is "balanced" (there are an equal number of open and closed parentheses in the string)
Return -1 if the string is "broken" (a closing parens has not been proceeded by one that opens) 
String must not start with an open parentheses.
'''

def balanced(text): 
    x = 0
    y = []
    for i in text:
        if i == ")":
            x -= 1
            y.append("open")
        elif i == "(":
            x += 1
            y.append("closed")
    if y[0] == "open":
        return "You have started with a closed parentheses. Invalid."
    elif x == 0:
        return 0
    elif x >= 1:
        return 1
    else: 
        return -1
