"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        word_ditionary = {}

        for word in strs:
            print(sorted(word))
            if "".join(sorted(word)) in word_ditionary:
                word_ditionary["".join(sorted(word))].append(word)
            else:
                word_ditionary["".join(sorted(word))] = [word]

        result = list(word_ditionary.values())

        print(result)




strs = ["eat","tea","tan","ate","nat","bat"]


s = Solution()

s.groupAnagrams(strs=strs)