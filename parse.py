#!/usr/bin/env python3

def chunks(s, n):
    """Produce `n`-character chunks from `s`."""
    for start in range(0, len(s), n):
        yield s[start:start+n]

with open('code.txt') as txt:
    # read in code, but strip linebreaks and spaces
    code=txt.read().replace('\n', '').replace('\r', '').replace(' ', '')
    for chunk in chunks(code, 8):
        print (chr(int(chunk, 2)), end='')
