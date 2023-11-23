Frog: a simple one player game.

We start with a board somewhat like:

    [Frog|Frog|Frog|....|Toad|Toad|Toad]

The frogs start on the left facing right. The toads start on
the rignt facing left. They are separated by a single space.
The goal of the game is to move all frogs to the right and all
toads to the left to reach this winning board state:

    [Toad|Toad|Toad|....|Frog|Frog|Frog]

The pieces (frogs and toads) can only move foreward in the
direction they face: frogs to the right, and toads to the
left.  If a piece faces an empty space, it may STEP into
that empty space. If a piece faces ONE other piece followed
by an empty space, it may JUMP over that one piece and into
the empty space.  If a piece faces TWO other pieces (or the
end of the board) it cannot move.

Examples:

    Here a frog faces an empty space to its right. It may
    STEP into that space:

           |Frog|....|
       =>  |....|Frog|
 
    Here a toad faces one frog to its left, followed by an
    empty space. It may JUMP into that space:

           |....|Frog|Toad|
       =>  |Toad|Frog|....|


