class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer1, pointer2 = 0, 1
        while pointer2 <len(nums):
            if nums[pointer1] == nums[pointer2]:
                del nums[pointer1]
            else:
                pointer1 +=1 
                pointer2 +=1
            
        return len(nums)