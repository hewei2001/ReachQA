import matplotlib.pyplot as plt

# Data: Language distribution in global literature
languages = ['English', 'Chinese', 'Spanish', 'Hindi', 'Arabic', 
             'Russian', 'French', 'German', 'Japanese', 'Others']
percentages = [35, 14, 12, 9, 8, 6, 5, 4, 3, 4]

# Define a color palette
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', 
          '#ffb3e6', '#ff6666', '#c2f0c2', '#f0e68c', '#80b3ff']

# Create figure and axis with a specific size and aspect
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(aspect="equal"))

# Create the ring chart
wedges, texts, autotexts = ax.pie(percentages, labels=languages, 
                                  autopct='%1.1f%%', startangle=140, 
                                  pctdistance=0.85, colors=colors, 
                                  wedgeprops=dict(width=0.3, edgecolor='w'))

# Decorate the plot with additional settings
plt.setp(autotexts, size=9, weight="bold", color="black")

# Add a central circle for the ring effect
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Add a title inside the ring space
ax.text(0, 0, 'Literature\nLanguage\nDistribution', 
        horizontalalignment='center', verticalalignment='center', 
        fontsize=13, fontweight='bold', color='gray')

# Title and customization
ax.set_title('World Language Distribution\nin Global Literature', fontsize=15, fontweight='bold', pad=20)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()