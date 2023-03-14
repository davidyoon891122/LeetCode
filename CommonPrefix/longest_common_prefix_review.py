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
    
    prefix = ""
    if len(strs[0]) == 0:
        return ""

    for char_index in range(len(strs[0])):
        prefix += strs[0][char_index]
        if len(strs) == 1:
            return strs[0]
        for index in range(1,len(strs)):
            if prefix == strs[index][:char_index+1]:
                continue
            else:
                return prefix[0:len(prefix) - 1]
    return prefix

            




example_1 = ['flower', 'flow', 'flight']
example_2 = ["dog","racecar","car"]
example_3 = [""]
example_4 = ["a"]
example_5 = ["", ""]
example_6 = ["ab", "a"]
example_7 = ["flower","flower","flower","flower"]

print("result1: {}".format(get_common_prefix(example_1)))
print("result2: {}".format(get_common_prefix(example_2)))
print("result3: {}".format(get_common_prefix(example_3)))
print("result4: {}".format(get_common_prefix(example_4)))
print("result5: {}".format(get_common_prefix(example_5)))
print("result6: {}".format(get_common_prefix(example_6)))
print("result7: {}".format(get_common_prefix(example_7)))
"""
Result:
Success
Details 
Runtime: 41 ms, faster than 83.36% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 13.9 MB, less than 50.07% of Python3 online submissions for Longest Common Prefix.
Next challenges:

"""