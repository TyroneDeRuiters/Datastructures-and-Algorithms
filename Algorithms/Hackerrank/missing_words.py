
def missingWords(s, t):
    s = s.strip()
    t = t.strip()
    s = s.split()
    t = t.split()
    missing_words = list()
    t_num_ocur = dict()
    for word in t:
        if(word in t_num_ocur.keys()):
            t_num_ocur[word] += 1
        else:
            t_num_ocur[word] = 1
    for i in range(len(s)):
        if(s[i] in t_num_ocur.keys()):
            if(t_num_ocur[s[i]] != 0):
                t_num_ocur[s[i]] -= 1
            else:
                missing_words.append(s[i])
        else:
                missing_words.append(s[i])
    return missing_words 
    
print(missingWords("          I am using HackerRank to improve programming", "chocolates chocolates"))
