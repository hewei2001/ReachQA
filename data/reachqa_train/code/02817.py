import matplotlib.pyplot as plt
import numpy as np

# Define the age categories with finer granularity
age_categories = [
    '13-15 years', '16-17 years', '18-20 years', '21-24 years',
    '25-29 years', '30-34 years', '35-39 years', '40-44 years',
    '45-49 years', '50-54 years', '55-59 years', '60-64 years', '65+ years'
]

# Complex distribution using a manually crafted pattern
subscriber_distribution = [5, 6, 9, 10, 12, 18, 9, 6, 8, 7, 5, 3, 2]

# Define colors for each age group slice with a gradient effect
colors = plt.cm.viridis(np.linspace(0, 1, len(age_categories)))

# Highlight the dominant age categories slices (25-34 years)
explode = [0, 0, 0, 0, 0.1, 0.1, 0, 0, 0, 0, 0, 0, 0]

# Create the pie chart
fig, ax = plt.subplots(figsize=(12, 9))
wedges, texts, autotexts = ax.pie(
    subscriber_distribution,
    labels=age_categories,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    explode=explode,
    shadow=True,
    wedgeprops={'edgecolor': 'black', 'linewidth': 1},
    textprops={'fontsize': 9}
)

# Add annotations for additional statistical information
total = sum(subscriber_distribution)
median_index = len(subscriber_distribution) // 2
median_value = subscriber_distribution[median_index]
median_angle = (360 * sum(subscriber_distribution[:median_index]) / total) + 360 * (median_value / (2 * total))
ax.annotate('Median Group',
            xy=(0.9 * np.cos(np.radians(median_angle)), 0.9 * np.sin(np.radians(median_angle))),
            xytext=(1.5, 1.5),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, fontweight='bold')

# Customize the percentage labels
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_weight('bold')

# Add a multi-line title for readability
plt.title(
    "Detailed Demographic Distribution\nof Online Streaming Subscribers in 2023", 
    fontsize=14, fontweight='bold', ha='center'
)

# Add a custom legend
plt.legend(wedges, age_categories, title="Age Groups", loc='center left', bbox_to_anchor=(1, 0, 0.5, 1), fontsize=9)

# Adjust layout to ensure no overlaps
plt.tight_layout()

# Add a secondary bar chart for trend comparison
fig, ax2 = plt.subplots(figsize=(12, 4))
previous_year_distribution = [4, 5, 8, 9, 10, 15, 8, 5, 7, 6, 4, 2, 2]  # Example data for a previous year
bar_width = 0.35
indices = np.arange(len(age_categories))

# Plotting current year data
bars1 = ax2.bar(indices - bar_width/2, subscriber_distribution, bar_width, label='2023', color='#66B3FF')

# Plotting previous year data
bars2 = ax2.bar(indices + bar_width/2, previous_year_distribution, bar_width, label='2022', color='#FF9999')

# Label and format bar chart
ax2.set_title("Comparison of Subscriber Distribution Across Years", fontsize=14, fontweight='bold')
ax2.set_ylabel('Number of Subscribers')
ax2.set_xticks(indices)
ax2.set_xticklabels(age_categories, rotation=45, ha='right')
ax2.legend()

# Adjust layout for the bar chart
plt.tight_layout()

# Show plots
plt.show()