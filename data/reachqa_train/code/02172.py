import matplotlib.pyplot as plt

# Define the energy sources and their percentage share in EcoVille
energy_sources = ['Solar', 'Wind', 'Hydropower', 'Biomass', 'Fossil Fuels']
consumption_percentage = [30, 25, 20, 15, 10]  # Total should be 100%

# Set colors for each segment to represent energy types
colors = ['#FDB813', '#76C7C0', '#8ECF72', '#F39C6B', '#B0BEC5']

# Create the donut pie chart
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    consumption_percentage, 
    labels=energy_sources, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    wedgeprops=dict(width=0.3),
    pctdistance=0.85
)

# Customize autotext for better readability
plt.setp(autotexts, size=10, weight="bold", color='white')

# Add a central circle for the donut shape
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Set the title with line breaks for improved readability
plt.title("EcoVille's 2023 Energy Consumption\nCommitment to Renewable Sources", fontsize=14, fontweight='bold', pad=20)

# Add a legend to provide context
ax.legend(wedges, energy_sources, title="Energy Sources", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Ensure the chart is rendered as a circle
ax.set_aspect('equal')

# Automatically adjust layout to fit elements without overlap
plt.tight_layout()

# Display the chart
plt.show()