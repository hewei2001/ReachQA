import matplotlib.pyplot as plt
import numpy as np

# Define the categories
categories = ['Vitamin C', 'Fiber', 'Antioxidants', 'Natural Sugars', 'Water Content', 'Calories']

# Nutritional data for each fruit (normalized scores out of 10)
dragon_fruit = np.array([8, 5, 6, 7, 9, 3])
durian = np.array([6, 4, 5, 8, 7, 7])
acai_berry = np.array([9, 7, 10, 6, 8, 2])
mangosteen = np.array([7, 4, 6, 5, 9, 4])
rambutan = np.array([5, 3, 4, 9, 6, 6])
lychee = np.array([6, 5, 5, 8, 8, 5])

# List of data and fruit names for easy iteration
data = [dragon_fruit, durian, acai_berry, mangosteen, rambutan, lychee]
fruit_names = ['Dragon Fruit', 'Durian', 'Acai Berry', 'Mangosteen', 'Rambutan', 'Lychee']

# Number of variables
num_vars = len(categories)

# Create a radar chart for each fruit
def create_radar_chart(data, labels, title):
    # Calculate angle for each category
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    
    # Complete the loop by appending the start to the end
    data = np.concatenate((data, [data[0]]))
    angles += angles[:1]
    
    # Create the figure
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    
    # Draw one axe per variable and add labels
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=10)
    
    # Plot data
    ax.plot(angles, data, color='blue', linewidth=2, linestyle='solid')
    
    # Fill the area
    ax.fill(angles, data, color='skyblue', alpha=0.4)
    
    # Set labels and title
    ax.set_yticklabels([])
    ax.set_title(title, size=14, color='navy', pad=20)
    
    # Layout
    plt.tight_layout()
    plt.show()

# Generate radar chart for each fruit
for i, fruit_data in enumerate(data):
    create_radar_chart(fruit_data, categories, f'Nutritional Profile of {fruit_names[i]}')