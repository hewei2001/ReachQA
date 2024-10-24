import matplotlib.pyplot as plt
import numpy as np

# Regions and EV sales data (in thousands)
regions = ['North America', 'Europe', 'Asia-Pacific', 'South America', 'Middle East & Africa']
ev_sales = {
    'North America': [220, 280, 330, 400, 470],
    'Europe': [170, 200, 250, 300, 360],
    'Asia-Pacific': [350, 420, 490, 570, 650],
    'South America': [60, 75, 90, 105, 120],
    'Middle East & Africa': [25, 35, 45, 55, 70]
}

# Total sales by region (2018-2022)
total_sales = [sum(sales) for sales in ev_sales.values()]

# Annual growth rates (%)
growth_rates = {
    region: [(sales[i + 1] - sales[i]) / sales[i] * 100 for i in range(len(sales) - 1)]
    for region, sales in ev_sales.items()
}

# X-axis positions for the bar chart
x_pos = np.arange(len(regions))

# Create figure and subplots
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Bar chart: Total EV Sales by Region
axs[0].bar(x_pos, total_sales, color='deepskyblue', alpha=0.8, width=0.6)
axs[0].set_xticks(x_pos)
axs[0].set_xticklabels(regions, rotation=45, ha='right', fontsize=10)
axs[0].set_xlabel('Region', fontsize=12)
axs[0].set_ylabel('Total EV Sales (thousands)', fontsize=12)
axs[0].set_title('Total EV Sales by Region (2018-2022)', fontsize=14)
axs[0].grid(axis='y', linestyle='--', alpha=0.7)

# Annotate bar values
for i, sales in enumerate(total_sales):
    axs[0].text(x_pos[i], sales + 20, f'{sales}k', ha='center', fontsize=10)

# Line chart: Annual Growth Rate of EV Sales
for region, rates in growth_rates.items():
    axs[1].plot(np.arange(1, len(rates) + 1), rates, marker='o', label=region)
axs[1].set_xticks(np.arange(1, 5))
axs[1].set_xticklabels(['2019', '2020', '2021', '2022'], fontsize=10)
axs[1].set_xlabel('Year', fontsize=12)
axs[1].set_ylabel('Annual Growth Rate (%)', fontsize=12)
axs[1].set_title('Annual Growth Rate of EV Sales (2018-2022)', fontsize=14)
axs[1].legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)
axs[1].grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout and display plot
fig.tight_layout(rect=[0, 0, 1, 0.95])
fig.suptitle('The Rise of Electric Vehicles: Global Sales by Region', fontsize=16)

plt.show()
