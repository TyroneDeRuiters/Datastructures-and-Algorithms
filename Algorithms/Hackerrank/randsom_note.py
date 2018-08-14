'''Solution to the random note problem from hackerrank.com.
This function checks whether words that appear in the note list also appear in the magazine list.'''

def checkMagazine(magazine, note):
    hash1 = dict()
    for word in magazine:
        if(word not in hash1):
            hash1[word] = 1
        else:
            hash1[word] += 1
    for word in note:
        if(word not in hash1 or hash1[word] == 0):
            return "No"
        else:
            hash1[word] -= 1
    return "Yes"
