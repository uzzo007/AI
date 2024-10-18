import constraint
import matplotlib.pyplot as plot
import networkx as nx
problem = constraint.Problem()
regions = ['Devgad', 'Malvan', 'Vaibhavwadi', 'Kankavli', 'Kudal', 'Vengurla', 'Sawantwadi','Dodamarg']
colors = ['White', 'Green', 'Blue','Orange','Yellow','Pink','Cyan']
for region in regions:
    problem.addVariable(region, colors)
sindhudurg = {
    'Devgad': ['Kankavli', 'Malvan'],
    'Malvan': ['Devgad', 'Kankavli', 'Kudal', 'Vengurla'],
    'Vaibhavwadi': ['Kankavli'],
    'Kankavli': ['Vaibhavwadi', 'Devgad', 'Malvan','Kudal'],
    'Kudal': ['Kankavli', 'Malvan', 'Vengurla','Sawantwadi'],
    'Vengurla': ['Malvan', 'Kudal','Sawantwadi'],
    'Sawantwadi': ['Vengurla','Kudal','Dodamarg'],
    'Dodamarg':['Sawantwadi']
}
for region, adjacent in sindhudurg.items():
    for neighbor in adjacent:
        problem.addConstraint(lambda R,N : R!=N,(region, neighbor))
solution = problem.getSolution()
print(solution)
group=nx.Graph(sindhudurg)
nx.draw(group,with_labels=True,node_color="white",font_color="black")
plot.show()
