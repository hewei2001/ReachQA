import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2019
years = np.arange(2010, 2020)

# Checkouts data in thousands
fiction = [120, 130, 125, 140, 150, 155, 160, 165, 170, 175]
non_fiction = [90, 95, 100, 105, 110, 115, 120, 125, 130, 135]
science = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
history = [40, 42, 45, 48, 50, 52, 55, 58, 60, 65]
romance = [70, 72, 75, 78, 80, 82, 85, 88, 90, 93]
mystery = [60, 63, 65, 68, 70, 73, 75, 78, 80, 82]
fantasy = [80, 85, 90, 95, 100, 105, 110, 115, 120, 125]

# Create stacked bar chart
fig, ax = plt.subplots(figsize=(14, 8))

ax.bar(years, fiction, label='Fiction', color='#FF9999')
ax.bar(years, non_fiction, bottom=fiction, label='Non-Fiction', color='#66B3FF')
ax.bar(years, science, bottom=np.array(fiction) + np.array(non_fiction), label='Science', color='#99FF99')
ax.bar(years, history, bottom=np.array(fiction) + np.array(non_fiction) + np.array(science), label='History', color='#FFCC99')
ax.bar(years, romance, bottom=np.array(fiction) + np.array(non_fiction) + np.array(science) + np.array(history), label='Romance', color='#C2C2F0')
ax.bar(years, mystery, bottom=np.array(fiction) + np.array(non_fiction) + np.array(science) + np.array(history) + np.array(romance), label='Mystery', color='#FFB3E6')
ax.bar(years, fantasy, bottom=np.array(fiction) + np.array(non_fiction) + np.array(science) + np.array(history) + np.array(romance) + np.array(mystery), label='Fantasy', color='#FFD699')

# Title and Labels
ax.set_title("Evolution of Library Book Categories\nOver a Decade", fontsize=18, fontweight='bold')
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Number of Checkouts (in Thousands)", fontsize=14)

# Rotate x-axis labels for better readability
plt.xticks(years, rotation=45)

# Legend placement
ax.legend(title='Book Categories', loc='upper left', bbox_to_anchor=(1, 1))

# Grid and layout adjustments
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

# Show plot
plt.show()