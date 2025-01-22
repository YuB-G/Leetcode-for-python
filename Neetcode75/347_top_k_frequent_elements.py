# Given an integer array nums and an integer k, 
# return the k most frequent elements.

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Input: nums = [1], k = 1
# Output: [1]

#method1 面试不推荐
# count = {1: 3, 2: 2, 3: 1}
# most_common(k)
# [(1,3,(2,2))]
# [1,2]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        return [item[0] for item in count.most_common(k)]

# method2：
# count = {1:3,2:2,3:1}

# heap = [(3:1)]
#         [(2:2),(3:1)]
# if len(heap)>k:
#     pop


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        heap = []
        for key, val in count.items():
            heapq.heappush(heap, (val, key))  # 将 (频率, 元素) 加入堆
            if len(heap) > k:  # 如果堆大小超过 k，则弹出堆顶
                heapq.heappop(heap)
        
        # 3. 提取结果
        return [item[1] for item in heap]
    
#时间: counter: O(n)
        heap: O(logk)
        result: O(n)
    total: O(nlogk)
# 空间：O（n）