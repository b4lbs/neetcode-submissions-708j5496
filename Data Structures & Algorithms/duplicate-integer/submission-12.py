class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums2 = []
        for n in nums:
            if n in nums2:
                return True
            else:
                nums2.append(n)
        
        return False