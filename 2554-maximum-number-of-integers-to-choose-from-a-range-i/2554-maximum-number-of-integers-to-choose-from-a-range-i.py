class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)  # Convert to set for O(1) lookups
        current_sum = 0
        count = 0
        
        for i in range(1, n + 1):  # Start from 1 to include all valid numbers in [1, n]
            if i not in banned_set:
                if current_sum + i > maxSum:  # Stop if adding i exceeds maxSum
                    break
                current_sum += i
                count += 1
        
        return count