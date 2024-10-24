import matplotlib.pyplot as plt
import numpy as np

# Define months and the number of papers published for each topic
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
algebra = [8, 10, 15, 12, 14, 20, 22, 24, 23, 19, 15, 13]
calculus = [10, 13, 14, 16, 18, 20, 21, 22, 20, 18, 17, 16]
geometry = [5, 7, 8, 10, 11, 13, 12, 14, 15, 13, 9, 8]
probability = [9, 12, 14, 15, 18, 21, 23, 25, 22, 20, 18, 17]
number_theory = [7, 9, 11, 13, 12, 15, 17, 18, 16, 14, 12, 11]

# Start plotting
plt.figure(figsize=(12, 8))

# Plot each mathematical topic's data with distinct styles and markers
plt.plot(months, algebra, label='Algebra', marker='o', linestyle='-', color='b', linewidth=2)
plt.plot(months, calculus, label='Calculus', marker='s', linestyle='--', color='g', linewidth=2)
plt.plot(months, geometry, label='Geometry', marker='^', linestyle=':', color='r', linewidth=2)
plt.plot(months, probability, label='Probability', marker='d', linestyle='-.', color='purple', linewidth=2)
plt.plot(months, number_theory, label='Number Theory', marker='x', linestyle='-', color='orange', linewidth=2)

# Annotate the peak point of each topic
for topic, label in zip([algebra, calculus, geometry, probability, number_theory], 
                        ['Algebra', 'Calculus', 'Geometry', 'Probability', 'Number Theory']):
    max_value = max(topic)
    max_index = topic.index(max_value)
    plt.annotate(f'Peak: {max_value}', (months[max_index], max_value), 
                 textcoords="offset points", xytext=(-15,10), ha='center', fontsize=8, color='black')

# Title and labels
plt.title('Monthly Trends in\nMathematical Research Publications', fontsize=16, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Number of Papers Published', fontsize=12)

# Grid, legend, and layout adjustments
plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
plt.xticks(rotation=45)
plt.yticks(np.arange(0, 30, 2))
plt.legend(title='Mathematical Topics', loc='upper left')

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()