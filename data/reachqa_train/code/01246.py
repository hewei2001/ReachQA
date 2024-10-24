import matplotlib.pyplot as plt
import numpy as np

# Define brew methods and age groups
brew_methods = ['Espresso', 'French Press', 'Drip Brew', 'Cold Brew']
age_groups = ['Teens (13-19)', 'Young Adults (20-35)', 'Adults (36-55)', 'Seniors (56+)']

# Average cups per week by brew method for each age group
consumption_data = [
    [1.5, 0.8, 2.2, 1.0],   # Teens
    [3.8, 2.5, 4.0, 3.0],   # Young Adults
    [4.5, 3.0, 5.5, 2.5],   # Adults
    [2.0, 1.5, 2.5, 1.0]    # Seniors
]

# Create a figure and a set of subplots
fig, ax = plt.subplots(figsize=(12, 7))

# Define bar width
bar_width = 0.2

# Define positions for each group of bars
x_positions = np.arange(len(brew_methods))

# Plot bars for each age group with annotations
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']  # Colors for each age group
for i, (age, color) in enumerate(zip(age_groups, colors)):
    offset = i * bar_width
    bars = ax.bar(x_positions + offset, consumption_data[i], width=bar_width, label=age, color=color)
    
    # Annotate bars with data values
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 0.1, f'{yval:.1f}', ha='center', va='bottom', fontsize=10, color='black')

# Set x-ticks and x-labels
ax.set_xticks(x_positions + bar_width * (len(age_groups) - 1) / 2)
ax.set_xticklabels(brew_methods, rotation=45, ha='right')

# Title and labels
ax.set_title('Average Weekly Coffee Consumption\nby Brew Method and Age Group', fontsize=16, fontweight='bold')
ax.set_xlabel('Brew Method', fontsize=12)
ax.set_ylabel('Average Cups per Week', fontsize=12)

# Grid lines
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Legend
ax.legend(title='Age Groups', loc='upper left', fontsize=10)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()