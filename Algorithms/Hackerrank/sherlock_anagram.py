def getSubsets(s):
    hash1 = dict()
    list1 = list()
    for i in range(len(s)):
        j = 0
        while(j+i+1 <= len(s)):
            substring = sort(s[j:j+i+1])
            if(substring not in hash1):
                hash1[substring] = 0
            else:
                hash1[substring] += 1
                for x in range(hash1[substring]):
                    list1.append(s[j:j+i+1])
            j += 1
    print(list1)
    print(len(list1))

def sort(string):
    list1 = list()
    for letter in string:
        list1.append(letter)
    list1.sort()
    string = ""
    for letter in list1:
        string += letter
    return string


            
