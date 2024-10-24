import matplotlib.pyplot as plt
import numpy as np

# Define decades and create hypothetical data
decades = np.array([1800, 1810, 1820, 1830, 1840, 1850, 1860, 1870, 1880, 1890,
                    1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000])

# Define the regions
regions = ['Europe', 'Asia', 'North America', 'South America', 'Africa']

# Hypothetical data for each region
literary_output = {
    'Europe': [500, 600, 700, 800, 850, 900, 950, 1000, 1100, 1200,
               1250, 1400, 1500, 1600, 1700, 1800, 2000, 2200, 2400, 2600, 2800],
    'Asia': [300, 320, 350, 380, 410, 450, 480, 510, 550, 590,
             620, 700, 800, 900, 980, 1100, 1200, 1300, 1400, 1500, 1600],
    'North America': [200, 220, 250, 280, 310, 340, 370, 400, 450, 500,
                      540, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050],
    'South America': [100, 110, 120, 130, 140, 150, 160, 170, 180, 190,
                      200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400],
    'Africa': [50, 60, 70, 80, 90, 100, 110, 120, 130, 140,
               150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250]
}

# Estimated standard deviation for the data (a fixed percentage error of 5%)
error = {region: np.array(output) * 0.05 for region, output in literary_output.items()}

# Convert data to numpy arrays
for region in regions:
    literary_output[region] = np.array(literary_output[region])

# Calculate cumulative output for each region
cumulative_output = {region: sum(output) for region, output in literary_output.items()}

# Define the figure size and create two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))

# Plot the line with error bars for each region in the first subplot
for region in regions:
    ax1.errorbar(decades, literary_output[region], yerr=error[region],
                 label=region, linewidth=2, elinewidth=1.5, capsize=4,
                 alpha=0.8)  # Reduced alpha for error bars

# Set up the title, axes labels, and legend for the first subplot
ax1.set_title('Historical Global Literary Output\nand Its Impact over Time', fontsize=16)
ax1.set_xlabel('Decades', fontsize=14)
ax1.set_ylabel('Number of Published Works', fontsize=14)
ax1.tick_params(axis='both', which='major', labelsize=12)
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.legend(title='Region', loc='upper left', bbox_to_anchor=(1.0, 1))

# Ensure tick labels are not overlapping in the first subplot
ax1.set_xticks(decades[::2])

# Create a bar chart for the cumulative output in the second subplot
ax2.bar(regions, cumulative_output.values(), color=['b', 'g', 'r', 'c', 'm'])

# Set up the title and axes labels for the second subplot
ax2.set_title('Cumulative Global Literary Output\nby Region', fontsize=16)
ax2.set_xlabel('Region', fontsize=14)
ax2.set_ylabel('Total Number of Published Works', fontsize=14)

# Adjust the layout for both subplots
plt.tight_layout()

# Display the plot
plt.show()