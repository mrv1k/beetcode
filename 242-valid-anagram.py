class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = {}

        for letter in s:
            letter_value = d.get(letter)
            if letter_value:
                d[letter] = letter_value + 1
            else:
                d[letter] = 1

        for letter in t:
            letter_value = d.get(letter)
            if letter_value is None or letter_value == 0:
                return False
            d[letter] -= 1

        return True


sol = Solution()
print(sol.isAnagram('bruh', 'nah'))
print(sol.isAnagram('ab', 'aa'))
print(sol.isAnagram('listen', 'silent'))
