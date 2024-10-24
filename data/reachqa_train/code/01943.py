import matplotlib.pyplot as plt
import numpy as np

# Define coffee types and their global consumption percentages
coffee_types = ['Espresso', 'Latte', 'Cappuccino', 'Americano', 'Cold Brew']
consumption_percentages = [30, 25, 20, 15, 10]

# Choose colors for each coffee type
colors = ['#e73030', '#f5c46b', '#a87f32', '#b5b5b5', '#35647f']

# Create a donut chart (pie chart with a hole in the middle)
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(consumption_percentages, labels=coffee_types, colors=colors,
                                  autopct='%1.1f%%', startangle=90, pctdistance=0.85,
                                  wedgeprops=dict(width=0.3, edgecolor='w'), explode=(0.1, 0, 0, 0, 0),
                                  shadow=True)

# Draw a circle at the center of pie to make it a donut
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Add a title to the plot
plt.title('Global Coffee Consumption by Type\nin 2023', fontsize=16, fontweight='bold', pad=20)

# Customize the percentage labels' properties
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(12)
    autotext.set_fontweight('bold')

# Add a legend with a proper position to avoid overlapping
ax.legend(wedges, coffee_types, title="Coffee Types", loc='center left', bbox_to_anchor=(1, 0.5),
          fontsize=10, title_fontsize='12')

# Ensure that the plot is a perfect circle
ax.axis('equal')  

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Show the plot
plt.show()