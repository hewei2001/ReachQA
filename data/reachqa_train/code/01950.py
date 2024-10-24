import matplotlib.pyplot as plt
import numpy as np

# Years for the data
years = np.arange(2018, 2023)

# Funding contributions by different organizations (in millions of USD)
wwf_funding = [5, 6, 7, 8, 9]  # World Wildlife Fund
wcs_funding = [4, 5, 6, 6, 7]  # Wildlife Conservation Society
ci_funding = [3, 3, 4, 5, 5]   # Conservation International
tusk_funding = [2, 2, 3, 3, 4] # Tusk Trust

# Total data for stacked plotting
funding_data = np.array([wwf_funding, wcs_funding, ci_funding, tusk_funding])

# Colors for the organizations
colors = ['#2ca02c', '#ff7f0e', '#1f77b4', '#d62728']

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))

# Stacked Bar Chart
ax.bar(years, wwf_funding, color=colors[0], label='World Wildlife Fund', width=0.6)
ax.bar(years, wcs_funding, bottom=wwf_funding, color=colors[1], label='Wildlife Conservation Society', width=0.6)
ax.bar(years, ci_funding, bottom=np.add(wwf_funding, wcs_funding), color=colors[2], label='Conservation International', width=0.6)
ax.bar(years, tusk_funding, bottom=np.add(np.add(wwf_funding, wcs_funding), ci_funding), color=colors[3], label='Tusk Trust', width=0.6)

# Title and labels
ax.set_title('Funding for Wildlife Conservation in Africa\nBy Major Organizations (2018-2022)', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Funding (Millions of USD)', fontsize=14)

# Customize x-ticks
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

# Legend
ax.legend(loc='upper left', title='Organizations', fontsize=10, frameon=False)

# Grid for better readability
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Annotations to highlight each contribution
for i, year in enumerate(years):
    cumulative = 0
    for j, organization in enumerate(funding_data):
        cumulative += organization[i]
        ax.text(year, cumulative - organization[i] / 2, f'{organization[i]}', ha='center', va='center', fontsize=10, color='white')

# Adjust layout to prevent clipping
plt.tight_layout()

# Display the chart
plt.show()