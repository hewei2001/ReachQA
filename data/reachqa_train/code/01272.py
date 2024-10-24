import matplotlib.pyplot as plt
import numpy as np

# Original data: Time allocation for activities in minutes
activities = ['Meetings', 'Desk Work', 'Breaks', 'Emails', 'Commuting']
time_spent = [90, 210, 60, 60, 60]  # 480 minutes total
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# New data: Productivity rating for each activity on a scale from 1 to 10
productivity_ratings = [6, 8, 4, 5, 3]

# Create subplots
fig, ax = plt.subplots(1, 2, figsize=(14, 7), gridspec_kw={'width_ratios': [1, 1]})

# Donut pie chart (original)
wedges, texts, autotexts = ax[0].pie(
    time_spent, 
    labels=activities, 
    autopct='%1.1f%%', 
    startangle=140, 
    pctdistance=0.85, 
    colors=colors, 
    wedgeprops={'width': 0.3, 'edgecolor': 'black'},
    textprops=dict(color="black", fontsize=10, weight='bold')
)

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_weight('bold')

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax[0].add_artist(centre_circle)
ax[0].set_title('Time Allocation (8-hour Workday)', fontsize=14, fontweight='bold', pad=20)
ax[0].axis('equal')
ax[0].legend(wedges, activities, title="Activities", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Bar chart for productivity
x = np.arange(len(activities))
ax[1].bar(x, productivity_ratings, color=colors, edgecolor='black')
ax[1].set_title('Productivity Ratings by Activity', fontsize=14, fontweight='bold')
ax[1].set_xticks(x)
ax[1].set_xticklabels(activities, rotation=45, ha='right', fontsize=10)
ax[1].set_ylim(0, 10)
ax[1].set_ylabel('Rating (1-10)', fontsize=12)
for i, v in enumerate(productivity_ratings):
    ax[1].text(i, v + 0.2, str(v), color='black', ha='center', fontweight='bold')

# Adjust layout to fit everything nicely
plt.tight_layout()
plt.show()