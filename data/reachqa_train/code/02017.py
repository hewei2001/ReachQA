import matplotlib.pyplot as plt
import numpy as np

# Define the years for the chart
years = np.arange(2020, 2031)

# Define the transport modes
transport_modes = ["Electric Bikes", "Autonomous Buses", "Solar-powered Trams"]

# Annual usage data (in million rides)
usage_data = np.array([
    [1, 3, 5, 8, 12, 18, 25, 30, 36, 42, 48],  # Electric Bikes
    [0, 1, 2, 4, 8, 12, 16, 20, 24, 28, 32],   # Autonomous Buses
    [0, 0, 1, 3, 7, 10, 14, 18, 22, 26, 30]    # Solar-powered Trams
])

# Create a figure and an axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plot line charts for each mode
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
for i, mode in enumerate(transport_modes):
    ax.plot(years, usage_data[i], label=mode, color=colors[i], linewidth=2, marker='o')

# Set titles and labels
ax.set_title('Greener Commute in EcoCity:\nAdoption of Eco-Friendly Transportation Modes (2020-2030)', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Usage (Million Rides)', fontsize=12)

# Add legend
ax.legend(title='Transport Modes', fontsize=10, loc='upper left')

# Add grid lines for readability
ax.grid(color='gray', linestyle='--', linewidth=0.5, axis='y', alpha=0.7)

# Annotate key milestones
milestones = {
    2022: 'Launch of\nAutonomous Buses',
    2025: 'Major expansion\nof Solar Trams',
    2028: 'Electric Bikes\nbecome dominant'
}

for year, annotation in milestones.items():
    idx = years.tolist().index(year)
    total_usage = usage_data[:, idx].sum()
    ax.annotate(annotation, xy=(year, total_usage), 
                xytext=(year, total_usage + 6),
                arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=9, ha='center')

# Highlight total usage
total_usage = usage_data.sum(axis=0)
ax.plot(years, total_usage, label='Total Usage', color='black', linestyle='--', marker='s', linewidth=1.5, alpha=0.5)

# Annotate each data point with its value for clarity
for i, mode in enumerate(transport_modes):
    for j, year in enumerate(years):
        ax.annotate(f'{usage_data[i, j]}', xy=(year, usage_data[i, j]), 
                    textcoords="offset points", xytext=(0,5), ha='center', fontsize=8, color=colors[i])

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()