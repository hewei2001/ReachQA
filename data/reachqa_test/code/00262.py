import matplotlib.pyplot as plt
import numpy as np

# Data for the line chart: Years and Adoption Rates
years = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])
adoption_rates = np.array([5, 10, 15, 22, 28, 35, 45, 55, 65])

# Data for the overlay bar chart: Investment in Wearable Technology ($ Millions)
investment = np.array([50, 75, 100, 150, 200, 220, 300, 400, 550])

# Create the plot
fig, ax1 = plt.subplots(figsize=(14, 7))

# Plot the line with markers for adoption rates
ax1.plot(years, adoption_rates, marker='o', linestyle='-', color='teal', linewidth=2, label='Adoption Rate (%)')
ax1.set_xlabel('Year', fontsize=12, weight='bold')
ax1.set_ylabel('Adoption Rate (%)', fontsize=12, weight='bold', color='teal')
ax1.tick_params(axis='y', labelcolor='teal')

# Annotate each data point with its adoption rate
for year, rate in zip(years, adoption_rates):
    ax1.annotate(f'{rate}%', xy=(year, rate), textcoords="offset points", xytext=(0, 8), ha='center', fontsize=9, color='darkred')

# Create a second y-axis for the investment data
ax2 = ax1.twinx()
ax2.bar(years, investment, color='coral', alpha=0.6, width=0.5, label='Investment ($ Millions)')
ax2.set_ylabel('Investment ($ Millions)', fontsize=12, weight='bold', color='coral')
ax2.tick_params(axis='y', labelcolor='coral')

# Annotate specific investment milestones
investment_milestones = {2018: 'Increased Funding', 2021: 'Major Tech Backing'}
for year, label in investment_milestones.items():
    value = investment[np.where(years == year)][0]
    ax2.annotate(label, xy=(year, value), xytext=(-70, 20), textcoords='offset points',
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=-0.3', color='gray'), fontsize=9, color='navy')

# Title and grid styling
ax1.set_title('Wearable Technology Trends:\nAdoption Rate vs. Investment (2015-2023)', fontsize=16, weight='bold', pad=20)
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.set_facecolor('#F9F9F9')

# Legends
ax1.legend(loc='upper left', fontsize=10)
ax2.legend(loc='upper right', fontsize=10)

# Automatically adjust the layout for better spacing
plt.tight_layout()

# Display the plot
plt.show()