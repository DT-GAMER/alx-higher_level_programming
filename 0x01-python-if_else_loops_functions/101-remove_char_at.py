#!/usr/bin/python3
def remove_char_at(string, n):
    if n < 0:
        return string
    return string[:n] + string[n + 1:]
