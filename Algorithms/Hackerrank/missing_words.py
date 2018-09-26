
def missingWords(s, t):
    s = s.strip()
    t = t.strip()
    s = s.split() #convert s and t to lists
    t = t.split()
    missing_words = list()
    t_num_ocur = dict()
    
    for word in t:                             #
        if(word in t_num_ocur.keys()):
            t_num_ocur[word] += 1
        else:
            t_num_ocur[word] = 1
            
    for word in s:
        if(word in t_num_ocur.keys()):
            if(t_num_ocur[word] != 0):
                t_num_ocur[word] -= 1
            else:
                missing_words.append(word)
        else:
                missing_words.append(word)
    return missing_words 
    
print(missingWords("I am using HackerRank to improve programming", "I using programming"))
