import matplotlib.pyplot as plt

# Data for the energy source distribution on Mars in 2050
energy_sources = ['Solar', 'Nuclear', 'Wind', 'Geothermal', 'Biofuel']
percentages = [40, 25, 10, 15, 10]

# Colors for each section of the donut
colors = ['#FFD700', '#8B0000', '#1E90FF', '#32CD32', '#FFA500']

# Explode the first and second slices slightly for emphasis
explode = (0.1, 0.1, 0, 0, 0)

# Create a donut pie chart
fig, ax = plt.subplots(figsize=(10, 7), subplot_kw=dict(aspect="equal"))

# Plot pie chart with defined properties
wedges, texts, autotexts = ax.pie(
    percentages, 
    colors=colors, 
    startangle=140, 
    autopct='%1.1f%%', 
    pctdistance=0.85,
    explode=explode,
    wedgeprops=dict(width=0.3, edgecolor='w'),
    shadow=True
)

# Add a circle at the center to create a donut effect
centre_circle = plt.Circle((0, 0), 0.70, fc='white', edgecolor='white')
ax.add_artist(centre_circle)

# Title and legend
ax.set_title("Energy Source Distribution for\nFuture Martian Colonies - 2050", fontsize=16, weight='bold', pad=20)
ax.legend(wedges, energy_sources, title="Energy Sources", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Customize text
plt.setp(autotexts, size=10, weight="bold", color='black')
plt.setp(texts, size=12, color='black')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()