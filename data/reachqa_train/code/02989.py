import matplotlib.pyplot as plt
import numpy as np

# Years of observation
years = np.arange(2000, 2024)

# Browsers' market shares over the years in percentages
chrome_market_share = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 20, 30, 38, 43, 48, 52, 57, 61, 65, 68, 70, 73])
firefox_market_share = np.array([0, 0, 0, 0, 0, 0, 3, 8, 12, 15, 20, 24, 23, 21, 18, 15, 13, 12, 11, 10, 9, 8, 7, 6])
safari_market_share = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 12, 13, 14, 14, 15, 16, 17, 18, 18, 19, 20, 21, 22])
edge_market_share = np.array([0, 0, 0, 0, 0, 5, 8, 10, 12, 12, 11, 8, 8, 7, 7, 8, 9, 9, 10, 10, 11, 12, 13, 14])
opera_market_share = np.array([10, 9, 8, 7, 6, 5, 5, 5, 4, 4, 5, 4, 4, 3, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1])
ie_market_share = np.array([70, 68, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 8, 6, 5, 3, 2, 1, 1, 1, 1, 0])
others_market_share = 100 - (chrome_market_share + firefox_market_share + safari_market_share + edge_market_share + opera_market_share + ie_market_share)

# Plot setup
fig, ax = plt.subplots(figsize=(14, 10))

# Plotting stacked bar chart
ax.bar(years, chrome_market_share, label='Chrome', color='blue')
ax.bar(years, firefox_market_share, bottom=chrome_market_share, label='Firefox', color='orange')
ax.bar(years, safari_market_share, bottom=chrome_market_share + firefox_market_share, label='Safari', color='green')
ax.bar(years, edge_market_share, bottom=chrome_market_share + firefox_market_share + safari_market_share, label='Edge', color='purple')
ax.bar(years, opera_market_share, bottom=chrome_market_share + firefox_market_share + safari_market_share + edge_market_share, label='Opera', color='red')
ax.bar(years, ie_market_share, bottom=chrome_market_share + firefox_market_share + safari_market_share + edge_market_share + opera_market_share, label='Internet Explorer', color='brown')
ax.bar(years, others_market_share, bottom=chrome_market_share + firefox_market_share + safari_market_share + edge_market_share + opera_market_share + ie_market_share, label='Others', color='grey')

# Title and labels
ax.set_title('Browser Market Share Evolution (2000-2023)\nA Comprehensive Overview', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Market Share (%)', fontsize=12)
ax.set_ylim(0, 100)

# Adding percentage labels on each bar section
for i in range(len(years)):
    total = 0
    for share, color in zip(
        [chrome_market_share, firefox_market_share, safari_market_share, edge_market_share, opera_market_share, ie_market_share, others_market_share],
        ['blue', 'orange', 'green', 'purple', 'red', 'brown', 'grey']):
        height = share[i]
        if height > 0:
            ax.text(years[i], total + height / 2, f'{height}%', ha='center', va='center', fontsize=8, color='white')
        total += height

# Overlay line plot for cumulative growth
total_users = np.array([50 + i * 5 + (i % 2) * 10 for i in range(len(years))])  # Simulated user base growth
ax2 = ax.twinx()
ax2.plot(years, total_users, label='Total Users (millions)', color='darkcyan', linestyle='--', linewidth=2)
ax2.set_ylabel('Total Users (Millions)', fontsize=12, color='darkcyan')
ax2.tick_params(axis='y', labelcolor='darkcyan')

# Legend and layout adjustment
ax.legend(title='Browsers', loc='upper left', bbox_to_anchor=(1.15, 1))
ax2.legend(loc='upper left', bbox_to_anchor=(1.15, 0.9))
plt.xticks(years, rotation=45, ha='right')
plt.tight_layout()

plt.show()