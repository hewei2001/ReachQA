import matplotlib.pyplot as plt
import numpy as np

# Define cities and their corresponding monthly solar power generation data in kWh
cities = ['San Diego', 'Cape Town', 'Berlin', 'Mumbai', 'Tokyo']
solar_generation = [
    [450, 500, 620, 680, 720, 750, 760, 740, 700, 640, 560, 490],  # San Diego
    [380, 400, 460, 580, 680, 720, 700, 680, 600, 540, 480, 420],  # Cape Town
    [150, 180, 240, 360, 500, 600, 580, 540, 400, 280, 200, 160],  # Berlin
    [320, 360, 450, 500, 540, 580, 600, 590, 540, 490, 430, 350],  # Mumbai
    [180, 240, 360, 460, 580, 640, 660, 650, 580, 460, 300, 200]   # Tokyo
]

# Define months for x-axis labels
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Setup plot
fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.15  # Width of each bar
index = np.arange(len(months))  # Index positions for months

# Assign distinct colors to each city using a colormap
colors = plt.cm.viridis(np.linspace(0, 1, len(cities)))

# Plot each city's data with offset bars
for i, (city, generation, color) in enumerate(zip(cities, solar_generation, colors)):
    ax.barh(index + i * bar_width, generation, bar_width, label=city, color=color, edgecolor='grey')

# Configure the y-axis
ax.set_yticks(index + bar_width * (len(cities) / 2))
ax.set_yticklabels(months)
ax.invert_yaxis()

# Adding labels, gridlines, and title
ax.set_xlabel('Average Solar Power Generation (kWh)')
ax.set_title('Monthly Solar Power Generation in Various Cities', pad=20)
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Add value labels on the bars
for i in range(len(cities)):
    for j in range(len(months)):
        ax.text(solar_generation[i][j] + 5, j + i * bar_width,
                f'{solar_generation[i][j]}', va='center', ha='left', fontsize=8, color='black')

# Display legend outside of the plot
ax.legend(title="Cities", loc='upper left', bbox_to_anchor=(1, 1))

# Apply tight layout for better spacing and visibility
plt.tight_layout()

# Display the plot
plt.show()