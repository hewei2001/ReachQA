import matplotlib.pyplot as plt
import numpy as np

# Data for the original donut chart
age_groups = [
    'Children (0-12 years)', 
    'Teens (13-19 years)', 
    'Young Adults (20-35 years)', 
    'Middle-Aged (36-55 years)', 
    'Seniors (56+ years)'
]
visitor_count = [5000, 15000, 45000, 25000, 10000]

# Data for the new bar chart: Average time spent in minutes by each age group
avg_time_spent = [30, 45, 60, 50, 40]

# Create subplots with a 1x2 grid
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# Colors for the charts
colors = plt.get_cmap('Pastel1')(np.linspace(0.1, 0.9, len(age_groups)))

# Plotting the donut chart
explode = (0, 0, 0.1, 0, 0)
wedges, texts, autotexts = ax1.pie(
    visitor_count, 
    labels=age_groups, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=colors, 
    explode=explode, 
    pctdistance=0.85
)

# Adding a circle at the center to make it a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax1.add_artist(centre_circle)
ax1.axis('equal')  # Ensure pie is a circle
ax1.set_title(
    "Visitor Demographics in\nGlobal Art Odyssey", 
    fontsize=14, 
    fontweight='bold'
)

plt.setp(autotexts, size=10, weight="bold", color='darkblue')
plt.setp(texts, size=12)

# Plotting the bar chart
bar_positions = np.arange(len(age_groups))
ax2.bar(bar_positions, avg_time_spent, color=colors, alpha=0.7)
ax2.set_xticks(bar_positions)
ax2.set_xticklabels(age_groups, rotation=45, ha='right')
ax2.set_ylabel('Average Time Spent (minutes)')
ax2.set_title('Average Time Spent by Age Group', fontsize=14, fontweight='bold')

# Tight layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()