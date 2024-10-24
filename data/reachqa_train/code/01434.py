import matplotlib.pyplot as plt
import numpy as np

# Years of exploration data
years = np.arange(1970, 2021, 5)

# Exploration data for each ocean
atlantic_exploration = [10, 15, 18, 25, 30, 40, 55, 65, 80, 90, 105]
pacific_exploration = [8, 12, 20, 30, 40, 55, 70, 85, 100, 115, 130]
indian_exploration = [5, 7, 10, 15, 20, 30, 45, 50, 60, 75, 85]
arctic_exploration = [3, 4, 7, 10, 12, 18, 25, 30, 40, 50, 60]

# Calculate percentage growth rates
atlantic_growth = np.diff(atlantic_exploration) / atlantic_exploration[:-1] * 100
pacific_growth = np.diff(pacific_exploration) / pacific_exploration[:-1] * 100
indian_growth = np.diff(indian_exploration) / indian_exploration[:-1] * 100
arctic_growth = np.diff(arctic_exploration) / arctic_exploration[:-1] * 100

# Initialize figure and axes
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# Plot stacked area chart
ax1.stackplot(years, atlantic_exploration, pacific_exploration, indian_exploration, arctic_exploration,
              labels=['Atlantic Ocean', 'Pacific Ocean', 'Indian Ocean', 'Arctic Ocean'],
              colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'], alpha=0.8)
ax1.set_title('The Surge of Ocean Exploration Activities\nAcross Major Oceans (1970-2020)', fontsize=14, weight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Expeditions per Year', fontsize=12)
ax1.legend(loc='upper left', fontsize=10, title='Ocean Regions', title_fontsize=12, frameon=False)
ax1.grid(True, linestyle='--', alpha=0.6)
ax1.tick_params(axis='x', rotation=45)

# Plot percentage growth rates on the second subplot
growth_years = years[1:]  # Exclude the first year because of diff calculation
ax2.plot(growth_years, atlantic_growth, marker='o', label='Atlantic Ocean', color='#1f77b4', linestyle='-')
ax2.plot(growth_years, pacific_growth, marker='o', label='Pacific Ocean', color='#ff7f0e', linestyle='-')
ax2.plot(growth_years, indian_growth, marker='o', label='Indian Ocean', color='#2ca02c', linestyle='-')
ax2.plot(growth_years, arctic_growth, marker='o', label='Arctic Ocean', color='#d62728', linestyle='-')
ax2.set_title('Percentage Growth of Exploration Activities\n(1975-2020)', fontsize=14, weight='bold')
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Growth Rate (%)', fontsize=12)
ax2.legend(loc='upper left', fontsize=10, title='Ocean Regions', title_fontsize=12, frameon=False)
ax2.grid(True, linestyle='--', alpha=0.6)
ax2.tick_params(axis='x', rotation=45)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()