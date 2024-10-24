import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Define years and data for community events and volunteer rates
years = np.array([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])
social_events = np.array([5, 8, 12, 18, 25, 30, 34, 40, 48, 55, 60])
volunteer_rates = np.array([5, 8, 10, 14, 20, 28, 35, 45, 50, 58, 65])

# Define a fitting function (quadratic)
def quadratic_fit(x, a, b, c):
    return a * x**2 + b * x + c

# Perform curve fitting for the quadratic function
params, _ = curve_fit(quadratic_fit, social_events, volunteer_rates)

# Generate smooth line data for fitting
events_range = np.linspace(min(social_events), max(social_events), 300)
fitted_rates = quadratic_fit(events_range, *params)

# Plotting the scatter chart with a smooth fitting line
plt.figure(figsize=(10, 6))
plt.scatter(social_events, volunteer_rates, color='orange', label='Actual Participation', alpha=0.7, edgecolors='k')
plt.plot(events_range, fitted_rates, color='blue', linestyle='-', linewidth=2, label='Quadratic Fit')

# Annotating key points for emphasis
key_points = [0, 3, 6, 9]
for i in key_points:
    plt.annotate(f'Year: {years[i]}', (social_events[i], volunteer_rates[i]), textcoords="offset points", xytext=(5,-10), ha='center')

# Title and labels
plt.title('Community Engagement: Correlation Between\nSocial Events and Volunteer Participation', fontsize=16)
plt.xlabel('Number of Social Events', fontsize=12)
plt.ylabel('Volunteer Participation Rate (%)', fontsize=12)
plt.xlim(0, 65)
plt.ylim(0, 70)

# Adding a legend and grid
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()