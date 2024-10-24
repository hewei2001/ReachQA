import matplotlib.pyplot as plt

# Energy sources and their projected percentage contributions in 2050
energy_sources = ['Solar', 'Wind', 'Nuclear', 'Coal', 'Natural Gas', 'Hydroelectric']
percentages = [25, 20, 15, 10, 20, 10]  # Example data

# Plotting the percentage bar chart
fig, ax = plt.subplots(figsize=(10, 6))

# Define colors for each energy source
colors = ['#FFD700', '#87CEEB', '#C0C0C0', '#696969', '#FF8C00', '#00CED1']

# Create horizontal bar chart
bars = ax.barh(energy_sources, percentages, color=colors)

# Add text annotations for each bar to show the percentage
for bar, percentage in zip(bars, percentages):
    ax.text(bar.get_width() - 1.5, bar.get_y() + bar.get_height()/2, f'{percentage}%', 
            va='center', ha='right', color='white', fontsize=10, fontweight='bold')

# Customizing the plot
ax.set_title('Global Energy Landscape 2050:\nA Shift Towards Sustainability', 
             fontsize=14, fontweight='bold')
ax.set_xlabel('Percentage of Global Energy Consumption', fontsize=12)
ax.set_xlim(0, 30)  # Range to allow for clear display of annotations

# Enhance grid aesthetics and readability
ax.xaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax.set_axisbelow(True)

# Custom legend to clarify the data representation
ax.legend(bars, energy_sources, title='Energy Sources', loc='lower right', 
          bbox_to_anchor=(1.2, 0.5), fontsize=10)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()