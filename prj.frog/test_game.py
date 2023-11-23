#!/usr/bin/env python3

from constants import F, T, E, START
from core import board, init
from game import frogstep, toadstep


def test_frogstep():
    init();                 assert board() == START
    init() ; frogstep(0);   assert board() == START
    init() ; frogstep(1);   assert board() == [F,E,F,E,E,T,T]
    init() ; frogstep(6);   assert board() == START
    init() ; frogstep(9);   assert board() == START


def test_toadstep():
    init();                 assert board() == START
    init() ; toadstep(6);   assert board() == START
    init() ; toadstep(5);   assert board() == [F,F,E,E,T,E,T]
    init() ; toadstep(1);   assert board() == START
    init() ; toadstep(9);   assert board() == START

