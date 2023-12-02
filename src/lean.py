#!/usr/bin/env python3
# coding: utf-8

from game import peek, swap, F, T, E, board

def can_frog_step(i):
    return ( peek(i), peek(i+1) ) == (F,E)
def can_frog_jump(i):
    return ( peek(i), peek(i+1), peek(i+2) ) == (F,T,E)
def can_toad_step(i):
    return ( peek(i-1), peek(i) ) == (E,T)
def can_toad_jump(i):
    return ( peek(i-2), peek(i-1), peek(i) ) == (E,F,T)

def move(i):
    if can_frog_step(i):
        swap(i,i+1)
    elif can_frog_jump(i):
        swap(i,i+2)
    elif can_toadi_step(i):
        swap(i,i-1)
    elif can_toad_jump(i):
        swap(i,i-2)
    else:
        print('Cannot move')
    print(board())

