import matplotlib.pyplot as plt
import numpy as np

# Data for the original bar chart
industries = ['Transportation', 'Manufacturing', 'Energy', 'Retail', 'Technology']
initiatives_count_2023 = [20, 25, 35, 15, 30]  # Number of sustainability initiatives in 2023

# Additional data for trend analysis (2019-2023)
years = np.array([2019, 2020, 2021, 2022, 2023])
initiatives_trend = {
    'Transportation': [10, 15, 18, 19, 20],
    'Manufacturing': [12, 18, 22, 23, 25],
    'Energy': [20, 25, 28, 30, 35],
    'Retail': [8, 12, 13, 14, 15],
    'Technology': [15, 20, 25, 28, 30]
}

# Create a color scheme
colors = ['#76c7c0', '#f4a460', '#8fbc8f', '#ffa07a', '#6a5acd']

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
fig.suptitle("Industry Sustainability Initiatives Overview (2019-2023)", fontsize=16, fontweight='bold')

# Bar chart (Subplot 1)
positions = np.arange(len(industries))
bars = ax1.bar(positions, initiatives_count_2023, color=colors, edgecolor='black', width=0.6)
ax1.set_title("Initiatives Count in 2023", fontsize=14)
ax1.set_xlabel("Industry", fontsize=12)
ax1.set_ylabel("Number of Initiatives", fontsize=12)
ax1.set_xticks(positions)
ax1.set_xticklabels(industries, rotation=45, ha='right', fontsize=11)

# Annotate bars
for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, yval + 0.5, yval, ha='center', va='bottom', fontsize=10, fontweight='bold', color='darkslategray')

ax1.yaxis.grid(True, linestyle='--', alpha=0.7)

# Line chart (Subplot 2)
for i, industry in enumerate(industries):
    ax2.plot(years, initiatives_trend[industry], marker='o', color=colors[i], label=industry, linewidth=2)

ax2.set_title("Trend of Initiatives (2019-2023)", fontsize=14)
ax2.set_xlabel("Year", fontsize=12)
ax2.set_ylabel("Number of Initiatives", fontsize=12)
ax2.legend(title='Industries', fontsize=10, title_fontsize='11', loc='upper left', frameon=True)
ax2.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust layout
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Show the plot
plt.show()