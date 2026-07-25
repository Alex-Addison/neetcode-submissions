class Solution {
public:
    int change(int amount, vector<int>& coins) {
        // Use unsigned int to prevent potential overflow on large inputs
        vector<unsigned int> dp(amount + 1, 0);
        dp[0] = 1; 
        
        // Sorting is not strictly necessary for this approach, so we can remove it.

        // 1. Outer loop: Iterate through each coin ONE by ONE.
        for (int i = 0; i < coins.size(); i++) {
            // 2. Inner loop: Update the DP table for the current coin
            for (int j = coins[i]; j <= amount; j++) {
                dp[j] += dp[j - coins[i]];
            }
        }
        
        // Return as int (assuming the final answer fits in standard constraints)
        return dp[amount];
    }
};