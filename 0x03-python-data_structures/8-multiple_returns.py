#!/usr/bin/python3
def multiple_returns(sentence):
    first_char = sentence[0]
    length = len(sentence)
    if sentence == "":
        first_char = None
    t = (length, first_char)
    return t
