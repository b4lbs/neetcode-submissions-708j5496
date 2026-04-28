class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_number = 0
        counter = 0
        for i in nums:
            if i == 1:
                counter +=1
            else:
                if max_number < counter:
                    max_number = counter
                counter = 0
        return max(max_number, counter)
