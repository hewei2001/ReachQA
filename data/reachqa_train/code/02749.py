import matplotlib.pyplot as plt
import numpy as np

# Define decades and sectors
decades = ["1960s", "1970s", "1980s", "1990s", "2000s", "2010s", "2020s"]
sectors = ["Manufacturing", "Information Technology", "Agriculture", "Healthcare", "Education"]

# Define workforce impact data for each sector and decade
workforce_data = {
    "Manufacturing": [35, 32, 28, 25, 22, 18, 15],
    "Information Technology": [5, 7, 10, 15, 20, 25, 30],
    "Agriculture": [40, 35, 30, 28, 25, 20, 18],
    "Healthcare": [8, 10, 12, 15, 18, 20, 23],
    "Education": [12, 13, 14, 15, 16, 18, 20]
}

# Define color scheme for each sector
colors = {
    "Manufacturing": "#d62728",
    "Information Technology": "#1f77b4",
    "Agriculture": "#2ca02c",
    "Healthcare": "#ff7f0e",
    "Education": "#9467bd"
}

# Plot each sector's data
fig, ax = plt.subplots(figsize=(12, 8))

for sector, data in workforce_data.items():
    ax.plot(decades, data, marker='o', linestyle='-', linewidth=2, color=colors[sector], label=sector)

# Annotate data points with percentage values
for sector, data in workforce_data.items():
    for i, value in enumerate(data):
        ax.annotate(f"{value}%", (decades[i], value), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=9)

# Add title and labels
ax.set_title("Technological Evolution and Its Impact\non the Workforce Over the Decades", fontsize=16, weight='bold', pad=20)
ax.set_xlabel("Decades", fontsize=12)
ax.set_ylabel("Percentage of Workforce (%)", fontsize=12)

# Add grid, customize legend, and adjust ticks
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(title="Sectors", loc='upper left', fontsize=10, frameon=False)
plt.xticks(rotation=45)

# Automatically adjust layout to ensure no overlapping
plt.tight_layout()

# Display the plot
plt.show()