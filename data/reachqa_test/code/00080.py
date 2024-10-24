import matplotlib.pyplot as plt
import numpy as np

# Define the generations and their internet usage categories
generations = ['Baby Boomers', 'Generation X', 'Millennials', 'Generation Z']
categories = [
    'Social Media - Active', 'Social Media - Passive', 'Streaming Services', 
    'Online Shopping', 'News', 'Gaming', 'Educational Content', 'Productivity Tools'
]
usage_data = {
    'Baby Boomers': [5, 5, 20, 15, 25, 10, 10, 10],
    'Generation X': [10, 10, 25, 15, 20, 5, 10, 5],
    'Millennials': [15, 20, 30, 10, 10, 5, 5, 5],
    'Generation Z': [20, 25, 25, 5, 5, 5, 10, 5]
}

# Create a color map to represent different categories
colors = plt.get_cmap('tab20c')(np.linspace(0, 1, len(categories)))

fig, axs = plt.subplots(3, 2, figsize=(16, 18))
axs = axs.flatten()

# Plot a donut chart for each generation
for i, generation in enumerate(generations):
    data = usage_data[generation]
    wedges, texts, autotexts = axs[i].pie(
        data,
        labels=categories,
        autopct='%1.1f%%',
        startangle=140,
        colors=colors,
        pctdistance=0.85,
        wedgeprops=dict(width=0.3),
        shadow=True,
        explode=[0.05] * len(data)
    )
    
    # Add a circle at the center to create the donut effect
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    axs[i].add_artist(centre_circle)
    
    # Title for each subplot
    axs[i].set_title(f"{generation} Internet Usage", fontsize=13, fontweight='bold')

    # Customize autotexts
    plt.setp(autotexts, size=8, weight='bold', color='darkred')

# Additional composite plot showing overall trends
total_usage = np.sum(np.array(list(usage_data.values())), axis=0)
axs[4].barh(categories, total_usage, color=colors)
axs[4].set_title("Overall Internet Usage Trends", fontsize=13, fontweight='bold')
axs[4].set_xlabel("Total Usage Hours")
axs[4].invert_yaxis()  # To align bars with legend order

# Main title for the entire figure
fig.suptitle(
    "Internet Usage Patterns Across Generations\nExploring Complex Digital Time Allocation",
    fontsize=18,
    fontweight='bold',
    color='navy',
    ha='center'
)

# Adjust layout to prevent overlap
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Add a legend outside the plots
fig.legend(wedges, categories, title="Activities", loc="center right", bbox_to_anchor=(1.25, 0.5))

# Remove the unused subplot
fig.delaxes(axs[5])

# Display the plot
plt.show()