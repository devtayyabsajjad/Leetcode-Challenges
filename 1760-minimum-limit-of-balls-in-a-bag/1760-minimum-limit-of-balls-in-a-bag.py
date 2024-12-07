class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def canAchieve(penalty):
        operations = 0
        for balls in nums:
            if balls > penalty:
                operations += (balls - 1) // penalty  # Number of splits needed
            if operations > maxOperations:
                return False
        return operations <= maxOperations

    low, high = 1, max(nums)
    while low < high:
        mid = (low + high) // 2
        if canAchieve(mid):
            high = mid  # Try for a smaller maximum penalty
        else:
            low = mid + 1  # Increase the penalty

    return low