import matplotlib.pyplot as plt
import numpy as np

# Define the gaming platforms and their respective popularity percentages
platforms = ['PC', 'PlayStation', 'Xbox', 'Nintendo Switch', 'Mobile']
popularity = [30, 25, 20, 15, 10]

# Additional data for bar chart: growth rate from 2022 to 2023
growth_rate = [5, 3, 4, 6, 7]  # Hypothetical growth rates in percentage

# Define colors for each platform
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Create a figure with two subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# Plot the pie chart
wedges, texts, autotexts = ax1.pie(
    popularity,
    labels=platforms,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    wedgeprops=dict(edgecolor='w'),
    explode=[0.1, 0.1, 0, 0, 0],
    shadow=True
)

ax1.set_title(
    "Gaming Platform Popularity in 2023",
    fontsize=14, weight='bold', pad=20
)

plt.setp(autotexts, size=10, weight='bold', color='black')
plt.setp(texts, size=12, weight='bold')

ax1.axis('equal')

# Add a legend for the pie chart
ax1.legend(
    wedges, platforms,
    title="Platforms",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1),
    fontsize=10
)

# Plot the bar chart
bar_positions = np.arange(len(platforms))
ax2.bar(
    bar_positions, growth_rate, color=colors, edgecolor='black'
)

ax2.set_xticks(bar_positions)
ax2.set_xticklabels(platforms)
ax2.set_ylabel("Growth Rate (%)")
ax2.set_title(
    "Growth Rate of Gaming Platforms (2022-2023)",
    fontsize=14, weight='bold', pad=20
)

for i, v in enumerate(growth_rate):
    ax2.text(
        i, v + 0.5, f"{v}%", ha='center', va='bottom', fontweight='bold'
    )

# Adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()