import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Subscription data for each platform (in millions)
netflix_subs = np.array([20, 30, 45, 60, 80, 100, 130, 160, 200, 230, 250])
prime_subs = np.array([10, 15, 20, 30, 45, 60, 80, 95, 120, 150, 180])
disney_subs = np.array([0, 0, 0, 0, 0, 0, 0, 10, 30, 60, 90])  # Disney+ launched in 2019

# Create the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot lines for each streaming platform
ax.plot(years, netflix_subs, 'o-', label='Netflix', color='red', linewidth=2, alpha=0.7)
ax.plot(years, prime_subs, 's-', label='Amazon Prime', color='blue', linewidth=2, alpha=0.7)
ax.plot(years, disney_subs, '^-', label='Disney+', color='green', linewidth=2, alpha=0.7)

# Annotate important points
for year, n_subs, p_subs, d_subs in zip(years, netflix_subs, prime_subs, disney_subs):
    ax.annotate(f'{n_subs}', xy=(year, n_subs), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8, color='red')
    ax.annotate(f'{p_subs}', xy=(year, p_subs), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8, color='blue')
    ax.annotate(f'{d_subs}', xy=(year, d_subs), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8, color='green')

# Titles and labels
ax.set_title("Global Streaming Platform Subscriptions Growth\n(2010-2020)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Subscriptions (in millions)", fontsize=12)

# Legend
ax.legend(title="Streaming Platforms", fontsize=10, title_fontsize=12, loc='upper left')

# Grid and axis settings
ax.grid(True, linestyle='--', alpha=0.5)
ax.set_xlim(2009, 2021)
ax.set_ylim(0, 300)

# Customize the x-axis ticks for clarity
plt.xticks(years, rotation=45)
plt.tight_layout()

# Display the chart
plt.show()