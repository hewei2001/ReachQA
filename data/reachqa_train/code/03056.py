import matplotlib.pyplot as plt
import squarify

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

# Create figure and axis
fig, ax = plt.subplots(figsize=(14, 9))
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.7, ax=ax, 
              text_kwargs={'fontsize': 10, 'weight': 'bold'}, edgecolor="black", linewidth=1.5)

# Set title with a subtitle for clarity
plt.title("Galactic Tech Expo 3023\nInnovations and Their Market Share", fontsize=16, fontweight='bold')

# Remove axis for clarity
ax.axis('off')

# Customizing plot background
ax.set_facecolor('#f0f8ff')

# Annotations for highlighting key insights
ax.annotate('AI Dominates\nwith 4 sectors', xy=(0.7, 0.7), xycoords='axes fraction', fontsize=12,
            bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="#FFB6C1", alpha=0.6))

ax.annotate('Largest Single\nInvestment in\nPropulsion\n(400 GU)', xy=(0.35, 0.05), xycoords='axes fraction', fontsize=12,
            bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="#FFD700", alpha=0.6))

# Display a legend in a separate subplot
fig.legend(labels=["AI", "Quantum Computing", "Nanotechnology", "Interstellar Propulsion"], 
           loc="upper left", fontsize=10, title="Innovation Categories")

# Adjust layout for better visibility and to avoid overlap
plt.tight_layout(rect=[0, 0, 0.85, 1])

# Display the plot
plt.show()