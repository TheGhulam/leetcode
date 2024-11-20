#Problem 2343: Query Kth Smallest Trimmed Number

# class Solution:
#     def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
#         def query(k: int, t: int) -> int:
#             trimmed = [(num[-t:], i) for i, num in enumerate(nums)]
#             trimmed.sort(key=lambda x:(x[0], x[1]))
#             _, i = trimmed[k-1]
#             return i

#         return [query(k, t) for k, t in queries]



class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        m = len(nums[0])

        # Position mapping
        pmap = {}  # {trim_length: [(num, original_index), ...]}

        currp = list(range(n))

        for t in range(1, m+1):
            # Counting sort
            count = [[] for _ in range(10)] #Buckets

            for idx in currp:
                digit = int(nums[idx][m-t])
                count[digit].append(idx)
            
            # Flatten buckets to get new position array
            newp = []
            for bucket in count:
                newp.extend(bucket)
            
            pmap[t] = newp.copy()
            currp = newp

        o = []
        for k, trim in queries:
            o.append(pmap[trim][k-1])

        return o