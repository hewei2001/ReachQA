import matplotlib.pyplot as plt

# Define employee satisfaction scores for four technology companies
company_names = [
    'Tech Innovators Inc.',
    'Digital Solutions Ltd.',
    'Cyber Systems Corp.',
    'Quantum Softworks'
]

# Satisfaction data for each company
company_a = [7.2, 7.5, 8.1, 8.3, 7.9, 8.0, 7.7, 7.8, 8.2, 8.1]
company_b = [6.5, 6.4, 6.3, 6.6, 6.5, 6.8, 6.7, 6.5, 6.9, 6.4]
company_c = [4.7, 5.0, 4.8, 5.1, 4.6, 4.9, 5.3, 5.1, 4.5, 5.2]
company_d = [9.0, 9.1, 9.2, 9.3, 9.4, 9.2, 9.3, 9.1, 9.2, 9.3]

# Combine data into a list for the box plot
all_data = [company_a, company_b, company_c, company_d]

# Create a figure and axis for the horizontal box plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot the horizontal box chart
bp = ax.boxplot(
    all_data, 
    vert=False, 
    patch_artist=True, 
    notch=True, 
    boxprops=dict(facecolor='#87CEEB', color='#4682B4'),
    whiskerprops=dict(color='#4682B4'), 
    capprops=dict(color='#4682B4'),
    medianprops=dict(color='red')
)

# Customize the colors of each box
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Set titles and labels
ax.set_title(
    'Global Tech Giants\' Employee Satisfaction in 2023', 
    fontsize=16, 
    fontweight='bold', 
    pad=20
)
ax.set_xlabel('Satisfaction Score (0 to 10)', fontsize=12)
ax.set_yticks([1, 2, 3, 4])
ax.set_yticklabels(company_names, fontsize=12)

# Add grid for better readability
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()