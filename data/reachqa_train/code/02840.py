import matplotlib.pyplot as plt
import numpy as np

# Coffee types and regions
coffee_types = ['Espresso', 'Latte', 'Cappuccino', 'Americano', 'Mocha']
regions = ['North America', 'Europe', 'Asia', 'South America', 'Africa']

# Preference data (in percentage)
preferences = np.array([
    [20, 25, 30, 15, 10],  # North America
    [35, 20, 25, 10, 10],  # Europe
    [15, 30, 10, 30, 15],  # Asia
    [10, 15, 20, 25, 30],  # South America
    [5, 10, 15, 35, 35]    # Africa
])

# Creating the heat map
fig, ax = plt.subplots(figsize=(10, 6))
cax = ax.imshow(preferences, cmap='YlGnBu', aspect='auto', interpolation='nearest')

# Adding title and labels
ax.set_title("Global Coffee Preferences\nA Regional Heatmap", fontsize=16, pad=20)
ax.set_xticks(np.arange(len(coffee_types)))
ax.set_yticks(np.arange(len(regions)))
ax.set_xticklabels(coffee_types)
ax.set_yticklabels(regions)

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Annotate each cell with the corresponding data value
for i in range(len(regions)):
    for j in range(len(coffee_types)):
        ax.text(j, i, f"{preferences[i, j]}%", va='center', ha='center', color='black')

# Add a color bar with a label
cbar = plt.colorbar(cax, ax=ax)
cbar.set_label('Preference Percentage', rotation=270, labelpad=15)

# Adjust layout to ensure everything fits without overlapping
plt.tight_layout()

# Display the heat map
plt.show()