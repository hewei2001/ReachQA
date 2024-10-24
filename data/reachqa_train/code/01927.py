import matplotlib.pyplot as plt
import numpy as np

# Artistic styles and their corresponding representation percentages in exhibitions
artistic_styles = ['Classical Realism', 'Impressionism', 
                   'Abstract Expressionism', 'Surrealism', 
                   'Contemporary Art']
percentages = [18, 22, 27, 12, 21]  # Total sums to 100%

# Define colors for each artistic style
colors = ['#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

# Create a horizontal bar chart
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(artistic_styles, percentages, color=colors, edgecolor='black', height=0.6)

# Add percentage labels to each bar
for bar, percentage in zip(bars, percentages):
    ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2, f'{percentage}%', 
            va='center', fontsize=10, color='black', fontweight='bold')

# Set the title and labels with line breaks to accommodate length
ax.set_title('Global Art Exhibition 2023:\nDiverse Artistic Styles Unveiled', fontsize=16, weight='bold', pad=20)
ax.set_xlabel('Percentage of Artworks Displayed')
ax.set_ylabel('Artistic Styles')

# Add grid lines for the x-axis and customize layout
ax.xaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)
ax.set_xlim(0, 35)  # Slightly more than the max percentage for spacing
ax.invert_yaxis()  # Reverse the order for aesthetic presentation
ax.set_xticks(np.arange(0, 36, 5))

# Improve layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()