import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Define the years for the chart
years = np.arange(2015, 2023)

# Hypothetical data for average player skill rating (SRP) over the years
player_skill_rating = np.array([1500, 1550, 1600, 1650, 1700, 1750, 1800, 1850])

# Hypothetical audience growth for eSports tournaments (in millions)
audience_growth = np.array([5, 10, 15, 25, 40, 60, 80, 100])

# Hypothetical revenue from eSports (in millions)
esports_revenue = np.array([200, 300, 500, 800, 1200, 1800, 2400, 3200])

# Create a new figure with subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

# Left subplot for player skill rating and audience growth
ax1.scatter(years, player_skill_rating, color='blue', label='Avg Player Skill Rating (SRP)', s=100, alpha=0.7)
ax1.set_title('Player Performance & Audience Growth', fontsize=16, fontweight='bold')

# Second y-axis for audience growth
ax1_twin = ax1.twinx()
ax1_twin.scatter(years, audience_growth, color='orange', label='Audience Growth (millions)', s=100, alpha=0.7)

# Smooth fitting lines
x_new = np.linspace(years.min(), years.max(), 300)
spl_player = make_interp_spline(years, player_skill_rating, k=3)
player_skill_smooth = spl_player(x_new)
ax1.plot(x_new, player_skill_smooth, color='darkblue', linestyle='--', linewidth=2)

spl_audience = make_interp_spline(years, audience_growth, k=3)
audience_smooth = spl_audience(x_new)
ax1_twin.plot(x_new, audience_smooth, color='gold', linestyle='--', linewidth=2)

# Set labels and legends for the first subplot
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Avg Player Skill Rating (SRP)', fontsize=14, color='blue')
ax1_twin.set_ylabel('Audience Growth (millions)', fontsize=14, color='orange')
ax1.legend(loc='upper left')
ax1_twin.legend(loc='upper right')
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Right subplot for eSports revenue
ax2.bar(years, esports_revenue, color='teal', alpha=0.7, label='eSports Revenue (millions)')
ax2.set_title('eSports Revenue Growth', fontsize=16, fontweight='bold')
ax2.set_xlabel('Year', fontsize=14)
ax2.set_ylabel('Revenue (millions)', fontsize=14, color='teal')
ax2.legend(loc='upper left')
ax2.grid(axis='y', linestyle='--', alpha=0.7)

# Set limits for clarity
ax1.set_xlim(years.min() - 0.5, years.max() + 0.5)
ax1.set_ylim(player_skill_rating.min() - 50, player_skill_rating.max() + 50)
ax1_twin.set_ylim(0, audience_growth.max() + 10)
ax2.set_ylim(0, esports_revenue.max() + 500)

# Adjust layout to avoid occlusion
plt.tight_layout()

# Display the plot
plt.show()