import matplotlib.pyplot as plt

# Fictional robots' data
robots = ["MediBot", "IndustriBot", "HomeBot", "EcoBot", "RescueBot"]

# Efficiency and safety ratings (0 to 100 scale)
efficiency = [85, 90, 75, 70, 65]
safety = [95, 80, 70, 85, 90]

# Deployment scale (in units of operation)
deployment_scale = [300, 500, 400, 200, 250]

# Create the scatter plot
plt.figure(figsize=(12, 8))
scatter = plt.scatter(efficiency, safety, s=deployment_scale, c=deployment_scale, cmap='coolwarm', alpha=0.7, edgecolors='w', linewidth=1.5)

# Annotate each point with robot names
for i, robot in enumerate(robots):
    plt.annotate(robot, (efficiency[i] + 0.5, safety[i] + 0.5), fontsize=11, fontweight='bold', bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray'))

# Titles and labels
plt.title("Performance Analysis of Specialized Robots\nin Fictional Domains", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Efficiency", fontsize=13)
plt.ylabel("Safety", fontsize=13)
plt.xlim(60, 100)
plt.ylim(60, 100)

# Add a color bar to show the deployment scale context
cbar = plt.colorbar(scatter)
cbar.set_label('Deployment Scale\n(Units in Operation)', fontsize=12)

# Add grid lines to improve readability
plt.grid(True, linestyle='--', alpha=0.6)

# Adjust layout to prevent overlap and ensure readability
plt.tight_layout()

# Show the plot
plt.show()