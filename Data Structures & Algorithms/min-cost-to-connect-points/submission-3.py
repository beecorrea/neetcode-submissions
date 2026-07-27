class UnionFind:
    def __init__(self, size):
        self.roots = [i for i in range(size)]
        self.rank = [1] * size

    def union(self, u: int, v: int) -> bool:
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return False # Already connected
        
        if self.rank[root_u] < self.rank[root_v]:
            self.roots[root_u] = root_v
        elif self.rank[root_u] > self.rank[root_v]:
            self.roots[root_v] =  root_u
        else:
            self.roots[root_v] = root_u
            self.rank[root_u] += 1
        
        return True

    def find(self, elem: int) -> int:
        """Finds which set this element belongs to."""
        if self.roots[elem] == elem:
            return elem
        
        # Path Compression: update roots for every element.
        # Costs O(V)/O(1) but we only do it once.
        root = self.find(self.roots[elem])
        self.roots[elem] = root
        return root

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
            uf = UnionFind(len(points))
            res = 0

            for weight, u, v in edges:
                if uf.union(u, v):
                    res += weight

            return res

        edges = build_edges()
        return kruskal(edges)
