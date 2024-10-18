import random
def objective_function(x):
    return -x**2 + 4*x
 
def generate_neighbor(current_x,step_size):
    return current_x+random.uniform(-step_size,step_size)
 
def hill_climbing(starting_point,step_size,max_iterations):
    current_x=starting_point
    current_value=objective_function(current_x)
 
    for _ in range(max_iterations):
        neighbor_x=generate_neighbor(current_x,step_size)
        neighbor_value=objective_function(neighbor_x)
 
        if neighbor_value>current_value:
            current_x=neighbor_x
            current_value=neighbor_value
 
    return current_x,current_value
 
starting_point=random.uniform(0,4)
step_size=0.1
max_iterations=100
 
best_x,best_value=hill_climbing(starting_point,step_size,max_iterations)
 
print(f"Best x:{best_x},Best value: {best_value}")
