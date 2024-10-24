import matplotlib.pyplot as plt
import numpy as np

# Define the categories
categories = ['Work', 'Sleep', 'Fitness', 'Leisure', 'Social', 'Family']
N = len(categories)

# Data for each personality type
professional = [50, 42, 8, 15, 13, 40]
fitness_enthusiast = [30, 49, 15, 10, 20, 44]
family_centric = [20, 56, 5, 12, 30, 45]

# Compute average time allocation per category
average_allocation = np.mean([professional, fitness_enthusiast, family_centric], axis=0)

# Extend data to close the loop for radar chart
professional += professional[:1]
fitness_enthusiast += fitness_enthusiast[:1]
family_centric += family_centric[:1]

# Calculate the angle for each axis
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]

# Create a figure with two subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8), subplot_kw={'polar': True})

# Radar chart on the first subplot
ax1.fill(angles, professional, color='b', alpha=0.25, label='The Professional')
ax1.plot(angles, professional, color='b', linewidth=2)
ax1.fill(angles, fitness_enthusiast, color='g', alpha=0.25, label='The Fitness Enthusiast')
ax1.plot(angles, fitness_enthusiast, color='g', linewidth=2)
ax1.fill(angles, family_centric, color='r', alpha=0.25, label='The Family-Centric')
ax1.plot(angles, family_centric, color='r', linewidth=2)

# Customize radar chart aesthetics
ax1.set_yticklabels([])
ax1.set_xticks(angles[:-1])
ax1.set_xticklabels(categories, fontsize=10, fontweight='bold')
ax1.set_title(
    "Lifestyle and Balance:\nTime Allocation in a Week for Different Personalities",
    fontsize=14, fontweight='bold', pad=20
)
ax1.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))

# Bar chart on the second subplot
ax2 = plt.subplot(122)
bar_width = 0.3
x = np.arange(N)

ax2.bar(x - bar_width, professional[:-1], width=bar_width, color='b', alpha=0.6, label='Professional')
ax2.bar(x, fitness_enthusiast[:-1], width=bar_width, color='g', alpha=0.6, label='Fitness Enthusiast')
ax2.bar(x + bar_width, family_centric[:-1], width=bar_width, color='r', alpha=0.6, label='Family-Centric')
ax2.plot(x, average_allocation, color='black', marker='o', linestyle='--', linewidth=2, label='Average')

# Customize bar chart aesthetics
ax2.set_xticks(x)
ax2.set_xticklabels(categories, fontsize=10, fontweight='bold')
ax2.set_ylabel('Hours Spent', fontsize=12)
ax2.set_title("Average Time Allocation Across Personalities", fontsize=14, fontweight='bold', pad=20)
ax2.legend(loc='upper right', fontsize=10)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()