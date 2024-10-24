import matplotlib.pyplot as plt
import numpy as np

# Years for projection
years = np.array([2030, 2031, 2032, 2033, 2034])

# Projected workforce (in thousands) in various technology sectors
ai_employment = np.array([120, 140, 160, 180, 200])
robotics_employment = np.array([80, 90, 105, 120, 135])
vr_employment = np.array([50, 60, 70, 85, 95])
blockchain_employment = np.array([30, 45, 60, 75, 90])
green_tech_employment = np.array([70, 85, 100, 115, 130])

# Create the stacked bar chart
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting the stacked bars
bars1 = ax.bar(years, ai_employment, label='AI', color='#4c72b0', alpha=0.9)
bars2 = ax.bar(years, robotics_employment, bottom=ai_employment, label='Robotics', color='#55a868', alpha=0.9)
bars3 = ax.bar(years, vr_employment, bottom=ai_employment+robotics_employment, label='VR', color='#c44e52', alpha=0.9)
bars4 = ax.bar(years, blockchain_employment, bottom=ai_employment+robotics_employment+vr_employment, label='Blockchain', color='#8172b2', alpha=0.9)
bars5 = ax.bar(years, green_tech_employment, bottom=ai_employment+robotics_employment+vr_employment+blockchain_employment, label='Green Tech', color='#ccb974', alpha=0.9)

# Adding title and labels
ax.set_title('Future Tech Occupation Trends\n(2030-2034)', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Number of Workers (in thousands)', fontsize=14)

# Adding legend
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Tech Sectors', fontsize=10, frameon=False)

# Adjust the y-axis to comfortably fit the data
ax.set_ylim(0, 700)

# Rotate x-axis labels if needed
ax.set_xticks(years)
ax.set_xticklabels(years)

# Adding data labels
for bars, employment in zip([bars1, bars2, bars3, bars4, bars5], 
                            [ai_employment, robotics_employment, vr_employment, blockchain_employment, green_tech_employment]):
    for bar, value in zip(bars, employment):
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_y() + height / 2,
            f'{value}',
            ha='center',
            va='center',
            fontsize=10,
            color='white' if bar.get_facecolor() != '#ccb974' else 'black',  # Use black text on yellow bars for contrast
            fontweight='bold'
        )

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()