class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # You basically have to build a graph from a list of edges
        # and check if there are any cycles.
        if numCourses == 1 or not prerequisites:
            return True
        
        # Build graph
        curriculum = dict()
        for i in range(numCourses):
            curriculum[i] = []
        for a, b in prerequisites:
            curriculum[b].append(a)

        path = set()
        def dfs(course: int):
            if course in path:
                # Cycle
                return False
            if not curriculum[course]:
                # End of DFS and no cycle detected.
                return True

            # Visit node
            path.add(course)
            for neigh in curriculum[course]:
                # For each neighbor
                has_cycle = dfs(neigh)
                if not has_cycle:
                    return False
            
            # Remove from path and add to visited
            path.remove(course)
            
            return True
            
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
