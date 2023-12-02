#!/usr/bin/env python3
# coding: utf-8

from game import peek, swap, F, T, E

#
# Code for the student to work on.
#


def frogjump(i):
    #
    # To the student: can you write code to support
    # a frog jumping?
    #
    #     |Frog|Toad|....|
    # =>  |....|Toad|Frog|
    #        i  i+1  i+2
    if (peek(i), peek(i+1), peek(i+2)) == (F,T,E):
        swap (i,i+2)
    else:
        print( "Cannot move" )


