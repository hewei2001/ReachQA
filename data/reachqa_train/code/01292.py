import matplotlib.pyplot as plt
import numpy as np

# Data setup: Years from 2000 to 2020
years = np.arange(2000, 2021)

# Adoption rates for different internet technologies
dial_up = np.array([70, 67, 65, 60, 55, 50, 45, 40, 30, 25, 20, 15, 10, 8, 5, 3, 2, 1, 0.5, 0.2, 0.1])
broadband = np.array([5, 8, 12, 20, 30, 40, 50, 60, 70, 75, 80, 82, 84, 86, 88, 90, 92, 94, 95, 96, 97])
fiber_optics = np.array([0, 0, 0, 1, 2, 3, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 65, 70, 75, 80])

# Initialize the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plotting each technology's adoption rate
ax.plot(years, dial_up, marker='o', color='#FF6347', label='Dial-up', linewidth=2, linestyle='--')
ax.plot(years, broadband, marker='s', color='#4682B4', label='Broadband', linewidth=2, linestyle='-')
ax.plot(years, fiber_optics, marker='^', color='#32CD32', label='Fiber Optics', linewidth=2, linestyle='-.')

# Annotate important points
for year, rate in zip(years, dial_up):
    if year % 4 == 0:
        ax.annotate(f'{rate:.1f}%', xy=(year, rate), xytext=(5, 5), textcoords='offset points', fontsize=9, color='#FF6347')
        
for year, rate in zip(years, broadband):
    if year % 4 == 0:
        ax.annotate(f'{rate:.1f}%', xy=(year, rate), xytext=(-10, 10), textcoords='offset points', fontsize=9, color='#4682B4')
        
for year, rate in zip(years, fiber_optics):
    if year % 4 == 0:
        ax.annotate(f'{rate:.1f}%', xy=(year, rate), xytext=(-10, -15), textcoords='offset points', fontsize=9, color='#32CD32')

# Highlight specific events with annotations
ax.annotate('Peak Broadband Growth', xy=(2008, 60), xytext=(2010, 40),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, fontweight='bold', color='navy')

ax.annotate('Fiber Optics Surge', xy=(2018, 65), xytext=(2015, 75),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, fontweight='bold', color='forestgreen')

# Title and axis labels
ax.set_title("Rise of Internet Technologies (2000-2020):\nAdoption Rates of Dial-up, Broadband, and Fiber Optics", 
             fontsize=16, weight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Adoption Rate (%)", fontsize=12)

# Legend positioning
ax.legend(loc='upper left', fontsize=10, title="Internet Technology")

# Enable grid lines
ax.grid(True, which='major', linestyle='--', linewidth=0.5, alpha=0.7)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()