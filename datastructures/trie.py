class Node:
    def __init__(self, val):
        self.val = val
        self.alphabet = [None] * 26

'''The addWord function is used to add a word to the trie.
The following is done by looping through each letter of the word:
We compute the index of the letter, called indx.
We then check whether the list of the alphabet -simply called alphabet- in the root node contains a node at indx.
If yes, we traverse the trie to that node. If no, we check whether the letter we are currently using is the last letter of the word.
If it is, we create a new node at alphabet[indx]: Node(val). Else, we create a new node at alphabet[indx]: Node(None)'''
def add(root, word, val):                                   
    for letter in word:
        indx = ord(letter) - 97                         # Here the index of the letter is calculated using ascii values. where the ascii for 'a' is 97.
        if(root.alphabet[indx] == None):   
            if(letter == word[len(word) - 1]):
                root.alphabet[indx] = Node(val)
            else:
                root.alphabet[indx] = Node(None)
        root = root.alphabet[indx]

def search(root, string):
    for letter in string:
        indx = ord(letter) - 97 
        if(root.alphabet[indx] == None):
            print(string + "does not exist in the trie.")
            return 
        if(letter == word[len(word) - 1]):
            print(string + "was successfully found.")
        root = root.alphabet[indx]

                
