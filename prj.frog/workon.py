#!/usr/bin/env python3
# coding: utf-8

#
# Code for the student to work on.
#

def frogjump(ii):
    #
    # To the student: can you write code to support
    # a frog jumping?
    #
    if (peek(ii), peek(ii+2)) in [ (F,T), (T,F) ] :
        swap (ii,ii+2)
    else:
        print( "Cannot move" )


