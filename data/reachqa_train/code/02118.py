import matplotlib.pyplot as plt

# Data: Distribution percentages of programming languages
languages = ['Python', 'JavaScript', 'Java', 'C++', 'Ruby', 'Go', 'Rust', 'PHP']
usage_percentages = [29, 24, 16, 12, 7, 5, 4, 3]

# Colors for each segment
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700', '#FFA07A', '#98FB98', '#C2C2F0']

# Create the pie chart
fig, ax = plt.subplots(figsize=(9, 9))

# Explode the largest segment for emphasis
explode = (0.1, 0, 0, 0, 0, 0, 0, 0)

# Plotting the pie chart
ax.pie(usage_percentages, labels=languages, autopct='%1.1f%%', startangle=140, colors=colors, explode=explode, shadow=True)

# Ensuring the pie chart is a circle
ax.axis('equal')

# Title with backstory context
ax.set_title('Programming Languages in Open Source Projects\nSurvey of 2025', fontsize=15, fontweight='bold', pad=20)

# Add a legend
ax.legend(languages, title="Languages", loc='upper right', bbox_to_anchor=(1.2, 1))

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()