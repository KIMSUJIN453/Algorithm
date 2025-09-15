from collections import deque

def dfs(v, visited, graph):
    visited[v] = True
    print(v, end=' ')
    for neighbor in sorted(graph[v]):
        if not visited[neighbor]:
            dfs(neighbor, visited, graph)

def bfs(v, visited, graph):
    queue = deque([v])
    visited[v] = True

    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for neighbor in sorted(graph[node]):
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

# 입력 처리
N, M, V = map(int, input().split())
graph = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# DFS
dfs_visited = [False] * (N + 1)
dfs(V, dfs_visited, graph)
print()

# BFS
bfs_visited = [False] * (N + 1)
bfs(V, bfs_visited, graph)