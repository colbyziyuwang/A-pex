import glob
import re

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

# Function to calculate average runtime for each text file
def calculate_average_runtime(file_pattern):
    files = glob.glob(file_pattern)
    averages = {}

    for file in files:
        runtimes = extract_runtimes_from_text(file)
        avg_runtime = sum(runtimes) / len(runtimes) if runtimes else 0
        averages[file] = avg_runtime

    return averages

# Specify the path to the text files
file_pattern = "results_large/*.txt"  # Update this path as needed
averages = calculate_average_runtime(file_pattern)

# Print the average runtime for each file
for file_name, avg in averages.items():
    variable_name = file_name.split('/')[-1].replace('.txt', '')
    print(f"{variable_name} average runtime: {avg:.2f} ms")
