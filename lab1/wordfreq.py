#import wordfreq


def tokenize(lines):
    
    words = []
    for line in lines:
        start = 0
        #print(line)
        while start < len(line):
            if line[start].isspace():
                start = start+1
                

            elif line[start].isalpha():
                    end = start
                    
                    while end < len(line) and line[end].isalpha(): 
                        
                        end = end+1

                    words.append(line[start:end].lower())
                        #print(f"{line[start]} is a letter")
                    start = end


            elif line[start].isdigit():
                    end = start
                    
                    while end < len(line) and line[end].isdigit(): 
                        
                        end = end+1
                    words.append(line[start:end])
                        #print(f"{line[start]} is a digit")
                    start = end
            else:
                    #print(f"{line[start]} is a symbol")
                    words.append(line[start])
                    start = start+1

            
    return words

#print(tokenize(['Apple','p1e!']))
#tokenize(['apple','p1e!'])
#wordfreq.tokenize(['apple','p1e!'])

