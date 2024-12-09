#Problem 420: Strong Password Checker

class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        def missing_types(s):
            types = 0
            if not any(c.islower() for c in s): types += 1
            if not any(c.isupper() for c in s): types += 1
            if not any(c.isdigit() for c in s): types += 1
            return types
        
        n = len(password)
        missing = missing_types(password)
        
        # Case 1: Length < 6
        if n < 6:
            # Return max of: chars needed for min length, or missing types
            return max(6 - n, missing)
        
        # Count repeating sequences
        replace = 0  # Count of replacements needed for repeating chars
        one = 0      # Count of repeating sequences with len % 3 == 0
        two = 0      # Count of repeating sequences with len % 3 == 1
        i = 2
        while i < n:
            if password[i] == password[i-1] == password[i-2]:
                length = 2
                while i < n and password[i] == password[i-1]:
                    length += 1
                    i += 1
                replace += length // 3
                if length % 3 == 0: one += 1
                elif length % 3 == 1: two += 1
            else:
                i += 1
        
        # Case 2: Length <= 20
        if n <= 20:
            return max(missing, replace)
        
        # Case 3: Length > 20
        delete = n - 20
        
        # Try to use deletions to reduce replacements needed
        replace -= min(delete, one)
        replace -= min(max(delete - one, 0), two * 2) // 2
        replace -= max(delete - one - 2 * two, 0) // 3
        
        return delete + max(missing, replace)