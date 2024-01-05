

from typing import List
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        
        
        pattern = r'[^a-zA-Z0-9\s]'

        paragraph = re.sub(pattern, ' ', paragraph)

        words = paragraph.lower().split(" ")

        print(words)
        count_dic = {}
        
        for word in words:
            if not word in count_dic and not word in banned:
                count_dic[word] = words.count(word)

        
        return max(count_dic, key=count_dic.get)


#paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]


paragraph = "Bob. hIt, baLl"

s = Solution()
s.mostCommonWord(paragraph=paragraph, banned=banned)