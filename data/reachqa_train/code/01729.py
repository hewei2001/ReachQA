import matplotlib.pyplot as plt
import numpy as np

# Define countries and their renewable energy investments in billion USD
countries = ['USA', 'China', 'Germany', 'India', 'Brazil']
investments = np.array([
    [30, 25, 10],  # USA: Solar, Wind, Hydro
    [20, 35, 15],  # China
    [15, 20, 5],   # Germany
    [25, 15, 10],  # India
    [10, 5, 20]    # Brazil
])

# Define labels and colors for the types of energy
energy_types = ['Solar', 'Wind', 'Hydroelectric']
colors = ['#FFA07A', '#20B2AA', '#4682B4']

# Calculate cumulative sums for stacking bars
cumulative_investments = investments.cumsum(axis=1)

# Create the horizontal bar chart
fig, ax = plt.subplots(figsize=(12, 7))

# Plot each segment of the horizontal bars
for i in range(len(energy_types)):
    ax.barh(countries, investments[:, i], left=(cumulative_investments[:, i] - investments[:, i]),
            color=colors[i], edgecolor='black', label=energy_types[i], height=0.6)

# Add titles and labels
ax.set_title('Renewable Energy Investments by Country in 2023', fontsize=16, fontweight='bold')
ax.set_xlabel('Investment in Renewable Energy (Billion USD)', fontsize=12)
ax.set_ylabel('Countries', fontsize=12)

# Add a legend
ax.legend(title='Energy Type', loc='upper right')

# Annotate investment values on each segment of the bars
for i, country in enumerate(countries):
    for j in range(len(energy_types)):
        ax.text(cumulative_investments[i, j] - investments[i, j] / 2, i, 
                f"${investments[i, j]}B", color='black', ha='center', va='center', fontsize=10)

# Add grid lines for better readability
ax.xaxis.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()