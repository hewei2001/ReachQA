import matplotlib.pyplot as plt

# Data for the pie chart representing sectors' investment in renewable energy
sectors = ['Technology', 'Finance', 'Manufacturing', 'Energy', 'Transportation']
investment_shares = [25, 20, 15, 30, 10]

# Colors assigned to each sector for distinction
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Optional explode to highlight the 'Energy' sector
explode = (0.1, 0, 0, 0, 0)  # Only "explode" the first sector

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    investment_shares, 
    labels=sectors, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    explode=explode,
    wedgeprops=dict(edgecolor='w'),
    textprops=dict(size=10)
)

# Set chart title with line break for clarity
ax.set_title('Global Initiatives in Renewable Energy Investment\n(2023)', fontsize=14, fontweight='bold', pad=20)

# Customize percentage text style
plt.setp(autotexts, size=9, weight='bold', color='white')

# Place legend outside the pie chart
ax.legend(wedges, sectors, title="Sectors", loc="center left", bbox_to_anchor=(1, 0.5), fontsize=10)

# Automatically adjust layout to ensure the pie is drawn as a circle and avoid overlap
plt.tight_layout()

# Display the plot
plt.show()