import matplotlib.pyplot as plt
import numpy as np

# Define the years of interest
years = np.arange(2010, 2021)

# Popularity indices for each art style over the decade
digital_painting = [50, 55, 60, 65, 70, 75, 78, 82, 86, 90, 94]
vector_art = [40, 42, 45, 47, 52, 60, 65, 70, 75, 80, 85]
pixel_art = [30, 32, 34, 38, 43, 48, 52, 55, 58, 60, 63]
ai_generated_art = [10, 15, 20, 25, 35, 50, 65, 80, 90, 100, 110]
modeling_3d = [20, 23, 28, 30, 35, 42, 50, 60, 70, 85, 95]

# Simulate an adoption rate dataset (percentages)
adoption_rate = [5, 10, 15, 18, 22, 28, 35, 45, 55, 70, 80]

# Creating the plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot each art style
ax1.plot(years, digital_painting, marker='o', linestyle='-', linewidth=2, color='skyblue', label='Digital Painting')
ax1.plot(years, vector_art, marker='s', linestyle='-', linewidth=2, color='coral', label='Vector Art')
ax1.plot(years, pixel_art, marker='^', linestyle='-', linewidth=2, color='limegreen', label='Pixel Art')
ax1.plot(years, ai_generated_art, marker='D', linestyle='-', linewidth=2, color='violet', label='AI-Generated Art')
ax1.plot(years, modeling_3d, marker='p', linestyle='-', linewidth=2, color='gold', label='3D Modeling')

# Secondary y-axis for adoption rates
ax2 = ax1.twinx()
ax2.bar(years, adoption_rate, color='gray', alpha=0.3, width=0.4, align='center', label='Adoption Rate (%)')
ax2.set_ylabel('Adoption Rate (%)', fontsize=12, color='dimgray')

# Highlight important milestones in the evolution of art styles
milestones = {
    2014: "Rise of AI Art",
    2017: "3D Software Advances",
    2020: "COVID-19 boosts online art"
}

for year, text in milestones.items():
    y_position = ai_generated_art[year - 2010] + 10 if year == 2014 else modeling_3d[year - 2010] - 10
    ax1.annotate(
        text,
        xy=(year, ai_generated_art[year - 2010] if year == 2014 else modeling_3d[year - 2010]),
        xytext=(year - 0.5, y_position),
        arrowprops=dict(facecolor='grey', arrowstyle="->", lw=1.5),
        fontsize=9,
        bbox=dict(facecolor='lightyellow', alpha=0.8, edgecolor='none')
    )

# Add titles and labels
ax1.set_title('The Digital Renaissance:\nEvolution of Art Styles Online (2010-2020)\nWith Adoption Rate Trends', fontsize=16, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Popularity Index', fontsize=12)

# Customize x-ticks
ax1.set_xticks(years)

# Grid for better readability
ax1.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Legends
ax1.legend(loc='upper left', frameon=False, fontsize=10)
ax2.legend(loc='upper right', frameon=False, fontsize=10)

# Automatically adjust layout
fig.tight_layout()

# Display the chart
plt.show()