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
# Projected growth rates over the next five years (arbitrary example data)
projected_growth_rates = [5.2, 3.8, 4.5, 2.9, 6.1, 3.3]

# Define consistent colors for each category
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

# Create a figure with two subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8), gridspec_kw={'width_ratios': [1, 1.2]})

# Create the ring chart (left subplot)
wedges, texts, autotexts = ax1.pie(
    funding_percentages,
    colors=colors,
    labels=categories,
    autopct='%1.1f%%',
    pctdistance=0.85,
    startangle=90,
    wedgeprops=dict(width=0.3, edgecolor='w', alpha=0.8)
)

plt.setp(texts, size=10, weight="bold", color="darkslategray")
plt.setp(autotexts, size=9, weight="bold", color="white")

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax1.add_artist(centre_circle)

ax1.text(0, 0, 'Global Marine\nResearch\nFunding 2023', horizontalalignment='center',
         verticalalignment='center', fontsize=12, color='navy', weight='bold')
ax1.set_title("Distribution of Global Marine\nResearch Funding (2023)", fontsize=14, fontweight='bold', pad=20, color='navy')

# Create the bar chart (right subplot)
ax2.barh(categories, projected_growth_rates, color=colors, edgecolor='grey')
ax2.set_xlabel('Projected Growth Rate (%)', fontsize=12, fontweight='bold', color='navy')
ax2.set_title("Projected Funding Growth Rates\nfor Marine Research (2023-2028)", fontsize=14, fontweight='bold', pad=20, color='navy')
ax2.invert_yaxis()  # Optional: to have the same order as in the pie chart

# Add annotations for the bar chart
for i, v in enumerate(projected_growth_rates):
    ax2.text(v + 0.2, i, f"{v:.1f}%", color='black', va='center', fontsize=10, fontweight='bold')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plots
plt.show()