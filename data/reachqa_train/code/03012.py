import matplotlib.pyplot as plt
import numpy as np

# Data for the donut pie chart
categories = ['Critically Endangered', 'Endangered', 'Vulnerable', 'Near Threatened', 'Least Concern']
species_count = [4, 7, 12, 15, 30]  # Fictional number of cat species in each category

# Colors for the categories
colors = ['#e74c3c', '#e67e22', '#f1c40f', '#2ecc71', '#3498db']

# Create the figure
fig, ax = plt.subplots(figsize=(10, 7), subplot_kw=dict(aspect="equal"))

# Plotting the donut pie chart
wedges, texts, autotexts = ax.pie(species_count, labels=categories, autopct='%1.1f%%',
                                  startangle=140, colors=colors, pctdistance=0.85,
                                  wedgeprops=dict(width=0.3, edgecolor='w'),
                                  shadow=True)

# Customize the autotexts
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)
    autotext.set_weight('bold')

# Draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Title and legend
plt.title('Global Cat Species Conservation Status\nin 2023', fontsize=14, fontweight='bold', pad=20)
ax.legend(wedges, categories, title="Conservation Status", loc='center left', bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()