from collections import deque

def isBipartite(n, adj):
    dist = [float('inf')] * (n + 1)  # Distance array to store color
    def bfs(start):
        queue = deque([start])
        dist[start] = 0  # Start coloring with 0
        
        while queue:
            now = queue.popleft()
            current_dist = dist[now]
            
            for v in adj[now]:
                if dist[v] == float('inf'):
                    dist[v] = current_dist + 1
                    queue.append(v)
                elif (dist[v] - dist[now]) % 2 == 0:
                    return False  # Found a conflict in coloring
        
        return True

    # Check each component of the graph
    for node in range(1, n + 1):
        if dist[node] == float('inf'):
            if not bfs(node):
                return 0
    
    return 1

if __name__ == '__main__':
    n_vertices, n_edges = map(int, input().split())
    adjacency_list = [[] for _ in range(n_vertices + 1)]
    for _ in range(n_edges):
        a, b = map(int, input().split())
        adjacency_list[a].append(b)
        adjacency_list[b].append(a)
    
    print(isBipartite(n_vertices, adjacency_list))
