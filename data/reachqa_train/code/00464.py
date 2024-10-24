import matplotlib.pyplot as plt

# Data for the sectors
sectors = ['Mining', 'Research', 'Tourism', 'Energy', 'Agriculture']
contributions = [35, 25, 20, 15, 5]
colors = ['#d4af37', '#6495ed', '#ff69b4', '#ff4500', '#3cb371']
explode = (0.1, 0, 0, 0, 0)  # Explode the first slice (Mining)

# Create a donut pie chart
fig, ax = plt.subplots(figsize=(8, 8))

# Plot the pie chart with a hole in the center
wedges, texts, autotexts = ax.pie(contributions, 
                                  explode=explode, 
                                  labels=sectors, 
                                  autopct='%1.1f%%', 
                                  startangle=90, 
                                  colors=colors, 
                                  pctdistance=0.85, 
                                  wedgeprops=dict(width=0.3, edgecolor='w'),
                                  shadow=True)

# Draw the circle for the hole
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')  

# Title and legend
plt.title('Sector Contributions to Lunar Resource Utilization\nin 2040', fontsize=14, fontweight='bold', pad=20)

# Customize autotexts for better visibility
for autotext in autotexts:
    autotext.set_color('navy')
    autotext.set_fontweight('bold')

# Legend configuration
ax.legend(wedges, sectors, title="Sectors", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Adjust layout to improve the appearance and prevent overlap
plt.tight_layout()

# Display the plot
plt.show()