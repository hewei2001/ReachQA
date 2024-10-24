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

# Calculate total checkouts for each year
total_checkouts = np.array(fiction) + np.array(non_fiction) + np.array(science) + np.array(history) + np.array(romance) + np.array(mystery) + np.array(fantasy)

# Creating subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8), gridspec_kw={'width_ratios': [2, 1]})

# Stacked Bar Chart
ax1.bar(years, fiction, label='Fiction', color='#FF9999')
ax1.bar(years, non_fiction, bottom=fiction, label='Non-Fiction', color='#66B3FF')
ax1.bar(years, science, bottom=np.array(fiction) + np.array(non_fiction), label='Science', color='#99FF99')
ax1.bar(years, history, bottom=np.array(fiction) + np.array(non_fiction) + np.array(science), label='History', color='#FFCC99')
ax1.bar(years, romance, bottom=np.array(fiction) + np.array(non_fiction) + np.array(science) + np.array(history), label='Romance', color='#C2C2F0')
ax1.bar(years, mystery, bottom=np.array(fiction) + np.array(non_fiction) + np.array(science) + np.array(history) + np.array(romance), label='Mystery', color='#FFB3E6')
ax1.bar(years, fantasy, bottom=np.array(fiction) + np.array(non_fiction) + np.array(science) + np.array(history) + np.array(romance) + np.array(mystery), label='Fantasy', color='#FFD699')

ax1.set_title("Evolution of Library Book Categories\nOver a Decade", fontsize=16, fontweight='bold')
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Checkouts (Thousands)", fontsize=12)
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)
ax1.legend(title='Book Categories', loc='upper left', bbox_to_anchor=(1, 1))

# Line Plot of Total Checkouts
ax2.plot(years, total_checkouts, marker='o', linestyle='-', color='navy', label='Total Checkouts')
ax2.set_title("Total Checkouts Per Year", fontsize=16, fontweight='bold')
ax2.set_xlabel("Year", fontsize=12)
ax2.set_ylabel("Checkouts (Thousands)", fontsize=12)
ax2.set_xticks(years)
ax2.set_xticklabels(years, rotation=45)
ax2.yaxis.grid(True, linestyle='--', alpha=0.7)
ax2.legend(loc='upper left')

# Adjust layout for clarity and to avoid overlap
plt.tight_layout()
plt.show()