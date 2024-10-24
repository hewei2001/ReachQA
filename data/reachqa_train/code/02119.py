import numpy as np
import matplotlib.pyplot as plt

# Years for the x-axis
years = np.array([2010, 2012, 2014, 2016, 2018, 2020])

# Popularity in thousands for each genre
fiction = np.array([30, 35, 40, 45, 50, 55])
non_fiction = np.array([20, 22, 25, 27, 30, 32])
mystery = np.array([15, 17, 19, 21, 25, 28])
sci_fi = np.array([10, 12, 14, 16, 18, 20])
fantasy = np.array([8, 10, 13, 16, 20, 25])
romance = np.array([5, 7, 10, 13, 15, 18])

# Colors for each genre
colors = ['#a8dadc', '#457b9d', '#1d3557', '#e63946', '#f4a261', '#2a9d8f']

# Create the stacked bar chart
fig, ax = plt.subplots(figsize=(12, 8))
ax.bar(years, fiction, color=colors[0], label='Fiction', alpha=0.9)
ax.bar(years, non_fiction, bottom=fiction, color=colors[1], label='Non-Fiction', alpha=0.9)
ax.bar(years, mystery, bottom=fiction + non_fiction, color=colors[2], label='Mystery', alpha=0.9)
ax.bar(years, sci_fi, bottom=fiction + non_fiction + mystery, color=colors[3], label='Science Fiction', alpha=0.9)
ax.bar(years, fantasy, bottom=fiction + non_fiction + mystery + sci_fi, color=colors[4], label='Fantasy', alpha=0.9)
ax.bar(years, romance, bottom=fiction + non_fiction + mystery + sci_fi + fantasy, color=colors[5], label='Romance', alpha=0.9)

# Title and labels
ax.set_title("The Rise and Influence of Literary Genres\nOver a Decade", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Number of Checkouts (Thousands)", fontsize=12)

# Rotate x-axis labels to prevent overlap
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha='right')

# Add a legend with larger spacing to avoid overlap
ax.legend(loc='upper left', title="Genres", bbox_to_anchor=(1.05, 1), fontsize=10, title_fontsize='12', frameon=False)

# Automatically adjust the layout to fit everything nicely
plt.tight_layout()

# Display the plot
plt.show()