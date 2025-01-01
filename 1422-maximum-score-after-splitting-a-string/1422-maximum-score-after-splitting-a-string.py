class Solution:
    def maxScore(self, s: str) -> int:
        left = ""
        right = ""
        res = []
        for i in range(1 , len(s)):
            left = s[0:i]
            print(left)
            right = s[i:]
            print(right)
            res.append(left.count("0") + right.count("1"))
        return max(res)
        

        