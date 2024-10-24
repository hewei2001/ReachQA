import matplotlib.pyplot as plt

# Data for each digital communication platform
platforms = ['Social Media', 'Email', 'Messaging Apps', 'Professional Networks', 'Video Calls']
usage_percentages = [35, 25, 20, 10, 10]

# Define distinct colors for each segment
colors = ['#FF6F61', '#6B5B95', '#88B04B', '#FF8C42', '#008080']

# Create a figure and axis
fig, ax = plt.subplots(figsize=(9, 9))

# Create the pie chart with specified wedge properties to form a ring
wedges, texts, autotexts = ax.pie(
    usage_percentages, 
    labels=platforms, 
    colors=colors, 
    autopct='%1.1f%%', 
    startangle=90, 
    pctdistance=0.85, 
    wedgeprops=dict(width=0.3, edgecolor='w', linewidth=2)
)

# Draw a center circle to enhance the ring effect
centre_circle = plt.Circle((0, 0), 0.60, fc='white', linewidth=1.5, edgecolor='black')
fig.gca().add_artist(centre_circle)

# Customize the autotexts for better visibility
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(11)
    autotext.set_fontweight('bold')

# Add a central title inside the ring
ax.text(0, 0, 'Global\nUsage 2023', horizontalalignment='center', verticalalignment='center',
        fontsize=14, fontweight='bold', color='black')

# Set a multi-line title for the plot
ax.set_title('Digital Communication Platforms\nUser Engagement Overview 2023', fontsize=16, fontweight='bold', pad=20)

# Ensure the pie chart is circular
ax.axis('equal')

# Add legend with custom position
plt.legend(title='Platforms', loc='upper right', bbox_to_anchor=(1.3, 1), fontsize=10, title_fontsize='12', frameon=False)

# Adjust layout to prevent any overlap
plt.tight_layout()

# Display the plot
plt.show()