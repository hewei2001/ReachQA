import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2010, 2021)

# Define the number of founders in each age group per year
age_18_24 = np.array([150, 180, 200, 220, 250, 270, 290, 310, 320, 330, 350])
age_25_34 = np.array([300, 320, 350, 380, 400, 420, 450, 480, 510, 550, 600])
age_35_plus = np.array([100, 120, 130, 150, 160, 170, 180, 190, 200, 210, 220])

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(12, 7))

ax.stackplot(years, age_18_24, age_25_34, age_35_plus, 
             labels=['Age 18-24', 'Age 25-34', 'Age 35+'], 
             colors=['skyblue', 'lightgreen', 'salmon'], alpha=0.8)

# Add title and labels
ax.set_title('Generations of Innovators:\nA Decade of Tech Startups\' Founders by Age Group', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Number of Founders', fontsize=14)

# Set the x-axis to show every year and rotate labels for better readability
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

# Add a legend outside the plot area
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()