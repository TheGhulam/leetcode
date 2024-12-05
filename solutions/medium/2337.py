class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if len(start) != len(target): return False
        
        # Step 2: Check if the strings are identical when removing blanks
        if start.replace('_', '') != target.replace('_', ''): return False
        
        n = len(start)
        i = j = 0  # Pointers for start and target strings
        
        # Step 3: Check if movements are possible
        while i < n and j < n:
            # Skip blank spaces
            while i < n and start[i] == '_': i += 1
            while j < n and target[j] == '_': j += 1
                
            # If both pointers are out of bounds, strings match
            if i == n and j == n: return True
                
            # If only one pointer is out of bounds, strings don't match
            if i == n or j == n: return False
                
            # Current characters must match
            if start[i] != target[j]: return False
                
            # Check if movement is possible:
            # For 'L', target position must be <= start position
            if start[i] == 'L' and i < j: return False

            # For 'R', target position must be >= start position
            if start[i] == 'R' and i > j: return False
                
            i += 1
            j += 1
            
        # Make sure we've processed both strings completely
        while i < n:
            if start[i] != '_': return False
            i += 1
        while j < n:
            if target[j] != '_': return False
            j += 1
            
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.canChange("R____", "____R"))  # True
    print(s.canChange("L____", "____R"))  # False
    print(s.canChange("_L__R__R_", "L______RR")) # True