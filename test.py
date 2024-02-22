import matplotlib.pyplot as plt
import networkx as nx
import random


distanceTotale = 0
distances_dict = {
    'Alger': [0, -1, -1, -1, -1, -1, -1],
    'Annaba': [40, 0, -1, -1, -1, -1, -1],
    'Tizi': [5, 32, 0, -1, -1, -1, -1],
    'Bejaya': [10, 29, 5, 0, -1, -1, -1],
    'Oran': [30, 85, 38, 42, 0, -1, -1],
    'Galma': [43, 5, 35, 29, 82, 0, -1],
    'Settif': [20, 22, 17, 11, 58, 21, 0]
}

distances = [
    [0, -1, -1, -1, -1, -1, -1],
    [40, 0, -1, -1, -1, -1, -1],
    [5, 32, 0, -1, -1, -1, -1],
    [10, 29, 5, 0, -1, -1, -1],
    [30, 85, 38, 42, 0, -1, -1],
    [43, 5, 35, 29, 82, 0, -1],
    [20, 22, 17, 11, 58, 21, 0]
]


def visualize():
    
    G = nx.Graph()

    
    for city, distances in distances_dict.items():
        G.add_node(city)
        for i, distance in enumerate(distances):
            if distance != -1 and distance != 0:
                G.add_edge(city, list(distances_dict.keys())[i], weight=distance)

    
    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=8, font_color='black', font_weight='bold', edge_color='gray')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.show()

unique_numbers = random.sample(range(0, 6), 6)

def generateSol(n, s):
    unique_numbers = [n]

    while len(unique_numbers) < 6:
        number = random.randint(0, 6)
        if number != s and number not in unique_numbers:
            unique_numbers.append(number)

    unique_numbers.append(n) 
    return unique_numbers





solution = generateSol(4, 4)

def calculate_total_distance(graph, solution):
    total_distance = 0

    for i in range(0, len(solution) - 1):
        current_city = solution[i]
        
        next_city = solution[i + 1]
      
        
        if(graph[current_city][next_city]==-1):
             total_distance += graph[next_city][current_city]
             print(graph[next_city][current_city]) 
        else:
            total_distance += graph[current_city][next_city]
            print(graph[current_city][next_city])

    # Add the distance from the last city back to the starting city
    
    

    return total_distance

def is_valid_solution(graph, solution):
    visited_cities = set()

    for i in range(len(solution) - 1):
        current_city = solution[i]
        next_city = solution[i + 1]

        if current_city == next_city or current_city in visited_cities:
            return False  # City visited twice or self-loop

        visited_cities.add(current_city)

    last_city = solution[-1]
    if last_city != solution[0]:
        print("that is the issue")
        return False 
         # Last city conditions not met

    return True

# Example usage:
generated_solution = generateSol(4, 4)
print("Generated Solution:", generated_solution)

# Assuming distances_dict is the graph representation
if is_valid_solution(distances, generated_solution):
    total_distance = calculate_total_distance(distances, generated_solution)
    print("The solution is valid. Total distance:", total_distance)
else:
    print("The solution is not valid.")
