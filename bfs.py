from collections import deque

def bfs(graph, start):
    
    visited = set()  
    queue = deque([start])  
    result = []  
    
    while queue:
        
        current = queue.popleft()
        
        if current not in visited:
            visited.add(current)  
            result.append(current) 
            
            
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)
    
return result
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    start_node = 'A'
    print("BFS Traversal:", bfs(graph, start_node))
