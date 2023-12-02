#!/usr/bin/env python3

from game import *
from lean import move

def test_move_no_jumping_empty():
    init()
    assert board() == [F,F,E,E,E,T,T]
    move(1)
    assert board() == [F,E,F,E,E,T,T]
