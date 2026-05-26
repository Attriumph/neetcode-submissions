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

        sorted_items = sorted(count_map.items(), key=lambda x: x[1])

        res = []
        while len(res) < k:
            res.append(sorted_items.pop()[0])

        return res
