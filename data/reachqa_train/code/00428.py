import matplotlib.pyplot as plt
import numpy as np

# Data setup
age_groups = ['Children', 'Teenagers', 'Adults', 'Seniors']
instruments = ['Piano', 'Guitar', 'Violin', 'Drums', 'Flute']

# Number of people in each age group who prefer each instrument
preferences = np.array([
    [35, 45, 50, 10, 25],  # Children
    [25, 55, 35, 45, 15],  # Teenagers
    [45, 40, 25, 35, 20],  # Adults
    [30, 25, 15, 5, 40]    # Seniors
])

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Define bar positions and width
bar_width = 0.15
indices = np.arange(len(age_groups))

# Plotting each instrument's preference by age group
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

for i, instrument in enumerate(instruments):
    bar = ax.bar(indices + i * bar_width, preferences[:, i], width=bar_width, label=instrument, color=colors[i])
    # Annotating each bar with the preference numbers
    ax.bar_label(bar, label_type='edge', padding=3, fontsize=10)

# Setting labels and title
ax.set_xlabel('Age Groups', fontsize=12)
ax.set_ylabel('Number of People', fontsize=12)
ax.set_title('Harmony in the Notes:\nMusical Instrument Preference Among Different Age Groups',
             fontsize=16, fontweight='bold')
ax.set_xticks(indices + bar_width * 2)
ax.set_xticklabels(age_groups)
ax.legend(title='Instruments', fontsize=10)

# Adjust x-axis labels if needed
plt.xticks(rotation=0, fontsize=10)

# Adding grid for better readability
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)

# Improve the layout
plt.tight_layout()

# Display the plot
plt.show()