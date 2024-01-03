from typing import List


class Solution:
    @classmethod
    def calPoints(self, operations: List[str]) -> int:
        score = []
        for char in operations:
            try:
                digit = int(char)
                score.append(digit)
            except:
                # not a digit
                if char == '+':
                    a = score[-1]
                    b = score[-2]
                    score.append(a + b)
                if char == 'D':
                    score.append(score[-1] * 2)
                if char == 'C':
                    score.pop()
        return sum(score)


# Explanation:
# "5" - Add 5 to the record, record is now [5].
# "2" - Add 2 to the record, record is now [5, 2].
# "C" - Invalidate and remove the previous score, record is now [5].
# "D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
# "+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
# The total sum is 5 + 10 + 15 = 30.
ops = ["5", "2", "C", "D", "+"]
result = Solution.calPoints(ops)
assert result, 30
print(ops, result)
