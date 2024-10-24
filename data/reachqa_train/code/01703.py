import matplotlib.pyplot as plt
import numpy as np

# Countries involved in the robotics innovation index
countries = ['USA', 'Germany', 'Japan', 'South Korea', 'China', 'France', 'UK', 'India']

# Hypothetical innovation index values for each country (composite score out of 100)
innovation_index = np.array([92, 88, 95, 91, 89, 85, 87, 80])

# Create a new figure for the bar chart
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting the bar chart
bars = ax.bar(countries, innovation_index, color=['navy', 'royalblue', 'skyblue', 'cornflowerblue', 'lightsteelblue', 'slategray', 'mediumslateblue', 'mediumpurple'])

# Annotate with the index scores
for bar, index in zip(bars, innovation_index):
    ax.annotate(f'{index}', xy=(bar.get_x() + bar.get_width() / 2, index),
                xytext=(0, 3), textcoords='offset points', ha='center', va='bottom', fontsize=11)

# Title and labels
ax.set_title("Global Robotics Innovation Index 2023:\nA Comparative Analysis", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Countries', fontsize=13)
ax.set_ylabel('Innovation Index (0-100)', fontsize=13)

# Rotate x-ticks for better readability
plt.xticks(rotation=45, ha='right')

# Adding gridlines for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Highlight the top innovator
ax.annotate('Top Innovator', xy=(2, 95), xytext=(3, 98),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12, color='black')

# Adjust layout to prevent overlap and ensure readability
plt.tight_layout()

# Display the plot
plt.show()