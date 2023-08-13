#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence == '':
        char_0 = None
    else:
        char_0 = sentence[0]
    return (len(sentence), char_0)
