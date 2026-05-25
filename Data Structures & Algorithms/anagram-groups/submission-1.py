class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = defaultdict(list)

        for cur_str in strs:
            count = [0] * 26
            for c in cur_str:
                count[ord(c) - ord('a')] += 1
            str_map[tuple(count)].append(cur_str)

        return list(str_map.values())