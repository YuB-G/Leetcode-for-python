# 269.Alien Dictionary
# Gievn a list of string "words" from alien dictionary
# Return a string of the unique letters in the new alien language sorted in lexicographically
# increasing order by the new language's rules. 
# In first different character, if s before t, then s < t
# abc and abcd, s.length<t.length. s<t
# Video: https://www.youtube.com/watch?v=6kTZYvNNyps

# input: words = ["wrt","wrf","er","ett","rftt"]
# output: "wertf"
# 

# Input: words = ["z","x"]
# output:"zx"

# Input: words = ["z","x","z"]
# output: ""

def alienDict(self, words):

    # preprocessing
    adjacencyList = {}
    for w in words:
        for char in w:
            adjacencyList[char] = set() 
            # The reason we use set() because we wanna use Topological sort for a DAG

    for i in range(len(words)-1):
        w1, w2 = words[i], words[i+1]
        minLen = min(len(w1), len(w2))
        # Determine if the prefix of a word comes after a longer word.
        if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]: 
            return ""
        for j in range(minLen):# Won't exceed the length of the word during traversal
            if w1[j] != w2[j]:# The first time a different letter appears in a different location.
                adjacencyList[w1[j]].add(w2[j]) # Add pointing relationship
                break
    
    visit = {}
    result = []

    #post order
    # All the neighboring nodes of a node are visit first, 
    # and then the node itself is visit. 
    # we need to visit the current char only after 
    # all the char pointing to it have already been visit.
    def dfs(char):
        if char in visit:
            return visit[char]
        
        visit[char] = True #in visit
# All the neighboring nodes of a node are visit first
        for neighbor in adjacencyList[char]:
            if dfs(neighbor): #has cycle
                return True

        visit[char] = False # visit finished
        result.append(char)
# and then the node itself is visit. 
    for char in adjacencyList:
        if dfs(char): # has cycle
            return ""
    result.reverse()# post order
    return "".join(result)

    

    