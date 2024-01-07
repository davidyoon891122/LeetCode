
# Time Limit Exceeded
# class Solution:
#     def longestPalindrome(self, s: str) -> str: 
#         long = ""

#         first = 0
#         next = first

#         while first < len(s):
#             target = s[first: next]
#             print(target)
#             if target == target[::-1]:
#                 if len(long) <= len(target):
#                     long = target
#             if next != len(s):
#                 next += 1
#             else:
#                 first += 1
#                 next = first + 1

#         return long

# LeetCode solution
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         longest_palindrom = ''
#         dp = [[0]*len(s) for _ in range(len(s))]

#         #filling out the diagonal by 1
#         for i in range(len(s)):
#             dp[i][i] = True
#             longest_palindrom = s[i]

#         # filling the dp table
#         for i in range(len(s)-1,-1,-1):
# 				# j starts from the i location : to only work on the upper side of the diagonal 
#             for j in range(i+1,len(s)): 
#                 if s[i] == s[j]:  #if the chars mathces
#                     # if len slicied sub_string is just one letter if the characters are equal, we can say they are palindomr dp[i][j] =True 
#                     #if the slicied sub_string is longer than 1, then we should check if the inner string is also palindrom (check dp[i+1][j-1] is True)
#                     if j-i ==1 or dp[i+1][j-1] is True:
#                         dp[i][j] = True
#                         # we also need to keep track of the maximum palindrom sequence 
#                         if len(longest_palindrom) < len(s[i:j+1]):
#                             longest_palindrom = s[i:j+1]

#         print(longest_palindrom)
                
#         return longest_palindrom


# first brute force
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         def is_palindrom(first, last):
#             while first < last:
#                 if s[first] != s[last]:
#                     return False
                
#                 first, last = first + 1, last - 1
#             return True
        
#         max_first, max_last = 0, 0 

#         for first in range(len(s)):
#             for last in range(len(s)):
#                 if is_palindrom(first, last) and max_last - max_first < last - first:
#                     max_first, max_last = first, last

#         print(s[max_first: max_last + 1])
#         return s[max_first: max_last + 1]
    

# O(n^2)
# class Solution:
    # def longestPalindrome(self, s: str) -> str:
    #     max_first, max_last = 0, 0

    #     for i in range(len(s)):
    #         first, last = i, i
    #         while 0 <= first and last < len(s) and s[first] == s[last]:
    #             if max_last - max_first < last - first:
    #                 max_first, max_last = first, last
    #             first, last = first - 1, last + 1
            
    #         first, last = i, i + 1
    #         while 0 <= first and last < len(s) and s[first] == s[last]:
    #             if max_last - max_first < last - first:
    #                 max_first, max_last = first, last
    #             first, last = first - 1, last + 1

    #     print(s[max_first: max_last + 1])
    #     return s[max_first: max_last + 1]
    

# Dynamic Programing
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         max_first, max_last = 0, 0

#         dp = {}

#         for first in range(len(s) - 1, -1, -1):
#             for last in range(first, len(s)):
#                 if first == last:
#                     dp[(first, last)] = True
#                 elif first + 1 == last:
#                     dp[(first, last)] = s[first] == s[last]
#                 else:
#                     dp[(first, last)] = s[first] == s[last] and dp[(first + 1, last - 1)]
                
#                 if dp[(first, last)] and max_last - max_first < last - first:
#                     max_first, max_last = first, last
        
#         print(s[max_first: max_last + 1])
#         return s[max_first: max_last + 1]
    

# Two Pointer
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            print(s[left + 1: right])
            return s[left + 1: right]
        if len(s) < 2 or s == s[::-1]:
            return s
        
        result = ''

        for i in range(len(s) - 1):
            result = max(result, expand(i, i+1), expand(i, i+2), key=len)

        return result 


str = "babad"

s = Solution()


str2 = "cbbd"
s.longestPalindrome(s=str)
# s.longestPalindrome(s=str2)