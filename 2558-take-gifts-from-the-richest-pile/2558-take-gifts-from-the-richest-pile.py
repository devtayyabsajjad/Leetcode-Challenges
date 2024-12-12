class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            a = max(gifts)
            gifts.remove(a)
            b = int(a**0.5)
            gifts.append(b)
        ans = sum(gifts)
        return ans



