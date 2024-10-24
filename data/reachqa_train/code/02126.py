import matplotlib.pyplot as plt

# Define the activity data with more categories and fractional percentages
activities = [
    'Work', 'Sleep', 'Leisure', 'Commute', 'Exercise', 
    'Other', 'Cooking', 'Cleaning', 'Reading', 'Family Time', 'Social Media'
]
time_spent = [28.5, 25.0, 12.3, 9.0, 5.5, 4.7, 3.0, 2.5, 3.5, 3.2, 2.3]

# Define colors for the pie sections with some repeats for variety
colors = [
    '#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', 
    '#ffb3e6', '#ff6666', '#99ffcc', '#ffccff', '#ff6666', '#66ffb3'
]

# Explode 'Leisure' and 'Family Time' to highlight them
explode = (0.05, 0, 0.1, 0, 0, 0, 0, 0, 0, 0.1, 0)

# Create a figure with a specific size
plt.figure(figsize=(12, 8))

# Create the main pie chart (donut)
plt.pie(
    time_spent, 
    explode=explode, 
    labels=activities, 
    colors=colors, 
    autopct='%1.1f%%', 
    startangle=140, 
    pctdistance=0.85, 
    shadow=True
)

# Draw a circle in the center to make it a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Title with multiple lines for clarity
plt.title(
    "Detailed Time Allocation in Pleasantville:\nAn Advanced View of a Typical Weekday", 
    fontsize=15, 
    fontweight='bold', 
    pad=20
)

# Adjust the legend to avoid overlapping
plt.legend(
    activities, 
    loc='upper center', 
    title="Activities", 
    fontsize=9, 
    bbox_to_anchor=(0.5, -0.1), 
    ncol=3
)

# Create an additional subplot for a bar chart showing variability
plt.gcf().subplots_adjust(left=0.05, right=0.95, top=0.85, bottom=0.15)
plt.figure(figsize=(12, 4))
daily_variability = [3, 2, 1, 2, 1, 1, 0.5, 0.5, 0.3, 0.5, 0.2]
plt.bar(activities, daily_variability, color=colors)
plt.title("Daily Variability in Time Allocation", fontsize=12)
plt.ylabel("Hours +/-")
plt.xticks(rotation=45, ha='right')

# Show the plots with tight layout to prevent overlap
plt.tight_layout()
plt.show()