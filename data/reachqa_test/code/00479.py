import matplotlib.pyplot as plt

# Data for waste management methods and their contributions
waste_methods = ['Recycled', 'Composted', 'Incinerated', 'Landfills']
percentages = [35, 20, 15, 30]  # must sum to 100%
colors = ['#4CAF50', '#FF9800', '#2196F3', '#F44336']
explode = (0.1, 0, 0, 0)  # "explode" the first slice (Recycled)

# Data for waste volumes processed (in tons)
waste_volumes = [2000, 1000, 800, 1500]  # Hypothetical values

# Creating the figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8), gridspec_kw={'width_ratios': [1, 1.2]})

# Creating the donut pie chart
wedges, texts, autotexts = ax1.pie(percentages, labels=waste_methods, colors=colors,
                                    autopct='%1.1f%%', startangle=90, explode=explode,
                                    wedgeprops=dict(width=0.3, edgecolor='w'), shadow=True)

# Customizing text properties for the donut chart
for text in texts:
    text.set_fontsize(12)
for autotext in autotexts:
    autotext.set_fontsize(12)

ax1.set_title("Waste Management Efficiency\n(Percentage Distribution)", fontsize=16, pad=20)

# Legend for the donut chart
ax1.legend(wedges, [f"{method} ({percent}%)" for method, percent in zip(waste_methods, percentages)],
           title="Waste Management Methods", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1),
           fontsize=10)

# Creating the bar chart
ax2.bar(waste_methods, waste_volumes, color=colors)
ax2.set_title("Estimated Volume of Waste Managed\n(tons)", fontsize=16, pad=20)
ax2.set_ylabel("Volume (tons)", fontsize=12)
ax2.set_xlabel("Waste Management Methods", fontsize=12)
ax2.grid(axis='y', linestyle='--', alpha=0.7)

# Adding data labels to the bar chart
for i, volume in enumerate(waste_volumes):
    ax2.text(i, volume + 50, f"{volume} tons", ha='center', fontsize=11)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()