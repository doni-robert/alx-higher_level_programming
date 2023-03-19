#!/usr/bin/python3
def best_score(a_dictionary):
    biggest_v = 0
    if a_dictionary is None:
        return None
    for k, v in a_dictionary.items():
        if v > biggest_v:
            biggest_v = v
            biggest_k = k
    return biggest_k
