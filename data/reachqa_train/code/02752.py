import matplotlib.pyplot as plt

# Define the data
platforms = ['Instagram', 'TikTok', 'Facebook', 'YouTube', 'Twitter', 'Snapchat']
user_percentages = [22, 18, 25, 15, 10, 10]
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700', '#FFB6C1']

# Create a donut pie chart
plt.figure(figsize=(10, 7))
wedges, texts, autotexts = plt.pie(
    user_percentages, 
    labels=platforms, 
    colors=colors, 
    startangle=140, 
    wedgeprops=dict(width=0.3, edgecolor='w'),
    autopct='%1.1f%%', 
    pctdistance=0.85
)

# Add a circle at the center to transform the pie chart into a donut chart
center_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(center_circle)

# Customize autotexts
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontweight('bold')

# Title of the chart
plt.title('The Spectrum of Social Media Influence:\nA Look at User Engagement in 2023',
          fontsize=16, fontweight='bold', pad=20)

# Add a legend
plt.legend(wedges, platforms, title='Platforms', loc='center left', bbox_to_anchor=(1, 0.5))

# Ensure the plot is a circle
plt.axis('equal')

# Automatically adjust layout
plt.tight_layout()

# Display the chart
plt.show()