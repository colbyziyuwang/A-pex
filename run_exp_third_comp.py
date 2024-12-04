import subprocess

# Path to the file containing random pairs
pairs_file = 'resources/ev_dataset_large/random_pairs.txt'

# Path to the commands file
commands_file = 'exp_commands_third_compV2.txt'

# Value of m
m_vals = [2000, 1000]

for m in m_vals:
    # Read pairs from file
    with open(pairs_file, 'r') as f:
        pairs = [line.strip().split(' ') for line in f.readlines()[:25]]  # Use only the first 25 pairs

    # Read commands from the commands file
    with open(commands_file, 'r') as f:
        commands = [line.strip() for line in f.readlines()]

    # Update the file name based on the value of m
    updated_file_name = f'resources/ev_dataset_large/USA-road-third_m{m}_V2.BAY.gr'
    log_file_prefix = f'results_third_comp_m{m}_V2'

    # Run commands for each pair
    for i, (start, goal) in enumerate(pairs):
        for command in commands:
            # Replace the placeholder file path with the updated file name
            updated_command = command.replace('resources/ev_dataset_large/USA-road-thirdV2.BAY.gr', updated_file_name)
            
            # Replace placeholders for start (-s) and goal (-g)
            updated_command = updated_command.replace('-s 0', f'-s {start}').replace('-g 25000', f'-g {goal}')
            
            # Update the logging file path to include the value of m
            updated_command = updated_command.replace(
                '--logging_file results_third_compV2/',
                f'--logging_file {log_file_prefix}/'
            )
            
            # Print the command to verify
            # print(f"Running command for pair {i + 1}: {updated_command}")
            
            # Execute the command
            subprocess.run(updated_command, shell=True)

    print("All commands have been executed.")
