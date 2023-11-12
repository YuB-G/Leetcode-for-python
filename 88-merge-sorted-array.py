# You are given two integer arrays nums1 and nums2, 
# sorted in non-decreasing order, 
# and two integers m and n, 
# representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]

# Thought:

# nums1 = [1,2,3,0,0,0]
# nums2 = [2,5,6]
# m = 3, n = 3 

# p1 = m-1
# p2 = n-1

# p = m+n-1, p is merged list

# while p1>=0 and p2 >=0:
#   if nums[p1] > nums[p2]:
#       put larger number to the end: nums[p] = nums1[p1]
#   else: (nums[p2] is larger)
#          nums[p] = nums1[p2]

# nums1[2] = 3 > nums2[2] = 6   not
# nums1[p] = nums[p2]
# nums1'[5] = 6
# p2 -=1

# len(p2) may larger than len(p1), copy left element to p1s
# nums1[:p2+1] = nums2[:p2+1]




def merge(nums1, m, nums2, n):

    p1, p2 = m - 1, n - 1
    p = m + n - 1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    # 如果nums2中还有剩余元素，直接拷贝到nums1的前面
    nums1[:p2 + 1] = nums2[:p2 + 1]
