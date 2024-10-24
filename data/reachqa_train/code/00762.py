import matplotlib.pyplot as plt
import numpy as np

# Define commodities and their trade volumes (in thousands of tons)
commodities = ['Martian Minerals', 'Earthly Technologies', 
               'Agricultural Products', 'Water Resources', 
               'Medical Supplies']
trade_volumes = [200, 150, 180, 120, 90]

# Additional data: Estimated trade values in billions
trade_values = [50, 70, 55, 40, 30]

# Define colors for the bars and pie chart segments
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#F3FF33']

# Create a figure with two subplots arranged horizontally
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

# First subplot: Bar chart for trade volumes
bars = ax1.bar(np.arange(len(commodities)), trade_volumes, color=colors, edgecolor='black')

ax1.set_title('Intergalactic Trade Commodities:\nEarth to Mars Exchange in 2150', fontsize=16, fontweight='bold')
ax1.set_xlabel('Commodities', fontsize=14)
ax1.set_ylabel('Trade Volume (in thousands of tons)', fontsize=14)
ax1.set_xticks(np.arange(len(commodities)))
ax1.set_xticklabels(commodities, rotation=45, ha='right')

# Add data labels above bars
for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, yval + 3, f'{yval}k', ha='center', va='bottom', fontsize=12)

# Add legend for the bar chart
ax1.legend(bars, ['Rich Martian ore deposits', 'Advanced Earth tech gadgets', 
                  'Essential food supplies', 'Vital water resources', 
                  'Crucial medical kits'],
           title='Commodity Description', loc='upper right')

# Add a grid for the y-axis
ax1.yaxis.grid(True, linestyle='--', alpha=0.6)

# Second subplot: Pie chart for trade values
ax2.pie(trade_values, labels=commodities, autopct='%1.1f%%', startangle=140, colors=colors, wedgeprops={'edgecolor': 'black'})
ax2.set_title('Trade Values in Billions: Distribution', fontsize=14, fontweight='bold')

# Tight layout to prevent overlap
plt.tight_layout()

# Show the combined plots
plt.show()