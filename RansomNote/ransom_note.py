"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        print(ransomNote)
        magazine_dic = {}
        for char in magazine:
            if char in magazine_dic:
                magazine_dic[char] += 1
            else:
                magazine_dic[char] = 1
        
        for char in ransomNote:
            if char in magazine_dic:
                if magazine_dic[char] == 0:
                    return False
                else:
                    magazine_dic[char] -= 1
            else:
                return False
        return True
            
first_3 = "aa"
second_3 = "aab"

first_1 = "a"
second_1 = "b"

first_2 = "aa"
second_2 = "ab"

s = Solution()

print(s.canConstruct(ransomNote=first_1, magazine=second_1))
print(s.canConstruct(ransomNote=first_2, magazine=second_2))
print(s.canConstruct(ransomNote=first_3, magazine=second_3))

