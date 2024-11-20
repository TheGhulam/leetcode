#Problem 2516: Take K of Each Character From Left and Right

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        counts = {c: 0 for c in ['a', 'b', 'c']}
        curr = counts.copy()

        for c in s:
            counts[c] += 1

        # Check if we have enough of each character
        if (any(counts[c] < k for c in 'abc')): return -1

        n = len(s)
        l = 0
        max_window = 0

        # Find max window we can exclude
        for r in range(n):
            curr[s[r]] += 1

            # while window contains too many of any character
            while any(curr[c] > counts[c] - k for c in 'abc'):
                curr[s[l]] -= 1
                l += 1

            max_window = max(max_window, r-l+1)

        return n - max_window

if __name__ == '__main__':
    sol = Solution()
    print(sol.takeCharacters("aabcabaca", 2))
    print(sol.takeCharacters("aabaaaacaabc", 2))
    print(sol.takeCharacters("a", 1))
