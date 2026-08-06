class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        cur = []
        ans = []

        mapping = [ "", "", "abc", "def", "ghi","jkl", "mno", "pqrs", "tuv", "wxyz"]

        def f(idx):
            if idx == len(digits):
                ans.append("".join(cur))
                return
            
            curDigit = int(digits[idx])
            choices = mapping[curDigit]

            for alphabet in choices:
                cur.append(alphabet)
                f(idx + 1)
                cur.pop()

        f(0)

        return ans