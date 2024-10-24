import matplotlib.pyplot as plt

# Sci-Fi languages and their linguistic diversity indices
languages = [
    "Klingon", 
    "Sindarin", 
    "Dothraki", 
    "High Valyrian", 
    "Quenya", 
    "Huttese", 
    "Navi", 
    "Kryptonian"
]

# Linguistic Diversity Index for each language
ldi_values = [85, 78, 65, 72, 82, 54, 67, 88]

# Colors for each language
colors = ['#ff6347', '#ffa07a', '#20b2aa', '#8a2be2', '#deb887', '#5f9ea0', '#7fff00', '#d2691e']

# Plotting the horizontal bar chart
fig, ax = plt.subplots(figsize=(12, 8))

# Create the horizontal bars
bars = ax.barh(languages, ldi_values, color=colors, edgecolor='grey')

# Invert y-axis to have the first language at the top
ax.invert_yaxis()

# Add value labels on the bars
for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width}',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(5, 0),  # 5 points horizontal offset
                textcoords="offset points",
                ha='left', va='center',
                fontsize=10, color='black')

# Title and axis labels
ax.set_title("Linguistic Diversity Index\nof Popular Sci-Fi Languages", fontsize=16, fontweight='bold', color='navy')
ax.set_xlabel("Linguistic Diversity Index (LDI)", fontsize=12, color='darkslategray')
ax.set_ylabel("Sci-Fi Languages", fontsize=12, color='darkslategray')

# Add vertical grid lines for easier readability
ax.xaxis.grid(True, linestyle='--', alpha=0.6)

# Enhance layout
plt.tight_layout()

# Show the plot
plt.show()