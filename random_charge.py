import random

# Function to read the file and determine the number of nodes
def get_num_nodes(input_file):
    max_node = 0
    with open(input_file, 'r') as infile:
        for line in infile:
            if line.startswith('a'):
                parts = line.split()
                u = int(parts[1])
                v = int(parts[2])
                max_node = max(max_node, u, v)
    return max_node

# Function to create an array indicating if a node has a charging station
def create_charging_stations(num_nodes, p):
    return [1 if random.random() < p else 0 for _ in range(num_nodes + 1)]  # Nodes are 1-indexed

# Function to modify edge costs in the file based on charging station presence
def modify_graph_file(input_file, output_file, charging_stations):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if line.startswith('c') or line.startswith('p'):
                outfile.write(line)  # Copy comment and problem definition lines as is
            elif line.startswith('a'):
                parts = line.split()
                u = int(parts[1])
                v = int(parts[2])
                cost = int(parts[3])
                
                # Modify cost based on whether the destination node has a charging station
                if charging_stations[v] == 1:
                    new_cost = 0  # Edge leads to a charging station
                else:
                    new_cost = 1  # Edge does not lead to a charging station
                
                # Write the modified edge line to the output file
                outfile.write(f"a {u} {v} {new_cost}\n")
            else:
                outfile.write(line)  # Copy any other lines as is

# Parameters
input_file = 'resources/ev_dataset_large/USA-road-d.BAY.gr'  # Input graph file
output_file = 'resources/ev_dataset_large/USA-road-c-0.2.BAY.gr'  # Output graph file
p = 0.2  # Probability of a node having a charging station

# Get the number of nodes dynamically from the file
num_nodes = get_num_nodes(input_file)

# Create an array indicating if a node has a charging station
charging_stations = create_charging_stations(num_nodes, p)

# Modify the graph file based on the charging stations
modify_graph_file(input_file, output_file, charging_stations)

print("Graph modification completed.")

