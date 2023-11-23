#!/usr/bin/env python3

from constants import F, T, E, START
from core import board, init, peek, swap

def test_peek():
    init()
    assert board() == START
    assert peek(0) == F
    assert peek(2) == E
    assert peek(6) == T
    assert peek(7) is None


def test_swap():
    init()
    board()[1] = 'hello'
    board()[5] = 'world'
    assert board() == [F,'hello',E,E,E,'world',T]
    swap(1,5)
    assert board() == [F,'world',E,E,E,'hello',T]



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
