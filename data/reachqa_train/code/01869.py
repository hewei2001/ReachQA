import matplotlib.pyplot as plt
import numpy as np

# Data: Investments in quantum computing by region in 2023 (in billion USD)
regions = ["North America", "Europe", "East Asia", "South Asia", 
           "Middle East", "Latin America", "Sub-Saharan Africa", "Oceania"]
investment_amounts = [25.4, 18.2, 30.7, 8.5, 10.3, 6.7, 3.1, 5.9]

# Calculate global average investment
global_average = np.mean(investment_amounts)

# Positions for the x-axis
x_positions = np.arange(len(regions))

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the bar chart
bars = ax.bar(x_positions, investment_amounts, color=['#4e79a7', '#f28e2b', '#e15759', '#76b7b2', '#59a14f', 
                                                      '#edc949', '#b07aa1', '#ff9da7'], width=0.6)

# Annotate each bar with the investment amount
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 0.5, f'${yval:.1f}B', ha='center', va='bottom', fontsize=10)

# Add a horizontal line for the global average
ax.axhline(global_average, color='gray', linestyle='--', linewidth=1.5, label=f'Global Avg: ${global_average:.1f}B')

# Set the title and labels
ax.set_title("Quantum Leap: Global Investment in Quantum Computing\nby Region (2023)", fontsize=16, weight='bold', pad=20)
ax.set_xlabel("Region", fontsize=12)
ax.set_ylabel("Investment (Billion USD)", fontsize=12)

# Set x-ticks to match the regions and adjust rotation for better readability
ax.set_xticks(x_positions)
ax.set_xticklabels(regions, rotation=45, ha='right', fontsize=11)

# Add a legend for the average line
ax.legend()

# Add grid lines for better visual reference
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Ensure the layout is tight so that no text overlaps
plt.tight_layout()

# Display the plot
plt.show()