class Solution:
    def confusingNumber(self, n: int) -> bool:
        original = n
        rotated = 0
        confusing_mapping = {0: 0, 1: 1, 9: 6, 6: 9, 8: 8}
        while n>0:
            num = n % 10
            if num not in confusing_mapping:
                return False
            else:
                rotated = rotated*10 + confusing_mapping[num]
                n = n//10
        return original != rotated