class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        words_list = []
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in hashmap:
                hashmap[sorted_word].append(word)
            else:
                hashmap[sorted_word] = [word]
        for i in hashmap.values():
            words_list.append(i)
        return words_list
