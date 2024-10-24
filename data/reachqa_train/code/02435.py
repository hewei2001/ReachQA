import numpy as np
import matplotlib.pyplot as plt

# Define periods and storytelling mediums
periods = ['Antiquity', 'Middle Ages', 'Renaissance', 'Industrial Age', 'Digital Age']
mediums = ['Oral Traditions', 'Manuscripts', 'Printed Books', 'Radio/Film', 'Digital Media']

# Prominence data for each medium across different historical periods
medium_data = np.array([
    [80, 15, 5, 0, 0],    # Antiquity
    [50, 30, 15, 5, 0],   # Middle Ages
    [30, 40, 25, 5, 0],   # Renaissance
    [10, 20, 50, 15, 5],  # Industrial Age
    [0, 5, 15, 30, 50]    # Digital Age
])

# Create a stacked area plot
fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(periods, medium_data.T, labels=mediums, alpha=0.8, cmap='Accent')

# Customize the plot
ax.set_title('The Evolution of Storytelling Mediums\nThrough the Ages', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Historical Period', fontsize=12)
ax.set_ylabel('Medium Prominence (arbitrary units)', fontsize=12)
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), title='Storytelling Mediums')
ax.grid(alpha=0.3)

# Adjust ticks for readability
ax.set_yticks(range(0, 101, 10))
ax.set_xticks(range(len(periods)))
ax.set_xticklabels(periods, rotation=15)

# Ensure layout fits well
plt.tight_layout()

# Display the plot
plt.show()