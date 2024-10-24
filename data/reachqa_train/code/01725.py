import matplotlib.pyplot as plt

# Data and labels for cuisines
cuisines = ['Italian', 'Chinese', 'Mexican', 'Indian', 'French', 'Japanese', 'Greek']
votes = [150, 100, 80, 70, 50, 30, 20]

# Define colors for each slice
colors = ['#FF5733', '#33FFBD', '#FF33F6', '#3375FF', '#FFFF33', '#FF33A6', '#33FF57']

# Explode the first slice (Italian) for emphasis
explode = (0.1, 0, 0, 0, 0, 0, 0)

# Plotting the donut pie chart
plt.figure(figsize=(10, 8))
wedges, texts, autotexts = plt.pie(votes, 
                                   explode=explode, 
                                   labels=cuisines, 
                                   autopct='%1.1f%%', 
                                   startangle=90, 
                                   colors=colors, 
                                   pctdistance=0.85, 
                                   wedgeprops=dict(width=0.3, edgecolor='w'),
                                   shadow=True)

# Draw circle for donut hole
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')  

# Title
plt.title("Exploring the Culinary World:\nFavorite Cuisines Among Food Enthusiasts", fontsize=16, fontweight='bold', pad=20)

# Customizing the legend
plt.legend(wedges, cuisines, title="Cuisines", loc="upper left", bbox_to_anchor=(1, 0.9))

# Customizing the autotexts
for autotext in autotexts:
    autotext.set_color('navy')
    autotext.set_fontsize(10)
    autotext.set_fontweight('bold')

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()