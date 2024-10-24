import matplotlib.pyplot as plt

# Define data
sectors = ['Education', 'Healthcare', 'Technology', 'Agriculture', 'Finance']
awareness_levels = [25, 15, 20, 30, 10]

# Define colors for each sector
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Create the pie chart
plt.figure(figsize=(9, 9))
wedges, texts, autotexts = plt.pie(
    awareness_levels,
    labels=sectors,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,
    pctdistance=0.85,
    explode=(0.1, 0, 0, 0, 0)  # Exploding the 'Education' sector for emphasis
)

# Draw circle for a donut style
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Customize the text elements
plt.setp(autotexts, size=10, weight='bold', color='darkblue')
plt.setp(texts, size=12, weight='bold')

# Add title
plt.title('Conservation Awareness by Professional Sector\nSurvey Results of 2023', fontsize=14, fontweight='bold', pad=20)

# Ensure layout is not cut off
plt.tight_layout()

# Display the plot
plt.show()