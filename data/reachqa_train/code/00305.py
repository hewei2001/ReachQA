import matplotlib.pyplot as plt
import numpy as np

# Years for projection
years = np.arange(2025, 2036)

# Calculate projected employment using compound growth rates for diversity
def calculate_growth(base_value, rate, years):
    return base_value * ((1 + rate) ** np.arange(len(years)))

# Base employment values for 2025
base_ai = 100
base_robotics = 50
base_vr = 40
base_blockchain = 25
base_green_tech = 60
base_quantum_computing = 10
base_bioinformatics = 30

# Annual growth rates
growth_ai = 0.10
growth_robotics = 0.12
growth_vr = 0.15
growth_blockchain = 0.18
growth_green_tech = 0.10
growth_quantum_computing = 0.25
growth_bioinformatics = 0.13

# Employment projections
ai_employment = calculate_growth(base_ai, growth_ai, years)
robotics_employment = calculate_growth(base_robotics, growth_robotics, years)
vr_employment = calculate_growth(base_vr, growth_vr, years)
blockchain_employment = calculate_growth(base_blockchain, growth_blockchain, years)
green_tech_employment = calculate_growth(base_green_tech, growth_green_tech, years)
quantum_computing_employment = calculate_growth(base_quantum_computing, growth_quantum_computing, years)
bioinformatics_employment = calculate_growth(base_bioinformatics, growth_bioinformatics, years)

# Create the stacked bar chart
fig, ax = plt.subplots(figsize=(14, 10))

# Plotting the stacked bars
ax.bar(years, ai_employment, label='AI', color='#4c72b0', alpha=0.9)
ax.bar(years, robotics_employment, bottom=ai_employment, label='Robotics', color='#55a868', alpha=0.9)
ax.bar(years, vr_employment, bottom=ai_employment+robotics_employment, label='VR', color='#c44e52', alpha=0.9)
ax.bar(years, blockchain_employment, bottom=ai_employment+robotics_employment+vr_employment, label='Blockchain', color='#8172b2', alpha=0.9)
ax.bar(years, green_tech_employment, bottom=ai_employment+robotics_employment+vr_employment+blockchain_employment, label='Green Tech', color='#ccb974', alpha=0.9)
ax.bar(years, quantum_computing_employment, bottom=ai_employment+robotics_employment+vr_employment+blockchain_employment+green_tech_employment, label='Quantum Computing', color='#64b5cd', alpha=0.9)
ax.bar(years, bioinformatics_employment, bottom=ai_employment+robotics_employment+vr_employment+blockchain_employment+green_tech_employment+quantum_computing_employment, label='Bioinformatics', color='#e07b39', alpha=0.9)

# Adding title and labels with line breaks for clarity
ax.set_title('Future Tech Occupation Trends\n(2025-2035) Including Diverse Growth Sectors', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Number of Workers (in thousands)', fontsize=14)

# Adding legend with adjustments for readability
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Tech Sectors', fontsize=10, frameon=False)

# Rotate x-axis labels to avoid overlap
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

# Adjust the y-axis to fit the cumulative data
ax.set_ylim(0, 1000)

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()