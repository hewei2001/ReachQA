import matplotlib.pyplot as plt
import numpy as np

# Define data for waste management efficiency in GreenVille
sectors = ['Residential', 'Commercial', 'Industrial', 'Public Institutions', 'Hospitality']
efficiency = [65, 50, 40, 75, 55]  # Efficiency percentages for each sector

# Create colors using a colormap to differentiate sectors
colors = plt.cm.viridis(np.linspace(0.15, 0.85, len(sectors)))

# Plotting the horizontal bar chart
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(sectors, efficiency, color=colors, edgecolor='black')

# Add percentage labels next to each bar
for bar in bars:
    width = bar.get_width()
    ax.text(width + 2, bar.get_y() + bar.get_height()/2, f'{width}%', 
            ha='center', va='center', color='black', fontsize=10)

# Set the title and labels with an appropriate style
ax.set_title('Waste Management Efficiency by Sector\nin GreenVille (2023)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Efficiency (%)', fontsize=12)
ax.set_ylabel('Sector', fontsize=12)

# Set x-axis limits from 0 to 100 for percentage
ax.set_xlim(0, 100)

# Add a line for the average efficiency across sectors
average_efficiency = np.mean(efficiency)
ax.axvline(average_efficiency, color='red', linestyle='--', linewidth=1, label=f'Average Efficiency: {average_efficiency:.1f}%')
ax.legend(loc='lower right', fontsize=10)

# Enable grid lines for better readability
ax.grid(True, which='major', axis='x', linestyle='--', alpha=0.6)
ax.set_facecolor('#f7f7f7')

# Adjust layout to prevent label overlap
plt.tight_layout()

# Display the plot
plt.show()