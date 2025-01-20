# Question:
# You are given a 0-indexed 1-dimensional (1D) integer array original, 
# and two integers, m and n. 
# You are tasked with creating a 2-dimensional (2D) array 
# with  m rows and n columns using all the elements from original.
# The elements from indices 0 to n - 1 (inclusive) 
# of original should form the first row of the constructed 2D array, 
# the elements from indices n to 2 * n - 1 (inclusive) 
# should form the second row of the constructed 2D array, and so on.
# Return an m x n 2D array constructed according to the above procedure, 
# or an empty 2D array if it is impossible.

# Example 1:
# Input: original = [1,2,3,4], m = 2, n = 2
# Output: [[1,2],[3,4]]

# Example 2:
# Input: original = [1,2], m = 1, n = 1
# Output: []

# Thoughts/visualization
# first row 0 to n-1 -> [0,n]
# second row n to 2*n-1 -> [n, 2n]
# third row 2n to 3*n-1 -> [2n, 3n]
# So we know that slice is [i*n:(i+1)*n]
# we create m rows 2D array -> for i in range(m)
# [original[i * n:(i + 1) * n] for i in range(m)]

# i = 0：
# original[0 * 2 : (0 + 1) * 2]，-> original[0:2]。
# we got list [1, 2]
# i = 1：
# original[1 * 2 : (1 + 1) * 2]，-> original[2:4]。
# we got list [3, 4]
# [[1, 2], [3, 4]]。

def construct2DArray(original, m, n):
    if m * n != len(original):
        return []
    
    return [original[i * n:(i + 1) * n] for i in range(m)]



