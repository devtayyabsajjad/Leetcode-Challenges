class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        que = len(queries)
        res = [-1] * que
        for idx, q in enumerate(queries):
            left, right = sorted(q)
            if left == right or heights[right] > heights[left]:
                res[idx] = right
            else:
                h = max(heights[left], heights[right])
                d[right].append((h, idx))
        min_heap = []
        for idx, h in enumerate(heights):
            for queri_h, queri_idx in d[idx]:
                heapq.heappush(min_heap, (queri_h, queri_idx))

            while min_heap and h > min_heap[0][0]:
                queri_h, queri_idx = heapq.heappop(min_heap)
                res[queri_idx] = idx
        return res
 
        