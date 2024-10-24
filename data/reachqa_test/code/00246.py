import matplotlib.pyplot as plt
import numpy as np

# Expanded data: 7 days of data for various cuisines
days = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7']
asian_dishes = [150, 180, 200, 220, 240, 250, 260]
european_dishes = [120, 140, 160, 180, 190, 200, 210]
american_dishes = [100, 130, 170, 150, 160, 180, 190]
african_dishes = [50, 60, 70, 80, 90, 95, 100]
middle_eastern_dishes = [30, 50, 60, 70, 85, 90, 95]

# Create the figure and axis for the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Positions for each bar along the x-axis
x = np.arange(len(days))

# Plot stacked bars for each cuisine category
ax.bar(x, asian_dishes, label='Asian', color='#FF9999')
ax.bar(x, european_dishes, bottom=asian_dishes, label='European', color='#66B3FF')
ax.bar(x, american_dishes, bottom=np.array(asian_dishes) + np.array(european_dishes), label='American', color='#99FF99')
ax.bar(x, african_dishes, bottom=np.array(asian_dishes) + np.array(european_dishes) + np.array(american_dishes), label='African', color='#FFD700')
ax.bar(x, middle_eastern_dishes, bottom=np.array(asian_dishes) + np.array(european_dishes) + np.array(american_dishes) + np.array(african_dishes), label='Middle-Eastern', color='#FF9966')

# Labels, title, and legend
ax.set_xticks(x)
ax.set_xticklabels(days)
ax.set_ylabel('Number of Dishes Sampled')
ax.set_title('Global Cuisine Festival:\nCulinary Preferences Across Seven Days', fontsize=14, weight='bold', pad=15)
ax.legend(title='Cuisine Type', loc='upper left', bbox_to_anchor=(1, 1))

# Grid for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.6)

# Add text annotations to each segment
for i in range(len(days)):
    ax.text(i, asian_dishes[i] / 2, f'{asian_dishes[i]}', ha='center', va='center', color='white', fontweight='bold', fontsize=8)
    ax.text(i, asian_dishes[i] + european_dishes[i] / 2, f'{european_dishes[i]}', ha='center', va='center', color='white', fontweight='bold', fontsize=8)
    ax.text(i, asian_dishes[i] + european_dishes[i] + american_dishes[i] / 2, f'{american_dishes[i]}', ha='center', va='center', color='white', fontweight='bold', fontsize=8)
    ax.text(i, asian_dishes[i] + european_dishes[i] + american_dishes[i] + african_dishes[i] / 2, f'{african_dishes[i]}', ha='center', va='center', color='white', fontweight='bold', fontsize=8)
    ax.text(i, asian_dishes[i] + european_dishes[i] + american_dishes[i] + african_dishes[i] + middle_eastern_dishes[i] / 2, f'{middle_eastern_dishes[i]}', ha='center', va='center', color='white', fontweight='bold', fontsize=8)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the final plot
plt.show()