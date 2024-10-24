import matplotlib.pyplot as plt
import numpy as np

# Define sectors and their market shares
sectors = ['Personal Vehicles', 'Public Transportation', 'Delivery Drones', 
           'Maritime Shipping', 'Aerial Taxis']
market_share = [35, 25, 15, 15, 10]

# Define the growth rates for each sector
growth_rates = [20, 15, 30, 10, 40]  # Hypothetical growth from 2020 to 2030

# Colors for each sector
colors = ['#FFD700', '#FF8C00', '#8A2BE2', '#20B2AA', '#FF4500']

# Explode the largest sector for emphasis
explode = (0.1, 0, 0, 0, 0)

# Create a subplot grid
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

# Create the donut pie chart
wedges, texts, autotexts = ax1.pie(
    market_share, 
    labels=sectors, 
    colors=colors, 
    autopct='%1.1f%%', 
    startangle=140,
    explode=explode,
    pctdistance=0.85,
    wedgeprops=dict(width=0.4)  # Donut style
)

# Customize label and percentage text for the pie chart
for text in texts:
    text.set_size(12)
    text.set_color('black')
for autotext in autotexts:
    autotext.set_size(12)
    autotext.set_color('white')

# Add a multi-line title to the pie chart
ax1.set_title(
    "The Evolution of Autonomous Transportation:\n"
    "Market Share by Sector in 2030",
    fontsize=14,
    fontweight='bold',
    color='navy',
    pad=20
)

# Add a center circle for the donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax1.add_artist(centre_circle)

# Ensure pie chart is a perfect circle
ax1.axis('equal')

# Create a horizontal bar chart for growth rates
y_pos = np.arange(len(sectors))
bars = ax2.barh(y_pos, growth_rates, color=colors)

# Set labels for the bar chart
ax2.set_yticks(y_pos)
ax2.set_yticklabels(sectors)
ax2.invert_yaxis()  # Invert y axis to have the largest growth at the top
ax2.set_xlabel('Growth Rate (%)')
ax2.set_title('Growth Rate by Sector from 2020 to 2030', fontsize=14, fontweight='bold', color='darkred', pad=20)

# Annotate bars with the growth rate values
for bar in bars:
    width = bar.get_width()
    ax2.text(width + 1, bar.get_y() + bar.get_height()/2,
             f'{width}%', va='center', fontsize=12, color='black')

# Ensure layout is properly adjusted
plt.tight_layout()

# Display the plots
plt.show()