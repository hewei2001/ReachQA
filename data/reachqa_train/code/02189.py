import matplotlib.pyplot as plt

# Define the data
os_names = ['Android', 'iOS', 'Others']
market_share = [72, 27, 1]
colors = ['#66b3ff', '#ff9999', '#99ff99']

# Explode 'Others' segment for emphasis
explode = (0.1, 0, 0.3)

# Start plotting
fig, ax = plt.subplots(figsize=(10, 7))

# Create the pie chart
wedges, texts, autotexts = ax.pie(market_share, explode=explode, labels=os_names, autopct='%1.1f%%', 
                                  startangle=90, colors=colors, wedgeprops=dict(width=0.3, edgecolor='w'), 
                                  shadow=True, pctdistance=0.85)

# Customize autotexts for better visibility
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(12)
    autotext.set_weight('bold')

# Draw a circle at the center of the pie chart to make it a donut
centre_circle = plt.Circle((0, 0), 0.55, fc='white')
fig.gca().add_artist(centre_circle)

# Add a title with line breaks for readability
plt.title('Global Smartphone Operating System\nMarket Share in 2023', fontsize=16, weight='bold', color='darkblue')

# Add a legend
ax.legend(wedges, os_names, title="Operating Systems", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Improve plot layout
plt.tight_layout()

# Display the plot
plt.show()