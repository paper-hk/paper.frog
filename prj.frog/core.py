#!/usr/bin/env python3
# coding: utf-8

"""Provide infrastracture support for board manipulation.

These functions provide raw board manipulation without 
respect to game logic.  
"""

import sys

from constants import START 


def board():
    try: 
        # If we have a current board, return it
        return sys._THEFROGBOARD
    except AttributeError:
        # The board was not created yet. Call init to create a new one.
        init()
        return sys._THEFROGBOARD


def init():
    """Initialize the board.
    We piggyback on the builtin sys module. 
    """
    # reset the board
    sys._THEFROGBOARD = START.copy()


def peek(i):
    """Peek at a board position.. 
    Like B[i], but return None if [i] is out of range.
    """
    B=board()
    try:
        return B[i]
    except IndexError:
        # This will 'catch' the error.
        return None

def swap(i,j):
    """Swap the pieces at [i] and [j] if possible.

    Possible here means programatically possible. Game rules are not
    inforced by this function.
    """
    B=board()
    try:
        B[i], B[j] = B[j], B[i]
    except IndexError:
        pass

