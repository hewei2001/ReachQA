import matplotlib.pyplot as plt
import numpy as np

# Define data for the pie chart
sectors = ['Education', 'Healthcare', 'Technology', 'Agriculture', 'Finance']
awareness_levels = [25, 15, 20, 30, 10]

# Define related data for the bar chart
investment_levels = [18, 22, 35, 25, 15]

# Colors for sectors
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Create a figure with 1x2 subplots
fig, ax = plt.subplots(1, 2, figsize=(16, 9))

# Donut pie chart
wedges, texts, autotexts = ax[0].pie(
    awareness_levels,
    labels=sectors,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,
    pctdistance=0.85,
    explode=(0.1, 0, 0, 0, 0)
)
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)
ax[0].set_title('Awareness Levels by Sector\nSurvey Results of 2023', fontsize=14, fontweight='bold', pad=20)
plt.setp(autotexts, size=10, weight='bold', color='darkblue')
plt.setp(texts, size=12, weight='bold')

# Bar chart for investment levels
x_pos = np.arange(len(sectors))
ax[1].bar(x_pos, investment_levels, color=colors, alpha=0.7)
ax[1].set_xticks(x_pos)
ax[1].set_xticklabels(sectors, rotation=45, ha='right')
ax[1].set_ylabel('Investment Level')
ax[1].set_title('Investment in Different Sectors\nAnalysis of 2023', fontsize=14, fontweight='bold', pad=20)

# Add data labels to the bar chart
for i, v in enumerate(investment_levels):
    ax[1].text(i, v + 1, str(v), ha='center', fontweight='bold', fontsize=10, color='darkblue')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()