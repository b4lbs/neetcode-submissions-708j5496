class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums1 = nums.copy()
        if len(nums) == len(set(nums1)):
            return False

        else:
            return True