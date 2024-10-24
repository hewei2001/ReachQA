import numpy as np
import matplotlib.pyplot as plt

# Define the personality traits
traits = ['Extraversion', 'Agreeableness', 'Conscientiousness', 'Neuroticism', 'Openness to Experience']

# Create data for each group
tech_entrepreneurs = np.array([80, 60, 70, 40, 90])
finance_entrepreneurs = np.array([70, 80, 90, 50, 60])
creative_entrepreneurs = np.array([90, 50, 60, 60, 80])

# Create a 2D array to hold all the data
data = np.array([tech_entrepreneurs, finance_entrepreneurs, creative_entrepreneurs])

# Define the groups
groups = ['Tech', 'Finance', 'Creative']

# Define industry distribution data
industry_distribution = np.array([200, 150, 300])  # number of entrepreneurs in each industry

# Set up the figure
fig = plt.figure(figsize=(12, 6))

# Create a polar subplot for the radar chart
ax1 = fig.add_subplot(121, polar=True)

# Distribute the variables evenly around the circle
angles = np.linspace(start=0, stop=2*np.pi, num=len(traits), endpoint=False)

# Plot data points for each variable on their respective spokes
for i, (group, values) in enumerate(zip(groups, data)):
    ax1.plot(np.concatenate((angles, [angles[0]])), np.concatenate((values, [values[0]])), 
             label=group, linewidth=2, color=plt.cm.tab20(i))

# Set the angle for each spoke
ax1.set_thetagrids(angles * 180/np.pi, traits)

# Adjust the range of each axis to make sure all data points are visible
ax1.set_ylim(0, 100)

# Set the title
ax1.set_title("Character Traits of Successful\nEntrepreneurs Across Different Industries", va='bottom', fontsize=14)

# Add legend
ax1.legend(loc='lower right', bbox_to_anchor=(1.2, 0))

# Create a bar subplot for the industry distribution
ax2 = fig.add_subplot(122)
bar_width = 0.6
bar_positions = np.arange(len(industry_distribution))
ax2.bar(bar_positions, industry_distribution, bar_width, color=plt.cm.tab20(0))
ax2.set_xticks(bar_positions)
ax2.set_xticklabels(groups)
ax2.set_ylabel('Number of Entrepreneurs')
ax2.set_title('Distribution of Entrepreneurs Across Industries')

# Adjust the layout
plt.tight_layout(rect=[0, 0, 1, 1])

# Show the plot
plt.show()