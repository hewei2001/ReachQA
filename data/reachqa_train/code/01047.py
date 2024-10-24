import numpy as np
import matplotlib.pyplot as plt
from math import pi

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
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot and fill each period's data
for i, data_period in enumerate(data):
    # Close the loop by creating a new list that repeats the first value at the end
    data_period_complete = np.concatenate((data_period, [data_period[0]]))
    ax.plot(angles, data_period_complete, linewidth=2, linestyle='solid', label=period_labels[i])
    ax.fill(angles, data_period_complete, alpha=0.25)

# Set the category labels at the corresponding angles
plt.xticks(angles[:-1], categories, color='black', size=10)

# Set radial limits and labels
plt.yticks([20, 40, 60, 80], ['20', '40', '60', '80'], color="grey", size=8)
plt.ylim(0, 100)

# Add a title and adjust the legend
plt.title('Creative Contributions:\nA Decade of Artistic Evolution', size=15, weight='bold', position=(0.5, 1.1), ha='center')
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1), fontsize=10, title='Time Periods')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()