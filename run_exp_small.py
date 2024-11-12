import subprocess

# Path to the file containing random pairs
pairs_file = 'resources/ev_dataset_small/random_pairs.txt'

# Path to the commands file
commands_file = 'exp_commands_small.txt'

# Read pairs from file
with open(pairs_file, 'r') as f:
    pairs = [line.strip().split(' ') for line in f.readlines()]

# Read commands from the commands file
with open(commands_file, 'r') as f:
    commands = [line.strip() for line in f.readlines()]

# Run commands for each pair
for i, (start, goal) in enumerate(pairs):
    for command in commands:
        # Replace placeholders for start (-s) and goal (-g)
        updated_command = command.replace('-s 0', f'-s {start}').replace('-g 25000', f'-g {goal}')
        
        # Print the command to verify
        # print(f"Running command for pair {i + 1}: {updated_command}")
        
        # Execute the command
        subprocess.run(updated_command, shell=True)

print("All commands have been executed.")

