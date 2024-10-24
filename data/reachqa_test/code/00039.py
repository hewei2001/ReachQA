import matplotlib.pyplot as plt
import numpy as np

# Define the ocean regions and exploration percentages
ocean_regions = [
    'Pacific Ocean', 
    'Atlantic Ocean', 
    'Indian Ocean', 
    'Southern Ocean', 
    'Arctic Ocean'
]
exploration_distribution = [40, 25, 20, 10, 5]

# Hypothetical data: Yearly exploration efforts for the Pacific Ocean
years = ['2019', '2020', '2021', '2022', '2023']
pacific_exploration = [35, 37, 39, 42, 40]  # in percentage

# Create the subplots
fig, axes = plt.subplots(1, 2, figsize=(14, 7))

# Use a color palette
colors = plt.get_cmap('ocean')(np.linspace(0.4, 0.9, len(ocean_regions)))

# Plotting the donut chart
wedges, texts, autotexts = axes[0].pie(
    exploration_distribution, 
    labels=ocean_regions, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    wedgeprops=dict(width=0.3, edgecolor='w')
)

# Center circle for the donut effect
centre_circle = plt.Circle((0, 0), 0.6, fc='white')
axes[0].add_artist(centre_circle)
axes[0].set_aspect('equal')

# Set text properties
plt.setp(autotexts, size=10, weight="bold", color='navy')
plt.setp(texts, size=12)

# Title for the donut chart
axes[0].set_title(
    "2023 Ocean Floor Exploration Efforts\n"
    "Global Oceanic Research Initiative (GORI)", 
    fontsize=14, 
    fontweight='bold', 
    pad=20
)

# Adding a legend outside the donut chart
axes[0].legend(
    wedges, 
    ocean_regions, 
    title="Ocean Regions", 
    loc="center left", 
    bbox_to_anchor=(1.1, 0, 0.5, 1), 
    fontsize=10
)

# Plotting the bar chart for Pacific Ocean exploration over the years
axes[1].bar(years, pacific_exploration, color='steelblue', edgecolor='navy')
axes[1].set_xlabel('Year', fontsize=12)
axes[1].set_ylabel('Exploration Efforts (%)', fontsize=12)
axes[1].set_title(
    "Pacific Ocean Exploration\n"
    "Trends Over the Years", 
    fontsize=14, 
    fontweight='bold', 
    pad=10
)
axes[1].set_ylim(30, 45)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()