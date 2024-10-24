import matplotlib.pyplot as plt
import numpy as np

# Original data representing the number of architectural wonders from ancient civilizations
civilizations = ['Egyptian', 'Mayan', 'Greek', 'Roman', 'Mesopotamian']
wonders_count = [10, 8, 7, 9, 6]

# New data representing the distribution of types of wonders for each civilization
# Assume each civilization has 3 types of wonders: Pyramids, Temples, and Others
types_distribution = {
    'Egyptian': [5, 3, 2],
    'Mayan': [3, 4, 1],
    'Greek': [2, 3, 2],
    'Roman': [4, 4, 1],
    'Mesopotamian': [2, 2, 2],
}
types = ['Pyramids', 'Temples', 'Others']
colors = ['#FFDDC1', '#FFD700', '#FF4500', '#8A2BE2', '#5F9EA0']

# Set up the subplots
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Bar chart subplot
axs[0].bar(civilizations, wonders_count, color=colors, width=0.6)
axs[0].set_title("Architectural Wonders of\nAncient Civilizations", fontsize=16, fontweight='bold', pad=10)
axs[0].set_xlabel("Civilization", fontsize=12)
axs[0].set_ylabel("Number of Wonders", fontsize=12)
axs[0].set_ylim(0, max(wonders_count) + 2)

# Annotating each bar with the number of wonders
for idx, bar in enumerate(axs[0].patches):
    height = bar.get_height()
    axs[0].annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords='offset points',
                    ha='center', va='bottom', fontsize=10)

axs[0].yaxis.grid(True, linestyle='--', alpha=0.7)
axs[0].set_xticklabels(civilizations, rotation=45, ha='right')

# Pie chart subplot for Egyptian civilization as an example
axs[1].pie(types_distribution['Egyptian'], labels=types, autopct='%1.1f%%', startangle=140, colors=['#FFDDC1', '#FFD700', '#FF4500'])
axs[1].set_title("Types of Egyptian Wonders", fontsize=16, fontweight='bold', pad=10)

# Automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()