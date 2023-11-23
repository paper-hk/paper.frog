#!/usr/bin/env python3
# coding: utf-8

import sys

from constants import F,T,E,START


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


def frogjump(ii):
    #
    # Can you write the code?
    #
    if (peek(ii), peek(ii+2)) in [ (F,T), (T,F) ] :
        swap (ii,ii+2)
    else:
        print( "Cannot move" )

