class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for w in strs:
            key = [0]*26
            for c in range(len(w)):
                key[ord(w[c])-ord("a")] += 1
            group[tuple(key)].append(w)
        return list(group.values())
        