class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            '(': ')',
            '[': ']',
            '{': '}',
        }

        stack = []
        for c in s:
            if c in d:
                stack.append(c)
            elif stack:
                opening = stack.pop()
                closing = d[opening]

                if not c == closing:
                    return False
            else:
                return False

        return not stack


sol = Solution()
a = '()[]{}'
print(a, sol.isValid(a))

b = '(]'
print(b, sol.isValid(b))

b = '({['
print(b, sol.isValid(b))

b = ')]]'
print(b, sol.isValid(b))

b = '({[]})'
print(b, sol.isValid(b))

# if it's an opening bracket, push onto stack
# if it's an closing bracket, pop from stack
# compare that lookup closing matches current char
