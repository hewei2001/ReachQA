import matplotlib.pyplot as plt

# Platforms and their market shares
platforms = ['ShopEase', 'QuickBuy', 'MegaMall', 'EcoShop', 'LocalMart']
market_shares = [35, 30, 20, 10, 5]

# Descriptions of platforms
descriptions = {
    'ShopEase': 'Exclusive deals, fast delivery.',
    'QuickBuy': 'AI recommendations, vast range.',
    'MegaMall': 'Personalized shopping with many brands.',
    'EcoShop': 'Eco-friendly, sustainable products.',
    'LocalMart': 'Supports local vendors.'
}

# Colors for each ring segment
colors = ['#4CAF50', '#FF9800', '#2196F3', '#8BC34A', '#FFC107']

# Create a ring chart
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(market_shares, labels=platforms, autopct='%1.1f%%', startangle=140,
                                  colors=colors, pctdistance=0.85, wedgeprops=dict(width=0.3, edgecolor='w'))

# Draw circle in the center to create a ring chart effect
centre_circle = plt.Circle((0, 0), 0.7, fc='white')
fig.gca().add_artist(centre_circle)

# Title positioned inside the ring
ax.set_title('E-commerce Market Share\nin Techland - 2023', fontsize=14, fontweight='bold', pad=20, va='center')

# Legend with platform descriptions
legend_labels = [f'{platforms[i]}: {descriptions[platforms[i]]}' for i in range(len(platforms))]
ax.legend(wedges, legend_labels, title="Platform Descriptions", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Customize text properties for clarity
plt.setp(texts, size=10, weight='bold')
plt.setp(autotexts, size=9, weight='bold', color="black")

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()