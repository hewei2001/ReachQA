import matplotlib.pyplot as plt
import numpy as np

# Data for the pie chart
sectors = [
    'Renewable Energy\nHarvesting', 
    'Carbon Capture\nand Storage', 
    'Urban Vertical\nFarming', 
    'Ocean Cleaning\nRobotics', 
    'Biodiversity\nAI Monitors'
]
investments = [250, 180, 120, 90, 60]

# Color palette
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Projected future investments or growth rates
growth_rates = [15, 10, 25, 18, 12]  # hypothetical growth rates in percentage

# Determine the explode setting for a highlight effect
explode = (0.1, 0, 0, 0, 0)  # Emphasize the Renewable Energy sector

# Create the figure and a grid of subplots
fig, ax = plt.subplots(figsize=(12, 8), nrows=1, ncols=2, gridspec_kw={'width_ratios': [3, 1]})

# Create the pie chart
wedges, texts, autotexts = ax[0].pie(
    investments, labels=sectors, colors=colors, autopct='%1.1f%%',
    startangle=140, pctdistance=0.85, explode=explode
)

# Draw center circle for a 'donut' look
centre_circle = plt.Circle((0,0),0.70,fc='white')
ax[0].add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
ax[0].axis('equal')

# Title and adjustments
ax[0].set_title('The Seeds of Tomorrow:\nFuturistic Innovations in Environmental Sustainability',
                fontsize=14, fontweight='bold', pad=20)
plt.setp(autotexts, size=10, weight='bold', color='white')
plt.setp(texts, size=10)

# Create the bar plot
ax[1].barh(sectors, growth_rates, color=colors)
ax[1].set_xlabel('Growth Rate (%)', fontsize=12)
ax[1].set_title('Projected Growth Rates', fontsize=12, fontweight='bold')
ax[1].invert_yaxis()  # To match the order of the pie chart sectors
ax[1].grid(axis='x', linestyle='--', alpha=0.7)

# Add a legend outside the pie chart
fig.legend(wedges, sectors, title="Innovation Sectors", loc="center left", bbox_to_anchor=(1, 0.5))

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()