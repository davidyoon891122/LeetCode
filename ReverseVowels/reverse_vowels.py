class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiou"

        vowel_list = []

        result = ""

        for ch in s:
            if ch.lower() in vowels:
                vowel_list.append(ch)


        for ch in s:
            if ch.lower() in vowels:
                result += vowel_list.pop()
            else:
                result += ch

        return result


case_1 = "hello"

s = Solution()

s.reverseVowels(s=case_1)