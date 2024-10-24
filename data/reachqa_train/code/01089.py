import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2010, 2023)

# Define the data for each protein source in million metric tons
plant_based = [2, 3, 4, 5, 6.5, 8, 10, 12.5, 15, 18, 21, 25, 30]
insect_based = [0.1, 0.1, 0.2, 0.2, 0.3, 0.5, 0.8, 1.2, 2, 3.5, 5, 7, 10]
lab_grown = [0, 0, 0, 0.1, 0.2, 0.3, 0.5, 0.8, 1.5, 3, 5.5, 8, 12]
algae_based = [0.5, 0.5, 0.6, 0.8, 1, 1.3, 1.7, 2, 2.5, 3, 3.5, 4, 5]

# Compile the data into an array for stacking
protein_data = np.array([plant_based, insect_based, lab_grown, algae_based])

# Define colors for each protein category
colors = ['#76C7C0', '#FFB74D', '#FF8A80', '#AED581']

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(years, protein_data, labels=[
    "Plant-based Proteins", "Insect-based Proteins", "Lab-grown Meat", "Algae-based Proteins"], 
    colors=colors, alpha=0.8)

# Customize the plot with titles, labels, and legend
ax.set_title("Global Growth of Alternative Protein Sources\nfrom 2010 to 2022", fontsize=16, fontweight='bold')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Consumption (Million Metric Tons)", fontsize=12)
ax.set_xlim(years[0], years[-1])
ax.set_ylim(0, 60)
ax.set_xticks(years)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{int(y)} Mt'))

# Add legend positioned outside the plot
ax.legend(loc='upper left', title="Protein Source", bbox_to_anchor=(1.02, 1), fontsize=10, frameon=False)

# Enable grid for y-axis
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout to prevent overlapping elements
plt.tight_layout()

# Display the plot
plt.show()