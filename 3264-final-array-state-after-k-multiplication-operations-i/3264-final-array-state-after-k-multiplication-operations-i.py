def perform_operations(nums, k, multiplier):
    for _ in range(k):
        # Find the minimum value and its index (first occurrence)
        min_value = min(nums)
        min_index = nums.index(min_value)
        
        # Replace the minimum value with min_value * multiplier
        nums[min_index] = min_value * multiplier
    
    return nums
