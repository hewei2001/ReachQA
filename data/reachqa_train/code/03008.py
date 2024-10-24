import matplotlib.pyplot as plt
import numpy as np

# Years and energy sources
years = ['2013', '2015', '2017', '2019', '2021', '2022']
energy_sources = ['Solar', 'Wind', 'Hydroelectric', 'Biomass', 'Geothermal']

# Hypothetical data for each energy source as a percentage of total renewable energy production
solar = [10, 15, 20, 25, 28, 30]
wind = [25, 30, 28, 26, 25, 24]
hydroelectric = [40, 35, 32, 30, 28, 25]
biomass = [15, 13, 12, 12, 13, 14]
geothermal = [10, 7, 8, 7, 6, 7]

# Data stack for plotting
data_stack = [solar, wind, hydroelectric, biomass, geothermal]

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Define bar width
bar_width = 0.6

# Positions of the bars on the x-axis
x = np.arange(len(years))

# Colors for each energy source
colors = ['#FFDD44', '#77AAFF', '#88CC99', '#FF8888', '#AA77CC']

# Plot each energy source in the stack
for i, (source_data, color) in enumerate(zip(data_stack, colors)):
    ax.bar(x, source_data, bar_width, label=energy_sources[i], color=color, 
           bottom=np.sum(data_stack[:i], axis=0))

# Annotate each bar with its data value
for j in range(len(years)):
    total = 0
    for i, source in enumerate(data_stack):
        ax.text(x[j], total + source[j]/2, f'{source[j]}%', ha='center', va='center', 
                color='white', fontsize=9, fontweight='bold')
        total += source[j]

# Adding titles and labels
ax.set_title('Renewable Energy Production Over the Decade\n (2013-2022)', 
             fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Year', fontsize=12, labelpad=10)
ax.set_ylabel('Percentage of Total Renewable Energy Production', fontsize=12, labelpad=10)

# Customize the x-axis with year labels
ax.set_xticks(x)
ax.set_xticklabels(years)

# Add a legend
ax.legend(title='Energy Source', fontsize=10, loc='upper left', bbox_to_anchor=(1, 1))

# Grid lines for better readability
ax.grid(linestyle='--', alpha=0.5, axis='y')

# Automatically adjust the layout
plt.tight_layout(rect=[0, 0, 0.85, 1])

# Display the plot
plt.show()