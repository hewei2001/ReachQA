import matplotlib.pyplot as plt
import numpy as np

# Years of observation
years = np.arange(2013, 2024)

# Browsers' market shares over the years in percentages
chrome_market_share = [38, 43, 48, 52, 57, 61, 65, 68, 70, 73, 74]
firefox_market_share = [24, 23, 21, 18, 15, 13, 12, 11, 10, 9, 8]
safari_market_share = [12, 13, 14, 14, 15, 16, 17, 18, 18, 19, 20]
edge_market_share = [8, 8, 7, 7, 8, 9, 9, 10, 10, 11, 12]
opera_market_share = [5, 4, 3, 3, 3, 2, 2, 1, 1, 1, 1]

# Calculate 'Others' to complete 100% total
others_market_share = [100 - (c + f + s + e + o) for c, f, s, e, o in zip(
    chrome_market_share, firefox_market_share, safari_market_share, edge_market_share, opera_market_share)]

# Plot setup
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting stacked bar chart
ax.bar(years, chrome_market_share, label='Chrome', color='blue')
ax.bar(years, firefox_market_share, bottom=chrome_market_share, label='Firefox', color='orange')
ax.bar(years, safari_market_share, bottom=np.array(chrome_market_share) + np.array(firefox_market_share), label='Safari', color='green')
ax.bar(years, edge_market_share, bottom=np.array(chrome_market_share) + np.array(firefox_market_share) + np.array(safari_market_share), label='Edge', color='purple')
ax.bar(years, opera_market_share, bottom=np.array(chrome_market_share) + np.array(firefox_market_share) + np.array(safari_market_share) + np.array(edge_market_share), label='Opera', color='red')
ax.bar(years, others_market_share, bottom=np.array(chrome_market_share) + np.array(firefox_market_share) + np.array(safari_market_share) + np.array(edge_market_share) + np.array(opera_market_share), label='Others', color='grey')

# Title and labels
ax.set_title('A Decade of Browsing:\nInternet Browser Market Share Evolution (2013-2023)', fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Market Share (%)', fontsize=12)
ax.set_ylim(0, 100)  # Ensure the y-axis is from 0 to 100

# Adding percentage labels on each bar section
for i in range(len(years)):
    total = 0
    for share, color in zip([chrome_market_share, firefox_market_share, safari_market_share, edge_market_share, opera_market_share, others_market_share], ['blue', 'orange', 'green', 'purple', 'red', 'grey']):
        height = share[i]
        if height > 0:
            ax.text(years[i], total + height / 2, f'{height}%', ha='center', va='center', fontsize=9, color='white')
        total += height

# Legend and layout adjustment
ax.legend(title='Browsers', loc='upper left', bbox_to_anchor=(1.05, 1))
plt.xticks(years, rotation=45, ha='right')
plt.tight_layout()

# Show the plot
plt.show()