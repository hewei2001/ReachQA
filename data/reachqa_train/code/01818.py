import matplotlib.pyplot as plt
import numpy as np

# Weekly working hours data for each industry
technology_hours = [38, 42, 45, 50, 52, 48, 46, 40, 37, 55, 43, 39, 41, 45, 47]
healthcare_hours = [50, 55, 60, 52, 58, 57, 56, 54, 53, 60, 62, 51, 55, 59, 61]
finance_hours = [45, 48, 50, 52, 55, 53, 49, 47, 46, 51, 54, 50, 52, 49, 53]
education_hours = [35, 38, 40, 42, 36, 37, 39, 41, 35, 34, 43, 38, 40, 39, 36]
hospitality_hours = [50, 52, 55, 60, 58, 53, 56, 54, 57, 61, 63, 50, 59, 55, 60]

# Group the data
data = [technology_hours, healthcare_hours, finance_hours, education_hours, hospitality_hours]
industries = ['Technology', 'Healthcare', 'Finance', 'Education', 'Hospitality']

# Initialize the figure
fig, ax = plt.subplots(figsize=(12, 8))

# Create horizontal box plot
box = ax.boxplot(data, vert=False, patch_artist=True, labels=industries, notch=True, whis=1.5)

# Use a color palette to differentiate industries
colors = plt.cm.Paired(np.linspace(0, 1, len(data)))

# Color customization
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Add annotations for medians
medians = [np.median(group) for group in data]
for i, median in enumerate(medians):
    ax.annotate(f'{median}h', xy=(median, i + 1), xytext=(5, -15), 
                textcoords='offset points', ha='center', va='center', color='black',
                bbox=dict(boxstyle='round,pad=0.3', edgecolor='none', facecolor='lightgray'))

# Enhance grid readability
ax.grid(True, linestyle='--', alpha=0.6, axis='x')

# Titles and labels
ax.set_title('Work-Life Balance Across Industries\nDistribution of Weekly Working Hours', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Weekly Working Hours', fontsize=12)
ax.set_ylabel('Industry', fontsize=12)

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Show the plot
plt.show()