import glob
import re
import numpy as np

# Function to extract runtimes from a text file
def extract_runtimes_from_text(file_path):
    runtimes = []
    with open(file_path, 'r') as file:
        for line in file:
            if '"total_runtime(ms)":' in line:
                # Extract the number after "total_runtime(ms)":
                match = re.search(r'"total_runtime\(ms\)": (\d+)', line)
                if match:
                    runtimes.append(int(match.group(1)))
    return runtimes

# Function to calculate average and standard deviation for each text file
def calculate_runtime_stats(file_pattern):
    files = glob.glob(file_pattern)
    stats = {}

    for file in files:
        runtimes = extract_runtimes_from_text(file)
        avg_runtime = np.mean(runtimes) if runtimes else 0
        std_dev_runtime = np.std(runtimes) if runtimes else 0
        stats[file] = (avg_runtime, std_dev_runtime)

    return stats

# Specify the path to the text files
file_pattern = "results_third_comp_m1000_V2/*.txt"  # Update this path as needed
stats = calculate_runtime_stats(file_pattern)

# Print the average runtime and standard deviation for each file
for file_name, (avg, std_dev) in stats.items():
    variable_name = file_name.split('/')[-1].replace('.txt', '')
    print(f"{variable_name} average runtime: {avg:.2f} ms, standard deviation: {std_dev:.2f} ms")
