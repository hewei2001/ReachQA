import numpy as np
import matplotlib.pyplot as plt

# Define decades
decades = np.arange(2100, 2210, 10)

# Artificial data for technological innovations (arbitrary units)
robotics = [5, 12, 30, 60, 100, 150, 220, 300, 380, 480, 600]
space_travel = [60, 90, 120, 150, 160, 170, 180, 190, 195, 200, 210]
quantum_computing = [4, 10, 18, 30, 50, 80, 130, 190, 270, 350, 450]
cybernetics = [25, 40, 70, 90, 115, 130, 160, 210, 260, 320, 380]

# Stack data for plotting
data = np.array([robotics, space_travel, quantum_computing, cybernetics])

# Colors for each technological innovation
colors = ['#FF6347', '#4682B4', '#8A2BE2', '#3CB371']

# Calculate total technological advancements
total_innovations = np.sum(data, axis=0)

# Plot setup
fig, ax = plt.subplots(figsize=(14, 8))

# Stackplot for technological innovations
ax.stackplot(decades, data, labels=['Robotics', 'Space Travel', 'Quantum Computing', 'Cybernetics'], colors=colors, alpha=0.8)

# Add line plot for total innovations
ax.plot(decades, total_innovations, label='Total Technological Advancements', color='black', linestyle='--', marker='o', linewidth=2)

# Title and labels
ax.set_title('Technological Innovations Over a Century\nin the Fictional Galaxy', fontsize=16, fontweight='bold', loc='center')
ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Innovation Units', fontsize=12)
ax.set_xticks(decades)

# Customize legends and grid
ax.legend(loc='upper left', title='Technological Sectors', fontsize=10, title_fontsize=12)
ax.grid(True, linestyle='--', alpha=0.5)

# Annotate significant points
max_robotics_decade = np.argmax(robotics) * 10 + 2100
max_robotics_value = max(robotics)
ax.annotate(f'Max Robotics\n{max_robotics_value} units', 
            xy=(max_robotics_decade, max_robotics_value), 
            xytext=(max_robotics_decade + 5, max_robotics_value + 100),
            arrowprops=dict(facecolor='red', arrowstyle='->'),
            fontsize=10, color='red', fontweight='bold')

max_total_decade = np.argmax(total_innovations) * 10 + 2100
max_total_value = max(total_innovations)
ax.annotate(f'Peak Total\n{max_total_value} units',
            xy=(max_total_decade, max_total_value),
            xytext=(max_total_decade, max_total_value + 150),
            arrowprops=dict(facecolor='blue', arrowstyle='->'),
            fontsize=10, color='blue', fontweight='bold')

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()