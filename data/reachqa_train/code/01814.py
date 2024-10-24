import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Subscription data for each platform (in millions)
netflix_subs = np.array([20, 30, 45, 60, 80, 100, 130, 160, 200, 230, 250])
prime_subs = np.array([10, 15, 20, 30, 45, 60, 80, 95, 120, 150, 180])
disney_subs = np.array([0, 0, 0, 0, 0, 0, 0, 10, 30, 60, 90])

# Create the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Set color palette
colors = cm.viridis(np.linspace(0, 1, 3))

# Plot lines for each streaming platform with varied styles
ax.plot(years, netflix_subs, 'o-', label='Netflix', color=colors[0], linewidth=2.5, linestyle='-')
ax.plot(years, prime_subs, 's-', label='Amazon Prime', color=colors[1], linewidth=2.5, linestyle='--')
ax.plot(years, disney_subs, '^-', label='Disney+', color=colors[2], linewidth=2.5, linestyle='-.')

# Fill between lines to show growth area
ax.fill_between(years, 0, netflix_subs, color=colors[0], alpha=0.1)
ax.fill_between(years, 0, prime_subs, color=colors[1], alpha=0.1)
ax.fill_between(years, 0, disney_subs, color=colors[2], alpha=0.1)

# Annotate significant points
ax.annotate('Launch', xy=(2019, 10), xytext=(2017, 30),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='green')

# Titles and labels
ax.set_title("Global Streaming Platform Subscriptions Growth\n(2010-2020)", fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Subscriptions (in millions)", fontsize=12)

# Add horizontal line for subscription milestone
ax.axhline(y=100, color='grey', linestyle='--', linewidth=1, label='100M Milestone')

# Legend
ax.legend(title="Streaming Platforms", fontsize=10, title_fontsize=12, loc='upper left', frameon=True, shadow=True, fancybox=True)

# Grid and axis settings
ax.grid(True, linestyle='--', alpha=0.5)
ax.set_xlim(2009, 2021)
ax.set_ylim(0, 300)

# Customize the x-axis ticks for clarity
plt.xticks(years, rotation=45)

# Adjust layout to avoid overlap
plt.tight_layout()

# Display the chart
plt.show()