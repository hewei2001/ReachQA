import matplotlib.pyplot as plt
import numpy as np

# Define the data for the pie chart
technologies = ['Solar Power', 'Wind Energy', 'Hydroelectric', 'Geothermal', 'Biomass']
shares = [35, 25, 20, 10, 10]

# Define the data for the bar chart (in billions of USD)
investments = [120, 90, 80, 30, 25]

# Define colors
pie_colors = ['#ffcc00', '#6699ff', '#66ff66', '#ff9966', '#ff66b3']
bar_colors = ['#cc9900', '#3366cc', '#33cc33', '#cc6633', '#cc3399']

# Define explode to highlight the 'Solar Power' sector in the pie chart
explode = (0.1, 0, 0, 0, 0)

# Create the figure and the subplots
fig, ax1 = plt.subplots(figsize=(12, 8))

# Create the pie chart
wedges, texts, autotexts = ax1.pie(
    shares, 
    labels=technologies, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=pie_colors, 
    explode=explode
)

# Customize the appearance of the pie chart text
plt.setp(texts, size=10, weight='bold', color='white')
plt.setp(autotexts, size=12, weight='bold')

# Create a secondary axis for the bar chart
ax2 = ax1.twinx()

# Create the bar chart on the secondary axis
bar_positions = np.arange(len(technologies))
bars = ax2.bar(
    bar_positions, 
    investments, 
    color=bar_colors, 
    width=0.2, 
    align='center', 
    alpha=0.7, 
    label='Annual Investment (in billions)'
)

# Set the position of the bar chart with respect to the pie chart
for bar, wedge in zip(bars, wedges):
    bar.set_x(wedge.theta1 + (wedge.theta2 - wedge.theta1) / 2)

# Add bar chart labels
ax2.bar_label(bars, fmt='$%dB', label_type='edge', padding=3, color='black', fontsize=10)

# Customize the bar chart
ax2.set_ylim(0, 130)  # Setting a common y limit to ensure a consistent scale
ax2.set_axis_off()  # Hide axis for a cleaner look

# Main title for the combined chart
plt.title(
    'Renewable Energy Sector Analysis\nMarket Share vs. Annual Investment - 2023', 
    fontsize=14, 
    weight='bold', 
    pad=30
)

# Add a legend
ax1.legend(
    wedges + [bars], 
    technologies + ['Investment'], 
    title="Legend", 
    loc="upper left", 
    bbox_to_anchor=(1, 1), 
    fontsize=9
)

# Automatically adjust layout to ensure everything fits without overlap
plt.tight_layout()

# Display the chart
plt.show()