class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Initialize the graph as an adjacency list.
        g = dict()
        for w in words:
            for c in w:
                # We can use a set since the order doesn't matter.
                g[c] = set()

        # Builds the topologically sorted graph .
        def compare_word_pairs(w1, w2):
            min_length = min(len(w1), len(w2))
            # Edge case: if w1 is a prefix of w2 but 
            # w1 is bigger than w2.
            if len(w1) > len(w2) and w1[:min_length] == w2[:min_length]:
                return ""
            
            # Add w1[c] as "comes before" w2[c]
            # and then go to the next word pair.
            for i in range(min_length):
                if w1[i] != w2[i]:
                    g[w1[i]].add(w2[i])
                    break
        
        # Build graph while checking for invalid graphs.
        for i in range(len(words) - 1):
            if compare_word_pairs(words[i], words[i+1]) == "":
                return ""

        # We're now going to compute the answer using DFS / Toposort.
        visited = dict()
        alien_letters = [] # Result
        def dfs(c):
            # If dfs(c) returns True, there's a cycle.
            # If not, we've visited this node previously, but not in the current DFS iteration.
            # So we can return False and then the if in the outer loop will do nothing and go to the next letter.
            if c in visited:
                return visited[c]
            
            visited[c] = True

            for neighbor in g[c]:
                # Can't have loops as that'd make the graph invalid.
                # We return true here so we can check the result outside
                # and return an empty string as asked.
                has_loop = dfs(neighbor) 
                if has_loop:
                    return True
            
            # Mark as unvisited for the next DFS.
            visited[c] = False
            alien_letters.append(c)
        
        # Compute topological sort.
        for c in g:
            if dfs(c):
                return ""

        # Reverse the result to return post-order traversal.
        alien_letters.reverse()
        return "".join(alien_letters)

        
