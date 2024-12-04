# Read the original graph file and create modified versions with different scales for absence of charging station
input_file = 'resources/ev_dataset_large/USA-road-c-0.5.BAY.gr'

for s in range(1, 6):  # s = 1, 2, 3, 4, 5
    output_file = f'resources/ev_dataset_large/USA-road-c-0.5-scale-{s}.BAY.gr'
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if line.startswith('a '):  # Only modify edge lines
                parts = line.split()
                u, v, cost = int(parts[1]), int(parts[2]), int(parts[3])
                
                # Check if the edge leads to a charging station (cost 0 indicates it does)
                if cost != 0:  
                    cost = s  # Assign new cost for not leading to a charging station
                
                # Write the modified edge line
                outfile.write(f'a {u} {v} {cost}\n')
            else:
                # Copy non-edge lines as-is
                outfile.write(line)

print("Graph files with modified costs created.")

