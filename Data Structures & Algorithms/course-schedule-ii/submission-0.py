class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        nodes = [ [] for i in range(numCourses) ]
        for a, b in prerequisites:
            nodes[a].append(b)

        visited = set()
        cycle = set()
        output = []

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            
            cycle.add(course)
            for pre in nodes[course]:
                if not dfs(pre):
                    return False
            
            cycle.remove(course)
            visited.add(course)
            output.append(course)
            return True

        for i in range(numCourses):
            if dfs(i) == False:
                return []
        
        return output

        
