import matplotlib.pyplot as plt
import numpy as np

# Data
fields = ["Artificial Intelligence", "Renewable Energy", "Biotechnology", "Quantum Computing", "Virtual Reality"]
innovative_ideas = [120, 90, 80, 110, 100]
years = [2015, 2016, 2017, 2018, 2019]
funding_amounts = [1000000, 800000, 700000, 900000, 1100000]

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), gridspec_kw={'width_ratios': [3, 1]})

# Histogram chart
ax1.barh(fields, innovative_ideas, color='#3498db', alpha=0.7)
ax1.set_title("Future Frontiers:\nDistribution of Innovative Ideas in Emerging Technologies")
ax1.set_xlabel('Number of Innovative Ideas', fontsize=12)
ax1.set_ylabel('Field of Technology', fontsize=12)
ax1.grid(axis='x', linestyle='--', alpha=0.7)

# Pie chart for funding amounts
ax2.pie(funding_amounts, labels=fields, autopct='%1.1f%%', startangle=90, colors=plt.cm.tab20(range(len(fields))))
ax2.set_title("Funding Distribution", fontsize=12)
ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Automatically adjust the image layout
plt.tight_layout(rect=[0, 0, 1, 0.9])

# Show the plot
plt.show()