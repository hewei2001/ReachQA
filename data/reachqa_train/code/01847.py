import matplotlib.pyplot as plt
import numpy as np

# Company names and their market share data
companies = ["SkyNet Drones", "DroneX Inc.", "AeroFleet", "WingTech", "ParcelCopter", 
             "RoboFly", "QuadDeliver", "UAV Systems", "HyperAir", "CloudCourier"]
market_shares = [25, 18, 15, 12, 10, 8, 6, 3, 2, 1]

# Sort companies by market share for a cleaner plot
sorted_indices = np.argsort(market_shares)[::-1]
companies_sorted = [companies[i] for i in sorted_indices]
market_shares_sorted = [market_shares[i] for i in sorted_indices]

# Create the horizontal bar chart
fig, ax = plt.subplots(figsize=(12, 8))
bars = ax.barh(companies_sorted, market_shares_sorted, color=plt.cm.viridis(np.linspace(0, 1, len(companies_sorted))))

# Add data labels to each bar
for bar in bars:
    width = bar.get_width()
    ax.text(width + 0.5, bar.get_y() + bar.get_height() / 2, f'{width}%', va='center', fontsize=10, color='black')

# Customize the plot
ax.set_xlabel('Market Share (%)', fontsize=12, fontweight='bold')
ax.set_title('Top 10 Autonomous Delivery Drone Companies\nby Market Share in 2045', fontsize=16, fontweight='bold')
ax.invert_yaxis()  # Highest market share on top
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}%'))
ax.grid(axis='x', linestyle='--', alpha=0.7)
ax.set_xlim(0, max(market_shares_sorted) + 5)  # Set x-axis limit for better spacing

# Adjust layout to ensure nothing overlaps and everything fits
plt.tight_layout()

# Display the plot
plt.show()