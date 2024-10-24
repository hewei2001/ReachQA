import matplotlib.pyplot as plt
import numpy as np

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

# Function to create radar chart
def create_radar_chart(data, categories, book_names):
    angles_with_closure = angles + angles[:1]
    
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

    # Draw one line per book
    for i, book in enumerate(data):
        values = np.append(book, book[0])  # Closing the loop
        ax.plot(angles_with_closure, values, linewidth=2, linestyle='solid', label=book_names[i])
        ax.fill(angles_with_closure, values, alpha=0.25)

    # Add labels for each category
    plt.xticks(angles, categories, color='black', size=12)

    # Add labels for the axes
    ax.set_rlabel_position(30)
    plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="grey", size=10)
    plt.ylim(0, 10)

    # Title and legend
    plt.title("The Perfect Book Traits:\nEvaluating Fictional Novels Across Key Attributes", 
              size=16, color='darkblue', y=1.1, fontweight='bold')
    plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))

    # Automatically adjust layout
    plt.tight_layout()
    
    # Show the radar chart
    plt.show()

# Call the function with our data
create_radar_chart(book_data, categories, book_names)