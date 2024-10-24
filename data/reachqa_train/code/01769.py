import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Years of analysis
years = np.arange(2011, 2021)

# Percentage data of digital payment adoption over the years
credit_cards = [60, 58, 56, 54, 52, 50, 48, 46, 44, 42]
digital_wallets = [10, 12, 14, 17, 20, 25, 30, 35, 40, 45]
bank_transfers = [25, 23, 22, 20, 18, 15, 15, 14, 13, 10]
cryptocurrencies = [5, 7, 8, 9, 10, 10, 7, 5, 3, 3]

# Additional Data: Cumulative Market Share over Years
cumulative_market_share = {
    'Credit Cards': np.cumsum(credit_cards),
    'Digital Wallets': np.cumsum(digital_wallets),
    'Bank Transfers': np.cumsum(bank_transfers),
    'Cryptocurrencies': np.cumsum(cryptocurrencies)
}

# Initialize the figure
fig = plt.figure(figsize=(18, 8))

# First subplot: 3D Bar Chart
ax1 = fig.add_subplot(121, projection='3d')

# Prepare 3D bar chart
methods = ['Credit Cards', 'Digital Wallets', 'Bank Transfers', 'Cryptocurrencies']
data = [credit_cards, digital_wallets, bank_transfers, cryptocurrencies]

xpos = np.repeat(np.arange(len(years)), len(methods))
ypos = np.tile(np.arange(len(methods)), len(years))
zpos = np.zeros_like(xpos)
dx = dy = 0.5
dz = np.hstack(data)
colors = ['royalblue', 'gold', 'seagreen', 'crimson']

for i, color in enumerate(colors):
    ax1.bar3d(xpos[ypos == i], ypos[ypos == i], zpos[ypos == i], dx, dy, dz[ypos == i],
              color=color, alpha=0.8, label=methods[i], zsort='average')

ax1.set_xticks(np.arange(len(years)))
ax1.set_xticklabels(years, rotation=45, ha='right')
ax1.set_yticks(np.arange(len(methods)))
ax1.set_yticklabels(methods)
ax1.set_zlabel('Percentage of Transactions (%)')
ax1.set_zlim(0, 100)
ax1.set_title('Adoption of Digital Payment Methods in E-commerce\n(2011-2020)', 
              fontsize=14, fontweight='bold', pad=20)
ax1.legend(loc='upper right', title='Payment Methods', fontsize=10)

# Second subplot: Line Chart for Cumulative Market Share
ax2 = fig.add_subplot(122)

for method, values in cumulative_market_share.items():
    ax2.plot(years, values, marker='o', label=method)

ax2.set_title('Cumulative Market Share of Payment Methods', fontsize=14, fontweight='bold')
ax2.set_xlabel('Years')
ax2.set_ylabel('Cumulative Market Share (%)')
ax2.set_xticks(years)
ax2.set_xticklabels(years, rotation=45, ha='right')
ax2.legend(title='Payment Methods', fontsize=10)
ax2.grid(True, linestyle='--', alpha=0.6)

# Adjust layout
plt.tight_layout()
plt.show()