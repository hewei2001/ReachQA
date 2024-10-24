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

# Hypothetical Popularity Index for each language
popularity_index = [90, 75, 55, 60, 80, 40, 70, 95]

# Colors for each language
colors = ['#ff6347', '#ffa07a', '#20b2aa', '#8a2be2', '#deb887', '#5f9ea0', '#7fff00', '#d2691e']

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8), gridspec_kw={'width_ratios': [3, 2]})

# Plot 1: Horizontal Bar Chart
bars = ax1.barh(languages, ldi_values, color=colors, edgecolor='grey')
ax1.invert_yaxis()
for bar in bars:
    ax1.annotate(f'{bar.get_width()}', xy=(bar.get_width(), bar.get_y() + bar.get_height() / 2),
                 xytext=(5, 0), textcoords="offset points", ha='left', va='center',
                 fontsize=10, color='black')
ax1.set_title("Linguistic Diversity Index\nof Popular Sci-Fi Languages", fontsize=16, fontweight='bold', color='navy')
ax1.set_xlabel("Linguistic Diversity Index (LDI)", fontsize=12, color='darkslategray')
ax1.set_ylabel("Sci-Fi Languages", fontsize=12, color='darkslategray')
ax1.xaxis.grid(True, linestyle='--', alpha=0.6)

# Plot 2: Pie Chart
ax2.pie(popularity_index, labels=languages, autopct='%1.1f%%', startangle=140, colors=colors, wedgeprops=dict(edgecolor='grey'))
ax2.set_title("Popularity Index\nof Sci-Fi Languages", fontsize=16, fontweight='bold', color='navy')

# Adjust layout
plt.tight_layout()

# Show the plots
plt.show()