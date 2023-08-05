from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        while queue:
            node = queue.popleft()
            if node not in visited:
                print(node, end=' ')
                visited.add(node)
                queue.extend(self.graph[node])
    
    def dfs(self, node, visited):
        visited.add(node)
        print(node, end=' ')
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)
    
    def count_nodes_at_level(self, start, level):
        visited = set()
        queue = deque([(start, 0)])
        count = 0
        while queue:
            node, current_level = queue.popleft()
            if current_level == level:
                count += 1
            if current_level > level:
                break
            visited.add(node)
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, current_level + 1))
        return count
    
    def count_trees_in_forest(self):
        visited = set()
        count = 0
        for node in self.graph:
            if node not in visited:
                self._dfs_count_trees(node, visited)
                count += 1
        return count
    
    def _dfs_count_trees(self, node, visited):
        visited.add(node)
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self._dfs_count_trees(neighbor, visited)
    
    def is_cyclic_util(self, node, visited, rec_stack):
        visited.add(node)
        rec_stack.add(node)
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                if self.is_cyclic_util(neighbor, visited, rec_stack):
                    return True
            elif neighbor in rec_stack:
                return True
        rec_stack.remove(node)
        return False
    
    def is_cyclic(self):
        visited = set()
        rec_stack = set()
        for node in self.graph:
            if node not in visited:
                if self.is_cyclic_util(node, visited, rec_stack):
                    return True
        return False

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Breadth First Traversal:")
g.bfs(2)
print("\nDepth First Traversal:")
g.dfs(2, set())
print("\nCount nodes at level 2:", g.count_nodes_at_level(2, 2))
print("\nCount trees in forest:", g.count_trees_in_forest())
print("\nCycle detection:", g.is_cyclic())
