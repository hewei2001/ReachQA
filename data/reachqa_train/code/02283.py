import matplotlib.pyplot as plt
import numpy as np

# Define the types of tea and countries for the study
tea_types = ['Black', 'Green', 'Herbal', 'Oolong']
countries = ['United Kingdom', 'Japan', 'China', 'United States']

# Create artificial data for the number of respondents preferring each type of tea
# Rows represent countries, columns represent types of tea
tea_data = np.array([
    [240, 60, 30, 10],   # United Kingdom
    [50, 180, 10, 60],   # Japan
    [100, 150, 30, 20],  # China
    [130, 80, 70, 20]    # United States
])

# Initialize the plot
fig, ax = plt.subplots(figsize=(12, 7))

# Define colors for each country
colors = ['#8B4513', '#6B8E23', '#D2691E', '#DAA520']

# X positions for the grouped bar charts
x_pos = np.arange(len(tea_types))

# Bar width
bar_width = 0.2

# Plot histograms (as bar plots here for clarity)
for i, country in enumerate(countries):
    ax.bar(x_pos + i * bar_width, tea_data[i], width=bar_width, label=country, color=colors[i], alpha=0.8)

# Customize x-axis with tea types
ax.set_xticks(x_pos + bar_width * 1.5)
ax.set_xticklabels(tea_types, fontsize=12)

# Titles and labels
ax.set_title('Tea Consumption Preferences by Country\nSurvey 2023', fontsize=16, fontweight='bold')
ax.set_xlabel('Type of Tea', fontsize=12)
ax.set_ylabel('Number of Respondents', fontsize=12)

# Legend
ax.legend(title='Countries', fontsize=10, loc='upper right')

# Customize y-axis grid lines
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()