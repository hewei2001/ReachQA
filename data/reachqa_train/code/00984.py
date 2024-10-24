import matplotlib.pyplot as plt
import numpy as np

# Years from 1990 to 2025
years = np.arange(1990, 2026)

# Modified Adoption rates (in millions) for each generation to improve clarity
adoption_2G = [0, 0, 5, 20, 50, 120, 220, 380, 550, 620, 700, 750, 800, 850, 900, 950, 980, 1000, 950, 900, 850, 800, 750, 700, 650, 600, 550, 500, 450, 400, 350, 300, 250, 200, 150, 100]
adoption_3G = [0, 0, 0, 0, 0, 0, 10, 30, 60, 150, 300, 500, 700, 850, 900, 950, 980, 1000, 1100, 1150, 1180, 1200, 1220, 1240, 1260, 1280, 1300, 1310, 1320, 1325, 1330, 1335, 1340, 1345, 1350, 1355]
adoption_4G = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 30, 80, 160, 300, 500, 700, 800, 900, 1000, 1100, 1150, 1200, 1250, 1300, 1325, 1340, 1350, 1360, 1370, 1380, 1390, 1400, 1410, 1420, 1430]
adoption_5G = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 50, 150, 300, 500, 700, 900, 1100, 1300, 1450, 1500, 1550, 1600, 1650, 1700, 1750, 1800, 1850, 1900, 1950]

# Plotting the data
plt.figure(figsize=(14, 8))
plt.plot(years, adoption_2G, label='2G', marker='o', color='#1f77b4', linewidth=2, linestyle='-')
plt.plot(years, adoption_3G, label='3G', marker='s', color='#ff7f0e', linewidth=2, linestyle='--')
plt.plot(years, adoption_4G, label='4G', marker='^', color='#2ca02c', linewidth=2, linestyle='-.')
plt.plot(years, adoption_5G, label='5G', marker='d', color='#d62728', linewidth=2, linestyle=':')

# Annotating significant points
annotations = {
    1995: '2G Launch',
    2001: '3G Launch',
    2010: '4G Growth',
    2020: '5G Rise'
}

for year, annotation in annotations.items():
    # Identify correct adoption level for annotation
    adoption_level = {
        1995: adoption_2G[year - 1990],
        2001: adoption_3G[year - 1990],
        2010: adoption_4G[year - 1990],
        2020: adoption_5G[year - 1990]
    }[year]
    
    plt.annotate(annotation, 
                 xy=(year, adoption_level), 
                 xytext=(year + 2, adoption_level + 200),
                 arrowprops=dict(facecolor='black', arrowstyle='->'), 
                 fontsize=10, color='black')

# Customizing the chart
plt.title('Evolution of Smartphone Connectivity\nFrom 2G to 5G', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Users (in millions)', fontsize=14)
plt.xticks(np.arange(1990, 2026, 5), rotation=45)
plt.legend(title='Network Generation', loc='upper left', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)

# Adjust layout for better spacing
plt.tight_layout()

# Display the plot
plt.show()