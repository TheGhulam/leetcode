#Problem 940: Distinct Subsequences II

class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7

        dp = [1]
        last_occ = {}

        for i, c in enumerate(s):
            current = dp[-1]

            new_count = (current * 2) % MOD

            if c in last_occ:
                j = last_occ[c]
                new_count = (new_count - dp[j]) % MOD
            
            dp.append(new_count)
            last_occ[c] = i

        return (dp[-1]-1)% MOD