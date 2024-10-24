import matplotlib.pyplot as plt

# Data for plotting
agencies = [
    "NASA", "ESA", "Roscosmos", "ISRO", "CNSA", "JAXA", "CSA", "Other"
]
missions_contributions = [
    30, 20, 15, 10, 12, 8, 3, 2
]

# Assign distinct colors to each segment for visual appeal
colors = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f'
]

# Create the plot
fig, ax = plt.subplots(figsize=(10, 7), subplot_kw=dict(aspect="equal"))

# Plotting the ring chart
wedges, texts, autotexts = ax.pie(
    missions_contributions,
    labels=agencies,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    wedgeprops=dict(width=0.3, edgecolor='w')
)

# Styling
plt.setp(autotexts, size=10, weight='bold', color='white')
plt.setp(texts, size=12)

# Central label for additional context
ax.text(0, 0, 'Total Missions\n100%', ha='center', va='center', fontsize=12, weight='bold', color='darkgrey')

# Title of the chart
plt.title('Planetary Exploration Missions: 2050\nAgency Contributions', fontsize=14, fontweight='bold')

# Adding a legend outside the plot area
ax.legend(wedges, agencies, title="Space Agencies", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()