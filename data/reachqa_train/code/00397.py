import matplotlib.pyplot as plt
import numpy as np

# Define the sectors and their investment percentages
sectors = ['Artificial Intelligence', 'Renewable Energy', 'Biotechnology', 
           'Space Exploration', 'Quantum Computing', 'Advanced Robotics']
investment_percentages = [25, 20, 15, 10, 20, 10]

# Define projected growth rates (arbitrary data for the demonstration)
projected_growth_rates = [7, 5, 6, 8, 9, 4]  # in percentage

# Define colors for each sector
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6']

# Define an explode pattern to highlight a few sectors more prominently
explode = (0.1, 0, 0.1, 0, 0.1, 0)

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# Pie chart
wedges, texts, autotexts = ax1.pie(
    investment_percentages, 
    labels=sectors, 
    autopct='%1.1f%%',
    startangle=140, 
    colors=colors, 
    explode=explode, 
    shadow=True,
    textprops=dict(color="w")
)

# Set custom style for text elements
for text in texts:
    text.set_fontsize(10)
    text.set_color("black")
for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_color("black")

ax1.set_title('Investment Distribution in 2030', fontsize=14, pad=10)

# Bar chart
x_pos = np.arange(len(sectors))
bars = ax2.bar(x_pos, projected_growth_rates, color=colors, edgecolor='black')

# Adding data labels to the bars
for bar in bars:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, yval + 0.2, f'{yval}%', ha='center', va='bottom', fontsize=10)

# Set title and labels for the bar chart
ax2.set_title('Projected Growth Rates', fontsize=14, pad=10)
ax2.set_xticks(x_pos)
ax2.set_xticklabels(sectors, rotation=45, ha='right')
ax2.set_ylabel('Growth Rate (%)')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the combined plot
plt.show()