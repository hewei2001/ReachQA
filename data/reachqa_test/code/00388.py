import matplotlib.pyplot as plt
import numpy as np

# City names
cities = ['Paris', 'Berlin', 'London', 'Rome', 'Madrid', 'Amsterdam', 'Vienna', 'Stockholm', 'Copenhagen', 'Helsinki']

# Household waste management percentages for each city
recycling_rates = [35, 40, 30, 25, 28, 38, 32, 45, 42, 40]
composting_rates = [20, 15, 18, 22, 20, 18, 20, 25, 22, 20]
landfilling_rates = [30, 35, 40, 45, 38, 32, 30, 20, 25, 22]
incineration_rates = [15, 10, 12, 8, 14, 12, 18, 10, 11, 18]

# Total waste generation (in tons) for each city
total_waste = [1200, 1000, 1100, 1050, 1150, 1300, 1250, 900, 950, 1000]

# Stack rates for plotting
rates = np.vstack((recycling_rates, composting_rates, landfilling_rates, incineration_rates)).T

# Create a figure and axis object with a specified size
fig, axs = plt.subplots(1, 2, figsize=(18, 8), gridspec_kw={'width_ratios': [3, 2]})

# Define the colors for each rate
colors = ['#66CC00', '#FFC080', '#B73D3D', '#3939BA']

# Set the bar positions
x = np.arange(len(cities))

# Set the width of the bars
width = 0.8

# Create a stacked bar chart
axs[0].bar(x, rates[:, 0], width, label='Recycling', color=colors[0])
axs[0].bar(x, rates[:, 1], width, bottom=rates[:, 0], label='Composting', color=colors[1])
axs[0].bar(x, rates[:, 2], width, bottom=rates[:, 0] + rates[:, 1], label='Landfilling', color=colors[2])
axs[0].bar(x, rates[:, 3], width, bottom=rates[:, 0] + rates[:, 1] + rates[:, 2], label='Incineration', color=colors[3])

# Set the x-axis tick labels
axs[0].set_xticks(x)
axs[0].set_xticklabels(cities, rotation=45, ha='right')

# Set the y-axis range and tick labels
axs[0].set_ylim(0, 100)
axs[0].set_yticks([25, 50, 75])

# Set the title
title = "European Cities' Household Waste Management\nMethods Distribution (in %)"
axs[0].set_title(title)

# Add legend
axs[0].legend(title='Waste Management Method', bbox_to_anchor=(1.04, 1), loc='upper left')

# Add percentage labels
for i in range(len(cities)):
    for j in range(4):
        value = rates[i, j]
        axs[0].text(x[i], np.sum(rates[i, :j]) + value / 2, f"{value}%", ha='center', va='center', color='white', fontsize=8)

# Create a line plot for total waste generation
axs[1].plot(cities, total_waste, marker='o', linestyle='-', color='black')
axs[1].set_title('European Cities\' Total Waste Generation (in tons)')
axs[1].set_xlabel('City')
axs[1].set_ylabel('Total Waste (tons)')
axs[1].set_xticks(x)
axs[1].set_xticklabels(cities, rotation=45, ha='right')
axs[1].grid(True)

# Layout so plots do not overlap
fig.tight_layout()

# Show the plot
plt.show()