import matplotlib.pyplot as plt
import numpy as np

# Define the years for the analysis
years = np.arange(2015, 2026)

# Define the number of VR applications in each sector over the years
gaming_vr = np.array([10, 15, 25, 35, 50, 70, 90, 120, 150, 180, 210])
healthcare_vr = np.array([5, 8, 12, 18, 30, 45, 65, 80, 100, 125, 150])
education_vr = np.array([2, 5, 10, 20, 35, 55, 75, 95, 120, 140, 170])
real_estate_vr = np.array([3, 4, 8, 14, 25, 40, 60, 80, 100, 130, 160])

# Stack the data for the area chart
vr_applications = np.vstack([gaming_vr, healthcare_vr, education_vr, real_estate_vr])

# Plotting the stacked area chart
fig, ax = plt.subplots(figsize=(12, 8))

ax.stackplot(years, vr_applications, labels=['Gaming', 'Healthcare', 'Education', 'Real Estate'],
             colors=['#8A2BE2', '#FF69B4', '#FFD700', '#20B2AA'], alpha=0.8)

# Customizing the chart
ax.set_title('Evolution of Virtual Reality Applications in Diverse Sectors\n(2015-2025)',
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Number of VR Installations', fontsize=14)

# Add the legend
ax.legend(loc='upper left', fontsize=12, title='Sectors', bbox_to_anchor=(1, 1))

# Custom ticks
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 301, 50))

# Add grid for better readability
ax.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Annotate significant milestones
ax.annotate('VR Healthcare Breakthrough', xy=(2021, 65), xytext=(2018, 250),
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=10, ha='center', backgroundcolor='white')

ax.annotate('Education Embraces VR', xy=(2019, 35), xytext=(2016, 200),
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=10, ha='center', backgroundcolor='white')

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()