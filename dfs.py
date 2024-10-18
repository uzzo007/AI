graph={"Devgarh" : ["kankauli","malvan"],
              "kankauli" : ["Devgarh","malvan","kudal"],
              "malvan" : ["Devgarh","kankauli","kudal","vengurla"],
              "kudal" : ["kankauli","vengurla","malvan","sawantwadi"],
              "vengurla" : ["malvan","sawantwadi","kudal"],
              "sawantwadi" : ["kudal","vengurla"]}
visited=[]
node="Devgarh"
def dfs(node,visited,graph):
    if node not in visited:
      print(node)
      visited.append(node)
      for i in graph[node]:
         dfs(i,visited,graph)
print("Following is the Depth-First Search")
dfs(node,visited,graph)    
