import matplotlib.pyplot as plt

# Define renewable energy sources and their respective production percentages
sources = ['Solar', 'Wind', 'Hydro', 'Geothermal', 'Biomass']
percentages = [30, 25, 20, 15, 10]

# Define colors for each segment
colors = ['#FFD700', '#1E90FF', '#32CD32', '#FF8C00', '#8B4513']

# Create a pie chart with a 'hole' in the center to make it a donut chart
fig, ax = plt.subplots(figsize=(9, 9))
wedges, texts, autotexts = ax.pie(percentages, labels=sources, autopct='%1.1f%%',
                                  startangle=90, colors=colors, wedgeprops=dict(width=0.4),
                                  explode=[0.05]*5, shadow=True)

# Add a circle in the middle to create a 'donut' appearance
centre_circle = plt.Circle((0, 0), 0.60, fc='white')
fig.gca().add_artist(centre_circle)

# Ensure that the pie is drawn as a circle
ax.axis('equal')

# Customize autotext size and color
plt.setp(autotexts, size=10, weight="bold", color="black")

# Set the title of the chart, split across two lines for readability
plt.title('Renewable Energy Production by Source\nin Energia for the Year 2023', fontsize=14, fontweight='bold', color='navy', pad=20)

# Add a legend to indicate the energy source
ax.legend(wedges, sources, title="Energy Sources", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Improve the layout of the plot to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()