import matplotlib.pyplot as plt
import numpy as np

# Renewable energy technologies and their installation rates in 2023 (in gigawatts)
technologies = ['Solar Power', 'Wind Power', 'Hydropower', 'Biomass']
installation_rates = [180, 140, 90, 60]

# Colors for each technology
colors = ['#FFD700', '#1E90FF', '#32CD32', '#8B4513']

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Positions for the bars
x_positions = np.arange(len(technologies))

# Create the bar chart
bars = ax.bar(x_positions, installation_rates, color=colors, width=0.6)

# Add data annotations on top of each bar
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height} GW',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 5),  # 5 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom', fontsize=10, color='black', weight='bold')

# Titles and labels
ax.set_title('The Rise of Renewable Energy Technologies\nGlobal Installation Rates in 2023', fontsize=14, weight='bold')
ax.set_xlabel('Renewable Energy Technologies', fontsize=12)
ax.set_ylabel('Installation Rates (GW)', fontsize=12)

# Set the x-ticks with the technology labels
ax.set_xticks(x_positions)
ax.set_xticklabels(technologies, fontsize=11)

# Add grid lines for the y-axis
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Display the plot
plt.show()