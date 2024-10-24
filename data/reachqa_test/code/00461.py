import matplotlib.pyplot as plt
import numpy as np

# Years of analysis
years = np.array([2021, 2022, 2023, 2024, 2025])

# Market share data (in percentage) for each category
consumer_electronics = np.array([30, 31, 33, 35, 36])
cloud_services = np.array([20, 22, 25, 27, 30])
social_media = np.array([25, 24, 23, 22, 21])

# Combine the data into a single array for the stacked bar chart
data = np.array([consumer_electronics, cloud_services, social_media]).T

# Create a stacked bar chart
fig, ax = plt.subplots(figsize=(12, 7))

# Define a color palette
colors = ['#4F94D4', '#FFA500', '#B2E1A2']

# Create stacked bars
ax.bar(years, data[:, 0], label='Consumer Electronics', color=colors[0], alpha=0.85)
ax.bar(years, data[:, 1], bottom=data[:, 0], label='Cloud Services', color=colors[1], alpha=0.85)
ax.bar(years, data[:, 2], bottom=data[:, 0] + data[:, 1], label='Social Media', color=colors[2], alpha=0.85)

# Titles and labels with line breaks for clarity
ax.set_title("Market Share Distribution of Tech Giants\n(2021-2025)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Market Share (%)", fontsize=12)
ax.set_xticks(years)

# Y-axis limit for better visibility
ax.set_ylim(0, 100)

# Adding horizontal grid lines
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.5)

# Adding the legend outside the plot area
ax.legend(title='Market Segments', fontsize=10, loc='upper left', bbox_to_anchor=(1, 1))

# Annotate the top of each stacked section with percentages
for i in range(len(years)):
    ax.text(years[i], data[i, 0] / 2, f'{data[i, 0]}%', ha='center', va='center', fontsize=9, color='black')
    ax.text(years[i], data[i, 0] + data[i, 1] / 2, f'{data[i, 1]}%', ha='center', va='center', fontsize=9, color='black')
    ax.text(years[i], data[i, 0] + data[i, 1] + data[i, 2] / 2, f'{data[i, 2]}%', ha='center', va='center', fontsize=9, color='black')

# Rotate x-axis labels for better visibility
plt.xticks(rotation=45)

# Adjust layout to avoid overlap and ensure visibility of elements
plt.tight_layout()

# Show the plot
plt.show()