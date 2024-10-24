import matplotlib.pyplot as plt
import squarify  # Needed to plot the tree map

# Define market share data in "galactic units"
innovations = {
    'Artificial Intelligence': [120, 180, 90, 60],
    'Quantum Computing': [150, 200, 160],
    'Nanotechnology': [300, 250],
    'Interstellar Propulsion': [400]
}

# Assign labels to each subcategory
innovation_labels = [
    'AI - Earth\n(120 GU)', 'AI - Zephyria\n(180 GU)', 'AI - Kronos\n(90 GU)', 'AI - Zogtron\n(60 GU)',
    'QC - Earth\n(150 GU)', 'QC - Zephyria\n(200 GU)', 'QC - Kronos\n(160 GU)',
    'Nano - Earth\n(300 GU)', 'Nano - Zephyria\n(250 GU)',
    'Propulsion - Earth\n(400 GU)'
]

# Flatten data and labels for plotting
sizes = [value for sublist in innovations.values() for value in sublist]
labels = [f'{lbl}' for lbl in innovation_labels]

# Define colors for each category (using different shades to represent hierarchy)
colors = ['#FFB6C1', '#FF69B4', '#FF1493', '#C71585',  # AI
          '#ADD8E6', '#4682B4', '#4169E1',            # QC
          '#90EE90', '#32CD32',                       # Nano
          '#FFD700']                                  # Propulsion

# Plot the tree map
plt.figure(figsize=(14, 9))
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.8, text_kwargs={'fontsize': 10, 'weight': 'bold'})

# Customize plot appearance
plt.title("Galactic Tech Expo 3023\nInnovations and Their Market Share", fontsize=18, fontweight='bold')
plt.axis('off')

# Adjust layout for better visibility
plt.tight_layout()

# Display the plot
plt.show()