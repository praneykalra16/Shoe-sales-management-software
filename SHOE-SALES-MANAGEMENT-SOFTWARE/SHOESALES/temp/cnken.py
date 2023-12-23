MOD = 10**9 + 7

def countValidPasswords(n, k):
    # Initialize a 2D array to store the valid password counts
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    # Initialize the base cases
    dp[0][0] = 1

    # Fill in the dynamic programming table
    for i in range(1, n + 1):
        for j in range(k + 1):
            dp[i][j] = (dp[i - 1][j] * 25) % MOD
            if j > 0:
                dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % MOD

    # Calculate the total number of valid passwords
    total_valid_passwords = (pow(26, n, MOD) - sum(dp[n][j] for j in range(k + 1))) % MOD

    return total_valid_passwords

# Sample input and output
print(countValidPasswords(3, 2))  # Output: 16250
