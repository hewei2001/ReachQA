import matplotlib.pyplot as plt

# Community service ratings over five years
public_transportation = [4, 6, 7, 5, 7, 8, 5, 6, 7, 5, 6, 8, 9, 4, 6, 7, 8, 5, 6, 5, 7, 8, 6, 5, 7]
health_services = [8, 8, 9, 7, 8, 9, 9, 7, 9, 8, 9, 7, 8, 9, 9, 7, 9, 8, 8, 7, 8, 9, 8, 8, 7]
recreational_facilities = [6, 5, 5, 6, 5, 7, 5, 4, 6, 5, 6, 5, 6, 5, 4, 5, 6, 7, 6, 5, 7, 6, 5, 5, 6]
waste_management = [5, 6, 5, 4, 5, 6, 5, 4, 6, 5, 4, 5, 4, 6, 5, 6, 5, 4, 6, 5, 5, 6, 5, 4, 6]
education = [7, 6, 8, 7, 7, 8, 7, 9, 8, 6, 8, 9, 7, 8, 9, 8, 7, 9, 8, 6, 8, 9, 7, 8, 8]

# Combine data into a list
data = [public_transportation, health_services, recreational_facilities, waste_management, education]

# Service labels
services = ['Public Transportation', 'Health Services', 'Recreational Facilities', 'Waste Management', 'Education']

# Create a horizontal boxplot
fig, ax = plt.subplots(figsize=(12, 6))
bp = ax.boxplot(data, vert=False, patch_artist=True, showmeans=True, meanline=True, notch=True, widths=0.6)

# Customize boxplot appearance
colors = ['#FF6347', '#FFD700', '#98FB98', '#87CEEB', '#9370DB']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Add plot title and labels
ax.set_title('Community Service Satisfaction in Greenfield:\n5-Year Rating Distribution', fontsize=14, fontweight='bold', pad=20)
ax.set_yticklabels(services, fontsize=10)
ax.set_xlabel('Satisfaction Rating (1-10)', fontsize=12)
ax.set_xlim(0, 10)

# Add gridlines for clarity
ax.xaxis.grid(True, linestyle='--', alpha=0.7)

# Ensure the layout is tight to prevent clipping of labels and titles
plt.tight_layout()

# Display the plot
plt.show()