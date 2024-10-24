import matplotlib.pyplot as plt
import numpy as np

# Define funding categories and their respective percentages
categories = [
    'Climate Studies',
    'Deep-Sea Exploration',
    'Marine Biodiversity',
    'Pollution Monitoring',
    'Renewable Energy',
    'Fisheries Management'
]
funding_percentages = [25, 20, 15, 10, 20, 10]

# Define colors for each category
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

# Create the ring chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(aspect="equal"))

# Create the pie chart and customize the appearance
wedges, texts, autotexts = ax.pie(
    funding_percentages,
    colors=colors,
    labels=categories,
    autopct='%1.1f%%',
    pctdistance=0.85,
    startangle=90,
    wedgeprops=dict(width=0.3, edgecolor='w', alpha=0.8)
)

# Format the labels and percentage text
plt.setp(texts, size=10, weight="bold", color="darkslategray")
plt.setp(autotexts, size=9, weight="bold", color="white")

# Center circle to create the ring chart effect
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Add a central label for additional context
ax.text(0, 0, 'Global Marine\nResearch\nFunding 2023', horizontalalignment='center',
        verticalalignment='center', fontsize=12, color='navy', weight='bold')

# Title for the ring chart
ax.set_title("Distribution of Global Marine Research Funding (2023)", fontsize=14, fontweight='bold', pad=20, color='navy')

# Adjust layout to ensure a neat fit and prevent overlap
plt.tight_layout()

# Display the plot
plt.show()