def numWays(words, target):
    from collections import Counter, defaultdict
    
    MOD = 10**9 + 7
    m, n = len(words), len(words[0])
    
    # Step 1: Preprocess the character counts at each position
    char_count = [defaultdict(int) for _ in range(n)]
    for word in words:
        for j, char in enumerate(word):
            char_count[j][char] += 1
    
    # Step 2: Dynamic Programming
    t_len = len(target)
    dp = [0] * (t_len + 1)
    dp[0] = 1  # Base case: 1 way to form an empty target
    
    for j in range(n):  # Iterate over positions in `words`
        for i in range(t_len - 1, -1, -1):  # Iterate target backwards
            char = target[i]
            if char in char_count[j]:
                dp[i + 1] += dp[i] * char_count[j][char]
                dp[i + 1] %= MOD
    
    return dp[t_len]

# Example Usage
words1 = ["acca", "bbbb", "caca"]
target1 = "aba"
print(numWays(words1, target1))  # Output: 6

words2 = ["abba", "baab"]
target2 = "bab"
print(numWays(words2, target2))  # Output: 4
