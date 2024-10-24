import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Years from 2000 to 2020
years = np.arange(2000, 2021)

# Renewable energy consumption (% of total energy) by region
north_america = [2, 3, 4, 5, 5, 6, 7, 8, 10, 12, 13, 14, 16, 17, 18, 19, 20, 22, 23, 25, 27]
europe = [5, 6, 7, 9, 10, 12, 14, 16, 19, 21, 23, 26, 29, 31, 34, 36, 39, 41, 44, 47, 50]
asia = [1, 2, 2, 3, 4, 5, 6, 8, 10, 12, 14, 16, 19, 21, 23, 26, 28, 30, 33, 35, 38]

# Global average target line
global_target = [20] * len(years)

# Create figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Set a color palette
palette = sns.color_palette("husl", 3)

# Plot lines with color gradients
ax.plot(years, north_america, marker='o', linestyle='-', linewidth=2, color=palette[0], label='North America')
ax.plot(years, europe, marker='s', linestyle='-', linewidth=2, color=palette[1], label='Europe')
ax.plot(years, asia, marker='^', linestyle='-', linewidth=2, color=palette[2], label='Asia')

# Plot a global target line
ax.plot(years, global_target, linestyle='--', color='gray', label='Global Target (20%)')

# Add title and labels with line breaks for long text
ax.set_title("Trends in Renewable Energy Adoption and Global Target\n(2000-2020)", fontsize=16, fontweight='bold')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Renewable Energy Consumption (%)", fontsize=12)

# Set grid for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Add a legend with title
ax.legend(loc='upper left', fontsize=10, title='Regions & Targets', title_fontsize=12)

# Highlight key events with annotations
ax.annotate('Paris Agreement', xy=(2015, 50), xytext=(2016, 55),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, ha='center', color='black')

# Display peak points in Europe
for i, txt in enumerate(europe):
    if txt == max(europe):
        ax.annotate(f'Peak: {txt}%', xy=(years[i], txt), xytext=(years[i]-2, txt+5),
                    arrowprops=dict(facecolor=palette[1], arrowstyle='->'),
                    fontsize=10, color=palette[1])

# Dual axis for secondary data example
ax2 = ax.twinx()
ax2.set_ylabel('Example Secondary Metric (Imaginary Units)', fontsize=12)
ax2.plot(years, [x + 20 for x in asia], linestyle='-', linewidth=1, color='blue', alpha=0.3, label='Imaginary Metric')
ax2.legend(loc='lower right', fontsize=10)

# Ensure tight layout
plt.tight_layout()

# Display the plot
plt.show()