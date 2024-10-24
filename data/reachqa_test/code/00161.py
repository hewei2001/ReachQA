import matplotlib.pyplot as plt
import numpy as np

# Decades from 1960 to 2020
decades = np.array([1960, 1970, 1980, 1990, 2000, 2010, 2020])

# Prevalence data for each graphic design trend over the decades
minimalism = [30, 25, 10, 5, 20, 40, 35]
pop_art = [20, 35, 25, 15, 10, 5, 5]
grunge = [0, 0, 5, 30, 20, 10, 0]
futurism = [10, 15, 20, 25, 30, 35, 45]

# Data for digital tool usage over the same decades
digital_tools = [5, 10, 20, 40, 50, 60, 70]

# Initialize the plot
fig, ax1 = plt.subplots(figsize=(12, 8))

# Plotting design trends
ax1.plot(decades, minimalism, 'o--', label='Minimalism', color='blue', linewidth=2, markersize=8)
ax1.plot(decades, pop_art, 's-', label='Pop Art', color='red', linewidth=2, markersize=8)
ax1.plot(decades, grunge, '^-', label='Grunge', color='green', linewidth=2, markersize=8)
ax1.plot(decades, futurism, 'd-', label='Futurism', color='purple', linewidth=2, markersize=8)

# Adding title and labels
ax1.set_title("The Evolution of Graphic Design Trends\nand Digital Tool Usage (1960 to 2020)",
              fontsize=16, fontweight='bold')
ax1.set_xlabel("Decade", fontsize=12)
ax1.set_ylabel("Trend Prevalence (%)", fontsize=12)

# Adding legend
ax1.legend(title="Design Trends", fontsize=10, loc='upper left', frameon=False)

# Enabling grid for readability
ax1.grid(True, linestyle='--', alpha=0.6)

# Secondary y-axis for digital tool usage
ax2 = ax1.twinx()
ax2.bar(decades, digital_tools, color='grey', alpha=0.3, width=6, label='Digital Tool Usage')
ax2.set_ylabel("Digital Tool Usage (%)", fontsize=12)
ax2.legend(title="Digital Tools", fontsize=10, loc='upper right', frameon=False)

# Configure x-ticks for clarity
ax1.set_xticks(decades)

# Annotating significant data points
for decade, value in zip(decades, digital_tools):
    ax2.annotate(f"{value}%", (decade, value), textcoords="offset points", xytext=(0,5),
                 ha='center', fontsize=9, color='black')

# Auto-adjust layout
fig.tight_layout()

# Show the plot
plt.show()