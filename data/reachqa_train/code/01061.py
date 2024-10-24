import matplotlib.pyplot as plt

# Tech companies and their respective R&D investment percentages
companies = ['Company A', 'Company B', 'Company C', 'Company D', 'Company E']
percentages = [25, 20, 15, 10, 30]

# Color palette for the tech companies
colors = ['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1']

# Explode the largest sector for emphasis
explode = (0, 0, 0, 0, 0.1)  # Only explode the largest investment segment

# Create a figure and axis for the plot
fig, ax = plt.subplots(figsize=(8, 8))

# Create a pie chart with a donut shape
wedges, texts, autotexts = ax.pie(
    percentages, 
    explode=explode, 
    labels=companies, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=colors, 
    wedgeprops=dict(width=0.3, edgecolor='w'),
    shadow=True
)

# Style the texts for better readability
for text in texts:
    text.set_fontsize(12)
    text.set_color('navy')
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')

# Add a central circle to create the donut effect
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Make the pie chart circular
ax.axis('equal')

# Add a title to the chart
ax.set_title(
    "Tech Giants' R&D Investments in 2023",
    fontsize=16,
    fontweight='bold',
    pad=20
)

# Add a central label for additional information
plt.text(0, 0, 'R&D\nInvestment\n2023', horizontalalignment='center', 
         verticalalignment='center', fontsize=12, color='gray', fontweight='bold')

# Add a legend to the chart
ax.legend(wedges, companies, title="Companies", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()