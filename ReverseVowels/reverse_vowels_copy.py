class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiou"

        string_list = list(s)
        first = 0
        last = len(s) - 1

        while first < last:
            if string_list[first].lower() in vowels and string_list[last].lower() in vowels:
                string_list[first], string_list[last] = string_list[last], string_list[first]
                first += 1
                last -= 1
            elif string_list[first].lower() in vowels:
                last -= 1
            elif string_list[last].lower() in vowels:
                first += 1
            else:
                first += 1
                last -= 1
        return ''.join(string_list)


case_1 = "hello"

s = Solution()

print(s.reverseVowels(s=case_1))