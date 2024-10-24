import matplotlib.pyplot as plt

# Explicitly defined weekly yield data (in kg) for each vegetable over a season
tomatoes = [3.5, 3.8, 4.2, 4.1, 3.7, 4.0, 4.4, 4.3, 3.9, 4.1]
cucumbers = [2.9, 3.0, 3.1, 3.4, 3.3, 2.8, 3.0, 3.5, 3.2, 3.1]
carrots = [4.0, 3.9, 4.3, 4.1, 4.0, 4.2, 4.4, 4.2, 4.5, 4.3]
lettuce = [1.2, 1.1, 1.3, 1.0, 1.2, 1.1, 1.3, 1.2, 1.1, 1.0]
bell_peppers = [2.5, 2.4, 2.6, 2.7, 2.8, 2.9, 3.0, 2.8, 2.7, 2.6]

# Aggregate the data into a list
data = [tomatoes, cucumbers, carrots, lettuce, bell_peppers]

# Vegetable labels
vegetables = ['Tomatoes', 'Cucumbers', 'Carrots', 'Lettuce', 'Bell Peppers']

# Compute total yield for each vegetable
total_yields = [sum(veg_data) for veg_data in data]

# Creating the figure and axes
fig, axs = plt.subplots(1, 2, figsize=(14, 6))
fig.patch.set_facecolor('#f4f4f8')

# First subplot: Box plot
ax1 = axs[0]
bp = ax1.boxplot(data, patch_artist=True, notch=True, vert=True, labels=vegetables)
colors = ['#FF6347', '#8FBC8F', '#FFA07A', '#ADFF2F', '#FFD700']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
plt.setp(bp['whiskers'], color='darkgrey', linewidth=1.5)
plt.setp(bp['caps'], color='darkgrey', linewidth=1.5)
plt.setp(bp['medians'], color='indigo', linewidth=2)
ax1.set_title('Weekly Vegetable Yield in\nUrban Community Gardens', fontsize=14, fontweight='bold', color='navy')
ax1.set_ylabel('Yield (kg)', fontsize=12)
ax1.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.25)
ax1.set_axisbelow(True)

# Second subplot: Bar chart
ax2 = axs[1]
bars = ax2.bar(vegetables, total_yields, color=colors, edgecolor='black')
ax2.set_title('Total Seasonal Yield', fontsize=14, fontweight='bold', color='navy')
ax2.set_ylabel('Total Yield (kg)', fontsize=12)

# Annotate bars with the total yield values
for bar in bars:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, yval + 0.1, round(yval, 1), ha='center', va='bottom', fontsize=10, fontweight='bold')

# Automatically adjusting layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()