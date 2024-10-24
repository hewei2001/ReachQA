import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# Years for the x-axis
years = np.array([2010, 2012, 2014, 2016, 2018, 2020])

# Popularity in thousands for each genre
fiction = np.array([30, 35, 40, 45, 50, 55])
non_fiction = np.array([20, 22, 25, 27, 30, 32])
mystery = np.array([15, 17, 19, 21, 25, 28])
sci_fi = np.array([10, 12, 14, 16, 18, 20])
fantasy = np.array([8, 10, 13, 16, 20, 25])
romance = np.array([5, 7, 10, 13, 15, 18])

# Calculate total popularity
total_popularity = fiction + non_fiction + mystery + sci_fi + fantasy + romance

# Calculate percentage growth for fiction
fiction_growth = (fiction / fiction[0] - 1) * 100

# Colors for each genre
colors = ['#a8dadc', '#457b9d', '#1d3557', '#e63946', '#f4a261', '#2a9d8f']

# Create figure with 2 subplots
fig = plt.figure(figsize=(14, 8))
gs = gridspec.GridSpec(1, 2, width_ratios=[3, 2])

# Stacked bar chart
ax1 = fig.add_subplot(gs[0])
ax1.bar(years, fiction, color=colors[0], label='Fiction', alpha=0.9)
ax1.bar(years, non_fiction, bottom=fiction, color=colors[1], label='Non-Fiction', alpha=0.9)
ax1.bar(years, mystery, bottom=fiction + non_fiction, color=colors[2], label='Mystery', alpha=0.9)
ax1.bar(years, sci_fi, bottom=fiction + non_fiction + mystery, color=colors[3], label='Science Fiction', alpha=0.9)
ax1.bar(years, fantasy, bottom=fiction + non_fiction + mystery + sci_fi, color=colors[4], label='Fantasy', alpha=0.9)
ax1.bar(years, romance, bottom=fiction + non_fiction + mystery + sci_fi + fantasy, color=colors[5], label='Romance', alpha=0.9)

ax1.set_title("The Rise and Influence of Literary Genres\nOver a Decade", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Number of Checkouts (Thousands)", fontsize=12)
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45, ha='right')
ax1.legend(loc='upper left', title="Genres", bbox_to_anchor=(1.05, 1), fontsize=10, title_fontsize='12', frameon=False)

# Line plot for percentage growth of fiction
ax2 = fig.add_subplot(gs[1])
ax2.plot(years, fiction_growth, marker='o', color='#e63946', linestyle='-', linewidth=2, label='Fiction Growth')
ax2.set_title("Fiction Popularity Growth (%)\nOver the Decade", fontsize=14, fontweight='bold')
ax2.set_xlabel("Year", fontsize=12)
ax2.set_ylabel("Growth (%)", fontsize=12)
ax2.grid(True, linestyle='--', alpha=0.7)
ax2.set_xticks(years)
ax2.set_xticklabels(years, rotation=45, ha='right')
ax2.legend(loc='upper left', fontsize=10, frameon=False)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()