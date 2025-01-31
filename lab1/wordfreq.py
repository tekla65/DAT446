#mport wordfreq


def tokenize(lines):
    
    words = []
    for line in lines:
        start = 0
        #print(line)
        while start < len(line):
            while line[start].isspace():
                start = start+1
                

            if line[start].isalpha():
                    end = start
                    
                    while end < len(line) and line[end].isalpha(): 
                        
                        end = end+1

                    words.append(line[start:end])
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
                    words.append(line[start:end])
                    start = start+1

            
    return words

print(tokenize(['apple','p1e!']))
#wordfreq.tokenize(['apple','pie'])
