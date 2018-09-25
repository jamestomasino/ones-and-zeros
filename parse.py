#!/usr/bin/env python3

def chunks(s, n):
    """Produce `n`-character chunks from `s`."""
    for start in range(0, len(s), n):
        yield s[start:start+n]

with open('code.txt') as txt:
    # read in code, but strip linebreaks
    code=txt.read().replace('\n', '').replace('\r', '')
    for chunk in chunks(code, 8):
        print (chr(int(chunk, 2)), end='')
#bin = [int(i) for element in ["{0:b}".format(ord(c)) for c in message] for i in element]
