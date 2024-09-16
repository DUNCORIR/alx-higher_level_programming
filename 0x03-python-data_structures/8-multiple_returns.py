#!/usr/bin/python3
def multiple_returns(sentence):
    # Check if the sentence is empty
    if len(sentence) == 0:
        # If empty, return a tuple with 0 and None
        return (0, None)
    else:
        # if not empty,return len and 1st character.
        return (len(sentence), sentence[0])
