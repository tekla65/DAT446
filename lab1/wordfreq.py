import wordfreq


def tokenize(lines):
    
    words = []
    for line in lines:
        start = 0
   
        while start < len(line):
           while start.isspace(): #något fel, ska inte vara start.
                #print(line[start]) <--tidigare kod
                if start.isdigit():
                    print(f"{start} is a digit")#ska inte vara start
                
                elif start.isalpha():
                    print(f"{start} is a letter")

                else:
                    print(f"{start} is a symbol")
                start = start+1
    return words

wordfreq.tokenize(['apple','pie'])