import matplotlib.pyplot as plt
import numpy as np

# Data for the chart
departments = ['R&D', 'Marketing', 'Operations', 'HR', 'Finance', 'Customer Support']
contributions = [35, 20, 15, 10, 10, 10]  # Contribution percentages
growth_rates = [10, 5, 8, -2, 3, 7]  # Year-on-year growth rates in percentage points

# Colors for bars and line plot
colors = ['#6A0572', '#FFD700', '#FF6347', '#4682B4', '#32CD32', '#DC143C']
line_color = '#FFA500'

# Plotting
fig, ax1 = plt.subplots(figsize=(12, 7))

# Create a horizontal bar chart
bars = ax1.barh(departments, contributions, color=colors, edgecolor='black')

# Add annotations to each bar
for bar, contribution in zip(bars, contributions):
    ax1.text(bar.get_width() - 3, bar.get_y() + bar.get_height() / 2, f'{contribution}%', 
             va='center', ha='center', color='white', fontsize=12, fontweight='bold')

# Set the x-axis limit from 0 to 100% for contributions
ax1.set_xlim(0, 100)
ax1.set_xlabel('Contribution to Sustainability Initiatives (%)', fontsize=12)

# Add a secondary y-axis for the growth rates
ax2 = ax1.twinx()

# Plot the line plot on the secondary y-axis
ax2.plot(growth_rates, departments, linestyle='--', marker='o', color=line_color, linewidth=2, label='Growth Rate')

# Set labels and limits for the secondary axis
ax2.set_ylabel('Year-on-Year Growth Rate (%)', fontsize=12)
ax2.set_xlim(min(growth_rates) - 5, max(growth_rates) + 5)

# Title with line break for clarity
plt.title('EcoInnovate Inc.: Departmental Contributions and Growth Rates\n to Sustainability Initiatives', 
          fontsize=16, fontweight='bold', pad=20)

# Add grid and legend
ax1.xaxis.grid(True, linestyle='--', alpha=0.7)
ax2.legend(loc='upper left')

# Improve layout to avoid overlapping
plt.tight_layout()

# Display the plot
plt.show()