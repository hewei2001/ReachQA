import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2012, 2023)

# Define the number of jobs available in thousands for each sector
software_development = np.array([150, 160, 170, 190, 210, 230, 255, 280, 305, 340, 380])
data_science = np.array([30, 40, 55, 70, 90, 120, 150, 185, 220, 270, 325])
cybersecurity = np.array([20, 25, 35, 45, 60, 80, 110, 145, 185, 230, 290])

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting the stacked area chart
ax.stackplot(years, software_development, data_science, cybersecurity, 
             labels=['Software Development', 'Data Science', 'Cybersecurity'],
             colors=['#1f77b4', '#ff7f0e', '#2ca02c'], alpha=0.8)

# Set title and labels
ax.set_title('Tech Sector Job Market Evolution\n(2012-2022)', fontsize=16, fontweight='bold', loc='left', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Job Openings (Thousands)', fontsize=12)

# Add a legend to the plot
ax.legend(loc='upper left', fontsize=10, frameon=False)

# Add grid lines for better readability
ax.grid(True, which='major', linestyle='--', alpha=0.6)

# Adjust x-axis ticks for clarity
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha='right')

# Customizing the y-axis format and minor grid lines
ax.tick_params(axis='y', which='both', direction='inout')
ax.minorticks_on()
ax.grid(True, which='minor', linestyle=':', linewidth='0.5', alpha=0.7)

# Annotate the plot with relevant data points
for i, year in enumerate(years):
    if i % 2 == 0:  # Adding annotations for alternating years for clarity
        ax.annotate(f"{software_development[i]}K", (year, software_development[i] - 10),
                    textcoords="offset points", xytext=(-10, -15), ha='center', fontsize=8, color='blue')
        ax.annotate(f"{data_science[i]}K", (year, software_development[i] + data_science[i] - 10),
                    textcoords="offset points", xytext=(-10, 5), ha='center', fontsize=8, color='orange')
        ax.annotate(f"{cybersecurity[i]}K", (year, software_development[i] + data_science[i] + cybersecurity[i] - 10),
                    textcoords="offset points", xytext=(-10, 5), ha='center', fontsize=8, color='green')

# Automatically adjust layout to prevent overlap and clipping
plt.tight_layout()

# Show the plot
plt.show()