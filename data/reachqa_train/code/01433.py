import matplotlib.pyplot as plt
import numpy as np

# Years of exploration data
years = np.arange(1970, 2021, 5)

# Exploration data for each ocean
atlantic_exploration = [10, 15, 18, 25, 30, 40, 55, 65, 80, 90, 105]
pacific_exploration = [8, 12, 20, 30, 40, 55, 70, 85, 100, 115, 130]
indian_exploration = [5, 7, 10, 15, 20, 30, 45, 50, 60, 75, 85]
arctic_exploration = [3, 4, 7, 10, 12, 18, 25, 30, 40, 50, 60]

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plot stacked area chart
ax.stackplot(years, atlantic_exploration, pacific_exploration, indian_exploration, arctic_exploration,
             labels=['Atlantic Ocean', 'Pacific Ocean', 'Indian Ocean', 'Arctic Ocean'],
             colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'], alpha=0.8)

# Add titles and labels
ax.set_title('The Surge of Ocean Exploration Activities\nAcross Major Oceans (1970-2020)', fontsize=16, weight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Expeditions per Year', fontsize=12)

# Customize legend
ax.legend(loc='upper left', fontsize=10, title='Ocean Regions', title_fontsize=12, frameon=False)

# Adjust x-ticks and rotate for clarity
plt.xticks(years, rotation=45)

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()