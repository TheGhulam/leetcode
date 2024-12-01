#Problem 1346: Check If N and Its Double Exist

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
    
        # Count zeros separately to handle the case where we need two zeros
        zero_count = 0
        
        for num in arr:
            if num == 0:
                zero_count += 1
                # If we've found a second zero, return True
                if zero_count > 1:
                    return True
            else:
                # Check if either double or half exists
                if 2 * num in seen or (num % 2 == 0 and num // 2 in seen):
                    return True
                seen.add(num)
        
        return False