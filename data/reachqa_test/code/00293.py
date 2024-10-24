import matplotlib.pyplot as plt
import numpy as np

# Define months and ice cream flavors
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
flavors = ["Vanilla", "Chocolate", "Strawberry", "Mint", "Coffee",
           "Cookie Dough", "Mango", "Pistachio", "Raspberry", "Lemon", "Peach", "Hazelnut"]

# Create artificial demand data (demand index, with higher numbers indicating higher demand)
demand_data = np.array([
    [30, 40, 50, 20, 25, 60, 70, 40, 20, 10, 15, 25],  # January
    [35, 45, 55, 22, 30, 65, 75, 42, 25, 12, 18, 28],  # February
    [40, 50, 60, 24, 35, 70, 80, 44, 30, 14, 20, 32],  # March
    [45, 55, 65, 26, 40, 75, 85, 46, 35, 18, 25, 35],  # April
    [50, 60, 70, 30, 50, 80, 90, 48, 40, 20, 30, 40],  # May
    [60, 70, 80, 40, 60, 90, 100, 50, 50, 25, 35, 45], # June
    [70, 80, 90, 50, 70, 100, 110, 55, 60, 30, 40, 50],# July
    [65, 75, 85, 48, 68, 95, 108, 53, 58, 28, 38, 48], # August
    [55, 65, 75, 38, 58, 85, 98, 52, 48, 22, 33, 42],  # September
    [45, 55, 65, 28, 48, 75, 88, 50, 38, 20, 28, 36],  # October
    [40, 50, 60, 25, 38, 70, 80, 48, 32, 18, 23, 33],  # November
    [35, 45, 55, 22, 35, 65, 75, 46, 28, 16, 20, 30],  # December
])

# Calculate average demand per flavor
average_demand_per_flavor = np.mean(demand_data, axis=0)

# Initialize the plots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Plot the heatmap using imshow on the first subplot
cax = ax1.imshow(demand_data, cmap='YlGnBu', aspect='auto', interpolation='nearest')

# Add colorbar
cbar = fig.colorbar(cax, ax=ax1, orientation='vertical')
cbar.set_label('Demand Index', fontsize=12)

# Set labels and titles for heatmap
ax1.set_xticks(np.arange(len(flavors)))
ax1.set_yticks(np.arange(len(months)))
ax1.set_xticklabels(flavors, rotation=45, ha='right', fontsize=10)
ax1.set_yticklabels(months, fontsize=10)
ax1.set_title("Seasonal Demand Fluctuations in Ice Cream Flavors\nat Ice Dream Parlor (2023)", fontsize=14, fontweight='bold', pad=20)

# Annotate the heatmap with demand values
for i in range(len(months)):
    for j in range(len(flavors)):
        ax1.text(j, i, demand_data[i, j], ha='center', va='center', color='black', fontsize=8)

# Plot the average demand per flavor on the second subplot
ax2.bar(flavors, average_demand_per_flavor, color='skyblue', edgecolor='blue')
ax2.set_xticklabels(flavors, rotation=45, ha='right', fontsize=10)
ax2.set_title("Average Demand Per Ice Cream Flavor in 2023", fontsize=14, fontweight='bold', pad=20)
ax2.set_xlabel("Flavor", fontsize=12)
ax2.set_ylabel("Average Demand Index", fontsize=12)

# Annotate bars with average demand values
for i, v in enumerate(average_demand_per_flavor):
    ax2.text(i, v + 0.5, f"{v:.1f}", ha='center', va='bottom', fontsize=8)

# Adjust layout for clarity and aesthetics
plt.tight_layout()

# Display the plots
plt.show()