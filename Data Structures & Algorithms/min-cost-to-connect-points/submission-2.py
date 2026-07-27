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
        
        def build_edges() -> List[List[int]]:
            edges = []
            for i in range(len(points)):
                for j in range (i+1, len(points)):
                    edge = connect_points(i, j)
                    edges.append(edge)
            edges.sort()
            return edges
        
        def kruskal(edges: List[List[int]]) -> int:
            sets = [i for i in range(len(points))]
            res = 0

            for weight, u, v in edges:
                if sets[u] == sets[v]:
                    continue

                res += weight
                og_set = sets[u]
                for i in range(len(points)):
                    if sets[i] == og_set:
                        sets[i] = sets[v]

            return res

        edges = build_edges()
        return kruskal(edges)
