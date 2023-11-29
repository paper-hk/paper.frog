#!/usr/bin/env python3
# coding: utf-8

import sys

###############################################################
# Game Logic
#
# Functions here should change the board only in ways that are
# legal according to the game rules.
###############################################################

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


###############################################################
# Board Logic
#
# These functions support board inspection and piece swapping
# without the client having to worry about IndexError.  There
# is no game logic here.
###############################################################

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

#########################################################################
# Board Creation.
#
# These functions provide a board to play with.
#########################################################################

def board(new=False):
    """Return the current board, optionally resetting it to new.
    """
    if new == True or not hasattr(sys, '__BOARD'):
        sys.__BOARD = START.copy()
    return sys.__BOARD

def init():
    """A convenience function to reset the board."""
    board(new=True)





#########################################################################
#  Constants: The pieces and starting position.
#########################################################################

F = 'frog' # Frog piece
T = 'toad' # Toad piece
E = '----' # Empty space
START = [F,F,E,E,E,T,T]


