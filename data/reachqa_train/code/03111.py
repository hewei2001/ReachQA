import matplotlib.pyplot as plt
import numpy as np

# Define wind directions
directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']

# Frequencies of winds from each direction in the Mystic Isles
spring_winds = np.array([8, 12, 15, 10, 6, 4, 3, 5])
summer_winds = np.array([5, 6, 8, 15, 18, 10, 4, 2])
autumn_winds = np.array([3, 5, 10, 8, 9, 14, 17, 10])
winter_winds = np.array([10, 7, 4, 3, 2, 5, 12, 18])

# Combine all seasonal data
wind_data = [spring_winds, summer_winds, autumn_winds, winter_winds]

# Define the angles for the rose chart
angles = np.linspace(0, 2 * np.pi, len(directions), endpoint=False).tolist()
angles += angles[:1]  # Repeat the first angle to close the plot

# Append the first data point to each season's data for closure
for i in range(len(wind_data)):
    wind_data[i] = np.append(wind_data[i], wind_data[i][0])

# Initialize subplot for polar plot
fig, ax = plt.subplots(figsize=(12, 12), subplot_kw=dict(polar=True))

# Define the colors for each season
colors = ['#FFDDC1', '#FFABAB', '#FFC3A0', '#FF677D']
labels = ['Spring', 'Summer', 'Autumn', 'Winter']

# Plot the wind data for each season
for data, color, label in zip(wind_data, colors, labels):
    ax.plot(angles, data, marker='o', linestyle='-', color=color, linewidth=2, label=label)
    ax.fill(angles, data, color=color, alpha=0.25)

# Annotate the maximum value for each season
for data, label in zip(wind_data, labels):
    max_idx = np.argmax(data[:-1])
    ax.annotate(f'{label}\nMax: {data[max_idx]}', xy=(angles[max_idx], data[max_idx]), 
                xytext=(angles[max_idx] + 0.1, data[max_idx] + 2), textcoords='data', 
                arrowprops=dict(arrowstyle="->", color='gray'), ha='center', fontsize=10, color='black')

# Customize plot appearance
ax.set_xticks(angles[:-1])
ax.set_xticklabels(directions, fontsize=12)
ax.set_yticklabels([])  # Hide the radial tick labels
ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)

# Set title with multi-line formatting
ax.set_title("Wind Patterns in the Mystic Isles\nSeasonal Frequencies by Direction", 
             fontsize=16, fontweight='bold', pad=30)

# Add a legend
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1), fontsize=10, title='Seasons', title_fontsize='13')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()