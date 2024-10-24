import matplotlib.pyplot as plt
import numpy as np

# Define expanded data for waste management efficiency and waste reduction rate in GreenVille
sectors = ['Urban Residential', 'Rural Residential', 'Commercial', 'Industrial', 'Public Institutions', 'Hospitality', 'Healthcare', 'Construction']
efficiency = [70, 60, 50, 45, 80, 55, 65, 35]  # Efficiency percentages for each sector
reduction_rate = [10, 15, 12, 9, 18, 14, 11, 8]  # Waste reduction rate in percent for each sector over last year

# Create colors using a colormap to differentiate sectors
colors = plt.cm.viridis(np.linspace(0.15, 0.85, len(sectors)))

# Plotting the bar chart
fig, ax1 = plt.subplots(figsize=(12, 8))

# Primary y-axis for efficiency
bars = ax1.barh(sectors, efficiency, color=colors, edgecolor='black', label='Efficiency (%)')
ax1.set_xlabel('Efficiency (%)', fontsize=12)
ax1.set_xlim(0, 100)

# Secondary y-axis for waste reduction rate
ax2 = ax1.twiny()
ax2.plot(reduction_rate, sectors, 'o-', color='darkorange', label='Waste Reduction Rate (%)')
ax2.set_xlabel('Waste Reduction Rate (%)', fontsize=12)
ax2.set_xlim(0, 20)

# Adding annotations for the second metric
for i, rate in enumerate(reduction_rate):
    ax2.text(rate + 0.5, i, f'{rate}%', ha='left', va='center', color='darkorange', fontsize=10)

# Set the title and legend
ax1.set_title('Waste Management Efficiency and Reduction Rates\nin GreenVille by Sector (2023)', fontsize=16, fontweight='bold', pad=20)
ax1.legend(loc='lower left', fontsize=10, frameon=False)
ax2.legend(loc='lower right', fontsize=10, frameon=False)

# Adding grid lines for better readability
ax1.grid(True, which='major', axis='x', linestyle='--', alpha=0.6)
ax1.set_facecolor('#f7f7f7')

# Calculate and draw the average efficiency line
average_efficiency = np.mean(efficiency)
ax1.axvline(average_efficiency, color='red', linestyle='--', linewidth=1, label=f'Average Efficiency: {average_efficiency:.1f}%')
ax1.text(average_efficiency + 1, -0.5, f'Average: {average_efficiency:.1f}%', color='red', fontsize=10)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()