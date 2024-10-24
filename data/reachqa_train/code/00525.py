import matplotlib.pyplot as plt
import numpy as np

# Data for the pie chart
labels = ['Solar Energy', 'Wind Energy', 'Hydropower', 'Biomass', 'Geothermal']
sizes = [25, 20, 30, 15, 10]
colors = ['#FFD700', '#1E90FF', '#228B22', '#8B4513', '#FF4500']
explode = (0.1, 0, 0, 0, 0)  # Explode the largest section to highlight Hydropower

# Data for the bar plot (growth percentages)
growth_rates = [5, 3, 7, 2, 4]  # Hypothetical growth rates for each energy source
bar_colors = colors

# Create a figure with a main plot and an inset for the bar chart
fig, ax1 = plt.subplots(figsize=(10, 8))

# Create the pie chart
wedges, texts, autotexts = ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
                                   startangle=140, pctdistance=0.85, textprops=dict(color="w"))

# Style the text
for text in texts:
    text.set_fontsize(10)
    text.set_color('black')
for autotext in autotexts:
    autotext.set_fontsize(8)
    autotext.set_weight('bold')

# Draw circle for 'doughnut' effect
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
ax1.axis('equal')

# Set title with a line break for better readability
plt.title("Distribution and Growth of Renewable Energy Sources\nin EcoLand - 2023", fontsize=14, weight='bold', y=1.05)

# Legend for pie chart
plt.legend(wedges, labels, title="Energy Sources", loc="upper right", bbox_to_anchor=(1, 0, 0.5, 1))

# Create an inset for the bar plot
ax2 = fig.add_axes([0.65, 0.05, 0.3, 0.3])  # [left, bottom, width, height]

# Create the bar plot
ax2.bar(labels, growth_rates, color=bar_colors, alpha=0.7)
ax2.set_title('Yearly Growth (%)', fontsize=10, weight='bold')
ax2.set_ylabel('Growth Rate (%)')
ax2.set_xticklabels(labels, rotation=45, ha="right", fontsize=8)
ax2.set_yticks(np.arange(0, 10, 2))
ax2.set_ylim(0, 8)

# Adjust layout for better fit
plt.tight_layout()

# Show the combined chart
plt.show()