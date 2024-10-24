import matplotlib.pyplot as plt
import numpy as np

# Wonder names
wonders = [
    'Great Pyramid of Giza', 
    'Hanging Gardens of Babylon', 
    'Statue of Zeus at Olympia', 
    'Temple of Artemis at Ephesus', 
    'Mausoleum at Halicarnassus'
]

# Hypothetical construction costs in millions of drachmas
costs = [90, 70, 60, 50, 40]

# Hypothetical construction duration in years
durations = [20, 15, 12, 10, 8]

# Set up subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7), sharey=False)

# Bar chart for construction costs
ax1.bar(wonders, costs, color=['#ffcccb', '#add8e6', '#90ee90', '#ffd700', '#ffb6c1'], width=0.6)
ax1.set_title('Hypothetical Construction Costs\nof Ancient Wonders (Million Drachmas)', fontsize=12, weight='bold')
ax1.set_xlabel('Wonder Name', fontsize=11, weight='bold')
ax1.set_ylabel('Cost (Million Drachmas)', fontsize=11, weight='bold')
ax1.set_xticklabels(wonders, rotation=30, ha='right')
ax1.grid(axis='y', linestyle='--', alpha=0.6)

# Annotate cost bars
for i, cost in enumerate(costs):
    ax1.text(i, cost + 1, f'{cost}', ha='center', va='bottom', fontsize=10, fontweight='bold')

# Line chart for construction durations
ax2.plot(wonders, durations, marker='o', color='tab:blue', linewidth=2, markersize=8)
ax2.set_title('Hypothetical Construction Durations\nof Ancient Wonders (Years)', fontsize=12, weight='bold')
ax2.set_xlabel('Wonder Name', fontsize=11, weight='bold')
ax2.set_ylabel('Duration (Years)', fontsize=11, weight='bold')
ax2.set_xticklabels(wonders, rotation=30, ha='right')
ax2.grid(axis='y', linestyle='--', alpha=0.6)

# Annotate duration points
for i, duration in enumerate(durations):
    ax2.text(i, duration + 0.5, f'{duration}', ha='center', va='bottom', fontsize=10, fontweight='bold')

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()