import math

# Function to compute the third cost using a two-sided logarithmic penalty
def compute_third_cost(distance, leads_to_charging_station, m=2000, penalty=20):
    base_cost = math.log(1 + abs(distance - m))
    if leads_to_charging_station:
        return base_cost
    else:
        return base_cost + penalty

def compute_third_costV2(distance, leads_to_charging_station, m=2000, penalty=20):
    base_cost = math.log(1 + distance - m) if distance >= m else 0
    if leads_to_charging_station:
        return base_cost
    else:
        return base_cost + penalty

# Paths to input files
dist_file_path = "resources/ev_dataset_large/USA-road-d.BAY.gr"
charge_file_path = "resources/ev_dataset_large/USA-road-c-0.5.BAY.gr"
output_file_path = "resources/ev_dataset_large/USA-road-third_m2000.BAY.gr"

# Open all three files simultaneously and process line by line
with open(dist_file_path, 'r') as dist_file, \
     open(charge_file_path, 'r') as charge_file, \
     open(output_file_path, 'w') as output_file:
    
    for dist_line, charge_line in zip(dist_file, charge_file):
        # Copy headers directly
        if dist_line.startswith('c') or dist_line.startswith('p'):
            output_file.write(dist_line)
            continue

        # Process only edge lines
        if dist_line.startswith('a') and charge_line.startswith('a'):
            _, u_dist, v_dist, dist_cost = dist_line.split()
            _, u_charge, v_charge, charge_cost = charge_line.split()
            
            # Ensure the edges match in both files
            if (u_dist, v_dist) == (u_charge, v_charge):
                dist_cost = int(dist_cost)
                leads_to_charging_station = int(charge_cost) == 0
                third_cost = compute_third_costV2(dist_cost, leads_to_charging_station)
                
                # Write the edge with the third cost component
                output_file.write(f"a {u_dist} {v_dist} {int(third_cost)}\n")

print("Third cost component file created successfully.")
