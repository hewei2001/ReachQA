import matplotlib.pyplot as plt
import numpy as np

# Define states and data
states = ['California', 'Texas', 'New York', 'Florida', 'Illinois']
solar_energy = [25, 15, 10, 20, 18]
wind_energy = [15, 30, 12, 10, 25]
hydro_energy = [12, 5, 15, 5, 10]

# Define bar width and positions
width = 0.25
ind = np.arange(len(states))

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot bars
ax.bar(ind - width, solar_energy, width, label='Solar', color='goldenrod', edgecolor='black')
ax.bar(ind, wind_energy, width, label='Wind', color='skyblue', edgecolor='black')
ax.bar(ind + width, hydro_energy, width, label='Hydroelectric', color='seagreen', edgecolor='black')

# Annotate bars
for i, (s, w, h) in enumerate(zip(solar_energy, wind_energy, hydro_energy)):
    ax.text(i - width, s + 0.5, f"{s}%", ha='center', va='bottom', fontsize=9, color='darkgoldenrod')
    ax.text(i, w + 0.5, f"{w}%", ha='center', va='bottom', fontsize=9, color='darkblue')
    ax.text(i + width, h + 0.5, f"{h}%", ha='center', va='bottom', fontsize=9, color='darkgreen')

# Set title and labels
ax.set_title('Renewable Energy Adoption\nin U.S. States (2023)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('State', fontsize=14, labelpad=10)
ax.set_ylabel('Percentage of Total Energy Consumption', fontsize=14, labelpad=10)

# Configure x-ticks
ax.set_xticks(ind)
ax.set_xticklabels(states, fontsize=12, rotation=30, ha='right')

# Add legend
ax.legend(title='Energy Source', fontsize=10, title_fontsize=12)

# Customize grid
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()