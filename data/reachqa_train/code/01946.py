import matplotlib.pyplot as plt

# Artistic mediums and their corresponding artist percentages
mediums = ['Painting', 'Sculpture', 'Digital Art', 'Performance Art', 'Mixed Media']
percentages = [30, 20, 25, 15, 10]

# Colors for each artistic medium
colors = ['#ffa07a', '#20b2aa', '#9370db', '#ff6347', '#87ceeb']

# Explode the 'Digital Art' slice for emphasis
explode = (0, 0, 0.1, 0, 0)

# Create the pie chart
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    percentages, 
    explode=explode, 
    labels=mediums, 
    colors=colors, 
    autopct='%1.1f%%', 
    startangle=140, 
    wedgeprops=dict(edgecolor='black'),
    shadow=True
)

# Customize the font and color of the percentage labels
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)

# Set chart title with line break for clarity
ax.set_title("Artistic Mediums in Artium:\nA Spectrum of Creativity", fontsize=16, fontweight='bold', pad=20)

# Position the legend outside the chart
ax.legend(wedges, mediums, title="Artistic Mediums", loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()