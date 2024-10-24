import matplotlib.pyplot as plt
from matplotlib.patches import Shadow

# Define age groups and corresponding percentages of EV ownership
age_groups = ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']
percentages = [8, 22, 30, 25, 10, 5]

# Define colors for each age group using a colormap for gradient effect
colors = plt.cm.viridis([0.1, 0.3, 0.5, 0.6, 0.8, 0.9])

# Explode the segment with the highest percentage for emphasis
explode = (0, 0, 0.1, 0, 0, 0)

# Create the ring chart
plt.figure(figsize=(12, 10))
wedges, texts, autotexts = plt.pie(percentages, labels=age_groups, colors=colors, explode=explode,
                                   autopct='%1.1f%%', startangle=140, pctdistance=0.85,
                                   wedgeprops=dict(width=0.3, edgecolor='w', linewidth=1))

# Add a subtle shadow effect
for wedge in wedges:
    shadow = Shadow(wedge, -0.02, -0.02, color='gray', alpha=0.2)
    plt.gca().add_patch(shadow)

# Improve the autotexts for readability and emphasis
for i, text in enumerate(autotexts):
    text.set_color('black')
    text.set_fontsize(11)
    if percentages[i] > 20:
        text.set_fontweight('bold')

# Add a center circle to transform the pie into a ring
centre_circle = plt.Circle((0, 0), 0.70, fc='white', linewidth=0)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Advanced title with multi-line for better readability
plt.title('2023 Electric Vehicle Ownership by Age Group\n'
          'Analyzing Consumer Trends in EV Adoption', 
          fontsize=16, fontweight='bold', ha='center', va='center', pad=40)

# Add legend with additional description
plt.legend(wedges, [f'{age}: {percent}% - Review Trends' for age, percent in zip(age_groups, percentages)],
           title="Age Group", loc='center left', bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Add a data source note
plt.figtext(0.5, 0.01, 'Data Source: Survey 2023', ha='center', fontsize=9, color='grey')

# Ensure the ring chart is displayed as a circle and adjust layout
plt.axis('equal')  
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Show the chart
plt.show()