import random
import os

def generate_random_pairs(nodes, num_pairs=100):
    """
    Generates random (start, goal) pairs from a list of nodes.

    Parameters:
    - nodes (list): List of nodes in the graph.
    - num_pairs (int): Number of random (start, goal) pairs to generate.

    Returns:
    - list: List of tuples representing (start, goal) pairs.
    """
    random_pairs = []
    for _ in range(num_pairs):
        start, goal = random.sample(nodes, 2)  # Randomly select two different nodes
        random_pairs.append((start, goal))
    
    return random_pairs

# Generate pairs
nodes = [i for i in range(1, 321270)] 
random_pairs = generate_random_pairs(nodes, num_pairs=100)

# Print the first 5 pairs to check
print(random_pairs[:5])

# Save it to a file (resources/ev_dataset_large/)
dir_path = 'resources/ev_dataset_large'

# Save the pairs to a text file
file_path = os.path.join(dir_path, 'random_pairs.txt')
with open(file_path, 'w') as f:
    for pair in random_pairs:
        f.write(f"{pair[0]} {pair[1]}\n")

# Output the path to the saved file
print(file_path)
