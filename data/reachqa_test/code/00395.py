import matplotlib.pyplot as plt
import numpy as np

# Define the regions
regions = ['North America', 'Europe', 'Asia-Pacific', 'Latin America', 'Middle East', 'Africa', 'Australia', 'Oceania', 'South America']

# Define the renewable and non-renewable energy production data for each region (in GWh)
energy_production = {
    'North America': {'Renewable': [1500, 1800, 2000, 2200, 2500, 2800, 3000, 3200, 3500, 3800], 
                      'Non-Renewable': [10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000]},
    'Europe': {'Renewable': [2000, 2300, 2500, 2800, 3000, 3200, 3500, 3800, 4100, 4400],
               'Non-Renewable': [8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000]},
    'Asia-Pacific': {'Renewable': [1000, 1200, 1500, 1800, 2000, 2200, 2500, 2800, 3100, 3400],
                    'Non-Renewable': [15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000]},
    'Latin America': {'Renewable': [800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600],
                     'Non-Renewable': [6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000, 10500]},
    'Middle East': {'Renewable': [400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200],
                   'Non-Renewable': [12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000]},
    'Africa': {'Renewable': [200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000],
              'Non-Renewable': [5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500]},
    'Australia': {'Renewable': [300, 500, 700, 900, 1100, 1300, 1500, 1700, 1900, 2100],
                  'Non-Renewable': [3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500]},
    'Oceania': {'Renewable': [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],
                'Non-Renewable': [2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500]},
    'South America': {'Renewable': [250, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000],
                     'Non-Renewable': [4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500]}
}

# Extract renewable and non-renewable energy production data
renewable_data = [values['Renewable'] for values in energy_production.values()]
non_renewable_data = [values['Non-Renewable'] for values in energy_production.values()]

# Create a figure and axis object
fig, ax = plt.subplots(2, figsize=(12, 8))

# Create a box plot for renewable energy production
positions = np.arange(len(regions))
bp_renewable = ax[0].boxplot(renewable_data, positions=positions, vert=True, patch_artist=True, notch=True)

# Set the x-axis ticks and labels
ax[0].set_xticks(positions)
ax[0].set_xticklabels(regions, rotation=45, ha='right')

# Customize the appearance of the boxes
for element in ['boxes', 'whiskers', 'fliers', 'means', 'medians', 'caps']:
    plt.setp(bp_renewable[element], linewidth=2)

# Set box colors
for patch in bp_renewable['boxes']:
    patch.set_facecolor('lightblue')
    patch.set_alpha(0.7)

# Set the title and y-axis label
ax[0].set_title("Renewable Energy Production by Region (GWh)\n2020-2029", fontsize=14)
ax[0].set_ylabel("Renewable Energy Production (GWh)", fontsize=12)

# Create a box plot for non-renewable energy production
positions = np.arange(len(regions))
bp_non_renewable = ax[1].boxplot(non_renewable_data, positions=positions, vert=True, patch_artist=True, notch=True)

# Set the x-axis ticks and labels
ax[1].set_xticks(positions)
ax[1].set_xticklabels(regions, rotation=45, ha='right')

# Customize the appearance of the boxes
for element in ['boxes', 'whiskers', 'fliers', 'means', 'medians', 'caps']:
    plt.setp(bp_non_renewable[element], linewidth=2)

# Set box colors
for patch in bp_non_renewable['boxes']:
    patch.set_facecolor('lightgreen')
    patch.set_alpha(0.7)

# Set the y-axis label
ax[1].set_ylabel("Non-Renewable Energy Production (GWh)", fontsize=12)

# Adjust layout to prevent occlusion
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Display the plot
plt.show()