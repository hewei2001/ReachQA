import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2020, 2031)

# Define adoption rates for each sector
gaming_adoption = np.array([20, 25, 30, 35, 40, 45, 50, 60, 70, 75, 80])
education_adoption = np.array([10, 12, 15, 20, 25, 30, 35, 40, 50, 55, 60])
healthcare_adoption = np.array([5, 8, 10, 15, 20, 25, 30, 35, 45, 50, 55])
real_estate_adoption = np.array([2, 4, 8, 12, 18, 24, 30, 38, 46, 52, 60])

# Set up the plot
fig, ax = plt.subplots(figsize=(12, 7))

# Stack the adoption data for the area plot using stackplot
ax.stackplot(years, gaming_adoption, education_adoption, healthcare_adoption, real_estate_adoption,
             labels=['Gaming', 'Education', 'Healthcare', 'Real Estate'],
             colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'], alpha=0.7)

# Add titles and labels
ax.set_title('Virtual Reality Market Adoption\nAcross Sectors (2020-2030)', fontsize=16, weight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Adoption Rate (%)', fontsize=12)

# Customize x and y ticks
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 101, 10))
ax.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Add a legend
ax.legend(title='Sectors', loc='upper left', fontsize=10, title_fontsize=12)

# Highlight significant adoption rates with annotations
for i, year in enumerate(years):
    if year == 2025:
        ax.annotate('Rapid Gaming Adoption', xy=(year, gaming_adoption[i]), xytext=(year, gaming_adoption[i] + 10),
                    arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=9, color='#1f77b4')
    if year == 2028:
        ax.annotate('Healthcare Breakthrough', xy=(year, healthcare_adoption[i]), xytext=(year, healthcare_adoption[i] + 10),
                    arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=9, color='#2ca02c')

# Automatically adjust layout for better fit
plt.tight_layout()

# Display the plot
plt.show()