import matplotlib.pyplot as plt

# Define the programming languages and their respective usage percentages
languages = ['Python', 'JavaScript', 'Java', 'C++', 'Go', 'Rust', 'Ruby']
usage_percentages = [30, 20, 15, 12, 8, 10, 5]

# Define colors for the segments
colors = ['#377eb8', '#ff7f00', '#4daf4a', '#f781bf', '#a65628', '#984ea3', '#999999']

# Create the pie chart
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    usage_percentages,
    labels=languages,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    wedgeprops=dict(width=0.3, edgecolor='w'),
    pctdistance=0.85
)

# Customize the text for labels and percentages
plt.setp(autotexts, size=10, weight='bold', color='black')
plt.setp(texts, size=12, weight='bold')

# Draw circle for donut shape
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Add a legend outside the chart
ax.legend(wedges, languages, title="Languages", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Set the title of the plot
plt.title("Diverse Programming Languages in\nTech Startups Ecosystem", size=14, weight='bold', pad=20)

# Adjust layout to avoid overlap
plt.tight_layout()

# Show plot
plt.show()