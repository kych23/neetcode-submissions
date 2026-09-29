# From nodes and edges, build a dictionary 
# { nodes: [outgoing edge nodes]}
# For each node, compute DFS
# When DFS completes, add +1 to num_connected_components

import collections

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodes = collections.defaultdict(list)
        for source, sink in edges:
            nodes[source].append(sink)
            nodes[sink].append(source)
        
        conn_comp = 0
        visited = set()

        for node in range(n):
            if node in visited:
                continue

            stack = [node]

            while stack:
                current_node = stack.pop()
                if current_node in visited:
                    continue

                visited.add(current_node)
                neighbors = nodes[current_node]

                for neighbor in neighbors:
                    if neighbor not in visited:
                        stack.append(neighbor)
            conn_comp += 1

        return conn_comp


