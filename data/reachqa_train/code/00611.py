import matplotlib.pyplot as plt

# Define the energy sources and their respective contribution percentages
energy_sources = ['Solar', 'Wind', 'Hydroelectric', 'Biomass', 'Geothermal']
contributions = [30, 25, 20, 15, 10]  # Total adds up to 100%

# Define colors for each segment
colors = ['#FFD700', '#87CEEB', '#32CD32', '#A0522D', '#FF4500']

# Optionally explode the first slice for emphasis
explode = (0.1, 0, 0, 0, 0)  # 'Solar' is emphasized by exploding its slice

# Create the pie chart
fig, ax = plt.subplots(figsize=(9, 9))
wedges, texts, autotexts = ax.pie(
    contributions, labels=energy_sources, autopct='%1.1f%%', startangle=140,
    colors=colors, explode=explode, shadow=True, wedgeprops=dict(edgecolor='white'))

# Customize the chart with better aesthetics
plt.setp(autotexts, size=12, weight="bold", color='white')
plt.setp(texts, size=14)
ax.set_title('Global Renewable Energy\nContribution in 2023', fontsize=16, weight='bold', pad=20)

# Add a legend outside the pie chart
plt.legend(wedges, energy_sources, title="Energy Sources", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=12)

# Ensure the pie is a circle (equal aspect ratio)
ax.axis('equal')

# Automatically adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()