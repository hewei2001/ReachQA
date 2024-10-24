import matplotlib.pyplot as plt
import numpy as np

# Time period from 2010 to 2020
years = np.arange(2010, 2021)

# Exchange rates to a hypothetical Global Reserve Currency (GRC)
usd_to_grc = np.array([1.00, 0.97, 0.95, 1.02, 1.05, 1.10, 1.08, 1.12, 1.15, 1.13, 1.20])  # USD fluctuations
eur_to_grc = np.array([1.00, 0.90, 0.85, 0.87, 0.92, 0.95, 0.94, 0.96, 0.91, 0.88, 0.90])  # EUR fluctuations
jpy_to_grc = np.array([1.00, 1.05, 1.07, 1.10, 1.08, 1.02, 1.03, 1.00, 0.98, 0.95, 0.97])  # JPY fluctuations

# Calculate percentage change for bar chart
def calculate_percentage_change(data):
    return [(data[i] - data[i-1]) / data[i-1] * 100 for i in range(1, len(data))]

usd_change = calculate_percentage_change(usd_to_grc)
eur_change = calculate_percentage_change(eur_to_grc)
jpy_change = calculate_percentage_change(jpy_to_grc)

# Create the figure and subplots
fig, axs = plt.subplots(1, 2, figsize=(16, 8), constrained_layout=True)

# Subplot 1: Line chart of currency fluctuations
axs[0].plot(years, usd_to_grc, marker='o', linestyle='-', color='b', linewidth=2, label='USD to GRC')
axs[0].plot(years, eur_to_grc, marker='s', linestyle='--', color='g', linewidth=2, label='EUR to GRC')
axs[0].plot(years, jpy_to_grc, marker='^', linestyle='-.', color='r', linewidth=2, label='JPY to GRC')

# Annotations for significant points
annotations = {
    2012: "Eurozone Crisis Impact",
    2016: "USD Strength Peak",
    2018: "Abenomics Effect"
}

for year, event in annotations.items():
    axs[0].annotate(event,
                    xy=(year, usd_to_grc[year - 2010]),
                    xytext=(year - 0.8, usd_to_grc[year - 2010] + 0.07),
                    arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5),
                    fontsize=9,
                    color='black')

axs[0].set_title('Rise and Fall of Major Global Currencies\n(2010-2020)', fontsize=14, fontweight='bold')
axs[0].set_xlabel('Year', fontsize=12)
axs[0].set_ylabel('Exchange Rate to GRC', fontsize=12)
axs[0].legend(loc='upper left', fontsize=10, frameon=False)
axs[0].grid(True, linestyle='--', alpha=0.5)

# Subplot 2: Bar chart of percentage changes
bar_width = 0.25
years_for_bars = years[1:]

axs[1].bar(years_for_bars - bar_width, usd_change, width=bar_width, color='b', label='USD Change (%)')
axs[1].bar(years_for_bars, eur_change, width=bar_width, color='g', label='EUR Change (%)')
axs[1].bar(years_for_bars + bar_width, jpy_change, width=bar_width, color='r', label='JPY Change (%)')

axs[1].set_title('Year-over-Year Percentage Change', fontsize=14, fontweight='bold')
axs[1].set_xlabel('Year', fontsize=12)
axs[1].set_ylabel('Percentage Change (%)', fontsize=12)
axs[1].legend(loc='upper right', fontsize=10, frameon=False)
axs[1].grid(True, linestyle='--', alpha=0.5)

# Display the plot
plt.show()