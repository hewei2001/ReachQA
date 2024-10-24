import matplotlib.pyplot as plt
import numpy as np

# Define the months and cumulative distances for each landscape
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct']
desert = [0, 50, 120, 200, 300, 370, 460, 510, 550, 600]
rainforest = [0, 80, 180, 280, 400, 480, 560, 640, 700, 760]
mountains = [0, 60, 150, 220, 320, 420, 490, 550, 600, 650]
plains = [0, 90, 200, 310, 430, 530, 600, 670, 720, 780]
coastal = [0, 70, 160, 240, 320, 400, 460, 500, 530, 570]

# Calculate total distances
landscapes = ['Desert', 'Rainforest', 'Mountains', 'Plains', 'Coastal']
total_distances = [
    sum(desert), 
    sum(rainforest), 
    sum(mountains), 
    sum(plains), 
    sum(coastal)
]

# Set up the subplots
fig, ax = plt.subplots(1, 2, figsize=(16, 8))

# Original line plot
ax[0].plot(months, desert, label='Desert Journey', marker='o', color='#FFA07A', linewidth=2)
ax[0].plot(months, rainforest, label='Rainforest Adventure', marker='v', color='#20B2AA', linewidth=2)
ax[0].plot(months, mountains, label='Mountain Trek', marker='s', color='#4682B4', linewidth=2)
ax[0].plot(months, plains, label='Plain Exploration', marker='D', color='#9ACD32', linewidth=2)
ax[0].plot(months, coastal, label='Coastal Voyage', marker='^', color='#DA70D6', linewidth=2)

# Enhance the line plot
ax[0].set_title('The Epic Expedition of Amelia Wanderlust:\nA Year of Diverse Landscapes', fontsize=14, weight='bold')
ax[0].set_xlabel('Month', fontsize=12)
ax[0].set_ylabel('Cumulative Distance Traveled (km)', fontsize=12)
ax[0].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax[0].legend(title='Regions Explored', fontsize=10, title_fontsize='13', loc='upper left')

# Add annotations for key milestones
milestones = {
    'Feb': {'Desert Journey': 50, 'Rainforest Adventure': 80, 'Mountain Trek': 60, 'Plain Exploration': 90, 'Coastal Voyage': 70},
    'May': {'Desert Journey': 300, 'Rainforest Adventure': 400, 'Mountain Trek': 320, 'Plain Exploration': 430, 'Coastal Voyage': 320},
    'Sep': {'Desert Journey': 550, 'Rainforest Adventure': 700, 'Mountain Trek': 600, 'Plain Exploration': 720, 'Coastal Voyage': 530}
}

for month, data in milestones.items():
    for journey, distance in data.items():
        ax[0].annotate(f'{distance} km', xy=(month, distance), xytext=(-30, 10),
                       textcoords='offset points', arrowprops=dict(arrowstyle='->', color='black'),
                       fontsize=9, color='black')

# Bar chart to show total distances
ax[1].bar(landscapes, total_distances, color=['#FFA07A', '#20B2AA', '#4682B4', '#9ACD32', '#DA70D6'], alpha=0.7)
ax[1].set_title('Total Distances Traveled Across Landscapes', fontsize=14, weight='bold')
ax[1].set_ylabel('Total Distance (km)', fontsize=12)

# Annotate total distances on top of bars
for i, total in enumerate(total_distances):
    ax[1].text(i, total + 20, f'{total} km', ha='center', va='bottom', fontsize=10)

# Adjust layout for better spacing
plt.tight_layout()
plt.show()