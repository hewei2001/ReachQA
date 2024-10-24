import matplotlib.pyplot as plt
import numpy as np

# Define years and initial revenue
years = [str(year) for year in range(2020, 2030)] + ["Total"]  # Match the number of revenue changes
initial_revenue = 450  # Initial revenue in million USD for 2020

# Define detailed revenue changes over years with more factors
revenue_changes = [
    {"Market Expansion": 50, "Supply Issues": -30, "New Products": 60},
    {"Competition": -20, "Efficiencies": 40, "Expansion": 25},
    {"Currency Fluctuation": -15, "E-commerce Growth": 35, "Technology Investment": 45},
    {"Tax Impact": -10, "Regulatory Changes": 20, "Market Volatility": -25},
    {"Geographic Expansion": 30, "Online Sales": 50, "Franchise Operations": -5},
    {"Retail Growth": 15, "Wholesale Dynamics": 40, "Logistics Optimisation": 10},
    {"Taxation Change": -5, "Market Stabilisation": 60, "Tech Upgrades": 25},
    {"Competitor Pressures": -30, "Operational Streamlining": 40, "New Market Entry": 55},
    {"Environmental Impact": -20, "Supplier Negotiation": 35, "Brand Expansion": 45},
    {"M&A Activities": 50, "Online Growth": 30, "Market Share Increase": 20}
]

# Calculate cumulative revenues
cumulative_revenue = [initial_revenue]
for year in revenue_changes:
    total_change = sum(year.values())
    cumulative_revenue.append(cumulative_revenue[-1] + total_change)

# Set up the waterfall chart
fig, ax = plt.subplots(figsize=(16, 10))

# Colors for revenue changes
colors = ['#2ecc71' if sum(year.values()) > 0 else '#e74c3c' for year in revenue_changes]
colors.insert(0, '#3498db')  # Initial color for the starting revenue
colors.append('#9b59b6')  # Color for the final total

# Plot bars for the waterfall chart
bars = ax.bar(years, cumulative_revenue, color=colors, edgecolor='grey', width=0.5, alpha=0.9)

# Connect each bar with lines to indicate progression
for i in range(1, len(years)):
    ax.plot([i, i], [cumulative_revenue[i-1], cumulative_revenue[i]], color='black', linestyle='-', linewidth=1.5)

# Annotate each bar with revenue change and cumulative value
for i in range(1, len(years)):
    change = sum(revenue_changes[i-1].values()) if i < len(years) else 0
    ax.text(i, cumulative_revenue[i] + (10 if change > 0 else -20), f'{change:+}M', ha='center', va='bottom', fontsize=10, color='black')
    ax.text(i, cumulative_revenue[i] + (30 if change > 0 else -40), f'{cumulative_revenue[i]}M', ha='center', fontsize=10, color='black')

# Annotate the final total bar separately
ax.text(len(years)-1, cumulative_revenue[-1] + 10, f'{cumulative_revenue[-1]}M', ha='center', fontsize=10, color='black')

# Title and labels
ax.set_title('Decade of Dynamics: Comprehensive Revenue Analysis (2020-2030)', fontsize=16, pad=20)
ax.set_ylabel('Revenue (Million USD)', fontsize=12)
ax.set_xlabel('Year', fontsize=12)

# Add grid and adjust layout
ax.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Show the plot
plt.show()