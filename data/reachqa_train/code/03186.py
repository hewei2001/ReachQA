import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2010, 2021)

# Define the number of founders in each age group per year
age_18_24 = np.array([150, 180, 200, 220, 250, 270, 290, 310, 320, 330, 350])
age_25_34 = np.array([300, 320, 350, 380, 400, 420, 450, 480, 510, 550, 600])
age_35_plus = np.array([100, 120, 130, 150, 160, 170, 180, 190, 200, 210, 220])

# Calculate additional data for overlay plot
total_founders = age_18_24 + age_25_34 + age_35_plus
average_age = (18*age_18_24 + 25*age_25_34 + 35*age_35_plus) / total_founders

# Create the plot
fig, ax1 = plt.subplots(figsize=(12, 7))

# Stacked area chart
ax1.stackplot(years, age_18_24, age_25_34, age_35_plus, 
              labels=['Age 18-24', 'Age 25-34', 'Age 35+'], 
              colors=['skyblue', 'lightgreen', 'salmon'], alpha=0.8)

ax1.set_title('Generations of Innovators:\nA Decade of Tech Startups\' Founders by Age Group', 
              fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Number of Founders', fontsize=14)
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)
ax1.grid(True, linestyle='--', alpha=0.5)

# Line plot overlay for total founders
ax1.plot(years, total_founders, label='Total Founders', color='navy', linewidth=2, linestyle='--')

# Secondary y-axis for average age
ax2 = ax1.twinx()
ax2.plot(years, average_age, label='Average Age', color='purple', linewidth=2, linestyle='-')
ax2.set_ylabel('Average Age of Founders', fontsize=14, color='purple')
ax2.tick_params(axis='y', labelcolor='purple')

# Combine legends from both axes
lns, lbls = ax1.get_legend_handles_labels()
lns2, lbls2 = ax2.get_legend_handles_labels()
ax1.legend(lns + lns2, lbls + lbls2, loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()