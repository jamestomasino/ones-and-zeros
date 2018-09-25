#!/usr/bin/env python3

def chunks(s, n):
    """Produce `n`-character chunks from `s`."""
    for start in range(0, len(s), n):
        yield s[start:start+n]

with open('code.txt') as txt:
    # read in code, but strip linebreaks and spaces
    code=txt.read().replace('\n', '').replace('\r', '').replace(' ', '')
    # loop through code string in chunks of 8 characters
    for chunk in chunks(code, 8):
        # convert binary to int, then to ascii character & print
        print (chr(int(chunk, 2)), end='')
