import matplotlib.pyplot as plt
import numpy as np

# Expanded data setup
age_groups = ['Children', 'Teenagers', 'Young Adults', 'Middle-Aged', 'Seniors']
instruments = ['Piano', 'Guitar', 'Violin', 'Drums', 'Flute', 'Trumpet', 'Saxophone']

# Number of people in each age group who prefer each instrument
# Note: These numbers are explicitly constructed for this example
preferences = np.array([
    [30, 40, 45, 20, 10, 15, 25],  # Children
    [20, 55, 35, 45, 20, 25, 30],  # Teenagers
    [50, 35, 30, 40, 15, 30, 20],  # Young Adults
    [60, 50, 30, 25, 10, 20, 15],  # Middle-Aged
    [20, 25, 20, 10, 50, 20, 40]   # Seniors
])

# Statistical measures: standard deviation (example data)
std_devs = np.array([
    [5, 3, 4, 2, 1, 2, 3],  # Children
    [4, 5, 2, 3, 2, 2, 4],  # Teenagers
    [3, 4, 3, 4, 2, 3, 3],  # Young Adults
    [4, 3, 2, 3, 1, 2, 2],  # Middle-Aged
    [3, 2, 4, 2, 3, 3, 4]   # Seniors
])

# Create the plot
fig, ax = plt.subplots(figsize=(14, 9))

# Define bar positions and width
bar_width = 0.12
indices = np.arange(len(age_groups))

# Colors for the instruments
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']

# Plotting each instrument's preference by age group with error bars
for i, instrument in enumerate(instruments):
    bar = ax.bar(
        indices + i * bar_width, 
        preferences[:, i], 
        width=bar_width, 
        yerr=std_devs[:, i], 
        label=instrument, 
        color=colors[i],
        capsize=4
    )
    ax.bar_label(bar, label_type='edge', padding=3, fontsize=9)

# Set labels and title
ax.set_xlabel('Age Groups', fontsize=12)
ax.set_ylabel('Number of People', fontsize=12)
ax.set_title('Harmony in the Notes:\nMusical Instrument Preference Among Varied Age Groups', fontsize=16, fontweight='bold')
ax.set_xticks(indices + bar_width * (len(instruments) / 2))
ax.set_xticklabels(age_groups, fontsize=10)

# Add a trend line for the average preference across age groups
average_preferences = preferences.mean(axis=1)
ax.plot(indices + bar_width * (len(instruments) / 2 - 0.5), average_preferences, label='Average Preference', color='black', linestyle='--', marker='o')

# Add legend
ax.legend(title='Instruments', fontsize=9)

# Adding grid for better readability
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)

# Improve the layout
plt.tight_layout()

# Display the plot
plt.show()