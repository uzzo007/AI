graph={"Devgad":["Malvan","Kankavli"],
       "Malvan":["Devgad","Vengurla","Kankavli"],
       "Vengurla":["Malvan","Kudal","Sawantwadi"],
       "Sawantwadi":["Kudal","Vengurla","Dodamarg"],
       "Kudal":["Kankavli","Vengurla","Sawantwadi"],
       "Kankavli":["Kudal","Malvan","Devgad","Vaibhavwadi"],
       "Dodamarg":["Sawantwadi"],
       "Vaibhavwadi":["Kankavli"]}
visited=[]
node="Kudal"
def dfs(node,visited,graph):
    if node not in visited:
        print(node)
        visited.append(node)
        for i in graph[node]:
            dfs(i,visited,graph)
dfs(node,visited,graph)
