#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 20:09:40 2020
by Miriam Stevens
@author: steve276

ABE65100 - ThinkPython - Excercise 3.2

This program prints a string four times using two defined functions:
one that prints a value twice,
and another that uses a nested function to call a value twice.

"""


# calls the value twice
def do_twice(f,value):
    f(value)
    f(value)

# prints a string twice
def print_twice(greg):
    print(greg)
    print(greg)
   
# calls the function that prints a string twice, twice
do_twice(print_twice,'spam')


