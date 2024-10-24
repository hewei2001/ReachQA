import matplotlib.pyplot as plt
import numpy as np

# Data for the original donut chart
categories = ['Electronics', 'Fashion', 'Home & Kitchen', 'Beauty & Health', 'Sports & Outdoors', 'Toys & Games', 'Books & Stationery']
market_share = [25, 20, 15, 10, 10, 10, 10]

# Colors for each segment
colors = ['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1', '#F4E1E1', '#B565A7']

# Related data for the new subplot (e.g., growth rates over a hypothetical year)
growth_rates = [4, 2.5, 3, 5, 3.5, 2, 1.5]
categories_for_growth = categories

# Create a figure with two subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Plot the donut chart
wedges, texts, autotexts = ax1.pie(
    market_share, labels=categories, colors=colors, autopct='%1.1f%%', startangle=140, 
    pctdistance=0.85, wedgeprops=dict(width=0.3, edgecolor='white')
)

# Add a center circle for the donut shape
centre_circle = plt.Circle((0, 0), 0.55, fc='white')
ax1.add_artist(centre_circle)
ax1.axis('equal')
ax1.set_title('E-Commerce Product Categories:\nMarket Share Insights for 2023', fontsize=15, weight='bold', pad=20)

# Beautify the plot
plt.setp(autotexts, size=11, weight="bold", color='black')
plt.setp(texts, size=10)

# Create a legend and place it outside the plot
ax1.legend(wedges, categories, title="Categories", loc="center left", bbox_to_anchor=(1.1, 0, 0.5, 1), fontsize=10)

# Plot a bar chart for the growth rates
x_pos = np.arange(len(categories_for_growth))
bars = ax2.bar(x_pos, growth_rates, color=colors, edgecolor='grey', alpha=0.7)

# Labeling
ax2.set_xticks(x_pos)
ax2.set_xticklabels(categories_for_growth, rotation=45, ha='right', fontsize=10)
ax2.set_title('Growth Rate of Product Categories in 2023', fontsize=15, weight='bold', pad=20)
ax2.set_ylabel('Growth Rate (%)', fontsize=12)

# Add data labels above the bars
for bar, rate in zip(bars, growth_rates):
    ax2.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{rate}%', ha='center', va='bottom', fontsize=11, weight='bold')

# Optimize layout
plt.tight_layout()

# Display the plots
plt.show()