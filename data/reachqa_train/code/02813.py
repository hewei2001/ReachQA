import matplotlib.pyplot as plt
import numpy as np

# Countries and preservation categories
countries = ['France', 'Italy', 'Greece', 'Egypt', 'India']
categories = ['Structural Restoration', 'Environmental Conservation', 
              'Cultural Preservation', 'Educational Programs']

# Percentage distribution of preservation efforts by category for each country
france_efforts = [40, 20, 25, 15]
italy_efforts = [35, 25, 30, 10]
greece_efforts = [30, 30, 25, 15]
egypt_efforts = [45, 15, 20, 20]
india_efforts = [25, 35, 20, 20]

# Collect data for plotting
data = np.array([france_efforts, italy_efforts, greece_efforts, egypt_efforts, india_efforts])

# Colors for each category
colors = ['#c0392b', '#27ae60', '#2980b9', '#f1c40f']

# Calculate average percentage investment for each category across all countries
average_efforts = np.mean(data, axis=0)

# Plotting the percentage bar chart
fig, ax1 = plt.subplots(figsize=(14, 8))

# Set the bar width
bar_width = 0.5
positions = np.arange(len(countries))

# Plot stacked bars for each country
for i, category in enumerate(categories):
    bottoms = np.sum(data[:, :i], axis=1) if i > 0 else np.zeros(len(countries))
    ax1.bar(positions, data[:, i], bottom=bottoms, width=bar_width, label=category, color=colors[i])

# Labeling and aesthetics
ax1.set_title('Historic Monument Preservation Efforts\nby Country (2023)', fontsize=16, fontweight='bold', pad=20)
ax1.set_ylabel('Percentage of Total Investment', fontsize=12, labelpad=10)
ax1.set_xticks(positions)
ax1.set_xticklabels(countries, fontsize=11)
ax1.set_ylim(0, 100)
ax1.legend(title="Preservation Categories", fontsize=10, title_fontsize=12, loc='upper left')
ax1.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

# Add a secondary y-axis for average trend line
ax2 = ax1.twinx()
ax2.set_ylabel('Average Investment Percentage', fontsize=12, labelpad=10)
ax2.plot(categories, average_efforts, color='purple', marker='o', linestyle='--', linewidth=2, label='Average Investment')
ax2.set_ylim(0, 50)
ax2.legend(loc='upper right', fontsize=10)

# Display percentage values on the bars
for i, country_data in enumerate(data):
    for j, value in enumerate(country_data):
        ax1.text(i, bottoms[j] + value / 2, f'{value}%', ha='center', va='center', color='white', fontsize=10)

# Annotation for the line plot
for i, avg_value in enumerate(average_efforts):
    ax2.text(i, avg_value + 1, f'{avg_value:.1f}%', ha='center', va='bottom', color='purple', fontsize=10)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()