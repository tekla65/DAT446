"""
import wordfreq


def tokenize(lines):
    
    words = []
    for line in lines:
        start = 0
   
        while start < len(line):
            while line[start].isspace(): #något fel, ska inte vara start.
                start = start+1

                if line[start].isdigit():
                    print(f"{line[start]} is a digit")#ska inte vara start
                
                elif line[start].isalpha():
                    print(f"{line[start]} is a letter")

                else:
                    print(f"{line[start]} is a symbol")
    return words

#wordfreq.tokenize(['apple','pie'])
"""

"""

import wordfreq


def tokenize(lines):
    
    words = []
    for line in lines:
        start = 0
        print(line)
        while start < len(line):
            if line[start].isalpha(): #något fel, ska inte vara start.
                print(f"{line[start]} is a letter")

            start = start+1
    return words

wordfreq.tokenize(['apple','pie'])


#print('p'.isspace())"""
