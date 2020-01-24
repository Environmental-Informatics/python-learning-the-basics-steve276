#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 23:22:10 2020
by Miriam Stevens
@author: steve276

ABE65100 - ThinkPython - Excercise 3.3

This program draws a 4x4 grid
"""
# prints row dividers
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

# prints row when prt_b passed as argument
def print_4times(f):
    f()
    f()
    f()
    f()
   
# defines grid size
def size_grid(row_div,p,row):
    row_div()                    # row_div is row div
    p(row)                       # p prints row
    row_div()
    p(row)
    row_div()
    p(row)
    row_div()
    p(row)
    row_div()

#prints grid    
size_grid(prt_a,print_4times,prt_b)    
    
    
    
