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

cycle = [
    {'ville': 'Alger', 'passage': 0},
    {'ville': 'Annaba', 'passage': 0},
    {'ville': 'Tizi', 'passage': 0},
    {'ville': 'Bejaya', 'passage': 0},
    {'ville': 'Oran', 'passage': 0},
    {'ville': 'Guelma', 'passage': 0},
    {'ville': 'Setif', 'passage': 0}
]

def visualize():
    # Create a directed graph
    G = nx.Graph()

    # Add nodes and edges to the graph
    for city, distances in distances_dict.items():
        G.add_node(city)
        for i, distance in enumerate(distances):
            if distance != -1 and distance != 0:
                G.add_edge(city, list(distances_dict.keys())[i], weight=distance)

    # Plot the graph
    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=8, font_color='black', font_weight='bold', edge_color='gray')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.show()

unique_numbers = random.sample(range(1, 8), 7)

def generateSol(n):
    unique_numbers = [n]

    while len(unique_numbers) < 6:
        number = random.randint(1, 8)
        if number != 4 and number not in unique_numbers:
            unique_numbers.append(number)

    unique_numbers.append(n) 
    return unique_numbers


def verifDistance():

    Tdistance = 0
    for i, c, cycle in enumerate(cycle):
        if c[i]['passage'] > 0:
            return 'not a cycle'
        else:
            c[i]['passage'] = 1
            Tdistance = Tdistance + distances_dict[c[i]['ville'][i]]

    return Tdistance


generateSol(4)