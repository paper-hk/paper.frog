#!/usr/bin/env python3
# coding: utf-8

"""Game Logic

Functions here should change the board only on ways that are
legal according to the game rules.
"""

from constants import F,T,E
from core import board, peek, swap


def frogstep(i):
    """Move the frog at [i] one step to the right if possible.
    """
    if (peek(i), peek(i+1)) == (F,E):
       swap(i,i+1)
    else:
        print( "Cannot move" )


def toadstep(i):
    """Move the toad at [i] one step to the left if possible.
    """
    if (peek(i), peek(i-1)) == (T,E):
       swap(i,i-1)
    else:
        print( "Cannot move" )


def step(i):
    """Have the player piece at [i] take one step if possible.

    Pedagogy:
    We do not check for an empty space.  The called steper function
    will check for us.
    """
    if peek(i) == F:
        frogstep(i)
    elif peek(i) == T:
        toadstep(i)
    else:
        print( 'Cannot Move' )
    print(board())

