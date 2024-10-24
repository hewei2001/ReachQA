import matplotlib.pyplot as plt
import numpy as np

# Define regions and coffee types
regions = ['Americas', 'Europe', 'Asia-Pacific']
coffee_types = ['Espresso', 'Latte', 'Cold Brew']

# Adjusted data: percentage of consumption for each coffee type by region
consumption_data = np.array([
    [55, 25, 20],  # Americas: Espresso, Latte, Cold Brew
    [35, 40, 25],  # Europe: Espresso, Latte, Cold Brew
    [20, 30, 50]   # Asia-Pacific: Espresso, Latte, Cold Brew
])

# Additional data: average price of coffee types by region
price_data = np.array([
    [3.0, 3.5, 4.0],  # Americas: Espresso, Latte, Cold Brew
    [2.5, 3.0, 3.2],  # Europe: Espresso, Latte, Cold Brew
    [4.0, 4.5, 4.8]   # Asia-Pacific: Espresso, Latte, Cold Brew
])

# Create a figure with two subplots
fig = plt.figure(figsize=(14, 8))

# 3D bar plot for consumption data
ax1 = fig.add_subplot(121, projection='3d')
xpos, ypos = np.meshgrid(np.arange(len(regions)), np.arange(len(coffee_types)))
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros_like(xpos)
dz = consumption_data.flatten()
dx = dy = 0.5
colors = ['#8B4513', '#DEB887', '#D2B48C']

for i in range(len(coffee_types)):
    ax1.bar3d(xpos[ypos == i], ypos[ypos == i], zpos[ypos == i], dx, dy, dz[ypos == i], 
             color=colors[i], alpha=0.8, label=coffee_types[i])

ax1.set_xlabel('Regions', fontsize=12, labelpad=10)
ax1.set_ylabel('Coffee Types', fontsize=12, labelpad=10)
ax1.set_zlabel('Percentage (%)', fontsize=12, labelpad=10)
ax1.set_xticks(np.arange(len(regions)))
ax1.set_xticklabels(regions, rotation=45, ha='right', fontsize=10)
ax1.set_yticks(np.arange(len(coffee_types)))
ax1.set_yticklabels(coffee_types, fontsize=10)
ax1.set_zlim(0, 100)
ax1.set_title('Regional Coffee Consumption\nBreakdown: 2023', fontsize=16, weight='bold', pad=20)
ax1.legend(title='Coffee Types', loc='upper left', fontsize=10)

# Grouped bar chart for price data
ax2 = fig.add_subplot(122)
bar_width = 0.2
indices = np.arange(len(regions))

for i, coffee_type in enumerate(coffee_types):
    ax2.bar(indices + i * bar_width, price_data[:, i], bar_width, label=coffee_type, color=colors[i], alpha=0.8)

ax2.set_xlabel('Regions', fontsize=12)
ax2.set_ylabel('Average Price ($)', fontsize=12)
ax2.set_title('Average Coffee Prices by Region', fontsize=16, weight='bold')
ax2.set_xticks(indices + bar_width)
ax2.set_xticklabels(regions, rotation=45, ha='right', fontsize=10)
ax2.legend(title='Coffee Types', fontsize=10)

# Adjust layout for better readability
plt.tight_layout()
plt.show()