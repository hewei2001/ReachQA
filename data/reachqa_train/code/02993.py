import matplotlib.pyplot as plt
import numpy as np

# Define years and data
years = np.arange(2010, 2021)
europe_renewables = np.array([150, 165, 180, 200, 230, 260, 300, 340, 390, 450, 500])
asia_renewables = np.array([100, 120, 150, 180, 220, 270, 320, 380, 450, 530, 610])
north_america_renewables = np.array([90, 110, 130, 150, 180, 210, 250, 290, 330, 370, 420])
africa_renewables = np.array([30, 35, 40, 50, 60, 80, 100, 130, 170, 220, 290])
oceania_renewables = np.array([20, 25, 30, 35, 45, 55, 70, 90, 110, 130, 160])

# Create a stacked area plot
fig, ax = plt.subplots(figsize=(14, 8))
ax.stackplot(years, europe_renewables, asia_renewables, north_america_renewables,
             africa_renewables, oceania_renewables, labels=['Europe', 'Asia', 'North America', 'Africa', 'Oceania'],
             colors=['#FFD700', '#FF6347', '#4682B4', '#32CD32', '#9370DB'], alpha=0.8)

# Add titles and labels
ax.set_title('Global Growth in Renewable Energy Production\n(2010-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Renewable Energy Production (TWh)', fontsize=12)

# Add legend
ax.legend(loc='upper left', title='Continents')

# Customize x-axis labels
plt.xticks(years, rotation=45)

# Annotate significant milestones
ax.annotate('Europe surpasses 400 TWh', xy=(2019, 450), xytext=(2016.5, 600),
             arrowprops=dict(arrowstyle='->', color='black'), color='black', fontsize=10, bbox=dict(facecolor='white', alpha=0.8))

ax.annotate('Asia takes the lead', xy=(2020, 610), xytext=(2018, 700),
             arrowprops=dict(arrowstyle='->', color='black'), color='black', fontsize=10, bbox=dict(facecolor='white', alpha=0.8))

# Improve layout to avoid overlapping
plt.tight_layout()

# Show grid for better readability
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Show the plot
plt.show()