import matplotlib.pyplot as plt

# Data for the pie chart
regions = [
    'Western Europe', 'Eastern Europe', 'East Asia', 'South Asia', 
    'North America', 'Central America', 'South America', 
    'Northern Africa', 'Sub-Saharan Africa', 'Australia', 'Pacific Islands'
]
capacity_percentage = [12, 8, 15, 13, 10, 5, 7, 4, 2, 2, 1]

# Colors for each region
colors = [
    '#1f77b4', '#aec7e8', '#ff7f0e', '#ffbb78', '#2ca02c', 
    '#98df8a', '#d62728', '#ff9896', '#9467bd', '#c5b0d5', '#8c564b'
]

# Exploding the top three sectors
explode = [0.1 if percentage >= 10 else 0 for percentage in capacity_percentage]

# Creating the pie chart
fig, ax = plt.subplots(figsize=(12, 8))
wedges, texts, autotexts = ax.pie(
    capacity_percentage, labels=regions, autopct='%1.1f%%',
    startangle=140, colors=colors, explode=explode, pctdistance=0.85
)

# Formatting for text inside and outside the pie chart
for text in texts:
    text.set_fontsize(10)
    text.set_color('navy')
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)
    autotext.set_fontweight('bold')

# Draw a circle at the center to make it look like a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Aspect ratio to ensure pie is drawn as a circle
ax.axis('equal')  

# Add title
plt.title('Global Renewable Energy Capacity by Region in 2023\nWith Hierarchical Data Representation', 
          fontsize=14, fontweight='bold', pad=20)

# Add a legend with more room and formatted to avoid overlap
ax.legend(wedges, regions, title="Regions", loc='center left', bbox_to_anchor=(1.1, 0.5), fontsize=10)

# Adjust layout to prevent text overlap
plt.tight_layout()

# Adding a secondary plot - a subplot bar chart to show trend data
trend_data = [3, 2.5, 4, 3.5, 2, 1.5, 2.2, 1.3, 0.8, 0.6, 0.4]
years = ['2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028']

# Create a new figure and axis
fig, ax2 = plt.subplots(figsize=(12, 4))
ax2.bar(years, trend_data, color='#1f77b4')
ax2.set_title('Trend of Global Renewable Energy Growth', fontsize=14, fontweight='bold')
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Growth Rate (%)', fontsize=12)
ax2.set_ylim(0, 5)
ax2.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout to prevent text overlap
plt.tight_layout()

# Display the plots
plt.show()