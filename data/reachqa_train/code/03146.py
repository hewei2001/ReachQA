import matplotlib.pyplot as plt

# Define ancient empires and their fictional agricultural productivity data
empires = ['Ancient Egypt', 'Mayan Empire', 'Roman Empire', 'Han Dynasty', 'Maurya Empire']
egypt_yield = [1200, 1500, 1400, 1300, 1450, 1550, 1600, 1500, 1400, 1380]
maya_yield = [950, 1000, 970, 930, 1050, 1100, 1080, 1150, 980, 1020]
rome_yield = [2000, 2050, 2100, 1900, 1950, 1980, 2200, 2300, 2150, 2250]
han_yield = [1700, 1650, 1800, 1750, 1850, 1900, 1600, 1720, 1800, 1820]
maurya_yield = [800, 750, 770, 790, 820, 830, 850, 870, 880, 860]

# Organize the data for the boxplot
boxplot_data = [egypt_yield, maya_yield, rome_yield, han_yield, maurya_yield]

# Additional data for a line plot to show the highest yield per year (fictional)
years = range(1, 11)
highest_yields = [max(yields) for yields in zip(egypt_yield, maya_yield, rome_yield, han_yield, maurya_yield)]

# Create the subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))

# Define colors for each boxplot
colors = ['#FFD700', '#008080', '#FF4500', '#8A2BE2', '#228B22']

# Boxplot properties
boxprops = dict(linestyle='-', linewidth=1.5, color='darkgray')
medianprops = dict(color='black', linewidth=1.5)
whiskerprops = dict(linestyle='--', linewidth=1.2, color='darkgray')
capprops = dict(color='darkgray')
flierprops = dict(marker='o', color='red', alpha=0.5)

# Create the box plots on the first subplot
bp = ax1.boxplot(boxplot_data, patch_artist=True, vert=True, notch=True,
                 boxprops=boxprops, whiskerprops=whiskerprops,
                 capprops=capprops, flierprops=flierprops,
                 medianprops=medianprops)

# Set the color of each box
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Customize the first subplot (boxplot)
ax1.set_xticklabels(empires, fontsize=11, fontweight='bold', rotation=30, ha='right')
ax1.set_ylabel("Agricultural Yield (tons/year)", fontsize=12, fontweight='bold')
ax1.set_title("Golden Harvest of Antiquity:\nAgricultural Productivity of Ancient Empires", fontsize=14, fontweight='bold', pad=20)
ax1.yaxis.grid(True, linestyle='--', alpha=0.6)

# Legend for the first plot
handles = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
ax1.legend(handles, empires, title='Ancient Empires', loc='upper right', fontsize=9)

# Create the line plot on the second subplot
ax2.plot(years, highest_yields, marker='o', linestyle='-', color='#1E90FF', linewidth=2)

# Customize the second subplot (line plot)
ax2.set_xlabel("Year", fontsize=12, fontweight='bold')
ax2.set_ylabel("Highest Yield (tons/year)", fontsize=12, fontweight='bold')
ax2.set_title("Yearly Highest Agricultural Yield\nAcross Ancient Empires", fontsize=14, fontweight='bold', pad=20)
ax2.grid(True, linestyle='--', alpha=0.6)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()