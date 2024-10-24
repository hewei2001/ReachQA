import matplotlib.pyplot as plt
import numpy as np

# Years
years = np.arange(2015, 2026)

# Valuation data for each sector (in billion USD)
ai_valuation = [10, 15, 22, 30, 40, 55, 70, 90, 115, 145, 180]
fintech_valuation = [12, 18, 25, 35, 45, 60, 78, 100, 125, 155, 190]
edtech_valuation = [5, 7, 10, 14, 18, 24, 31, 40, 52, 67, 85]
healthtech_valuation = [8, 12, 16, 22, 30, 40, 54, 70, 90, 115, 145]
cleantech_valuation = [3, 5, 7, 10, 14, 20, 28, 38, 50, 65, 85]

# Stack data for area plot
valuations = np.vstack([ai_valuation, fintech_valuation, edtech_valuation, healthtech_valuation, cleantech_valuation])

# Create a list of colors for each sector
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Create the area plot
plt.figure(figsize=(14, 9))
plt.stackplot(years, valuations, labels=['AI', 'FinTech', 'EdTech', 'HealthTech', 'CleanTech'], colors=colors, alpha=0.85)

# Title and labels
plt.title("Global Tech Startup Growth:\nAn Area Chart Analysis (2015-2025)", fontsize=18, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Valuation (Billion USD)', fontsize=12)

# Add a legend
plt.legend(loc='upper left', title="Sectors", fontsize=10)

# Enhance grid visibility
plt.grid(linestyle='--', alpha=0.5)

# Adding annotations for significant points
for year, ai, fintech, edtech, healthtech, cleantech in zip(years, ai_valuation, fintech_valuation, edtech_valuation, healthtech_valuation, cleantech_valuation):
    if year in [2015, 2025]:  # Example of significant points: start and end year
        plt.text(year, ai, f'{ai}', fontsize=9, ha='center', color='#ff9999', weight='bold')
        plt.text(year, ai + fintech, f'{fintech}', fontsize=9, ha='center', color='#66b3ff', weight='bold')
        plt.text(year, ai + fintech + edtech, f'{edtech}', fontsize=9, ha='center', color='#99ff99', weight='bold')
        plt.text(year, ai + fintech + edtech + healthtech, f'{healthtech}', fontsize=9, ha='center', color='#ffcc99', weight='bold')
        plt.text(year, ai + fintech + edtech + healthtech + cleantech, f'{cleantech}', fontsize=9, ha='center', color='#c2c2f0', weight='bold')

# Adjust the layout
plt.tight_layout()

# Show plot
plt.show()