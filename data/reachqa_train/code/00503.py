import matplotlib.pyplot as plt

# Hypothetical average monthly sunshine hours for each city
sunshine_data = {
    "San Francisco": [160, 155, 180, 210, 240, 280, 300, 310, 270, 230, 180, 160],
    "Cairo": [300, 290, 310, 310, 340, 360, 380, 370, 350, 330, 310, 300],
    "Mumbai": [250, 230, 220, 180, 160, 150, 160, 170, 180, 210, 230, 250],
    "Sydney": [220, 200, 190, 180, 160, 160, 170, 200, 210, 220, 230, 240],
    "Tokyo": [180, 160, 170, 180, 200, 220, 240, 230, 220, 190, 180, 170]
}

# Extract the data for plotting
cities = list(sunshine_data.keys())
sunshine_hours = list(sunshine_data.values())

# Create the box plot
fig, ax = plt.subplots(figsize=(12, 7))
ax.boxplot(sunshine_hours, vert=True, patch_artist=True, notch=True, labels=cities,
           boxprops=dict(facecolor='lightblue', color='blue', alpha=0.7),
           whiskerprops=dict(color='blue'),
           capprops=dict(color='blue'),
           medianprops=dict(color='darkred'),
           flierprops=dict(markerfacecolor='red', marker='o', markersize=5, linestyle='none', alpha=0.5))

# Title and labels
ax.set_title("Global Sunshine Patterns:\nA Yearly Overview Across Five Cities", fontsize=14, weight='bold')
ax.set_ylabel("Average Monthly Sunshine Hours", fontsize=12)
ax.set_xlabel("Cities", fontsize=12)

# Customize grid
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()