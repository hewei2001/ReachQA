import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# Define the categories for the radar chart
categories = ['Plot', 'Character\nDevelopment', 'Writing\nStyle', 'Emotional\nImpact', 'Originality']

# Create data for five fictional books
book1 = np.array([9, 7, 8, 6, 8])  # Book A: The Shadowed Path
book2 = np.array([8, 8, 9, 5, 7])  # Book B: Echoes of Tomorrow
book3 = np.array([6, 9, 7, 9, 5])  # Book C: Whispers in the Wind
book4 = np.array([7, 5, 6, 8, 9])  # Book D: The Mirror's Edge
book5 = np.array([5, 8, 9, 7, 8])  # Book E: Luminary Tides

# Combine all book data
book_data = np.vstack([book1, book2, book3, book4, book5])

# Book names for the legend
book_names = ['The Shadowed Path', 'Echoes of Tomorrow', 'Whispers in the Wind', 'The Mirror\'s Edge', 'Luminary Tides']

# Number of variables
num_vars = len(categories)

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# Color palette
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Function to create radar chart
def create_radar_chart(data, categories, book_names):
    angles_with_closure = angles + angles[:1]

    fig, ax = plt.subplots(figsize=(12, 12), subplot_kw=dict(polar=True))

    # Draw one line per book
    for i, (book, color) in enumerate(zip(data, colors)):
        values = np.append(book, book[0])  # Closing the loop
        ax.plot(angles_with_closure, values, linewidth=2, linestyle='-', marker='o', color=color, label=book_names[i])
        ax.fill(angles_with_closure, values, alpha=0.2, color=color)

    # Add labels for each category
    plt.xticks(angles, categories, color='black', size=12)

    # Add labels for the axes
    ax.set_rlabel_position(45)
    plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="grey", size=10)
    plt.ylim(0, 10)

    # Title and legend
    plt.title("The Perfect Book Traits:\nEvaluating Fictional Novels Across Key Attributes", 
              size=16, color='darkblue', y=1.1, fontweight='bold')
    legend_elements = [Patch(facecolor=color, edgecolor=color, alpha=0.2, label=name) for color, name in zip(colors, book_names)]
    plt.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(1.2, 1.1))

    # Automatically adjust layout
    plt.tight_layout()

    # Show the radar chart
    plt.show()

# Call the function with our data
create_radar_chart(book_data, categories, book_names)