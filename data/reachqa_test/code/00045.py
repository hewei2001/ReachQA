import matplotlib.pyplot as plt
import numpy as np

# Define the programming languages and their respective number of developers in millions
languages = ['Python', 'JavaScript', 'Java', 'C#', 'C++', 'PHP', 'Ruby', 'Go']
developers_count = np.array([10.2, 9.5, 8.0, 6.2, 5.3, 3.8, 2.7, 1.8])  # in millions

# Calculate the percentage of developers for the pie chart
percentages = 100 * developers_count / np.sum(developers_count)

# Define the positions for the bars
x_positions = np.arange(len(languages))

# Create the subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# Bar chart
bars = ax1.bar(x_positions, developers_count, color=['#357ABD', '#E78124', '#66A3C9', '#A5B3D1', '#FFBF47', '#D4725E', '#BFBFBF', '#5C848E'], width=0.6)
ax1.set_title('Popularity of Programming Languages in 2023\nNumber of Active Developers', fontsize=14, pad=20)
ax1.set_xlabel('Programming Languages', fontsize=12)
ax1.set_ylabel('Developers (in Millions)', fontsize=12)
ax1.set_xticks(x_positions)
ax1.set_xticklabels(languages, rotation=45, ha='right')
ax1.set_ylim(0, max(developers_count) + 2)
ax1.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Add data annotations for the bar chart
for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, yval + 0.2, f'{yval:.1f}M', ha='center', va='bottom', fontsize=10, fontweight='bold')

# Pie chart
ax2.pie(percentages, labels=languages, autopct='%1.1f%%', startangle=90, colors=['#357ABD', '#E78124', '#66A3C9', '#A5B3D1', '#FFBF47', '#D4725E', '#BFBFBF', '#5C848E'], pctdistance=0.85)
ax2.set_title('Proportion of Active Developers\nby Programming Language in 2023', fontsize=14, pad=20)
ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Draw a circle at the center of the pie chart for aesthetics
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Adjust layout to ensure everything fits without overlap
plt.tight_layout()

# Display the plot
plt.show()