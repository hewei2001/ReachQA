import matplotlib.pyplot as plt

# Artistic mediums and their corresponding artist percentages
mediums = ['Painting', 'Sculpture', 'Digital Art', 'Performance Art', 'Mixed Media']
percentages = [30, 20, 25, 15, 10]

# Average creation time for each artistic medium (in hours)
creation_times = [50, 120, 40, 100, 70]

# Colors for each artistic medium
colors = ['#ffa07a', '#20b2aa', '#9370db', '#ff6347', '#87ceeb']

# Explode the 'Digital Art' slice for emphasis in the pie chart
explode = (0, 0, 0.1, 0, 0)

# Create a figure with two subplots side-by-side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Pie chart for artistic mediums percentages
wedges, texts, autotexts = ax1.pie(
    percentages, 
    explode=explode, 
    labels=mediums, 
    colors=colors, 
    autopct='%1.1f%%', 
    startangle=140, 
    wedgeprops=dict(edgecolor='black'),
    shadow=True
)

for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)

ax1.set_title("Artistic Mediums in Artium:\nA Spectrum of Creativity", fontsize=14, fontweight='bold', pad=20)
ax1.legend(wedges, mediums, title="Artistic Mediums", loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

# Bar chart for average creation times
bars = ax2.bar(mediums, creation_times, color=colors, edgecolor='black')

ax2.set_title("Average Creation Time per Medium", fontsize=14, fontweight='bold', pad=20)
ax2.set_xlabel("Artistic Medium")
ax2.set_ylabel("Average Creation Time (Hours)")
ax2.set_ylim(0, max(creation_times) + 20)

# Adding value labels on top of each bar
for bar in bars:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, yval + 3, f'{yval}', ha='center', va='bottom')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()