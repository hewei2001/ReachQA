import matplotlib.pyplot as plt
import numpy as np

# Define the cuisines and proficiency levels of the chef
cuisines = ['Italian', 'Japanese', 'Mexican', 'Indian', 'French']
proficiency_levels = [85, 70, 90, 75, 80]

# Additional data for the bar chart
# Here we define how frequently the chef cooks each cuisine (arbitrary but meaningful values)
cooking_frequencies = [150, 120, 180, 130, 160]  # Times cooked per year

# Extend the data by adding the first value to close the radar chart loop
radar_values = proficiency_levels + [proficiency_levels[0]]

# Calculate angles for the radar chart
num_vars = len(cuisines)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Closing the circle

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7), subplot_kw=dict(polar=False))

# Radar chart in the first subplot
ax1 = plt.subplot(121, polar=True)
ax1.fill(angles, radar_values, color='skyblue', alpha=0.4)
ax1.plot(angles, radar_values, color='blue', linewidth=2)
ax1.set_yticklabels([])
ax1.set_xticks(angles[:-1])
ax1.set_xticklabels(cuisines, fontsize=12, color='navy')
ax1.spines['polar'].set_visible(False)
ax1.grid(color='gray', linestyle='--', linewidth=0.5)
ax1.set_title("Culinary Explorer:\nMastering Global Cuisine", size=15, color='darkblue', weight='bold', pad=30)

# Bar chart in the second subplot
ax2 = plt.subplot(122)
bars = ax2.bar(cuisines, cooking_frequencies, color='lightcoral', edgecolor='darkred')
ax2.set_title("Frequency of Cooking Each Cuisine", size=15, color='darkred', weight='bold', pad=20)
ax2.set_ylabel('Times Cooked per Year', fontsize=12, color='darkred')
ax2.set_xticks(range(len(cuisines)))
ax2.set_xticklabels(cuisines, fontsize=12, rotation=45, ha="right")
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.grid(axis='y', linestyle='--', alpha=0.7)

# Adding value annotations on top of the bars for clarity
for bar in bars:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, yval + 5, int(yval), ha='center', va='bottom', fontsize=10, color='darkred')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the charts
plt.show()