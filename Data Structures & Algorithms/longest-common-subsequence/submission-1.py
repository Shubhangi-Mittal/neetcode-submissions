# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         dp = [[0 for j in range(len(text2) + 1)]
#                 for i in range(len(text1) + 1)]

#         for i in range(len(text1) -1, -1, -1):
#             for j in range(len(text2) -1, -1, -1):
#                 if text1[i] == text2[j]:
#                     dp[i][j] = 1 + dp[i+1][j+1]
#                 else:
#                     dp[i][j] = max(dp[i][j+1], dp[i+1][j])
#         return dp[0][0]

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        next_row = [0] * (len(text2) + 1)

        for i in range(len(text1) - 1, -1, -1):
            current_row = [0] * (len(text2) + 1)
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    current_row[j] = 1 + next_row[j + 1]
                else:
                    current_row[j] = max(current_row[j + 1], next_row[j])
            next_row = current_row  # Move up to the next iteration
            
        return next_row[0]
