import queue

def DFS(node):
    global Windows
    global arr
    global N
    print(node, end = ' ')
    Windows[node] = True
    for i in range(1, N+1):
        if (arr[node][i] == 1) and (Windows[i] == False):
            DFS(i)

def BFS(node):
    global Windows
    global arr
    global N
    q = queue.Queue()
    Windows[node] = True
    q.put(node)
    while q.qsize() > 0:
        tmp = q.get()
        print(tmp, end = ' ')
        for i in range(1, N+1):
            if (arr[tmp][i] == 1) and (Windows[i] == False):
                q.put(i)
                Windows[i] = True
        
    


N, M, V = map(int, input().split())
arr = [[0 for i in range(N+1)] for i in range (N+1)]
Windows = [False for i in range(N+1)]
for i in range(M):
    A, B = map(int, input().split())
    arr[A][B] = 1
    arr[B][A] = 1

DFS(V)
Windows = [False for i in range(N+1)]
print()
BFS(V)