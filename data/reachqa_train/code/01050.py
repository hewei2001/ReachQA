import numpy as np
import matplotlib.pyplot as plt
from math import pi
from matplotlib import cm

# Define the art forms and their impact over periods
categories = ['Painting', 'Sculpture', 'Photography', 'Film', 'Literature']
n_vars = len(categories)

# Cultural impact index for three periods (fictional data)
data_2010_2013 = [75, 60, 50, 40, 35]
data_2014_2017 = [55, 50, 65, 70, 45]
data_2018_2021 = [45, 40, 60, 65, 80]

# Combine data into a numpy array
data = np.array([data_2010_2013, data_2014_2017, data_2018_2021])

# Period labels for the datasets
period_labels = ['2010-2013', '2014-2017', '2018-2021']

# Calculate the angles for the radar chart
angles = np.linspace(0, 2 * pi, num=n_vars, endpoint=False).tolist()
angles += angles[:1]  # Complete the loop by repeating the first angle

# Create a radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Define color palette and line styles
colors = cm.tab10.colors
line_styles = ['-', '--', '-.']

# Plot and fill each period's data
for i, data_period in enumerate(data):
    # Close the loop by repeating the first value at the end
    data_period = np.concatenate((data_period, [data_period[0]]))
    ax.plot(angles, data_period, linewidth=2.5, linestyle=line_styles[i], label=period_labels[i], color=colors[i])
    ax.fill(angles, data_period, color=colors[i], alpha=0.2)

    # Add markers for each data point
    ax.scatter(angles, data_period, color=colors[i], s=50, edgecolor='black', zorder=5)

# Set the category labels at the corresponding angles
plt.xticks(angles[:-1], categories, color='black', size=12, ha='center', va='center')

# Set radial limits and labels with annotations
plt.yticks([20, 40, 60, 80], ['20', '40', '60', '80'], color="grey", size=10)
plt.ylim(0, 100)

# Add a central focal point
ax.set_facecolor('#f2f2f2')
central_icon = plt.Circle((0, 0), 0.1, color='lightgrey', transform=ax.transData._b, zorder=3)
ax.add_artist(central_icon)

# Add a title and adjust the legend
plt.title('Creative Contributions:\nA Decade of Artistic Evolution\n(2010-2021)', size=16, weight='bold', va='top')
plt.legend(loc='upper right', bbox_to_anchor=(0.15, 0.15), fontsize=11, title='Time Periods', title_fontsize='13')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()