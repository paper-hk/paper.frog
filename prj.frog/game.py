#!/usr/bin/env python3
# coding: utf-8

"""Game Logic

Implement game logic. 

Functions here should change the board only on ways that are
legal according to the game rules.

Pedagogically, the teacher should first introduce the student
to the development of [frogstep()], culminating in a working
[frogstep()] function. The student should use this as a model
to develop a working [toadstep()] function. 

Both functions take an index value [i]. The teacher should
show the student that the end user does not need to see two
stepping functions.  We can provide the user with a single
[step()] function which will take take the same [i] index
from the user, look at the kind of piece sitting at that
index, and *delegate* the stepping responsibilities to 
the appropriate stepping function.

The functions [frogstep()] and [toadstep()] are necessary,
but should be considered part of the game infrastructure
rather than part of the user interface.

This points to splitting game logic functions into 
different modules.
"""

import sys

from constants import F,T,E
from core import board, peek, swap


def frogstep(i):
    """Move the frog at [i] one step to the right if possible.

    This function enforces GAME LOGIC.  The move is possible only
    if legal according to game rules. There must actually be a frog
    at [i] and an empty space at [ii+1].
    """
    if (peek(i), peek(i+1)) == (F,E):
       swap(i,i+1)
    else:
        print( "Cannot move" )


def toadstep(i):
    """Move the toad at [i] one step to the left if possible.

    This function enforces GAME LOGIC.  The move is possible only
    if legal according to game rules. There must actually be a toad
    at [i] and an empty space at [ii-1].
    """
    if (peek(i), peek(i-1)) == (T,E):
       swap(i,i-1)
    else:
        print( "Cannot move" )


def step(i):
    """Have the player piece at [i] take one step if possible.

    This function enforces GAME LOGIC.  The move is possible only
    if legal according to game rules. There must actually be a 
    player piece (frog or toad) at [i].  We look at the piece and
    dispatch (ie delegate) the actual stepping to the appropriate
    stepper function.  

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

