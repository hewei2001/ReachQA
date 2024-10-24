import matplotlib.pyplot as plt
import numpy as np

# Data setup: Years from 2000 to 2020
years = np.arange(2000, 2021)

# Adoption rates for different internet technologies
dial_up = np.array([70, 67, 65, 60, 55, 50, 45, 40, 30, 25, 20, 15, 10, 8, 5, 3, 2, 1, 0.5, 0.2, 0.1])
broadband = np.array([5, 8, 12, 20, 30, 40, 50, 60, 70, 75, 80, 82, 84, 86, 88, 90, 92, 94, 95, 96, 97])
fiber_optics = np.array([0, 0, 0, 1, 2, 3, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 65, 70, 75, 80])

# Mobile internet adoption rates (additional data for the new subplot)
mobile_internet = np.array([2, 5, 10, 15, 22, 30, 40, 50, 60, 68, 75, 80, 85, 88, 90, 92, 93, 94, 95, 96, 97])

# Initialize the plot with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# Plotting each technology's adoption rate on the first subplot
ax1.plot(years, dial_up, marker='o', color='#FF6347', label='Dial-up', linewidth=2, linestyle='--')
ax1.plot(years, broadband, marker='s', color='#4682B4', label='Broadband', linewidth=2, linestyle='-')
ax1.plot(years, fiber_optics, marker='^', color='#32CD32', label='Fiber Optics', linewidth=2, linestyle='-.')

# Annotate important points on the first subplot
for year, rate in zip(years, dial_up):
    if year % 4 == 0:
        ax1.annotate(f'{rate:.1f}%', xy=(year, rate), xytext=(5, 5), textcoords='offset points', fontsize=9, color='#FF6347')
for year, rate in zip(years, broadband):
    if year % 4 == 0:
        ax1.annotate(f'{rate:.1f}%', xy=(year, rate), xytext=(-10, 10), textcoords='offset points', fontsize=9, color='#4682B4')
for year, rate in zip(years, fiber_optics):
    if year % 4 == 0:
        ax1.annotate(f'{rate:.1f}%', xy=(year, rate), xytext=(-10, -15), textcoords='offset points', fontsize=9, color='#32CD32')

# Highlight specific events with annotations on the first subplot
ax1.annotate('Peak Broadband Growth', xy=(2008, 60), xytext=(2010, 40),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, fontweight='bold', color='navy')
ax1.annotate('Fiber Optics Surge', xy=(2018, 65), xytext=(2015, 75),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, fontweight='bold', color='forestgreen')

# Title and axis labels for the first subplot
ax1.set_title("Internet Technologies Adoption (2000-2020): Dial-up, Broadband, Fiber Optics",
              fontsize=14, weight='bold', pad=15)
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Adoption Rate (%)", fontsize=12)

# Legend positioning for the first subplot
ax1.legend(loc='upper right', fontsize=10, title="Technology")

# Enable grid lines for the first subplot
ax1.grid(True, which='major', linestyle='--', linewidth=0.5, alpha=0.7)

# Second subplot: Mobile internet adoption rates
ax2.bar(years, mobile_internet, color='#FFD700', label='Mobile Internet', alpha=0.7)

# Title and axis labels for the second subplot
ax2.set_title("Mobile Internet Adoption Rates (2000-2020)", fontsize=14, weight='bold', pad=15)
ax2.set_xlabel("Year", fontsize=12)
ax2.set_ylabel("Adoption Rate (%)", fontsize=12)

# Annotate important bars in the second subplot
for year, rate in zip(years, mobile_internet):
    if year % 5 == 0:
        ax2.annotate(f'{rate:.1f}%', xy=(year, rate), xytext=(-15, 5), textcoords='offset points', fontsize=9, color='black')

# Legend for the second subplot
ax2.legend(loc='upper left', fontsize=10)

# Enable grid lines for the second subplot
ax2.grid(True, which='major', linestyle='--', linewidth=0.5, alpha=0.7)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()