class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c for c in s if c.isalnum()).lower()
        pointer1 = 0
        pointer2 = -1
        for i in range(len(s)):
            if s[pointer1] != s[pointer2]:
                return False
            
            pointer1 += 1
            pointer2 -= 1

        return True