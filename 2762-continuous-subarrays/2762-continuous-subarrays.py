class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        
        count = 0
        left = 0
        right = 0
        max_heap = []
        min_heap = []
        while right < len(nums) :
            heappush(max_heap, (-nums[right] , right))
            heappush(min_heap, (nums[right], right))
            while max_heap and min_heap and (-max_heap[0][0]) - (min_heap[0][0]) >2:
                left += 1
                while max_heap and max_heap[0][1] < left:
                    heappop(max_heap)
                while min_heap and max_heap[0][1] < left:
                    heappop(min_heap)
            count +=(right -left + 1)
            right += 1
        return count
        