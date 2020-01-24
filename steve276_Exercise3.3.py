#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 23:22:10 2020
by Miriam Stevens
@author: steve276

ABE65100 - ThinkPython - Excercise 3.3

This program draws a 4x4 grid
"""
# prints row separators
def prt_a():
    print('+ - - - -', end =" ")
    print('+ - - - -', end =" ")
    print('+ - - - -', end =" ")
    print('+ - - - -', end =" ")
    print('+')

# prints column separators 
def prt_b():
    print('|        ', end =" ")
    print('|        ', end =" ")
    print('|        ', end =" ")
    print('|        ', end =" ")
    print('|')
    
#def prt_part(f):                 function to test row and column separators
#    f()
    
#prt_part(prt_a)                  tests row separators

#prt_part(prt_b)                  tests column separators

# defines size of grid
def prt_grid(f,g):
    f()
    g()
    g()
    g()
    g()
    f()
    g()
    g()
    g()
    g()
    f()
    g()
    g()
    g()
    g()
    f()
    g()
    g()
    g()
    g()
    f()
    
# prints grid
prt_grid(prt_a,prt_b)
    
    
    