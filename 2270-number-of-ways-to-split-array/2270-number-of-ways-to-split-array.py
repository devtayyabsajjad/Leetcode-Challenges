class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_sum = sum(nums)  # Calculate the total sum of the array
        prefix_sum = 0         # Initialize prefix sum
        valid_splits = 0       # Initialize the count of valid splits
        
        # Iterate through the array, stopping at the second-to-last element
        for i in range(len(nums) - 1):
            prefix_sum += nums[i]  # Incrementally calculate the prefix sum
            suffix_sum = total_sum - prefix_sum  # Calculate the suffix sum
            if prefix_sum >= suffix_sum:  # Check the condition
                valid_splits += 1        # Increment the count if valid
        
        return valid_splits  # Return the total count of valid splits
