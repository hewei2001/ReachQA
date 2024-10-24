import matplotlib.pyplot as plt
import numpy as np

# Define the attributes for workplace satisfaction
attributes = ['Compensation', 'Work-Life Balance', 'Career Development', 'Work Environment', 'Management Relations']

# Define the data for each company
tech_innovators = [9, 6, 8, 7, 5]
green_solutions = [7, 9, 6, 8, 7]
blue_horizon = [6, 7, 5, 8, 8]

# Combine the data in a list
companies = [tech_innovators, green_solutions, blue_horizon]
company_names = ['Tech Innovators Inc.', 'Green Solutions Ltd.', 'Blue Horizon Corp.']

# Number of variables
num_vars = len(attributes)

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Make the plot
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Loop over data to plot each company
for idx, company in enumerate(companies):
    # Complete the data circle
    data = company + company[:1]
    
    # Draw the radar chart
    ax.fill(angles, data, alpha=0.3, label=company_names[idx])
    ax.plot(angles, data, linewidth=2, linestyle='solid')

# Set the attributes as labels on the axes
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(attributes, fontsize=10, weight='bold')

# Adjust the radial limits for clear data representation
ax.set_ylim(0, 10)

# Set the title and add a legend
ax.set_title("The Five Pillars of Workplace Satisfaction:\nA Comparative Analysis", size=16, color='navy', pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=9)

# Automatically adjust layout to fit elements
plt.tight_layout()

# Display the radar chart
plt.show()