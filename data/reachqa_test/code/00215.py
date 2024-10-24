import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Set the style and color palette
sns.set_theme(style="whitegrid")
palette = sns.color_palette("pastel")

# Define the years for the study
years = np.arange(2018, 2024)

# Define sales data (in thousands) for each fantasy subgenre
epic_fantasy_sales = [250, 260, 270, 290, 320, 350]
urban_fantasy_sales = [180, 185, 190, 200, 215, 230]
dark_fantasy_sales = [160, 165, 175, 185, 195, 210]

# Calculate cumulative sales for overlay line plot
cumulative_sales = np.array(epic_fantasy_sales) + np.array(urban_fantasy_sales) + np.array(dark_fantasy_sales)

# Subgenres and associated data
subgenres = ['Epic Fantasy', 'Urban Fantasy', 'Dark Fantasy']
sales_data = [epic_fantasy_sales, urban_fantasy_sales, dark_fantasy_sales]

# Create a figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Width of a single bar
bar_width = 0.25

# Create bars for each subgenre
for i, sales in enumerate(sales_data):
    bar_positions = np.arange(len(years)) + i * bar_width
    ax.bar(bar_positions, sales, width=bar_width, color=palette[i], edgecolor='grey', alpha=0.8, label=subgenres[i], hatch='/' * i)

# Overlay cumulative sales as a line plot
ax.plot(np.arange(len(years)) + bar_width, cumulative_sales, color='purple', marker='o', linewidth=2, linestyle='--', label='Total Cumulative Sales')

# Annotate the cumulative sales line
for (x, y) in zip(np.arange(len(years)) + bar_width, cumulative_sales):
    ax.text(x, y + 5, f'{y}', ha='center', fontsize=9, color='purple')

# Title and labels
ax.set_title('Enchantment in Numbers:\nFantasy Book Sales from 2018 to 2023', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Sales (Thousands)', fontsize=12)

# Customize x-ticks
ax.set_xticks(np.arange(len(years)) + bar_width)
ax.set_xticklabels(years, rotation=45, ha='right')

# Vertical grid lines and layout adjustment
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_axisbelow(True)

# Legend outside the plot area
ax.legend(title='Fantasy Subgenres', fontsize=10, title_fontsize=11, loc='upper left', bbox_to_anchor=(1, 1))

# Add a footnote
plt.figtext(0.99, 0.01, 'Note: All sales figures are in thousands.', horizontalalignment='right', fontsize=9, color='gray')

# Ensure layout fits well
plt.tight_layout()

# Show plot
plt.show()