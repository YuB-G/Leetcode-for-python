# Question:
# Given a non-empty array of integers nums, 
# every element appears twice except for one. 
# Find that single one.
# You must implement a solution with 
# a linear runtime complexity and use 
# only constant extra space.

# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Hash (but using O(n) space complexity)

# Thoughts/visualization

# Hash Table
# create a hashtable: dic = {} 
# for loop traversal all elements in list
# if num in dic:
#    delect num
# if num not in dic: 
#   add num    
# After traversal list
# The remaining items in the list are single numbers  

# [2,2,1]
# 2 not in hash
# add 2 in hash {2:1}
# 2' in hash
# delete 2 in hash
# 1 not in hash
# add 1 in hash
# After traversal list
# The only item in list is 1
# So, 1 is signle number in this list

class Number:
    def singleNumber(self, nums):
        dic = {}
        for i in nums:
            if i in dic:
                del dic[i]
            else:
                dic[i] = 1

        for single in dic:
            return single


# XOR operation
# Any number XORed with 0 will remain unchanged, a xor 0 = a.
# Any number XORed with itself will result in 0, a xor a = 0.
# The XOR operation is commutative and associative

# for loop traversal all elements in list
# use xor operation calculate all numbers
# return result

# [2,2,1]
# 2 ^ 2 ^ 1
# = 1

class Number:
    def singleNumber (self, nums):
        single = 0
        for num in nums:
            single ^= num 
        return single
            