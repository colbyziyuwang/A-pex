import subprocess

# Path to the file containing random pairs
pairs_file = 'resources/ev_dataset_large/random_pairs.txt'

# Path to the commands file
commands_file = 'exp_commands_large.txt'

# Read pairs from file
with open(pairs_file, 'r') as f:
    pairs = [line.strip().split(' ') for line in f.readlines()]

# Read commands from the commands file
with open(commands_file, 'r') as f:
    commands = [line.strip() for line in f.readlines()]

# Run commands for each scale and pair
scales = [1, 2, 3, 4, 5]
for scale in scales:
    modified_file = f'resources/ev_dataset_large/USA-road-c-0.5-scale-{scale}.BAY.gr'
    log_file_name = f'results_scale/log_scale_{scale}.txt'  # Unique log file name based on p value
        
    for i, (start, goal) in enumerate(pairs):
        for command in commands:
            # Replace the original file path with the modified file path
            updated_command = command.replace('resources/ev_dataset_large/USA-road-c.BAY.gr', modified_file)
            # Replace placeholders for start (-s) and goal (-g)
            updated_command = updated_command.replace('-s 0', f'-s {start}').replace('-g 25000', f'-g {goal}')
                
            # Change the --logging_file to a unique name based on p
            updated_command = updated_command.replace('--logging_file file.txt', f'--logging_file {log_file_name}')
                
            # Print the command to verify
            # print(f"Running command for scale={scale}, pair {i + 1}: {updated_command}")
                
            # Execute the command
            subprocess.run(updated_command, shell=True)

print("All commands have been executed.")
