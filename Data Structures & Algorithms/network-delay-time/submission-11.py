class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Proposal:
        # 1. Build graph
        # 2. Run Dijkstra until all nodes are visited (len(visited) == n)
        # 3. Return the total cost of the path or -1 if len(visited) < n
        
        # Questions
        # - Should we care about cycles?
        # - Are there negative weights?
        
        g = collections.defaultdict(list)
        for src, dst, time in times:
            g[src].append((dst, time))
            
        visited = set()
        heap = [(0, k)]
        res = 0

        while heap:
            curr_time, curr = heapq.heappop(heap)
            if curr in visited: 
                continue

            visited.add(curr)
            res = curr_time
            
            for dst, t in g[curr]:
                if dst not in visited:
                    heapq.heappush(heap, (t + curr_time, dst))

        return res if len(visited) == n else -1

                


                