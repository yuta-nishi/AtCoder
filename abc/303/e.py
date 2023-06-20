import collections


def main() -> None:
    N = int(input())
    graph = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, N + 1):
        if len(graph[i]) == 1:
            root = i
            break

    visited = [False] * (N + 1)
    queue = collections.deque()
    queue.append([root, 0])
    visited[root] = True
    res = []

    while queue:
        node, depth = queue.popleft()
        if depth % 3 == 1 and len(graph[node]) > 1:
            res.append(len(graph[node]))

        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append([next_node, depth + 1])

    res.sort()
    print(*res)


if __name__ == "__main__":
    main()
