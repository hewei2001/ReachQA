import matplotlib.pyplot as plt
import numpy as np

# Define industry sectors and corresponding AI adoption levels
sectors = ['Healthcare', 'Finance', 'Manufacturing', 'Retail', 'Education', 'Transportation']
adoption_levels = [85, 75, 65, 55, 45, 35]  # AI Adoption levels in percentage

# Create the bar chart
fig, ax = plt.subplots(figsize=(12, 8))

# Define colors for the bars
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

# Plot bars
bars = ax.bar(sectors, adoption_levels, color=colors, alpha=0.8, width=0.6)

# Add data annotations on top of each bar
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}%',  # Annotation text
                xy=(bar.get_x() + bar.get_width() / 2, height),  # Position of the annotation
                xytext=(0, 3),  # Offset text position upwards by 3
                textcoords="offset points",
                ha='center', va='bottom', fontsize=10, color='black')

# Customize axes labels and title
ax.set_xlabel('Industry Sectors', fontsize=12)
ax.set_ylabel('AI Adoption Level (%)', fontsize=12)
ax.set_title('AI Adoption in Various Industry Sectors by 2030', fontsize=16, fontweight='bold', pad=20)

# Enhance the visual appeal by adding gridlines
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

# Rotate x-axis labels to avoid overlap
plt.xticks(rotation=30, ha='right')

# Adjust layout to accommodate annotations and labels
plt.tight_layout()

# Display the plot
plt.show()