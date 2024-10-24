import matplotlib.pyplot as plt
import numpy as np

# Years for the data
years = np.arange(2018, 2023)

# Funding contributions by different organizations (in millions of USD)
wwf_funding = [5, 6, 7, 8, 9]  # World Wildlife Fund
wcs_funding = [4, 5, 6, 6, 7]  # Wildlife Conservation Society
ci_funding = [3, 3, 4, 5, 5]   # Conservation International
tusk_funding = [2, 2, 3, 3, 4] # Tusk Trust

# Calculate percentage changes
def percentage_change(data):
    return [(data[i] - data[i-1]) / data[i-1] * 100 if i != 0 else 0 for i in range(len(data))]

wwf_change = percentage_change(wwf_funding)
wcs_change = percentage_change(wcs_funding)
ci_change = percentage_change(ci_funding)
tusk_change = percentage_change(tusk_funding)

# Colors for the organizations
colors = ['#2ca02c', '#ff7f0e', '#1f77b4', '#d62728']

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Stacked Bar Chart
ax1.bar(years, wwf_funding, color=colors[0], label='World Wildlife Fund', width=0.6)
ax1.bar(years, wcs_funding, bottom=wwf_funding, color=colors[1], label='Wildlife Conservation Society', width=0.6)
ax1.bar(years, ci_funding, bottom=np.add(wwf_funding, wcs_funding), color=colors[2], label='Conservation International', width=0.6)
ax1.bar(years, tusk_funding, bottom=np.add(np.add(wwf_funding, wcs_funding), ci_funding), color=colors[3], label='Tusk Trust', width=0.6)

ax1.set_title('Funding for Wildlife Conservation in Africa\nBy Major Organizations (2018-2022)', fontsize=14, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Funding (Millions of USD)', fontsize=12)
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)
ax1.legend(loc='upper left', title='Organizations', fontsize=9)
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Annotations for the stacked bar chart
for i, year in enumerate(years):
    cumulative = 0
    for j, organization in enumerate([wwf_funding, wcs_funding, ci_funding, tusk_funding]):
        cumulative += organization[i]
        ax1.text(year, cumulative - organization[i] / 2, f'{organization[i]}', ha='center', va='center', fontsize=9, color='white')

# Line Plot for percentage change
ax2.plot(years, wwf_change, marker='o', color=colors[0], label='WWF Change (%)')
ax2.plot(years, wcs_change, marker='o', color=colors[1], label='WCS Change (%)')
ax2.plot(years, ci_change, marker='o', color=colors[2], label='CI Change (%)')
ax2.plot(years, tusk_change, marker='o', color=colors[3], label='Tusk Change (%)')

ax2.axhline(0, color='grey', linewidth=0.8, linestyle='--')
ax2.set_title('Year-over-Year Percentage Change\nin Funding (2018-2022)', fontsize=14, fontweight='bold')
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Percentage Change (%)', fontsize=12)
ax2.set_xticks(years)
ax2.set_xticklabels(years, rotation=45)
ax2.legend(loc='upper left', title='Organizations', fontsize=9)
ax2.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()