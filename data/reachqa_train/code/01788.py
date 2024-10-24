import matplotlib.pyplot as plt

# Cybercrime methods and their percentage share
methods = ['Phishing', 'Ransomware', 'Denial-of-Service', 'Data Breaches', 'Social Engineering', 'Cryptojacking']
incidents_percentage = [35, 25, 15, 10, 8, 7]  # Fictional data representing percentage of each method

# Colors for each method for better visual distinction
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

# Explode the 'Phishing' slice to highlight it
explode = (0.1, 0, 0, 0, 0, 0)

# Create the pie chart
fig, ax = plt.subplots()
ax.pie(incidents_percentage, labels=methods, autopct='%1.1f%%', startangle=140,
       colors=colors, explode=explode, shadow=True, wedgeprops=dict(edgecolor='w'))

# Adding a circle at the center to transform pie chart into a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')

# Title, split into two lines for readability
plt.title('Virtual Heists:\nThe Top Cybercrime Methods in 2023', fontsize=16, fontweight='bold', pad=20)

# Place the legend outside the pie chart
plt.legend(loc='best', bbox_to_anchor=(1, 0, 0.5, 1), title='Methods')

# Adjust layout to fit elements properly
plt.tight_layout()

# Display the plot
plt.show()