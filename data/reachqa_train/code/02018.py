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

# Calculate annual growth rates for each mode
growth_rates = np.diff(usage_data) / usage_data[:, :-1] * 100
growth_rates = np.pad(growth_rates, ((0,0), (1,0)), constant_values=np.nan)  # Pad with NaNs for the first year

# Create a figure with two subplots
fig, axes = plt.subplots(1, 2, figsize=(18, 8))

# First subplot: Line plot of usage data
ax1 = axes[0]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
for i, mode in enumerate(transport_modes):
    ax1.plot(years, usage_data[i], label=mode, color=colors[i], linewidth=2, marker='o')

# Titles and labels
ax1.set_title('Greener Commute in EcoCity:\nAdoption of Eco-Friendly Transportation Modes (2020-2030)', 
              fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Usage (Million Rides)', fontsize=12)
ax1.legend(title='Transport Modes', fontsize=10, loc='upper left')
ax1.grid(color='gray', linestyle='--', linewidth=0.5, axis='y', alpha=0.7)

# Annotate key milestones
milestones = {
    2022: 'Launch of\nAutonomous Buses',
    2025: 'Major expansion\nof Solar Trams',
    2028: 'Electric Bikes\nbecome dominant'
}
for year, annotation in milestones.items():
    idx = years.tolist().index(year)
    total_usage = usage_data[:, idx].sum()
    ax1.annotate(annotation, xy=(year, total_usage), 
                xytext=(year, total_usage + 6),
                arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=9, ha='center')

# Highlight total usage
total_usage = usage_data.sum(axis=0)
ax1.plot(years, total_usage, label='Total Usage', color='black', linestyle='--', marker='s', linewidth=1.5, alpha=0.5)

# Annotate each data point with its value
for i, mode in enumerate(transport_modes):
    for j, year in enumerate(years):
        ax1.annotate(f'{usage_data[i, j]}', xy=(year, usage_data[i, j]), 
                    textcoords="offset points", xytext=(0,5), ha='center', fontsize=8, color=colors[i])

# Second subplot: Bar plot for growth rates
ax2 = axes[1]
bar_width = 0.25
x_indexes = np.arange(len(years))

for i, mode in enumerate(transport_modes):
    ax2.bar(x_indexes + i * bar_width, growth_rates[i], width=bar_width, color=colors[i], label=mode, alpha=0.7)

# Titles and labels
ax2.set_title('Annual Growth Rates of Eco-Friendly Transportation Modes (2020-2030)', 
              fontsize=16, fontweight='bold', pad=20)
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Growth Rate (%)', fontsize=12)
ax2.set_xticks(x_indexes + bar_width)
ax2.set_xticklabels(years)
ax2.legend(title='Transport Modes', fontsize=10, loc='upper left')
ax2.grid(color='gray', linestyle='--', linewidth=0.5, axis='y', alpha=0.7)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plots
plt.show()