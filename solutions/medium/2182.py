#Problem 2182: Construct String With Repeat Limit

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        count = Counter(s)
        heap = [(-ord(c), c) for c in count]
        heapq.heapify(heap)
        
        result = []
        while heap:
            neg_ascii, char = heappop(heap)
            times = min(repeatLimit, count[char])
            
            # If result is not empty and last char is same as current
            if result and result[-1] == char:
                if len(heap) == 0:  # No other chars available
                    break
                    
                # Get next largest char
                next_neg_ascii, next_char = heappop(heap)
                result.append(next_char)
                count[next_char] -= 1
                if count[next_char] > 0:
                    heappush(heap, (next_neg_ascii, next_char))
                heappush(heap, (neg_ascii, char))  # Put back current char
                
            else:
                # Add current char up to repeat limit
                result.extend([char] * times)
                count[char] -= times
                if count[char] > 0:
                    heappush(heap, (neg_ascii, char))
        
        return ''.join(result)