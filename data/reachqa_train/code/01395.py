import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Define years and data for community events and volunteer rates
years = np.array([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])
social_events = np.array([5, 8, 12, 18, 25, 30, 34, 40, 48, 55, 60])
volunteer_rates = np.array([5, 8, 10, 14, 20, 28, 35, 45, 50, 58, 65])

# Additional dataset: Community budget allocation in $1000s
community_budget = np.array([2, 4, 6, 10, 15, 20, 25, 32, 40, 50, 62])

# Define a fitting function (quadratic)
def quadratic_fit(x, a, b, c):
    return a * x**2 + b * x + c

# Perform curve fitting for the quadratic function
params, _ = curve_fit(quadratic_fit, social_events, volunteer_rates)

# Generate smooth line data for fitting
events_range = np.linspace(min(social_events), max(social_events), 300)
fitted_rates = quadratic_fit(events_range, *params)

# Create the plot
fig, ax1 = plt.subplots(figsize=(12, 7))

# Plot the scatter chart with a smooth fitting line
ax1.scatter(social_events, volunteer_rates, color='orange', label='Actual Participation', alpha=0.7, edgecolors='k')
ax1.plot(events_range, fitted_rates, color='blue', linestyle='-', linewidth=2, label='Quadratic Fit')

# Secondary y-axis for community budget
ax2 = ax1.twinx()
ax2.bar(social_events, community_budget, color='green', alpha=0.3, label='Community Budget ($1000s)', width=1.5)

# Annotating key points for emphasis
key_points = [0, 3, 6, 9]
for i in key_points:
    ax1.annotate(f'Year: {years[i]}', (social_events[i], volunteer_rates[i]),
                 textcoords="offset points", xytext=(5, -10), ha='center', fontsize=9, color='purple')

# Title and labels
ax1.set_title('Community Engagement: Correlation Between Social Events and Volunteer Participation', fontsize=16, pad=20)
ax1.set_xlabel('Number of Social Events', fontsize=12)
ax1.set_ylabel('Volunteer Participation Rate (%)', fontsize=12, color='blue')
ax2.set_ylabel('Community Budget ($1000s)', fontsize=12, color='green')

# Set limits for axes
ax1.set_xlim(0, 65)
ax1.set_ylim(0, 70)
ax2.set_ylim(0, 70)

# Adding legends
ax1.legend(loc='upper left', fontsize=10)
ax2.legend(loc='upper right', fontsize=10)

# Adding grid and customizing it
ax1.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()