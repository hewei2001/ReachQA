import matplotlib.pyplot as plt

# Transportation modes and their respective percentages
modes = ['Bicycles', 'Electric Scooters', 'Public Transit', 'Electric Cars', 'Walking']
percentages = [30, 15, 25, 20, 10]

# Define the colors for each section
colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854']

# Explode the first slice (Bicycles) for emphasis
explode = (0.1, 0, 0, 0, 0)

# Create the pie chart
plt.figure(figsize=(9, 9))
wedges, texts, autotexts = plt.pie(percentages, labels=modes, autopct='%1.1f%%', startangle=120,
                                   colors=colors, explode=explode, shadow=True)

# Enhance the visual appearance of text labels
for text in texts:
    text.set_color('darkblue')
    text.set_fontsize(12)

for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)

# Title of the plot, formatted for readability
plt.title('Greenville Eco-Friendly Transportation\nUsage Breakdown', fontsize=16, fontweight='bold', pad=30)

# Add a legend
plt.legend(title='Transportation Modes', loc='upper right', bbox_to_anchor=(1.15, 0.9))

# Automatically adjust the subplot parameters to give specified padding
plt.tight_layout()

# Display the plot
plt.show()