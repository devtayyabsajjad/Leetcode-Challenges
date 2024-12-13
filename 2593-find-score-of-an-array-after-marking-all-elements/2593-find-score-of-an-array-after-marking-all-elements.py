class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        score = 0  
        marked = [False] * n  
        heap = []
        
        for i in range(n):
            heapq.heappush(heap, (nums[i], i))
        
        while heap:
            value, index = heapq.heappop(heap)            
            if marked[index]:
                continue            
            score += value           
            # Mark the chosen element and its adjacent elements
            marked[index] = True
            if index - 1 >= 0:
                marked[index - 1] = True
            if index + 1 < n:
                marked[index + 1] = True
        
        return score 
            
        