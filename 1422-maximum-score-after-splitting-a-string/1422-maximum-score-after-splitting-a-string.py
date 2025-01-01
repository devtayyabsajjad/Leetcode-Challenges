
class Solution:
    def maxScore(self, s: str) -> int:
        total_ones = s.count('1')  # Total number of ones in the string
        count_zeros = 0  # Count of zeros in the left substring
        count_ones = total_ones  # Count of ones in the right substring
        max_score = -1  # Initialize max score
        
        # Iterate through the string, skipping the last character to ensure two non-empty substrings
        for i in range(len(s) - 1):
            if s[i] == '0':
                count_zeros += 1
            else:
                count_ones -= 1
            
            # Calculate the score at the current split
            max_score = max(max_score, count_zeros + count_ones)
        
        return max_score
#1422. Maximum Score After Splitting a String
