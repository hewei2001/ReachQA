import matplotlib.pyplot as plt
import numpy as np

# Data for global tea consumption share
tea_types = ['Green Tea', 'Black Tea', 'Oolong Tea', 'White Tea', 'Herbal Tea', 'Matcha']
consumption_share = [30, 45, 8, 5, 7, 5]

# Data for regional preferences
regions = ['Asia', 'Europe', 'America']
region_preferences = [
    [50, 20, 5],  # Green Tea
    [20, 60, 20], # Black Tea
    [10, 5, 3],   # Oolong Tea
    [5, 5, 5],    # White Tea
    [10, 5, 2],   # Herbal Tea
    [5, 5, 65]    # Matcha
]

# Color palette for each tea type
colors = ['#8DB600', '#4B3832', '#FFB600', '#F7F7F2', '#A8A8A8', '#1D7A46']

# Creating the figure and two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8), gridspec_kw={'width_ratios': [1, 1]})

# Donut pie chart
wedges, texts, autotexts = ax1.pie(
    consumption_share, 
    labels=tea_types, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    pctdistance=0.85,
    wedgeprops=dict(width=0.3)
)

# Enhance text readability for the donut chart
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(12)
    autotext.set_weight('bold')

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax1.add_artist(centre_circle)
ax1.set_title('Global Tea Consumption by Type\nA Taste Across Cultures', fontsize=14, fontweight='bold', color='saddlebrown', pad=30)

# Bar chart for regional preferences
x = np.arange(len(regions))  # the label locations
bar_width = 0.1
for i, tea_type in enumerate(tea_types):
    ax2.bar(x + i * bar_width, region_preferences[i], bar_width, label=tea_type, color=colors[i])

# Add labels, title, and legend for the bar chart
ax2.set_xlabel('Region', fontsize=12)
ax2.set_ylabel('Preference (%)', fontsize=12)
ax2.set_title('Regional Tea Preferences', fontsize=14, fontweight='bold', color='saddlebrown', pad=20)
ax2.set_xticks(x + bar_width * 2.5)
ax2.set_xticklabels(regions)
ax2.legend(title="Tea Types", bbox_to_anchor=(1.05, 1), loc='upper left')

# Automatically adjust layout
plt.tight_layout()

# Display the plots
plt.show()