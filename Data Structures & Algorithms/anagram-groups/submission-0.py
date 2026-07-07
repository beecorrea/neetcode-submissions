class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. Hashmap from a set of characters to a list of words
        # 2. For each word, turn it into a set of chars and look it up.
        # 3. If the word is there, add it to its list.
        # 4. If the word is not there, initialize a list and add the word.
        # 4. In the end, return all values as a list.
        # Time Complexity: O(m*n)
        # Space Complexity: O(m)

        lookup = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            lookup[tuple(count)].append(word)
            
        return list(lookup.values())
