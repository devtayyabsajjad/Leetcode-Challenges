class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        """
        Function to calculate the maximum beauty of an array
        after applying operations with a given range limit k.
        """
        # Step 1: Define the range for each number
        # Each number can be replaced within the range [num - k, num + k]
        ranges = [(num - k, num + k) for num in nums]

        # Step 2: Collect all range boundaries for efficient calculation
        boundaries = []
        for r in ranges:
            boundaries.append((r[0], 'start'))  # Mark the start of a range
            boundaries.append((r[1] + 1, 'end'))  # Mark the end of a range (+1 for inclusivity)

        # Step 3: Sort the boundaries
        # Sorting ensures we process ranges in the correct order
        boundaries.sort()

        # Step 4: Find the maximum overlap (maximum beauty)
        max_beauty = 0
        current_overlap = 0

        for boundary, kind in boundaries:
            if kind == 'start':
                current_overlap += 1  # A new range starts, increase overlap
            else:
                current_overlap -= 1  # A range ends, decrease overlap

            # Update max_beauty with the maximum overlap seen so far
            max_beauty = max(max_beauty, current_overlap)

        return max_beauty