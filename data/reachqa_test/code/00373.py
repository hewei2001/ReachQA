import matplotlib.pyplot as plt
import squarify

# Data for the platforms
platforms = ['Facebook', 'Instagram', 'Twitter', 'YouTube', 'Reddit', 'Quora']
active_users = [2500000000, 1000000000, 330000000, 2000000000, 430000000, 300000000]
avg_time_spent = [30, 40, 20, 60, 45, 35]

# Create hierarchy with list comprehension
hierarchy = [(platform, active_users[i], avg_time_spent[i]) for i, platform in enumerate(platforms)]

# Define a color palette
color_palette = ['#3498db', '#f1c40f', '#2ecc71', '#e74c3c', '#9b59b6', '#1abc9c']

# Plotting
plt.figure(figsize=(12, 10))
squarify.plot(
    sizes=[h[1] for h in hierarchy],
    label=[f"{h[0]}\nActive Users: {h[1]:,.0f}\nAvg Time Spent: {h[2]:.0f} min" for h in hierarchy],
    color=color_palette[:len(hierarchy)],  # Simplified color assignment
    alpha=0.8
)

# Set title and axis properties
plt.title("Social Media Landscape: A Tree Map of User Engagement")
plt.axis('off')

# Adjust layout and save
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()