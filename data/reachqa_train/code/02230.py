import matplotlib.pyplot as plt
import numpy as np

# Define the decades and the number of films produced in each genre
decades = np.arange(1950, 2030, 10)

# Film production data by genre
drama_films = [80, 85, 90, 70, 60, 55, 50, 40]
comedy_films = [70, 75, 85, 95, 100, 80, 70, 65]
western_films = [60, 55, 50, 30, 20, 15, 10, 5]

# Revenue data by genre (in millions)
drama_revenue = [300, 350, 400, 500, 480, 450, 420, 400]
comedy_revenue = [250, 270, 320, 350, 380, 360, 340, 330]
western_revenue = [200, 180, 160, 140, 120, 110, 100, 90]

# Create the line chart and bar chart overlay
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot each genre's film production data
ax1.plot(decades, drama_films, label='Drama Films', color='#2b83ba', linewidth=2, linestyle='-', marker='o')
ax1.plot(decades, comedy_films, label='Comedy Films', color='#fdae61', linewidth=2, linestyle='--', marker='s')
ax1.plot(decades, western_films, label='Western Films', color='#d7191c', linewidth=2, linestyle=':', marker='^')

# Create a secondary y-axis for revenue
ax2 = ax1.twinx()
width = 2  # Width of the bars

# Plot bar charts for revenue on the secondary y-axis
ax2.bar(decades - width, drama_revenue, width=width, color='#2b83ba', alpha=0.3, label='Drama Revenue')
ax2.bar(decades, comedy_revenue, width=width, color='#fdae61', alpha=0.3, label='Comedy Revenue')
ax2.bar(decades + width, western_revenue, width=width, color='#d7191c', alpha=0.3, label='Western Revenue')

# Set chart titles and labels
ax1.set_title("Rise and Fall of Classic Film Genres (1950-2020)\n Film Production & Revenue Trends", fontsize=14, fontweight='bold', pad=15)
ax1.set_xlabel("Decades", fontsize=12)
ax1.set_ylabel("Number of Films Produced", fontsize=12)
ax2.set_ylabel("Revenue in Millions (USD)", fontsize=12)

# Set grid and legend
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)
fig.legend(loc='upper right', fontsize=10, title='Legend', bbox_to_anchor=(0.9, 0.9))

# Annotate key trends
ax1.annotate('Comedy Boom', xy=(1980, 95), xytext=(1985, 110),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1.5),
             fontsize=10, fontweight='bold', color='green')
ax1.annotate('Western Decline', xy=(1970, 50), xytext=(1975, 60),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1.5),
             fontsize=10, fontweight='bold', color='red')

# Tighten layout to fit elements neatly
plt.tight_layout()

# Show the plot
plt.show()