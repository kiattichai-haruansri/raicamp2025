#define Tree
graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : [],
    'F' : []
}

#define var
start = 'A'
goal = 'B'
frontier = [start]
explored = set()

while len(frontier) > 0: #stop when frontier list empty
    current = frontier.pop() #delete last member in frontier and store in current
    print(current) #print current
    
    if current == goal: #if reach goal
        print("Goal reach")
        break
    
    for neighbor in graph[current]: #when meet many child
        frontier.append(neighbor) #add child to frontier