import matplotlib.pyplot as plt
import numpy as np

# Data setup
platforms = ['Facebook', 'Instagram', 'Twitter', 'Snapchat', 'TikTok']
market_shares = [25, 20, 15, 10, 30]  # Percentage values summing to 100%
daily_active_users = [2900, 1500, 330, 500, 800]  # Hypothetical daily active users in millions

# Define colors for each platform
colors = ['#3b5998', '#e4405f', '#1da1f2', '#fffc00', '#69c9d0']

# Create the subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7), gridspec_kw={'width_ratios': [1, 1]})

# Plot 1: Horizontal Bar Chart for Market Share
bar_container = ax1.barh(platforms, market_shares, color=colors, edgecolor='black')
ax1.set_title('2023 Social Media Platform Market Share', fontsize=16, fontweight='bold', pad=15)
ax1.set_xlabel('Market Share (%)', fontsize=12)
ax1.set_ylabel('Platforms', fontsize=12)
ax1.bar_label(bar_container, fmt='%.0f%%', padding=3, fontsize=11)
ax1.set_xlim(0, 100)

# Plot 2: Pie Chart for Daily Active Users
ax2.pie(daily_active_users, labels=platforms, autopct='%1.1f%%', startangle=90, colors=colors,
        wedgeprops={'edgecolor': 'black'})
ax2.set_title('Average Daily Active Users in 2023\n(Millions)', fontsize=16, fontweight='bold', pad=15)

# Adjust layout to prevent overlap and ensure clarity
plt.tight_layout()

# Display the charts
plt.show()