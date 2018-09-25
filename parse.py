#!/usr/bin/env python3

import textwrap # for pretty formatting of output

def chunks(s, n):
    for start in range(0, len(s), n):
        yield s[start:start+n]

with open('code.txt') as txt:
    # read in code, but strip linebreaks and spaces
    code=txt.read().replace('\n', '').replace('\r', '').replace(' ', '')
    # prep out output string for collection
    output=''
    # loop through code string in chunks of 8 characters
    for chunk in chunks(code, 8):
        # convert binary to int, then to ascii character & print
        output += chr(int(chunk, 2))
    # Cleaning up output with some extra line splitting and character
    # replacement. Then using a textwrap fill to make pretty paragraphs.
    # At this point you could just print (output) and be done
    for line in output.splitlines():
        if (line.strip()):
            print (textwrap.fill(line.strip()) + '\n')
