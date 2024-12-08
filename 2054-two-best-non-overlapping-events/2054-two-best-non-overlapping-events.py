class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Step 1: Sort events by end time
        events.sort(key=lambda x: x[1])
        
        max_value = 0  # Tracks the maximum value up to the current point
        max_sum = 0    # Tracks the overall maximum sum of two events
        max_values = []  # List to store max values for binary search
        
        # Add dummy event with end time 0 to simplify binary search for the first event
        ends = [0]
        max_values.append(0)
        
        for start, end, value in events:
            # Step 2: Binary search to find the last compatible event
            idx = bisect.bisect_right(ends, start - 1) - 1
            # Max sum for this event is either:
            # 1. The event's value alone
            # 2. Its value + the best earlier event's value
            max_sum = max(max_sum, value + max_values[idx])
            # Update max_value to include the current event's value
            max_value = max(max_value, value)
            # Add the current event's end time and max_value for future binary search
            ends.append(end)
            max_values.append(max_value)
        
        return max_sum