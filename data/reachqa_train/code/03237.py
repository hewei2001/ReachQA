import matplotlib.pyplot as plt
import numpy as np

# Define spells and their usage frequency for two consecutive years
spells = [
    "Lumos", "Alohomora", "Expelliarmus", "Accio", 
    "Wingardium Leviosa", "Expecto Patronum", "Riddikulus",
    "Protego", "Stupefy", "Obliviate", "Petrificus Totalus", 
    "Crucio", "Imperio", "Avada Kedavra"
]

usage_2022 = [1200, 950, 800, 600, 850, 400, 450, 700, 670, 500, 520, 90, 65, 30]
usage_2023 = [1300, 1050, 750, 620, 900, 380, 480, 800, 640, 550, 490, 80, 70, 25]

# Color palette for each spell
colors = [
    '#FFD700', '#FF4500', '#ADFF2F', '#00BFFF', '#BA55D3', '#8A2BE2', '#FF6347', 
    '#32CD32', '#FF69B4', '#4682B4', '#D2691E', '#8B0000', '#FF1493', '#000000'
]

# Create a figure with two subplots: one for bar chart and another for cumulative sum
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))

# Bar chart: Compare usage between years
bar_width = 0.35
index = np.arange(len(spells))

bars1 = ax1.bar(index, usage_2022, bar_width, color=colors, edgecolor='black', label='2022')
bars2 = ax1.bar(index + bar_width, usage_2023, bar_width, color=colors, alpha=0.7, edgecolor='black', label='2023')

# Add data labels above each bar
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width() / 2, height + 15,
                 f'{int(height)}', ha='center', va='bottom', fontsize=9, color='black')

# Customize the appearance of the bar chart
ax1.set_ylabel('Usage Frequency', fontsize=12, fontweight='bold')
ax1.set_title('Comparison of Magical Spell Usage\nBetween 2022 and 2023', fontsize=14, fontweight='bold')
ax1.set_xticks(index + bar_width / 2)
ax1.set_xticklabels(spells, fontsize=10, weight='bold', rotation=45, ha='right')
ax1.set_ylim(0, max(usage_2022 + usage_2023) + 150)
ax1.grid(axis='y', linestyle='--', alpha=0.7)
ax1.legend()

# Cumulative sum line chart
cumulative_usage_2022 = np.cumsum(usage_2022)
cumulative_usage_2023 = np.cumsum(usage_2023)

ax2.plot(spells, cumulative_usage_2022, marker='o', linestyle='-', color='#FF4500', label='2022')
ax2.plot(spells, cumulative_usage_2023, marker='s', linestyle='-', color='#32CD32', label='2023')

# Customize the appearance of the line chart
ax2.set_ylabel('Cumulative Usage', fontsize=12, fontweight='bold')
ax2.set_title('Cumulative Sum of Magical Spell Usage', fontsize=14, fontweight='bold')
ax2.set_xticks(index)
ax2.set_xticklabels(spells, fontsize=10, weight='bold', rotation=45, ha='right')
ax2.set_ylim(0, sum(max(usage_2022, usage_2023)) + 500)
ax2.grid(axis='y', linestyle='--', alpha=0.7)
ax2.legend()

# Adjust layout for a visually appealing presentation
plt.tight_layout()

# Display the plot
plt.show()