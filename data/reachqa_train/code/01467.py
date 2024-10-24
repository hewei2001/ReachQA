import matplotlib.pyplot as plt

# Define energy sources and their percentage contributions
energy_sources = ['Solar', 'Wind', 'Hydropower', 'Geothermal', 'Natural Gas', 'Coal', 'Oil']
percentages = [25, 20, 15, 10, 15, 10, 5]

# Define colors corresponding to each energy type
colors = ['#FFD700', '#1E90FF', '#00CED1', '#228B22', '#8B4513', '#A9A9A9', '#000000']

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 7))

# Create a horizontal bar chart
bars = ax.barh(energy_sources, percentages, color=colors)

# Invert y-axis to have the largest bar at the top
ax.invert_yaxis()

# Add percentage annotations to the bars
for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width}%', xy=(width - 3, bar.get_y() + bar.get_height() / 2),
                xytext=(5, 0), textcoords='offset points',
                ha='right', va='center', color='white', fontweight='bold')

# Set titles and labels
ax.set_title('Energy Source Distribution in Green Valley\nPaving the Path to 100% Renewable by 2030', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Percentage (%)', fontsize=12)
ax.set_xlim(0, 100)  # Ensure x-axis is set to 0-100 to indicate percentage
ax.xaxis.grid(False)  # Disable x-axis grid lines to reduce clutter

# Remove unnecessary spines for a cleaner look
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()