class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get count_map
        # sort map items via count
        # get the top k

        count_map = {}
        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1

        # arr = []
        # for num, ct in count_map.items():
        #     arr.append([ct, num])
        # arr.sort()

        # sorted_items = sorted(count_map.items(), key=lambda x: x[1])
        min_heap = []
        for num, ct in count_map.items():
            heapq.heappush(min_heap, (ct, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
            
        res = []
        for i in range(k):
            res.append(heapq.heappop(min_heap)[1])

        return res
