#!/usr/bin/env python3

from game import *
from workon import *

#def test_frogjump():
#    init()
#    board()[2]=T
#    assert board() == [F,F,T,E,E,T,T]
#    frogjump(1)
#    assert board() == [F,E,T,F,E,T,T]


def test_frogstep():
    init();              assert board() == START
    init(); frogstep(0); assert board() == START
    init(); frogstep(1); assert board() == [F,E,F,E,E,T,T]
    init(); frogstep(6); assert board() == START
    init(); frogstep(9); assert board() == START


def test_toadstep():
    init();              assert board() == START
    init(); toadstep(6); assert board() == START
    init(); toadstep(5); assert board() == [F,F,E,E,T,E,T]
    init(); toadstep(1); assert board() == START
    init(); toadstep(9); assert board() == START


def test_peek():
    init()
    assert board() == [F,F,E,E,E,T,T]
    assert peek(0) == F
    assert peek(2) == E
    assert peek(6) == T
    assert peek(7) is None


def test_swap():
    init()
    assert board() == [F,F,E,E,E,T,T]
    board()[1] = 'hello'
    board()[5] = 'world'
    assert board() == [F,'hello',E,E,E,'world',T]
    swap(1,5)
    assert board() == [F,'world',E,E,E,'hello',T]


def test_init():
    init()
    assert board() == [F,F,E,E,E,T,T]
    board()[0] = 42
    assert board() == [42,F,E,E,E,T,T]
    init()
    assert board() == [F,F,E,E,E,T,T]

def test_named():
    init()
    named = board()

    assert named   [0] == F
    assert board() [0] == F 
    assert peek    (0) == F 

    named[0] = 10
    assert named   [0] == 10
    assert board() [0] == 10
    assert peek    (0) == 10

    init()
    assert named   [0] == 10
    assert board() [0] == F
    assert peek    (0) == F
