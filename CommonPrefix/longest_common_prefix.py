"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""

"""
Constraints
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""
from typing import List

def get_common_prefix(strs: List[str]) -> str:
    flag = False
    if len(strs[0]) == 0:
        return ""
    
    for char_index in range(0, len(strs[0])):     
        firstChar = strs[0][char_index]
        for elem_index in range(1, len(strs)):
            if len(strs[elem_index]) == char_index:
                flag = True
                break
            if strs[elem_index][char_index] == firstChar:
                continue
            else:
                flag = True
                break
        if flag == True:
            return strs[0][:char_index]
        elif flag != True and len(strs) == 1:
            return strs[0]
    return strs[0]



example_1 = ['flower', 'flow', 'flight']
example_2 = ["dog","racecar","car"]
example_3 = [""]
example_4 = ["a"]
example_5 = ["", ""]
example_6 = ["ab", "a"]
example_7 = ["flower","flower","flower","flower"]

print("result: {}".format(get_common_prefix(example_1)))
print("result: {}".format(get_common_prefix(example_2)))
print("result: {}".format(get_common_prefix(example_3)))
print("result: {}".format(get_common_prefix(example_4)))
print("result: {}".format(get_common_prefix(example_5)))
print("result: {}".format(get_common_prefix(example_6)))
print("result: {}".format(get_common_prefix(example_7)))
"""
Result:
Success
Details 
Runtime: 41 ms, faster than 83.36% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 13.9 MB, less than 50.07% of Python3 online submissions for Longest Common Prefix.
Next challenges:

"""