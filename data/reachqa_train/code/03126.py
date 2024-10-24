import matplotlib.pyplot as plt
import numpy as np

# Data representing the number of architectural wonders from ancient civilizations
civilizations = ['Egyptian', 'Mayan', 'Greek', 'Roman', 'Mesopotamian']
wonders_count = [10, 8, 7, 9, 6]

# Create the bar chart
fig, ax = plt.subplots(figsize=(10, 6))
colors = ['#FFDDC1', '#FFD700', '#FF4500', '#8A2BE2', '#5F9EA0']
bars = ax.bar(civilizations, wonders_count, color=colors, width=0.6)

# Add title and labels
ax.set_title("Architectural Wonders of Ancient Civilizations", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Civilization", fontsize=12)
ax.set_ylabel("Number of Wonders", fontsize=12)
ax.set_ylim(0, max(wonders_count) + 2)

# Annotating each bar with the number of wonders
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # Offset text by 3 points above the bar
                textcoords='offset points',
                ha='center', va='bottom', fontsize=10, color='black')

# Rotate x-axis labels if necessary to prevent overlap
plt.xticks(rotation=45, ha='right')

# Add grid lines for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust the layout to prevent clipping
plt.tight_layout()

# Display the plot
plt.show()