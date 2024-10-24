import matplotlib.pyplot as plt
import numpy as np

# Original data for the pie chart
hobbies = ['Reading', 'Gardening', 'Cooking', 'Painting', 'Cycling', 'Photography', 'Gaming']
percentages = [25, 20, 15, 10, 10, 10, 10]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c4e17f']

# New data for the bar chart
average_hours = [5, 4, 3, 2, 2, 3, 4]

# Set up the subplots
fig, axs = plt.subplots(1, 2, figsize=(16, 8))

# Create the pie chart
explode = [0.1 if hobby == 'Reading' else 0 for hobby in hobbies]
wedges, texts, autotexts = axs[0].pie(percentages, labels=hobbies, colors=colors, autopct='%1.1f%%', 
                                      startangle=140, explode=explode, shadow=True)
axs[0].set_title("Hobby Distribution in Hobbyville\n2023 Survey Results", fontsize=14, fontweight='bold', pad=20)
plt.setp(texts, size=10)
plt.setp(autotexts, size=10, weight='bold')
axs[0].legend(wedges, hobbies, title="Hobbies", loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

# Create the bar chart
bar_colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854', '#ffd92f', '#e5c494']
bars = axs[1].barh(hobbies, average_hours, color=bar_colors, edgecolor='black')
axs[1].set_title("Average Hours Spent Weekly\non Hobbies", fontsize=14, fontweight='bold', pad=20)
axs[1].set_xlabel('Hours')
axs[1].set_ylabel('Hobbies')
axs[1].set_xlim(0, 6)

# Annotate bars with hours
for bar, hours in zip(bars, average_hours):
    axs[1].text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2, f'{hours} hrs',
                va='center', ha='left', fontsize=10)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()