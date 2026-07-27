class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # O que fazer no caso (0, 0)?
        # Arestas negativas? Arestas com peso igual? Arestas com peso máximo?
        # Como calcular a distância?
        # Como ligar os pontos?
        
        # Happy path: [[0,0],[2,2],[3,3],[2,4],[4,2]]
        # Edge case: Identical weights - [[0,0], [0,1], [0,2], [0, 3]]

        def calculate_weight(p1: List[int], p2: List[int]) -> int:
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        def connect_points(p1: int, p2: int) -> List[int]:
            """Create a weighted undirected edge by connecting p1 and p2"""
            return [calculate_weight(points[p1], points[p2]), p1, p2]
        
        def build_graph() -> dict[List[int]]:
            g = collections.defaultdict(list)
            for i in range(len(points)):
                for j in range (i+1, len(points)):
                    edge = connect_points(i, j)
                    g[edge[1]].append((edge[0], edge[2]))
                    g[edge[2]].append((edge[0], edge[1]))
            
            return g
        
        def prim(g: dict[List[int]], src: int, points: List[List[int]]) -> int:
            visited = set()
            heap = [(0, src)]
            res = 0
            while len(visited) < len(points):
                curr_cost, curr = heapq.heappop(heap)
                if curr in visited:
                    continue
                
                res += curr_cost
                visited.add(curr)

                for weight, neigh in g[curr]:
                    if neigh not in visited:
                        heapq.heappush(heap, (weight, neigh))

            return res

        g = build_graph()
        return prim(g, 0, points)
