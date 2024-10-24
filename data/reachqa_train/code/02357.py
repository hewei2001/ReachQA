import matplotlib.pyplot as plt

# Define the categories and their respective consumption data
categories = ['Streaming Services', 'Social Media', 'Online Gaming', 'E-books', 'Podcasts']
consumption_data = [35, 25, 20, 10, 10]

# Define the colors for each category
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Explode the 'Streaming Services' sector slightly for emphasis
explode = (0.1, 0, 0, 0, 0)

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    consumption_data, 
    labels=categories, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    explode=explode, 
    wedgeprops=dict(width=0.3)
)

# Customize the text and wedges
plt.setp(texts, size=12, weight="bold", color='navy')
plt.setp(autotexts, size=10, weight="bold", color='black')

# Add a center circle for a donut look
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Set the title and ensure no overlap by breaking it into two lines
ax.set_title('Global Digital Content\nConsumption Trends in 2023', fontsize=16, fontweight='bold', color='darkblue', pad=20)

# Add a legend with clear placement outside the pie chart
ax.legend(wedges, categories, title="Content Types", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10, title_fontsize=12)

# Automatically adjust layout to prevent overlap and ensure neat presentation
plt.tight_layout()

# Display the plot
plt.show()