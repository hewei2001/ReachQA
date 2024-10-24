import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2010 to 2020
years = np.arange(2010, 2021)

# Original data: Social media usage in percentage for each generation
baby_boomers = [10, 12, 15, 17, 20, 22, 23, 25, 28, 30, 32]
gen_x = [25, 27, 30, 35, 38, 40, 42, 43, 45, 48, 50]
millennials = [40, 45, 50, 55, 58, 60, 62, 63, 65, 68, 70]
gen_z = [5, 8, 12, 15, 18, 20, 25, 28, 30, 35, 40]

# Additional data: Average time spent on social media in hours/day
time_baby_boomers = [0.5, 0.6, 0.7, 0.9, 1.1, 1.2, 1.3, 1.4, 1.6, 1.8, 2.0]
time_gen_x = [1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.5, 2.7, 3.0]
time_millennials = [2.0, 2.3, 2.6, 2.9, 3.1, 3.3, 3.5, 3.7, 3.9, 4.2, 4.5]
time_gen_z = [0.2, 0.4, 0.8, 1.1, 1.5, 1.8, 2.3, 2.7, 3.0, 3.5, 4.0]

# Initialize plot with two subplots
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(14, 7))

# Plot the stacked bar chart
ax1.bar(years, baby_boomers, label='Baby Boomers', color='skyblue', alpha=0.9)
ax1.bar(years, gen_x, bottom=baby_boomers, label='Generation X', color='lightgreen', alpha=0.9)
ax1.bar(years, millennials, bottom=np.array(baby_boomers) + np.array(gen_x), label='Millennials', color='salmon', alpha=0.9)
ax1.bar(years, gen_z, bottom=np.array(baby_boomers) + np.array(gen_x) + np.array(millennials), label='Gen Z', color='orange', alpha=0.9)

# Customize the stacked bar chart
ax1.set_title('Social Media Usage (%)\nAcross Generations (2010-2020)', fontsize=14, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Usage (%)', fontsize=12)
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)
ax1.set_ylim(0, 160)
ax1.legend(title='Generations', fontsize=10, title_fontsize=11, loc='upper left')
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)

# Plot the line chart for average time spent
ax2.plot(years, time_baby_boomers, label='Baby Boomers', color='skyblue', marker='o')
ax2.plot(years, time_gen_x, label='Generation X', color='lightgreen', marker='s')
ax2.plot(years, time_millennials, label='Millennials', color='salmon', marker='^')
ax2.plot(years, time_gen_z, label='Gen Z', color='orange', marker='d')

# Customize the line chart
ax2.set_title('Average Time on Social Media (hours/day)\nAcross Generations (2010-2020)', fontsize=14, fontweight='bold')
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Time (hours)', fontsize=12)
ax2.set_xticks(years)
ax2.set_xticklabels(years, rotation=45)
ax2.set_ylim(0, 5)
ax2.legend(title='Generations', fontsize=10, title_fontsize=11, loc='upper left')
ax2.yaxis.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()