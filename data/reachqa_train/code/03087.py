import matplotlib.pyplot as plt

# Define ocean regions and their MPA distribution percentages
ocean_regions = ['Pacific Ocean', 'Atlantic Ocean', 'Indian Ocean', 'Southern Ocean', 'Arctic Ocean']
mpa_distribution = [35, 25, 15, 20, 5]

# Define colors for each ocean region slice
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Highlight the largest sector (Pacific Ocean)
explode = [0.1, 0, 0, 0, 0]

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(
    mpa_distribution,
    labels=ocean_regions,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,
    explode=explode,
    shadow=True,
    wedgeprops={'edgecolor': 'black', 'linewidth': 1}
)

# Customize the percentage labels
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(12)
    autotext.set_weight('bold')

# Add a multi-line title for better readability
plt.title("Global Distribution of Marine Protected Areas\nAcross Major Ocean Regions", 
          fontsize=16, fontweight='bold', ha='center')

# Add a legend for the ocean regions
plt.legend(wedges, ocean_regions, title="Ocean Regions", loc='center left', bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Adjust layout to ensure no overlaps
plt.tight_layout()

# Show the plot
plt.show()