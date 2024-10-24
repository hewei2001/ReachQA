import matplotlib.pyplot as plt
import numpy as np

# Define the months
months = np.arange(1, 13)
month_labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Number of passengers transported monthly
electric_buses = np.array([1000, 1200, 1400, 1600, 1800, 2000, 2200, 2300, 2400, 2500, 2600, 2700])
cycling_lanes = np.array([500, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2100, 2200, 2300])
autonomous_shuttles = np.array([200, 300, 500, 700, 1000, 1200, 1400, 1600, 1800, 1900, 2000, 2100])

# Create a figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Colors for each area
colors = ['#66c2a5', '#fc8d62', '#8da0cb']

# Plot a stacked area chart
ax.stackplot(months, electric_buses, cycling_lanes, autonomous_shuttles,
             labels=['Electric Buses', 'Cycling Lanes', 'Autonomous Shuttles'],
             colors=colors, alpha=0.8)

# Set title and labels
ax.set_title("Greenville's Transition to Sustainable Transportation (2040)\nMonthly Passenger Trends by Mode",
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Month", fontsize=12)
ax.set_ylabel("Number of Passengers", fontsize=12)

# Customize x-ticks for better readability
ax.set_xticks(months)
ax.set_xticklabels(month_labels, rotation=45, ha="right")

# Add a legend
ax.legend(loc='upper left', title='Transportation Modes', fontsize=10)

# Enhance gridlines for readability
ax.grid(True, linestyle='--', alpha=0.5, which='both', linewidth=0.7)

# Annotate significant growth points
notable_months = [3, 6, 9]  # March, June, September
labels = ['Electric Buses', 'Cycling Lanes', 'Autonomous Shuttles']
data_sets = [electric_buses, cycling_lanes, autonomous_shuttles]
for idx, data in enumerate(data_sets):
    month = notable_months[idx]
    ax.annotate(f'{labels[idx]} growth', xy=(month, data[month-1]), 
                xytext=(month+0.5, data[month-1]+500), 
                arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, color=colors[idx])

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()