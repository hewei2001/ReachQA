import matplotlib.pyplot as plt

# Data for global tea consumption share
tea_types = ['Green Tea', 'Black Tea', 'Oolong Tea', 'White Tea', 'Herbal Tea', 'Matcha']
consumption_share = [30, 45, 8, 5, 7, 5]  # Percentage of each type's global consumption

# Color palette for each tea type
colors = ['#8DB600', '#4B3832', '#FFB600', '#F7F7F2', '#A8A8A8', '#1D7A46']

# Creating the donut pie chart
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    consumption_share, 
    labels=tea_types, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    pctdistance=0.85,
    wedgeprops=dict(width=0.3)
)

# Enhance text readability
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(12)
    autotext.set_weight('bold')

# Center circle to complete donut shape
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Adding a legend outside the donut chart
ax.legend(wedges, tea_types, title="Tea Types", loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

# Set chart title, breaking into two lines for readability
plt.title('Global Tea Consumption by Type\nA Taste Across Cultures', fontsize=16, fontweight='bold', color='saddlebrown', pad=30)

# Automatically adjust layout to prevent overlapping elements
plt.tight_layout()

# Display the chart
plt.show()