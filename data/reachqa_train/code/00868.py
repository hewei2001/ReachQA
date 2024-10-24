import matplotlib.pyplot as plt

# Define the data for the ring chart
energy_sources = ['Solar Energy', 'Wind Energy', 'Biomass Energy', 'Hydropower', 'Other Renewables']
percentages = [35, 25, 20, 15, 5]
colors = ['#FFD700', '#00BFFF', '#8B4513', '#228B22', '#FF69B4']

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))

# Create the ring (donut) chart
wedges, texts, autotexts = ax.pie(
    percentages, 
    labels=energy_sources, 
    colors=colors, 
    autopct='%1.1f%%', 
    startangle=90, 
    pctdistance=0.85, 
    wedgeprops=dict(width=0.3, edgecolor='w'),
    explode=(0.05, 0.05, 0.05, 0.05, 0.05),
    shadow=True
)

# Draw circle for the donut shape
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Title and annotations
ax.set_title('GreenTech 2025: Renewable Energy Share\nin FutureCity', fontsize=14, fontweight='bold', va='bottom')

# Adjust text properties for better readability
plt.setp(autotexts, size=10, weight="bold", color="black")
plt.setp(texts, size=10)

# Equal aspect ratio ensures that pie chart is drawn as a circle
ax.axis('equal')

# Add a legend outside the plot area
ax.legend(wedges, energy_sources, title="Energy Sources", loc='center left', bbox_to_anchor=(1.1, 0.5), fontsize=10)

# Central annotation to utilize empty space effectively
ax.annotate('Renewable\nFocus 2025', xy=(0, 0), fontsize=12, fontweight='bold', color='#444444',
            ha='center', va='center')

# Automatically adjust layout
plt.tight_layout()

# Display the chart
plt.show()