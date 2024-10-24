import matplotlib.pyplot as plt

# Data for the pie chart
pollution_sources = [
    'Transportation Emissions', 
    'Industrial Discharges', 
    'Residential Heating', 
    'Construction Dust', 
    'Agricultural Activities', 
    'Waste Burning', 
    'Other Sources'
]
percentages = [30, 25, 15, 10, 10, 5, 5]

# Colors for each pollution source
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']

# Explode the first slice slightly to highlight it
explode = (0.1, 0, 0, 0, 0, 0, 0)

# Plotting the pie chart
plt.figure(figsize=(10, 7))
plt.pie(
    percentages, labels=pollution_sources, autopct='%1.1f%%', startangle=140, colors=colors, 
    wedgeprops={'edgecolor': 'black'}, explode=explode, shadow=True
)

# Title with line break for better readability
plt.title("Air Pollution Sources in Greenfield City:\nA Breakdown of Pollutant Contributions", fontsize=16, pad=20)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()