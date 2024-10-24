import matplotlib.pyplot as plt
import numpy as np

# Data Setup
years = np.arange(2013, 2024)
ev_count = [500, 800, 1200, 1800, 2500, 3500, 5000, 7500, 11000, 16000, 23000]

# Significant events to annotate
events = {
    2015: "First Govt\nIncentives",
    2018: "Battery\nTech Breakthrough",
    2021: "EV Mandate\nPolicy"
}

# Create the line plot
plt.figure(figsize=(14, 7))
plt.plot(years, ev_count, marker='o', color='teal', linestyle='-', linewidth=2, markersize=8, label='EV Count')

# Annotate significant events
for year, event in events.items():
    plt.annotate(event, 
                 xy=(year, ev_count[year-2013]), 
                 xytext=(year, ev_count[year-2013] + 2500),
                 arrowprops=dict(facecolor='black', arrowstyle='->'),
                 fontsize=10, color='darkred', ha='center')

# Add text annotations for each data point
for i, count in enumerate(ev_count):
    plt.text(years[i], count + 500, f'{count:,}', fontsize=9, ha='center', color='navy')

# Add labels and title
plt.title("The Rise of Electric Vehicle Adoption in Electrica\nA Decade of Growth (2013-2023)", fontsize=16, fontweight='bold')
plt.xlabel("Year", fontsize=12)
plt.ylabel("Number of Electric Vehicles", fontsize=12)
plt.xticks(years, rotation=45)
plt.grid(True, linestyle='--', alpha=0.5)

# Add legend
plt.legend(loc='upper left')

# Adjust layout to prevent clipping
plt.tight_layout()

# Show the plot
plt.show()