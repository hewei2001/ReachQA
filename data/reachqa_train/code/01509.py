import matplotlib.pyplot as plt

# Data: Percentage allocations of space exploration missions by destination
labels = ['Moon', 'Mars', 'Jupiter', 'Saturn', 'Outer Space']
missions = [25, 35, 10, 10, 20]

# Colors for each segment in the pie chart
colors = ['#FFD700', '#FF6347', '#8A2BE2', '#4682B4', '#32CD32']

# Creating the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    missions,
    labels=labels,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    explode=(0.1, 0, 0, 0, 0.1),
    shadow=True
)

# Customize font properties for better visibility
for text in texts:
    text.set_fontsize(10)
    text.set_fontweight('bold')

for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_color('white')
    autotext.set_fontweight('bold')

# Setting the title of the chart
ax.set_title(
    "Allocation of Space Exploration Missions by Destination\n(2023-2033)",
    fontsize=14, fontweight='bold', pad=20
)

# Position the legend outside the pie chart for clarity
ax.legend(
    wedges, labels,
    title="Destinations",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1)
)

# Ensure the layout fits well on display
plt.tight_layout()

# Display the plot
plt.show()