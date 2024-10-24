import matplotlib.pyplot as plt
import numpy as np

# Define the criteria and city models data
criteria = ['Environmental\nSustainability', 'Technological\nIntegration', 
            'Human\nWell-being', 'Infrastructure\nEfficiency', 'Cultural\nVibrancy']
cities = {
    'EcoMetropolis': [9, 6, 7, 8, 5],
    'TechSmart City': [7, 9, 6, 8, 6],
    'HumaNature Urban': [8, 5, 9, 7, 7],
    'Cultural Fusion Hub': [6, 7, 8, 5, 9]
}

# Additional data: Financial investments in millions
investments = {
    'EcoMetropolis': [30, 25, 35, 40, 20],
    'TechSmart City': [20, 40, 25, 35, 25],
    'HumaNature Urban': [35, 15, 45, 30, 30],
    'Cultural Fusion Hub': [25, 30, 30, 20, 50]
}

# Number of criteria
num_criteria = len(criteria)

# Compute the angle for each axis in radar chart
angles = np.linspace(0, 2 * np.pi, num_criteria, endpoint=False).tolist()
angles += angles[:1]  # Close the loop

# Create a subplot grid with 1 row and 2 columns
fig, axs = plt.subplots(1, 2, figsize=(18, 8), subplot_kw=dict(polar=True), gridspec_kw={'wspace': 0.4})

# Colors for each city model
colors = ['#1abc9c', '#e74c3c', '#3498db', '#9b59b6']

# Radar Chart
ax = axs[0]
for idx, (city, values) in enumerate(cities.items()):
    values += values[:1]  # Close the loop
    ax.fill(angles, values, color=colors[idx], alpha=0.25)
    ax.plot(angles, values, linewidth=2, color=colors[idx], label=city)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(criteria, fontsize=11, color='navy')
ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels([2, 4, 6, 8, 10], color='gray', size=10)
ax.set_title('Future Cities Index:\nAssessing Urban Prototypes Across Key Criteria', 
             size=14, color='midnightblue', weight='bold', pad=30)
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1), fontsize='medium', title='City Models')
ax.yaxis.grid(True, linestyle='--', linewidth=0.5, color='gray')
ax.set_facecolor('#f0f5f5')

# Bar Chart: Financial Investments
ax2 = axs[1]
criteria_index = np.arange(num_criteria)
bar_width = 0.2

for idx, (city, values) in enumerate(investments.items()):
    ax2.bar(criteria_index + idx * bar_width, values, bar_width, label=city, color=colors[idx], alpha=0.8)

ax2.set_xticks(criteria_index + bar_width * (len(cities) - 1) / 2)
ax2.set_xticklabels(criteria, fontsize=11, rotation=45)
ax2.set_xlabel('Investment (Millions)')
ax2.set_title('Investment in City Model Features', size=14, color='midnightblue', weight='bold', pad=20)
ax2.legend(title='City Models', loc='upper right', bbox_to_anchor=(1.2, 1))
ax2.yaxis.grid(True, linestyle='--', linewidth=0.5, color='gray')

# Save and show plot
plt.show()