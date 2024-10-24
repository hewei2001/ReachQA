import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# Years from 2050 to 2060
years = np.arange(2050, 2061)

# Internet users (in thousands) for each colony
internet_users_mars = np.array([50, 70, 95, 120, 160, 210, 280, 360, 460, 580, 720])
internet_users_europa = np.array([10, 15, 22, 30, 45, 65, 90, 120, 160, 210, 280])
internet_users_titan = np.array([5, 8, 12, 20, 30, 45, 65, 85, 110, 140, 180])

# Calculate additional metrics for a secondary plot
growth_rate_mars = np.diff(internet_users_mars, prepend=internet_users_mars[0])
growth_rate_europa = np.diff(internet_users_europa, prepend=internet_users_europa[0])
growth_rate_titan = np.diff(internet_users_titan, prepend=internet_users_titan[0])

# Set up the figure and axes
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 12), sharex=True, gridspec_kw={'height_ratios': [3, 1]})

# Primary plot: Stackplot
ax1.stackplot(years, internet_users_mars, internet_users_europa, internet_users_titan,
              labels=['Mars', 'Europa', 'Titan'],
              colors=['#8B0000', '#1E90FF', '#FF8C00'], alpha=0.8)

# Annotations
ax1.annotate('Mars: Rapid Growth Begins', xy=(2055, 210), xytext=(2052, 500),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='crimson')
ax1.annotate('Titan: Infrastructure Boom', xy=(2058, 110), xytext=(2056, 300),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='darkorange')

# Title and labels
ax1.set_title("Internet Usage Trends in Galactic Colonies\n(2050-2060)", fontsize=16, fontweight='bold')
ax1.set_ylabel("Internet Users (in thousands)", fontsize=12)

# Legend
custom_legend = [Patch(facecolor='#8B0000', label='Mars'),
                 Patch(facecolor='#1E90FF', label='Europa'),
                 Patch(facecolor='#FF8C00', label='Titan')]
ax1.legend(handles=custom_legend, title="Colonies", title_fontsize='13', fontsize='11', loc='upper left')

# Grid lines
ax1.grid(True, linestyle='--', alpha=0.5)

# Secondary plot: Growth rate
ax2.plot(years, growth_rate_mars, label='Mars Growth Rate', color='crimson', marker='o')
ax2.plot(years, growth_rate_europa, label='Europa Growth Rate', color='royalblue', marker='x')
ax2.plot(years, growth_rate_titan, label='Titan Growth Rate', color='darkorange', marker='s')

# Subplot title and labels
ax2.set_title("Annual Growth Rate of Internet Users", fontsize=14, fontweight='bold')
ax2.set_xlabel("Year", fontsize=12)
ax2.set_ylabel("Growth Rate", fontsize=12)

# Legend for growth rate
ax2.legend(loc='upper left')

# Rotate x-axis labels for both subplots
plt.xticks(rotation=45)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()