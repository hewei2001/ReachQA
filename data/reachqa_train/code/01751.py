import matplotlib.pyplot as plt

# Sectors and their respective resource allocations
sectors = ["Energy", "Military", "Technology", "Healthcare", "Education"]
allocations = [30, 25, 20, 15, 10]

# Define colors for each sector
colors = ['#007acc', '#cc0000', '#33cc33', '#ffcc00', '#b266ff']

# Explode the 'Technology' sector slightly to highlight it
explode = (0, 0, 0.1, 0, 0)

# Create the pie chart
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    allocations, labels=sectors, colors=colors, startangle=140, explode=explode,
    autopct='%1.1f%%', pctdistance=0.85, textprops=dict(color="w", fontsize=10),
    shadow=True
)

# Adjust text colors for clarity
for text in texts:
    text.set_color('black')

# Configure the title of the plot
plt.title('Resource Allocation Across Sectors\nin the Galactic Empire (2223)', fontsize=14, fontweight='bold', pad=20)

# Add legend
plt.legend(wedges, sectors, title='Sectors', loc='upper right', bbox_to_anchor=(1.3, 0.9))

# Enhance layout and display the chart
plt.tight_layout()
plt.show()