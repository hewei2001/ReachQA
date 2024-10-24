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

# Calculate the percentage growth
def calculate_growth(data):
    return np.diff(data) / data[:-1] * 100

gaming_growth = calculate_growth(gaming_vr)
healthcare_growth = calculate_growth(healthcare_vr)
education_growth = calculate_growth(education_vr)
real_estate_growth = calculate_growth(real_estate_vr)

# Adjust the years for the growth data
growth_years = years[1:]

# Create the plot with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8), gridspec_kw={'width_ratios': [3, 2]})

# First subplot: Stacked Area Chart
ax1.stackplot(years, vr_applications, labels=['Gaming', 'Healthcare', 'Education', 'Real Estate'],
              colors=['#8A2BE2', '#FF69B4', '#FFD700', '#20B2AA'], alpha=0.8)

ax1.set_title('Evolution of Virtual Reality Applications in Diverse Sectors\n(2015-2025)', fontsize=16, fontweight='bold')
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Number of VR Installations', fontsize=14)

ax1.legend(loc='upper left', fontsize=12, title='Sectors', bbox_to_anchor=(1, 1))
ax1.set_xticks(years)
ax1.set_yticks(np.arange(0, 301, 50))
ax1.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

ax1.annotate('VR Healthcare Breakthrough', xy=(2021, 65), xytext=(2018, 250),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, ha='center', backgroundcolor='white')

ax1.annotate('Education Embraces VR', xy=(2019, 35), xytext=(2016, 200),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, ha='center', backgroundcolor='white')

# Second subplot: Line Chart for Percentage Growth
ax2.plot(growth_years, gaming_growth, label='Gaming', color='#8A2BE2', marker='o')
ax2.plot(growth_years, healthcare_growth, label='Healthcare', color='#FF69B4', marker='o')
ax2.plot(growth_years, education_growth, label='Education', color='#FFD700', marker='o')
ax2.plot(growth_years, real_estate_growth, label='Real Estate', color='#20B2AA', marker='o')

ax2.set_title('Annual Percentage Growth of VR Applications', fontsize=16, fontweight='bold')
ax2.set_xlabel('Year', fontsize=14)
ax2.set_ylabel('Percentage Growth (%)', fontsize=14)

ax2.legend(loc='upper right', fontsize=12, title='Sectors')
ax2.set_xticks(growth_years)
ax2.set_yticks(np.arange(0, 101, 10))
ax2.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plots
plt.show()