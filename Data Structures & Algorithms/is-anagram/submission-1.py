class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map_s = dict()
        map_t = dict()

        # Compute frequency map
        for c in range(len(s)):
            map_s[s[c]] = 1 + map_s.get(s[c], 0)
            map_t[t[c]] = 1 + map_t.get(t[c], 0)

        return map_s == map_t