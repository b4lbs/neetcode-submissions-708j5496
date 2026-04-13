class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            temp = nums.copy()
            temp[i] = 1
            product = 1
            for j in temp:
                product = product * j
            res.append(product)
        return res