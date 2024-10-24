import matplotlib.pyplot as plt
import numpy as np

# Technologies and their hypothetical adoption percentages in smart cities
technologies = ['IoT', 'AI-Driven\nPublic Services', 'Autonomous\nVehicles', 'Smart Grids', 'Blockchain\nGovernance']
adoption_rates = np.array([85, 70, 50, 65, 40])

# Remaining share (non-adoption) for each technology to complete to 100%
non_adoption_rates = 100 - adoption_rates

# Setting up the bar chart
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the stacked bars
bar1 = ax.barh(technologies, adoption_rates, color='#1f77b4', label='Adoption')
bar2 = ax.barh(technologies, non_adoption_rates, left=adoption_rates, color='#c7c7c7', label='Non-Adoption')

# Titles and labels
ax.set_title('Adoption of Emerging Technologies in Smart Cities (2023)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Percentage (%)', fontsize=12)
ax.set_xlim(0, 100)

# Add percentage labels inside each bar for clarity
for b1, b2, rate in zip(bar1, bar2, adoption_rates):
    ax.text(b1.get_width() / 2, b1.get_y() + b1.get_height() / 2, f'{int(rate)}%', ha='center', va='center', color='white', fontsize=10, weight='bold')
    ax.text(b1.get_width() + b2.get_width() / 2, b2.get_y() + b2.get_height() / 2, f'{int(100-rate)}%', ha='center', va='center', color='black', fontsize=10)

# Set grid for x-axis only for better readability
ax.xaxis.grid(True, linestyle='--', alpha=0.7)
ax.yaxis.set_tick_params(rotation=0)

# Add a legend
ax.legend(loc='lower right', fontsize=10, title='Adoption Status')

# Optimize layout
plt.tight_layout()

# Display the plot
plt.show()