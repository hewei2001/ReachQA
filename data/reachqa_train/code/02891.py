import matplotlib.pyplot as plt
import numpy as np

# Data for the ring chart
cuisines = ['Italian', 'Chinese', 'Indian', 'Mexican', 'Japanese', 'French', 'Thai', 'Greek']
vote_percentages = [18, 22, 16, 14, 10, 8, 7, 5]

# Colors for each segment
colors = ['#FF5733', '#FFBD33', '#75FF33', '#33FF57', '#33FFBD', '#3375FF', '#8A33FF', '#FF33A6']

# Plot the ring chart
fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(aspect="equal"))

# Create wedges for the pie chart, which will appear as a ring chart
wedges, texts, autotexts = ax.pie(
    vote_percentages, labels=cuisines, startangle=90,
    colors=colors, wedgeprops=dict(width=0.3, edgecolor='white'),
    autopct='%1.1f%%', pctdistance=0.85, textprops=dict(color="w", weight='bold', fontsize=10)
)

# Adding a central circle to convert the pie chart to a ring (donut) chart
centre_circle = plt.Circle((0, 0), 0.65, fc='white')
ax.add_artist(centre_circle)

# Title of the chart
plt.title('World Cuisine Preferences\nat International Food Festival', fontsize=16, pad=20)

# Customize autotexts to be more readable
for autotext in autotexts:
    autotext.set_color('black')

# Legend with title outside the plot
plt.legend(wedges, cuisines, title="Cuisines", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Automatic layout adjustment
plt.tight_layout()

# Show the chart
plt.show()