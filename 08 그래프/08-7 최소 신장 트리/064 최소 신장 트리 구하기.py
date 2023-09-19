import sys
from queue import PriorityQueue
sys.setrecursionlimit(10*6)
input = sys.stdin.readline

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]
        
def union(a, b):
    a = find(a)
    b = find(b)
    
    if a != b:
        parent[b] = a

v, e = map(int, input().split())
edges = PriorityQueue()
parent = [i for i in range(v+1)]
count = 0
result = 0

for i in range(e):
    a, b, w = map(int, input().split())
    edges.put((w, a, b))
    
while count < v-1:
    w, a, b = edges.get()
    if find(a) != find(b):
        union(a, b)
        result += w
        count += 1

print(result)
