import matplotlib.pyplot as plt
import numpy as np

# Years and number of active users (in millions) for each platform
years = np.arange(2010, 2021)

instagram_users = [0.1, 1.0, 2.0, 3.5, 5.0, 7.5, 10.0, 15.0, 20.0, 25.0, 30.0]
facebook_users = [500, 600, 700, 800, 900, 1000, 1100, 1100, 1150, 1200, 1250]
twitter_users = [50, 70, 100, 150, 200, 250, 280, 300, 320, 340, 350]

# Create the figure and axis
plt.figure(figsize=(14, 8))

# Plot lines for each platform
plt.plot(years, instagram_users, marker='o', linestyle='-', color='purple', linewidth=2, label='Instagram')
plt.plot(years, facebook_users, marker='o', linestyle='-', color='blue', linewidth=2, label='Facebook')
plt.plot(years, twitter_users, marker='o', linestyle='-', color='cyan', linewidth=2, label='Twitter')

# Annotate significant points on the plots
plt.annotate('Rapid Growth', xy=(2014, 5.0), xytext=(2015, 8.0),
             arrowprops=dict(facecolor='gray', arrowstyle='->'), fontsize=10, backgroundcolor='white')
plt.annotate('Stagnation', xy=(2018, 1100), xytext=(2016, 900),
             arrowprops=dict(facecolor='gray', arrowstyle='->'), fontsize=10, backgroundcolor='white')
plt.annotate('Steady Increase', xy=(2012, 100), xytext=(2013, 150),
             arrowprops=dict(facecolor='gray', arrowstyle='->'), fontsize=10, backgroundcolor='white')

# Set title and labels
plt.title('Social Media User Engagement Trends\n(2010-2020)', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=14)
plt.ylabel('Active Users (in millions)', fontsize=14)

# Customize x-axis and y-axis ticks
plt.xticks(years)
plt.yticks(np.arange(0, 1301, 100))

# Add grid lines
plt.grid(True, linestyle='--', alpha=0.7)

# Add a legend
plt.legend(title='Platforms', loc='upper left', fontsize=10)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()