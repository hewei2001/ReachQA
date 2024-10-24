import numpy as np
import matplotlib.pyplot as plt

# Define the novels and worldbuilding elements
novels = [
    "The Forgotten Realm", "Arcane Chronicles",
    "Ember's Tales", "Kingdom's Oath", "Myth's End"
]
categories = ['Geography', 'Magic System', 'Cultural Complexity', 'Political Intrigue', 'Mythology']

# Define the data for each novel
data = np.array([
    [8, 7, 6, 5, 9],  # The Forgotten Realm
    [5, 9, 7, 6, 8],  # Arcane Chronicles
    [7, 6, 8, 5, 7],  # Ember's Tales
    [6, 5, 9, 8, 6],  # Kingdom's Oath
    [9, 8, 5, 7, 9]   # Myth's End
])

# Calculate the number of variables
num_vars = len(categories)

# Calculate average scores across all novels for each category
average_scores = data.mean(axis=0)

# Function to create radar chart with an overlay
def create_complex_chart(title, labels, data, averages, legend_labels):
    # Calculate angles for each category
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]

    # Extend data for closure
    data = np.concatenate((data, data[:, [0]]), axis=1)
    averages = np.append(averages, averages[0])

    # Initialize the plot
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
    
    # Plot each novel's data
    colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#C2C2F0']
    for idx, (d, color) in enumerate(zip(data, colors)):
        ax.fill(angles, d, color=color, alpha=0.25)
        ax.plot(angles, d, color=color, label=legend_labels[idx])

    # Overlay line plot for average scores
    ax.plot(angles, averages, color='black', linewidth=2, linestyle='--', label='Category Average')
    ax.fill(angles, averages, color='black', alpha=0.1)

    # Customize the radar chart
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=10)

    # Add title and legend
    plt.title(title, size=16, fontweight='bold', pad=20)
    plt.legend(loc='upper right', bbox_to_anchor=(1.25, 1.1))

    # Adjust layout to prevent overlapping text
    plt.tight_layout()

    # Display the plot
    plt.show()

# Call the function with the data
create_complex_chart(
    "Worldbuilding Focus in Fantasy Novels\nWith Average Category Scores",
    categories, data, average_scores, novels
)