class Solution:
    def maxScore(self, s: str) -> int:
        res = []
        for i in range(1 , len(s)):
            
            res.append(s[0:i].count("0") + s[i:].count("1"))
        return max(res)
        

        