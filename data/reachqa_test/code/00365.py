import matplotlib.pyplot as plt
import numpy as np

# Data
years = [2015, 2016, 2017, 2018, 2019, 2020]
lattes = [150, 170, 190, 200, 220, 240]
cappuccinos = [120, 140, 160, 170, 180, 200]
americanos = [80, 90, 100, 110, 120, 130]
espressos = [50, 60, 70, 80, 90, 100]

# Create a figure and axis object
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the data
ax.plot(years, lattes, marker='o', linestyle='-', linewidth=2, color='b', label='Lattes')
ax.plot(years, cappuccinos, marker='s', linestyle='--', linewidth=2, color='g', label='Cappuccinos')
ax.plot(years, americanos, marker='^', linestyle='-.', linewidth=2, color='r', label='Americanos')
ax.plot(years, espressos, marker='D', linestyle=':', linewidth=2, color='y', label='Espressos')

# Set title and labels
ax.set_title("Annual Sales of Popular Coffee Drinks in the United States\n"
             "(2015-2020)\n"
             "Source: National Coffee Association", fontsize=14)
ax.set_xlabel("Year")
ax.set_ylabel("Sales (Millions of Dollars)")

# Add grid and legend
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), ncol=2)

# Add annotations
for i, year in enumerate(years):
    ax.annotate(f"{lattes[i]:.0f}M", xy=(year, lattes[i]), xytext=(0, 10), textcoords='offset points', ha='center', fontsize=10)
    ax.annotate(f"{cappuccinos[i]:.0f}M", xy=(year, cappuccinos[i]), xytext=(0, 10), textcoords='offset points', ha='center', fontsize=10)
    ax.annotate(f"{americanos[i]:.0f}M", xy=(year, americanos[i]), xytext=(0, 10), textcoords='offset points', ha='center', fontsize=10)
    ax.annotate(f"{espressos[i]:.0f}M", xy=(year, espressos[i]), xytext=(0, 10), textcoords='offset points', ha='center', fontsize=10)

# Adjust layout and show plot
plt.tight_layout(rect=[0, 0, 1, 0.8])
plt.show()