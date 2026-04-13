class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = []
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if nums[i] + nums[j] == target:
                    if i == j:
                        pass
                    else:
                        indexes.append(i)
                        indexes.append(j)
                        return indexes
            

        