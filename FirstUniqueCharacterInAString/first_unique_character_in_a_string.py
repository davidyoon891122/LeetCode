"""
Given a string s, find the first non-repeating character in it and return its index.
If it does not exist, return -1.
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_dic = {}
        for char in s:
            if char in char_dic:
                char_dic[char] += 1
            else:
                char_dic[char] = 1

        result = next((key for key, value in char_dic.items() if value == 1), None)
        if result == None:
            return -1
        return s.index(result)




exam_1 = "leetcode"
exam_2 = "loveleetcode"
exam_3 = "aabb"

s = Solution()
print(s.firstUniqChar(s=exam_1))
print(s.firstUniqChar(s=exam_2))
print(s.firstUniqChar(s=exam_3))