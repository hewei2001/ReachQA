import matplotlib.pyplot as plt
import numpy as np

# Define countries and their renewable energy investments in billion USD
countries = ['USA', 'China', 'Germany', 'India', 'Brazil', 'UK', 'France', 'Japan', 'Australia', 'Canada']
# Investments across Solar, Wind, Hydro, Geothermal, Biomass
investments = np.array([
    [30, 25, 10, 5, 3],   # USA
    [20, 35, 15, 5, 8],   # China
    [15, 20, 5, 2, 4],    # Germany
    [25, 15, 10, 1, 2],   # India
    [10, 5, 20, 3, 7],    # Brazil
    [18, 22, 5, 2, 3],    # UK
    [13, 18, 8, 3, 6],    # France
    [19, 30, 10, 4, 5],   # Japan
    [11, 14, 6, 2, 4],    # Australia
    [14, 10, 7, 5, 6]     # Canada
])

# Define labels and colors for the types of energy
energy_types = ['Solar', 'Wind', 'Hydroelectric', 'Geothermal', 'Biomass']
colors = ['#FFA07A', '#20B2AA', '#4682B4', '#8B4513', '#DAA520']

# Calculate cumulative sums for stacking bars
cumulative_investments = investments.cumsum(axis=1)

# Create the horizontal bar chart
fig, ax = plt.subplots(figsize=(14, 10))

# Plot each segment of the horizontal bars
for i in range(len(energy_types)):
    ax.barh(countries, investments[:, i], left=(cumulative_investments[:, i] - investments[:, i]),
            color=colors[i], edgecolor='black', label=energy_types[i], height=0.6)

# Add titles and labels
ax.set_title('Renewable Energy Investments by Country in 2023\n(Across Multiple Energy Types)', fontsize=16, fontweight='bold')
ax.set_xlabel('Investment in Renewable Energy (Billion USD)', fontsize=12)
ax.set_ylabel('Countries', fontsize=12)

# Add a legend
ax.legend(title='Energy Type', loc='upper right', bbox_to_anchor=(1.15, 1))

# Annotate investment values on each segment of the bars
for i, country in enumerate(countries):
    for j in range(len(energy_types)):
        ax.text(cumulative_investments[i, j] - investments[i, j] / 2, i, 
                f"${investments[i, j]}B", color='black', ha='center', va='center', fontsize=8, fontweight='bold')

# Add grid lines for better readability
ax.xaxis.grid(True, linestyle='--', alpha=0.7)

# Additional plot: Total Investment Comparison
fig2, ax2 = plt.subplots(figsize=(14, 4))
total_investments = investments.sum(axis=1)
ax2.bar(countries, total_investments, color='skyblue', edgecolor='black')
ax2.set_title('Total Renewable Energy Investments per Country in 2023', fontsize=16, fontweight='bold')
ax2.set_ylabel('Total Investment (Billion USD)', fontsize=12)
ax2.set_xlabel('Countries', fontsize=12)
ax2.yaxis.grid(True, linestyle='--', alpha=0.7)

# Annotate total investment values on bars
for i, val in enumerate(total_investments):
    ax2.text(i, val + 2, f"${val}B", ha='center', va='bottom', fontsize=10, fontweight='bold')

# Adjust layouts
plt.tight_layout()

# Display the plots
plt.show()