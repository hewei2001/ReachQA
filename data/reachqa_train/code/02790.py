import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.arange(2030, 2041)
gso_investment = np.array([1.2, 1.8, 2.5, 3.1, 4.0, 5.0, 6.3, 7.2, 8.5, 9.5, 10.2])
pea_investment = np.array([0.8, 1.5, 2.0, 2.6, 3.5, 4.5, 5.1, 6.0, 7.0, 7.8, 8.4])
egc_investment = np.array([0.6, 1.1, 1.8, 2.3, 3.0, 3.7, 4.5, 5.3, 6.5, 7.0, 7.9])

# Calculate total investments for secondary y-axis
total_investment = gso_investment + pea_investment + egc_investment

# Plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Stackplot for cumulative investment
ax1.stackplot(years, gso_investment, pea_investment, egc_investment,
              labels=['Global Space Organization', 'Pacific Exploration Alliance', 'Euro-Galactic Coalition'],
              colors=['#1f77b4', '#ff7f0e', '#2ca02c'], alpha=0.8)

# Titles and Labels
plt.title('Investment in Ocean Worlds Exploration\nand Colonization (2030-2040)', fontsize=16, fontweight='bold')
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Investment (Billions of Dollars)', fontsize=14)

# Legend
ax1.legend(loc='upper left', title='Space Agencies', fontsize=12)

# Grid
ax1.grid(True, linestyle='--', alpha=0.7)

# Customize x-axis and y-axis ticks
ax1.set_xticks(years)
ax1.set_yticks(np.arange(0, 31, 5))
ax1.set_xticklabels(years, rotation=45)

# Secondary y-axis for percentage share
ax2 = ax1.twinx()
ax2.set_ylabel('Percentage Share of Total Investment', fontsize=14)
ax2.plot(years, (gso_investment / total_investment) * 100, 'o-', color='#1f77b4', label='GSO Share')
ax2.plot(years, (pea_investment / total_investment) * 100, 'o-', color='#ff7f0e', label='PEA Share')
ax2.plot(years, (egc_investment / total_investment) * 100, 'o-', color='#2ca02c', label='EGC Share')
ax2.set_yticks(np.arange(0, 101, 20))

# Annotations to highlight key trends
ax1.annotate('GSO Leads Investment', xy=(2035, 4.0), xytext=(2036, 8.0),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12, backgroundcolor='white')
ax1.annotate('PEA Steady Growth', xy=(2038, 6.0), xytext=(2039, 11.0),
             arrowprops=dict(facecolor='gray', arrowstyle='->'), fontsize=12, backgroundcolor='white')
ax1.annotate('EGC Catching Up', xy=(2040, 7.9), xytext=(2040, 15.0),
             arrowprops=dict(facecolor='green', arrowstyle='->'), fontsize=12, backgroundcolor='white')

# Optimize layout
plt.tight_layout()

# Show the plot
plt.show()