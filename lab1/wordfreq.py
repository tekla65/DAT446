import wordfreq


def tokenize(lines):
    
    words = []
    for line in lines:
        start = 0
   
        while start < len(line):
           while line[start].isspace(): #något fel, ska inte vara start.
                #print(line[start]) <--tidigare kod
                if line[start].isdigit():
                    print(f"{line[start]} is a digit")#ska inte vara start
                
                elif line[start].isalpha():
                    print(f"{line[start]} is a letter")

                else:
                    print(f"{line[start]} is a symbol")
                start = start+1
    return words

wordfreq.tokenize(['apple','pie'])

