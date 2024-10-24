import matplotlib.pyplot as plt

# Data for the renewable energy sources in Greenlandia
energy_sources = ['Solar', 'Wind', 'Hydro', 'Geothermal', 'Biomass']
percentages = [25, 30, 20, 15, 10]
colors = ['#FFCC00', '#66CCFF', '#99CC99', '#FF9966', '#CC99FF']

# Create the ring chart
fig, ax = plt.subplots(figsize=(9, 9))
wedges, texts, autotexts = ax.pie(percentages, labels=energy_sources, autopct='%1.1f%%',
                                  startangle=90, colors=colors, pctdistance=0.85,
                                  wedgeprops={'width': 0.3, 'edgecolor': 'w', 'linewidth': 2},
                                  textprops={'fontsize': 12, 'fontweight': 'bold'})

# Draw a white circle at the center to complete the ring chart
center_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(center_circle)

# Set the title with a line break for clarity
ax.set_title("Harnessing Nature's Power:\nRenewable Energy Distribution in Greenlandia", 
             fontsize=16, fontweight='bold', ha='center', va='center', pad=40)

# Adding a central annotation inside the ring
ax.annotate('Total Renewable\nEnergy Portfolio',
            xy=(0, 0), fontsize=12, fontweight='bold', ha='center', va='center', color='grey')

# Ensure equal aspect ratio
ax.axis('equal')

# Adjust the layout to prevent text overlap
plt.tight_layout()

# Display the plot
plt.show()