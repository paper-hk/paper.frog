# coding: utf-8
F='frog' # Frog piece
T='toad' # Toad piece
E='----' # Empty space



def init():
    global B
    # This is the board. 
    B = [F,F,E,E,E,T,T]

# a function to peek at the board.

def peek(ii):
    """Peek at the board. 

    This function takes a number amd returns what
    is at that position."""
    try:
        return B[ii]
    except IndexError:
        # This will 'catch' the error.
        return None


def swap(ii,jj):
    try:
        B[ii], B[jj] = B[jj], B[ii]
    except IndexError:
        pass

def frogstep(ii):
    if (peek(ii), peek(ii+1)) == (F,E):
       swap(ii,ii+1)
    else:
        print( "Cannot move" )

def toadstep(ii):
    if (peek(ii), peek(ii-1)) == (T,E):
       swap(ii,ii-1)
    else:
        print( "Cannot move" )

def frogjump(ii):
    # Can you write the code?
    if (peek(ii), peek(ii+2)) in [ (F,T), (T,F) ] :
        swap (ii,ii+2)
    else:
        print( "Cannot move" )
def step(ii):
    if peek(ii) == F:
        frogstep(ii)
    elif peek(ii) == T:
        toadstep(ii)
    else:
        print( 'Cannot Move' )
    print(B)
