import matplotlib.pyplot as plt
import numpy as np

# Urban Wildlife Sightings Data
categories = ['Birds', 'Mammals', 'Reptiles', 'Amphibians', 'Insects']
sightings = [420, 250, 90, 40, 200]  # Number of sightings in thousands
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Additional data: Sightings over months for a selected category ('Birds' in this example)
birds_monthly = [35, 30, 40, 50, 55, 60, 65, 70, 45, 50, 55, 65]

# Assign colors for each category
colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854']

# Initialize the figure and subplots
fig, axs = plt.subplots(1, 2, figsize=(14, 7))

# -------- First Subplot: Donut Chart --------
# Create the ring chart
wedges, texts, autotexts = axs[0].pie(
    sightings, labels=categories, autopct='%1.1f%%', pctdistance=0.85,
    colors=colors, startangle=140, wedgeprops=dict(width=0.3, edgecolor='w'),
    textprops=dict(color="black", fontsize=10, weight="bold")
)

# Adding a center circle for the "donut" effect
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
axs[0].add_artist(centre_circle)

# Title and central label inside the ring
axs[0].text(0, 0, 'Wildlife Sightings\n2023', fontsize=12, ha='center', va='center', color='gray')

# Set the main title of the subplot
axs[0].set_title('Urban Wildlife Proportions:\nSightings in Greenfield Park', fontsize=14, fontweight='bold', pad=20)

# Customize the legend
axs[0].legend(wedges, categories, title="Categories", loc='upper right', bbox_to_anchor=(1.2, 0, 0.5, 1), fontsize=10)

# -------- Second Subplot: Line Chart --------
axs[1].plot(months, birds_monthly, marker='o', color=colors[0], linewidth=2)
axs[1].fill_between(months, birds_monthly, color=colors[0], alpha=0.3)

# Add labels and title
axs[1].set_xlabel('Month', fontsize=12)
axs[1].set_ylabel('Bird Sightings (in thousands)', fontsize=12)
axs[1].set_title('Monthly Trend of Bird Sightings\n in 2023', fontsize=14, fontweight='bold')

# Adjust tick parameters
axs[1].tick_params(axis='x', rotation=45)
axs[1].grid(True, linestyle='--', alpha=0.5)

# Enhance layout to prevent overlap
plt.tight_layout()

# Show the final plot
plt.show()