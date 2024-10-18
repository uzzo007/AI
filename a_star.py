import heapq
def a_star(graph,heuristics,start,goal):
    open_list=[]
    heapq.heappush(open_list,(heuristics.get(start),0,start,[]))
    came_from={}
    cost_so_far={start:0}
    while open_list:
        f,current_cost,current_node,path=heapq.heappop(open_list)
        if current_node==goal:
            return path+[current_node]
        for neighbor,cost in graph.get(current_node,{}).items():
            new_cost=current_cost+cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor]=new_cost
                priority=new_cost+heuristics.get(neighbor)
                heapq.heappush(open_list,(priority,new_cost,neighbor,path+[current_node]))
                came_from[neighbor]=current_node
    return None
graph={ 'A':{'B':1,'C':4}, 'B':{'C':2,'D':5}, 'C':{'D':1}, 'D':{} }
heuristics={ 'A':7,'B':6,'C':2,'D':0}
start_node='A'
goal_node='D'
path=a_star(graph,heuristics,start_node,goal_node)
if path:
    print("Path found : ",path)
else:
    print("No path found")
