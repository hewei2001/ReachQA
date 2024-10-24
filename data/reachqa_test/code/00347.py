import matplotlib.pyplot as plt
import numpy as np

# Expanded years from 2000 to 2050
years = np.arange(2000, 2051)

# Investment data in billion USD
asia_investments = np.array([
    5, 6, 7, 9, 11, 12, 15, 20, 25, 30, 36, 42, 50, 58, 65, 73, 82, 91, 101, 112, 125, 140, 155, 170, 185, 200, 220, 240, 260, 280, 300, 325, 350, 375, 400, 430, 460, 490, 520, 550, 580, 610, 640, 670, 700, 730, 760, 790, 820, 850, 880
])

europe_investments = np.array([
    4, 5, 6, 8, 10, 13, 17, 22, 28, 35, 42, 50, 60, 70, 81, 93, 106, 120, 135, 151, 168, 186, 205, 225, 245, 270, 295, 320, 345, 370, 395, 420, 450, 480, 510, 540, 570, 600, 630, 660, 690, 720, 750, 780, 810, 840, 870, 900, 930, 960, 990
])

north_america_investments = np.array([
    8, 9, 10, 12, 15, 18, 22, 27, 34, 42, 51, 61, 73, 86, 100, 115, 131, 148, 166, 185, 205, 226, 248, 271, 295, 320, 345, 370, 395, 420, 445, 470, 500, 530, 560, 590, 620, 650, 680, 710, 740, 770, 800, 830, 860, 890, 920, 950, 980, 1010, 1040
])

africa_investments = np.array([
    1, 1.5, 2, 2.5, 3, 4, 5, 7, 10, 14, 19, 25, 32, 40, 49, 59, 70, 82, 95, 109, 124, 140, 157, 175, 194, 215, 236, 257, 278, 299, 320, 341, 362, 383, 404, 425, 446, 467, 488, 509, 530, 551, 572, 593, 614, 635, 656, 677, 698, 719, 740
])

south_america_investments = np.array([
    2, 3, 4, 5, 6, 8, 11, 15, 20, 26, 33, 41, 50, 60, 71, 83, 96, 110, 125, 141, 158, 176, 195, 215, 236, 258, 280, 302, 324, 346, 368, 390, 412, 434, 456, 478, 500, 522, 544, 566, 588, 610, 632, 654, 676, 698, 720, 742, 764, 786, 808
])

# Calculate Compound Annual Growth Rate (CAGR)
def calculate_cagr(start, end, periods):
    return ((end/start)**(1/periods) - 1) * 100

asia_cagr = calculate_cagr(asia_investments[0], asia_investments[-1], len(years) - 1)
europe_cagr = calculate_cagr(europe_investments[0], europe_investments[-1], len(years) - 1)
north_america_cagr = calculate_cagr(north_america_investments[0], north_america_investments[-1], len(years) - 1)
africa_cagr = calculate_cagr(africa_investments[0], africa_investments[-1], len(years) - 1)
south_america_cagr = calculate_cagr(south_america_investments[0], south_america_investments[-1], len(years) - 1)

# Create the figure and subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 12), gridspec_kw={'height_ratios': [3, 1]})

# Plot each line on the first subplot with a focus on more intricate detail
ax1.plot(years, asia_investments, label='Asia', marker='o', color='#FF5733', alpha=0.8)
ax1.plot(years, europe_investments, label='Europe', marker='^', color='#33FFCE', alpha=0.8)
ax1.plot(years, north_america_investments, label='North America', marker='s', color='#335BFF', alpha=0.8)
ax1.plot(years, africa_investments, label='Africa', marker='d', color='#FF33A8', alpha=0.8)
ax1.plot(years, south_america_investments, label='South America', marker='p', color='#FFD133', alpha=0.8)

ax1.set_title('Global Expansion of AI R&D Investments from 2000 to 2050\nand their Growth Rates', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Investment in AI R&D (Billion USD)', fontsize=14)

ax1.set_xticks(years[::5])
ax1.set_xticklabels(years[::5], rotation=45)
ax1.grid(alpha=0.3, linestyle='--')
ax1.legend(loc='upper left', fontsize=10, title='Continents', ncol=3)

# Second subplot for growth rates
ax2.bar(['Asia', 'Europe', 'North America', 'Africa', 'South America'],
        [asia_cagr, europe_cagr, north_america_cagr, africa_cagr, south_america_cagr],
        color=['#FF5733', '#33FFCE', '#335BFF', '#FF33A8', '#FFD133'])
ax2.set_title('Compound Annual Growth Rate (CAGR) from 2000 to 2050', fontsize=14, pad=10)
ax2.set_ylabel('CAGR (%)', fontsize=12)
ax2.grid(axis='y', alpha=0.3, linestyle='--')

plt.tight_layout()
plt.show()