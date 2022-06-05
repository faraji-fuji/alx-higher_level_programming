#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        t = (0, None)
        return t
    first_char = sentence[0]
    length = len(sentence)
    t = (length, first_char)
    return t
