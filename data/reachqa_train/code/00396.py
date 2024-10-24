import matplotlib.pyplot as plt

# Define the sectors and their investment percentages
sectors = ['Artificial Intelligence', 'Renewable Energy', 'Biotechnology', 
           'Space Exploration', 'Quantum Computing', 'Advanced Robotics']
investment_percentages = [25, 20, 15, 10, 20, 10]

# Define colors for each sector
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6']

# Define an explode pattern to highlight a few sectors more prominently
explode = (0.1, 0, 0.1, 0, 0.1, 0)

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(investment_percentages, labels=sectors, autopct='%1.1f%%',
                                  startangle=140, colors=colors, explode=explode, shadow=True,
                                  textprops=dict(color="w"))

# Set custom style for text elements
for text in texts:
    text.set_fontsize(12)
    text.set_color("black")
for autotext in autotexts:
    autotext.set_fontsize(12)
    autotext.set_color("black")

# Title with a descriptive theme split into two lines
plt.title('Global Innovation and Futurism\nInvestments in 2030', fontsize=16, pad=20)

# Add a legend outside the plot area
ax.legend(wedges, sectors, title="Sectors", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Adjust layout to fit all elements cleanly
plt.tight_layout()

# Display the chart
plt.show()