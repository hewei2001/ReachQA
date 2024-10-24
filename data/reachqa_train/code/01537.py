import numpy as np
import matplotlib.pyplot as plt

# Data for plotting
years = np.arange(2010, 2020)
strawberries_yield = np.array([1.0, 1.2, 1.5, 2.0, 2.2, 2.4, 2.8, 3.0, 3.5, 3.8])
kale_yield = np.array([0.8, 1.0, 1.1, 1.3, 1.6, 1.8, 2.0, 2.2, 2.5, 2.7])
tomatoes_yield = np.array([1.5, 1.7, 1.8, 2.1, 2.4, 2.6, 3.0, 3.2, 3.4, 3.9])

# Prices per tonne for revenue calculation
price_strawberries = 1000
price_kale = 800
price_tomatoes = 900

# Calculating revenues
revenue_strawberries = strawberries_yield * price_strawberries
revenue_kale = kale_yield * price_kale
revenue_tomatoes = tomatoes_yield * price_tomatoes

# Total revenue for each year
total_revenue = revenue_strawberries + revenue_kale + revenue_tomatoes

# Calculate the cumulative yields for stacked area plotting
cumulative_kale = strawberries_yield + kale_yield
cumulative_tomatoes = cumulative_kale + tomatoes_yield

# Initialize plot
fig, ax1 = plt.subplots(figsize=(12, 7))

# Plotting stacked areas
ax1.fill_between(years, strawberries_yield, color='#FF6347', alpha=0.6, label='Strawberries')
ax1.fill_between(years, cumulative_kale, strawberries_yield, color='#228B22', alpha=0.6, label='Kale')
ax1.fill_between(years, cumulative_tomatoes, cumulative_kale, color='#FFD700', alpha=0.6, label='Tomatoes')

# Titles and labels
ax1.set_title('Organic Farm Harvest and Revenue Trends\n(2010-2019)', fontsize=16, fontweight='bold', color='darkgreen')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Yield in Tonnes', fontsize=12, color='black')

# Creating a second y-axis for the revenue data
ax2 = ax1.twinx()
ax2.plot(years, total_revenue, color='blue', linewidth=2.5, linestyle='-', marker='o', label='Total Revenue ($)')
ax2.set_ylabel('Revenue in $', fontsize=12, color='blue')

# Customize legend
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 1.0), fontsize=10, title='Crops and Revenue', title_fontsize='12')

# Grid lines for readability
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Beautify x and y ticks
ax1.set_xticks(years)
ax1.set_yticks(np.arange(0, 12, 1))
ax1.yaxis.set_tick_params(labelsize=10)
ax1.xaxis.set_tick_params(labelsize=10)
ax2.set_yticks(np.arange(0, 30000, 5000))
ax2.yaxis.set_tick_params(labelsize=10, colors='blue')

# Avoid overlapping x-axis labels
plt.xticks(rotation=45)

# Annotation to highlight significant data points
ax1.annotate('Peak Strawberry Yield', xy=(2019, 3.8), xytext=(2016, 9),
             arrowprops=dict(facecolor='black', arrowstyle='->', linewidth=1.5),
             fontsize=10, color='black', fontweight='bold')

ax2.annotate('Peak Revenue', xy=(2019, total_revenue[-1]), xytext=(2016, 25000),
             arrowprops=dict(facecolor='blue', arrowstyle='->', linewidth=1.5),
             fontsize=10, color='blue', fontweight='bold')

# Tidy layout to prevent clipping
plt.tight_layout()

# Show plot
plt.show()