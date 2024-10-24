import matplotlib.pyplot as plt
import numpy as np

# Departments and their average monthly antibiotic prescriptions
departments = [
    "General Medicine", 
    "Pediatrics", 
    "Emergency", 
    "Surgery", 
    "Dermatology", 
    "Ophthalmology"
]
antibiotics_prescriptions = [120, 95, 200, 150, 45, 30]

# Hypothetical target prescriptions for each department
target_prescriptions = [100, 100, 180, 140, 50, 35]

# Create color map
colors = plt.cm.viridis(np.linspace(0, 1, len(departments)))

# Create the figure and axis objects
fig, ax = plt.subplots(figsize=(14, 8))

# Create the horizontal bar chart
bars = ax.barh(departments, antibiotics_prescriptions, color=colors, edgecolor='black', height=0.6, label='Prescriptions')

# Add data labels to each bar
for bar in bars:
    ax.text(bar.get_width() + 5, bar.get_y() + bar.get_height() / 2, 
            f'{bar.get_width()}', va='center', ha='left', fontsize=10, fontweight='bold')

# Overlay plot: line for target prescriptions
ax.plot(target_prescriptions, departments, marker='o', color='orange', linewidth=2, linestyle='--', label='Target')

# Set labels and title
ax.set_xlabel('Average Monthly Prescriptions', fontsize=12, fontweight='bold')
ax.set_title('Guardians of Health:\nAntibiotics Prescription Trends\nand Targets Across Medical Departments', 
             fontsize=16, fontweight='bold', pad=20)

# Customize y-axis ticks
ax.set_yticks(np.arange(len(departments)))
ax.set_yticklabels(departments, fontsize=12, fontweight='bold')

# Add a grid for better readability
ax.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.6)

# Set x-axis limits
ax.set_xlim(0, max(max(antibiotics_prescriptions), max(target_prescriptions)) + 50)

# Reverse the y-axis to have the most prescribing department on top
ax.invert_yaxis()

# Add legend to describe bars and target line
ax.legend(title='Legend', fontsize=10, title_fontsize=11, bbox_to_anchor=(1.05, 1), loc='upper left')

# Adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()